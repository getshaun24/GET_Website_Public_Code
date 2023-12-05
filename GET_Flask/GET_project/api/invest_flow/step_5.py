from flask import Blueprint, session, url_for, request, redirect, jsonify, current_app
from flask_login import login_required
from flask_session import Session
import sys
import datetime
from datetime import datetime, timedelta
import uuid
import re
from GET_project.api.dwolla import dwolla_initiate_investment_transfer, dwolla_link_new_account_funding_source
from GET_project.api.plaid import plaid_client
from GET_project import db 
from flask_mail import Mail
from flask_mail import Message
from GET_project.api.mail import mail, get_html_email_template
from GET_project.api.functions import generate_password_token


GET_invest_flow_step_5_Blueprint = Blueprint('GET_invest_flow_step_5', __name__)
@GET_invest_flow_step_5_Blueprint.route('/api/invest_flow/step_5/', methods=['GET', 'POST']) # <- from '/'
def GET_invest_flow_step_5():


    print(request.json)

    print('start transact ------- >')

    investor_ID = request.json.get("investor_ID", None)
    fund_ID = request.json.get("fund_ID", None)
    investment_amount = request.json.get("investment_amount", None)
    institution_ID = request.json.get("institution_ID", None)
    account_selected_value = request.json.get("account_selected_value", None)
    account_selected_value_step_2 = request.json.get("account_selected_value_step_2", None)
    email = request.json.get("email", None)
    pre_formated_phone = request.json.get("phone", None)
    print('phone_number: ------------------------_> ', pre_formated_phone)
    phone = '+' + re.sub('\D', '', pre_formated_phone)
    print('investor_ID investor_ID investor_ID investor_ID investor_ID investor_ID: ------------------------_> ', investor_ID)

    link_token = None


    get_investor = db.investor_info.find_one({ "investor_ID": investor_ID })
    investor_funding_source = get_investor["investments"][fund_ID]["active_investor_dwolla_account_url"]
    selected_bank_account_id = get_investor["investments"][fund_ID]["active_selected_bank_account_id"]
    investor_email = get_investor["email"]
    dwolla_customer_url = get_investor["dwolla"]['customer_url']

    current_investor_balance = None
    plaid_access_token = None
    for intitution in get_investor["plaid"]["institutions"]:
        if intitution['institution_ID'] == institution_ID:
            plaid_access_token = intitution['plaid_access_token']
            for auth_obj in intitution["plaid_pulls"]["Auth"]:
                for acct in auth_obj['auth_response']['accounts']:
                    print(selected_bank_account_id)
                    print(acct['account_id'])
                    if acct['account_id'] == selected_bank_account_id:
                        print(acct)
                        current_investor_balance = acct['balances']['current']
                        break



    print('current_investor_balance ----- > ', current_investor_balance)
    print('investment_amount ----- > ', investment_amount)


    try:
        print('NEW_FUNDING_SOURCE')
        dw_url_path = 'investments.' + str(fund_ID) + '.active_investor_dwolla_account_url'
        dw_acct_id_path = 'investments.' + str(fund_ID) + '.active_selected_bank_account_id'
        all_dw_accts_path = 'dwolla.all_funding_source_accounts'
        if investor_funding_source == None:
            print('check it 1')
            funding_source_account = dwolla_link_new_account_funding_source(plaid_access_token, account_selected_value_step_2, dwolla_customer_url)
            print(funding_source_account)
            print('check it 2')
            db.investor_info.update({"investor_ID": investor_ID}, {"$set": {dw_url_path:funding_source_account, dw_acct_id_path:account_selected_value_step_2}})
            db.investor_info.update({"investor_ID": investor_ID}, {"$push": { all_dw_accts_path:{'funding_source_account':funding_source_account, 'account_selected_value':account_selected_value_step_2, 'institution_ID':institution_ID}}})
        elif account_selected_value != None:
            print('check it 3')
            funding_source_account = dwolla_link_new_account_funding_source(plaid_access_token, account_selected_value, dwolla_customer_url)
            print(funding_source_account)
            print('check it 4')
            db.investor_info.update({"investor_ID": investor_ID}, {"$set": {dw_url_path:funding_source_account, dw_acct_id_path:account_selected_value}})
            db.investor_info.update({"investor_ID": investor_ID}, {"$push": { all_dw_accts_path:{'funding_source_account':funding_source_account, 'account_selected_value':account_selected_value, 'institution_ID':institution_ID}}})
    except:
        print('funding_already_created')


    # A Fake Amount in the Plaid Sandbox Account      
    # -------------------------------
    if current_app.config['TEST_INVESTOR_BALANCE']:
        current_investor_balance = current_app.config['TEST_INVESTOR_BALANCE_AMOUNT']
    # -------------------------------

    if current_investor_balance is None:
        current_investor_balance = 0

    if float(current_investor_balance) > float(investment_amount):

        get_fund = db.fund_details.find_one({ "fund_ID": fund_ID })
        fund_name = get_fund["fund_name"]
        fundX_funding_source = get_fund['dwolla']['GET_fund_dwolla_account_url']
    
        try:
            if get_investor["transaction_initiated"] == True:
                print('transaction already initiated')
                return jsonify( link_token=link_token, status='transaction_already_initiated', message='Transaction Already Initiated' )
            else:
                db.investor_info.update({"investor_ID": investor_ID}, {"$set": {"transaction_initiated": True}})
        except:
            db.investor_info.update({"investor_ID": investor_ID}, {"$set": {"transaction_initiated": True}})

        transfer_list = dwolla_initiate_investment_transfer(fund_ID, investment_amount, investor_funding_source, fundX_funding_source, fund_name)


        print(transfer_list)
        for transfer_elm in transfer_list:
            transfer_url = transfer_elm[0]
            transfer_status = transfer_elm[1]
            transfer_amount = transfer_elm[2]
            print(transfer_url, transfer_status, transfer_amount)
            db.transfers.insert_one({"investor_ID": investor_ID, 'fund_ID':fund_ID, 'dwolla_customer_url':dwolla_customer_url, 'transfer_url':transfer_url, 'transfer_status':transfer_status, "transfer_amount":transfer_amount, "transfer_datetime":datetime.now(), "to_from":"To_Fund_From_Investor"})
            print(transfer_url, transfer_status, transfer_amount)


        investment_amount_update_path = 'investments.' + fund_ID + '.investment_amount'
        investment_status_path = 'investments.' + fund_ID + '.investment_status'
        db.investor_info.update({"investor_ID": investor_ID}, {"$set": {
            "signup_progress": 'Signup Successful', 
            "notification_count":0,
            "dashboard_config":{},
            investment_amount_update_path:investment_amount,
            investment_status_path:"invested_payment_pending"
        }})

        db.investor_info.update({"investor_ID": investor_ID}, {"$unset": {"transaction_initiated": True}})


        print(' Transacted and Sent ------------------------------------------------>')


        # ----------------------------- investor_email --------------------------------

        # TEST_EMAIL_RECIPIENTS = current_app.config['TEST_EMAIL_RECIPIENTS']
        # MAIL_USERNAME = current_app.config['MAIL_USERNAME']
        # SITE_DOMAIN = current_app.config['SITE_DOMAIN']
        # # email_url_link = EMAIL_DOMAIN + '/investor_dashboard/investor_welcome/?ivid=' + investor_ID
        # data_to_load = {'user_ID': investor_ID, 'email': investor_email} # Anything else to add???
        # email_url_link = SITE_DOMAIN + '/investor_dashboard/investor_welcome/?ivid=' + generate_password_token(data_to_load)

        # new_investor_email = get_html_email_template(email_url_link)

        # if TEST_EMAIL_RECIPIENTS == True:
        #     email_to = current_app.config['EMAIL_LIST']
        # else:
        #     email_to = [email]

        # msg = Message(

        #             sender=MAIL_USERNAME,
        #             recipients=email_to,
        #             subject="GET Equity Partners - Account Validate & Login",
        #             html=new_investor_email
        #             )
        # mail.send(msg)


        # ----------------------------- investor_email --------------------------------




        print('email sent')
        status = 'payment_completed'
        message = 'successful payment'

        return jsonify(link_token=link_token, status=status, message=message), 200





    else:
        
        status = 'Insufficient_Funds'
        message = 'Not enough funds in account'


    redirect_uri_2 = current_app.config['SITE_DOMAIN'] + current_app.config['PLAID_REDIRECT_URI_2']
    # ---- RETURNING USER EXPEIENCE TEST ----
    if current_app.config['PLAID_RUX']:
        phone = "+1 415 555 0123"
        email = "example@plaid.com"


    plaid_products = ['auth'] 
    plaid_response = plaid_client.link_token_create({
        'client_name': "GET Website",
        'products': plaid_products,
        'country_codes': current_app.config['PLAID_COUNTRY_CODES'],
        'language': "en",
        'redirect_uri': redirect_uri_2,
        'user': {
        'client_user_id':investor_ID,
        'phone_number': phone,
        'email_address': email
        },
        })

    link_token = plaid_response['link_token']
    print('LINK TOKEN', link_token)



    return jsonify(
            link_token=link_token,
            status=status,
            message=message
        ), 200








    



