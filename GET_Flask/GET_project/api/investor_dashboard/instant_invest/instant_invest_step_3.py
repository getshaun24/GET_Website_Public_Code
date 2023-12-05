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
from GET_project.api.plaid import get_plaid_balance_for_account


GET_instant_invest_step_3_Blueprint = Blueprint('GET_instant_invest_step_3', __name__)
@GET_instant_invest_step_3_Blueprint.route('/api/investor_dashboard/instant_invest/instant_invest_step_3/', methods=['GET', 'POST']) # <- from '/'
def GET_instant_invest_step_3():


    print(request.json)

    print('start transact ------- >')

    investor_ID = request.json.get("investor_ID", None)
    fund_ID = request.json.get("fund_ID", None)
    investment_amount = request.json.get("investment_amount", None)
    funding_selected_value = request.json.get("funding_selected_value", None)
    account_selected_value_step_2 = request.json.get("account_selected_value_step_2", None)

    link_token = None


    get_investor = db.investor_info.find_one({ "investor_ID": investor_ID })
    dwolla_customer_url = get_investor["dwolla"]['customer_url']
    first_last = get_investor["first_name"] + ' ' + get_investor["last_name"]
    investor_email = get_investor["email"]
    phone = get_investor["phone"]


    selected_bank_account_id = None
    institution_ID = None
    for fs in get_investor["dwolla"]['all_funding_source_accounts']:
        if fs['investor_dwolla_account_url'] == funding_selected_value:
            selected_bank_account_id = fs['selected_bank_account_id']
            institution_ID = fs['institution_ID']
            break



    invest_url_path = 'investments.' + fund_ID + '.active_investor_dwolla_account_url'
    invest_id_path = 'investments.' + fund_ID + '.active_selected_bank_account_id'
    invest_insti_path = 'investments.' + fund_ID + '.active_institution_id'
    db.investor_info.update({"investor_ID": investor_ID}, {"$set": { invest_url_path:funding_selected_value, invest_id_path:selected_bank_account_id, invest_insti_path:institution_ID}})




    current_investor_balance = None
    for intitution in get_investor["plaid"]["institutions"]:
        if intitution['institution_ID'] == institution_ID:
            plaid_access_token = intitution['plaid_access_token']
            current_investor_balance = get_plaid_balance_for_account(plaid_access_token, selected_bank_account_id)
            break




    print('current_investor_balance ----- > ', current_investor_balance)
    print('investment_amount ----- > ', investment_amount)






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

        transfer_list = dwolla_initiate_investment_transfer(fund_ID, investment_amount, funding_selected_value, fundX_funding_source, fund_name)


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
            investment_amount_update_path:investment_amount,
            investment_status_path:"invested_payment_pending"
        }})

        db.investor_info.update({"investor_ID": investor_ID}, {"$unset": {"transaction_initiated": True}})


        print(' Transacted and Sent ------------------------------------------------>')


        # ----------------------------- investor_email --------------------------------

        # ----------------------------- investor_email --------------------------------


        MAIL_USERNAME = current_app.config['MAIL_USERNAME']
        EMAIL_LIST = current_app.config['EMAIL_LIST']

        # ----------------------------- Internal Info Email --------------------------------

        
        new_investor_update_info = "<br> <b>fund_name - </b> " + str(fund_name) + "<br> <b>investment_amount - </b> " + str(investment_amount) + "<br> <>investing_as - <br> <b>investor_name - </b> " + str(first_last) +  "<br> <b>email - </b> " + str(investor_email) + "<br> <b>phone - </b> " + str(phone) + "<br><b>investor_ID - </b> " + str(investor_ID) + "<br> <b>fund_ID - </b> " + str(fund_ID)

        msg = Message(
                    sender=MAIL_USERNAME,
                    recipients=EMAIL_LIST,
                    subject="New Investor Update",
                    html=new_investor_update_info
                    )
        mail.send(msg)



        # ----------------------------- investor_email --------------------------------




        print('email sent')
        status = 'payment_completed'
        message = 'successful payment'

        return jsonify(link_token=link_token, status=status, message=message), 200





    else:
        
        status = 'Insufficient_Funds'
        message = 'Not enough funds in account'


    redirect_uri_2 = current_app.config['SITE_DOMAIN'] + current_app.config['PLAID_REDIRECT_URI_2']


    plaid_products = ['auth'] 
    plaid_response = plaid_client.link_token_create({
        'client_name': "GET Website",
        'products': plaid_products,
        'country_codes': current_app.config['PLAID_COUNTRY_CODES'],
        'language': "en",
        'redirect_uri': redirect_uri_2,
        'user': {
        'client_user_id':investor_ID,
        },
        })

    link_token = plaid_response['link_token']
    print('LINK TOKEN', link_token)



    return jsonify(
        link_token=link_token,
        status=status,
        message=message
    ), 200








    



