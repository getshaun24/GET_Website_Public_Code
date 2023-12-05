from flask import Blueprint, session, url_for, request, redirect, render_template, flash, current_app, jsonify
from flask_session import Session
import pymongo
import sys
from GET_project.api.mail import mail
# from GET_project.api.mongo import mongo as db
from GET_project import db 
from flask_jwt_extended import jwt_required
from GET_project.api.functions import generate_password_token
from GET_project.api.mail import mail, get_html_email_template
from GET_project.api.functions import confirm_password_token, get_token_data
from GET_project.api.dwolla import dwolla_initiate_investment_transfer
from GET_project.api.plaid import get_plaid_balance_for_account
from flask_mail import Mail
from flask_mail import Message
import datetime
from datetime import datetime, timedelta

Manager_Upsell_Received_Blueprint = Blueprint('Manager_Upsell_Received', __name__)
@Manager_Upsell_Received_Blueprint.route('/api/manager_dashboard/manager_upsell_received/', methods=['POST']) # <- from '/'
# @jwt_required()
def Manager_Upsell_Received():


    token = request.json.get('ivid', None)
    investment_amount = request.json.get('investment_amount', None)


    if token is None:
        return jsonify(msg='No token provided as a parameter', status='token_error'), 400
    token_valid = confirm_password_token(token, expire_time=10000000)

    if investment_amount is None:
        return jsonify(msg='Did not recieve investment amount', status='token_error')
    
    if token_valid:
        
        token_data = get_token_data(token, expire_time=10000000)


        if token_data is not None:
            if token_data['investor_ID'] is not None and token_data['fundX_ID']:

                investor_ID = token_data['investor_ID']
                fund_ID = token_data['fundX_ID']
                print(fund_ID)

                get_investor = db.investor_info.find_one({ "investor_ID": investor_ID })

                try:
                    if get_investor["investments"][fund_ID]:
                        print('investment exists')
                except:
                    return jsonify(msg='Investment In This Fund Does Not Exist', status='fund_does_not_exist'), 403



                dwolla_customer_url = get_investor["dwolla"]['customer_url']
                first_last = get_investor["first_name"] + ' ' + get_investor["last_name"]
                investor_email = get_investor["email"]
                phone = get_investor["phone"]
                active_institution_id = get_investor["investments"][fund_ID]["active_institution_id"]
                active_investor_dwolla_account_url = get_investor["investments"][fund_ID]["active_investor_dwolla_account_url"]
                active_selected_bank_account_id = get_investor["investments"][fund_ID]["active_selected_bank_account_id"]
                



                current_investor_balance = None
                for intitution in get_investor["plaid"]["institutions"]:
                    if intitution['institution_ID'] == active_institution_id:
                        plaid_access_token = intitution['plaid_access_token']
                        current_investor_balance = get_plaid_balance_for_account(plaid_access_token, active_selected_bank_account_id)
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
                            return jsonify( status='transaction_already_initiated', message='Transaction Already Initiated' )
                        else:
                            db.investor_info.update({"investor_ID": investor_ID}, {"$set": {"transaction_initiated": True}})
                    except:
                        db.investor_info.update({"investor_ID": investor_ID}, {"$set": {"transaction_initiated": True}})

                    transfer_list = dwolla_initiate_investment_transfer(fund_ID, investment_amount, active_investor_dwolla_account_url, fundX_funding_source, fund_name)


                    print(transfer_list)
                    for transfer_elm in transfer_list:
                        transfer_url = transfer_elm[0]
                        transfer_status = transfer_elm[1]
                        transfer_amount = transfer_elm[2]
                        print(transfer_url, transfer_status, transfer_amount)
                        db.transfers.insert_one({"investor_ID": investor_ID, 'fund_ID':fund_ID, 'dwolla_customer_url':dwolla_customer_url, 'transfer_url':transfer_url, 'transfer_status':transfer_status, "transfer_amount":transfer_amount, "transfer_datetime":datetime.now(), "to_from":"To_Fund_From_Investor"})
                        print(transfer_url, transfer_status, transfer_amount)



                    db.investor_info.update({"investor_ID": investor_ID}, {"$unset": {"transaction_initiated": True}})


                    print(' Transacted and Sent ------------------------------------------------>')



                    additional_invest_path = 'investments.' + fund_ID + '.additional_investments'
                    db.investor_info.update({"investor_ID": investor_ID}, {"$push": { additional_invest_path:{"investment_datetime":datetime.today(), "investment_amount":investment_amount, "investment_status":"invested_payment_pending"}}})




                    MAIL_USERNAME = current_app.config['MAIL_USERNAME']
                    EMAIL_LIST = current_app.config['EMAIL_LIST']

                    # ----------------------------- Internal Info Email --------------------------------

                    
                    new_investor_update_info = "<br> <b>fund_name - </b> " + str(fund_name) + "<br> <b>investment_amount - </b> " + str(investment_amount) + "<br> <>investing_as - <br> <b>investor_name - </b> " + str(first_last) +  "<br> <b>email - </b> " + str(investor_email) + "<br> <b>phone - </b> " + str(phone) + "<br><b>investor_ID - </b> " + str(investor_ID) + "<br> <b>fund_ID - </b> " + str(fund_ID)

                    msg = Message(
                                sender=MAIL_USERNAME,
                                recipients=EMAIL_LIST,
                                subject="New Investor Upsell Update",
                                html=new_investor_update_info
                                )
                    mail.send(msg)




                    return jsonify(msg='Transaction Success', status='success'), 200







                else:
                    return jsonify(msg='Insufficient Funds', status='insufficient_funds'), 403
                    
            else:
                print('Token was corrupted')
                return jsonify(msg='Token was corrupted', status='token_error'), 403
        else:
            print('Could not retrieve token data')
            return jsonify(msg='Could not retrieve token data',  status='token_error'), 403
    else:
        print('Token is not valid')
        return jsonify(msg='Token is not valid',  status='token_error'), 403
    



