from flask import Blueprint, session, url_for, request, redirect, jsonify, current_app
from flask_login import login_required
from flask_session import Session
import sys
import datetime
from datetime import datetime, timedelta
import uuid
from GET_project.api.dwolla import get_dwolla_token
from GET_project import db 
from flask_mail import Mail
from flask_mail import Message
from GET_project.api.mail import mail
from flask_jwt_extended import jwt_required

GET_returns_Blueprint = Blueprint('GET_returns', __name__)
@GET_returns_Blueprint.route('/api/returns/', methods=['GET', 'POST']) # <- from '/'
@jwt_required()
def GET_returns():


    fund_ID = request.json.get("fund_ID", None)
    investor_ID = request.json.get("investor_ID", None)
    return_amount = float(request.json.get("return_amount", None))


    print('-------------------------------------------')
    print('-------------------------------------------')
    print('-------------------------------------------')
    print('-------------------------------------------')
    print('-------------------------------------------')
    print(fund_ID)

    get_user = db.investor_info.find_one({ "investor_ID": investor_ID })
    investor_funding_source = get_user["investments"][fund_ID]["investor_dwolla_account_url"]
    dwolla_customer_url = get_user["dwolla"]['customer_url']

    get_fund = db.fund_details.find_one({ "fund_ID": fund_ID })
    fund_name = get_fund["fund_name"]
    fundX_funding_source = get_fund['dwolla']['GET_fund_dwolla_account_url']
   


    transfer_list = dwolla_initiate_investment_transfer_returns(fund_ID, return_amount, investor_funding_source, fundX_funding_source, fund_name)


    print(transfer_list)
    for transfer_elm in transfer_list:
        transfer_url = transfer_elm[0]
        transfer_status = transfer_elm[1]
        transfer_amount = transfer_elm[2]
        print(transfer_url, transfer_status, transfer_amount)
        db.transfers.insert_one({"investor_ID": investor_ID, 'fund_ID':fund_ID, 'dwolla_customer_url':dwolla_customer_url, 'transfer_url':transfer_url, 'transfer_status':transfer_status, "transfer_amount":transfer_amount, "transfer_datetime":datetime.now(), "to_from":"To_Investor_From_Fund"})
        print(transfer_url, transfer_status, transfer_amount)


    investment_amount_update_path = 'investments.' + fund_ID + '.investment_amount'
    investment_status_path = 'investments.' + fund_ID + '.investment_status'
    db.investor_info.update({"investor_ID": investor_ID}, {"$set": { 
        investment_amount_update_path:return_amount,
        investment_status_path:"Invested - Payment Pending"
    }})




    print(' Transacted and Sent ------------------------------------------------>')


    # ----------------------------- investor_email --------------------------------
    msg = Message(
                sender="getresources@fastmail.com",
                recipients=['shauncohen24@gmail.com'],
                subject="secure-bank",
                body=current_app.config['SITE_DOMAIN'] + "/new_investor_intro/"
                )
    # mail.send(msg)



    return jsonify(
        status="return_completed",
        message="Return Completed."
    ), 200








def dwolla_initiate_investment_transfer_returns(fund_ID, return_amount, investor_funding_source, fundX_funding_source, fund_name):


    dwolla_app_token = get_dwolla_token()


    DEV_TEST_VAL = 3000
    print(return_amount)

    transfer_list = []

    headers = {
    'Idempotency-Key': str(uuid.uuid5(uuid.NAMESPACE_DNS, str(return_amount) + str(datetime.now().strftime("%m/%d/%Y, %H:%M:%S"))))}


    if return_amount > DEV_TEST_VAL:

        invest_loop_amount = return_amount

        while invest_loop_amount >= 0:

            if invest_loop_amount >= DEV_TEST_VAL:

                transfer_amount = DEV_TEST_VAL

                request_body = {
                '_links': {
                    'source': {
                    'href': fundX_funding_source
                    },
                    'destination': {
                    'href': investor_funding_source  
                    }
                },
                'amount': {
                    'currency': 'USD',
                    'value': DEV_TEST_VAL,
                },
                'metadata': {
                    'note': 'GET Equity Partners ' + fund_name + 'investment '
                },
                'clearing': {
                    'destination': 'next-available'
                },
                'correlationId': fund_ID,
                }

            elif invest_loop_amount < DEV_TEST_VAL:

                transfer_amount = invest_loop_amount

                request_body = {
                '_links': {
                    'source': {
                    'href': fundX_funding_source   
                    },
                    'destination': {
                    'href': investor_funding_source   
                    }
                },
                'amount': {
                    'currency': 'USD',
                    'value': invest_loop_amount,
                },
                'metadata': {
                    'note': 'GET Equity Partners ' + fund_name + ' investment'
                },
                'clearing': {
                    'destination': 'next-available'
                },
                'correlationId': fund_ID,
                }


            transfer = dwolla_app_token.post('transfers', request_body, headers)
            transfer_url = transfer.headers['location'] 
            transfer = dwolla_app_token.get(transfer_url)
            transfer_status = transfer.body['status'] 

            transfer_list.append([transfer_url, transfer_status, transfer_amount])

            invest_loop_amount -= DEV_TEST_VAL


            if invest_loop_amount <= 0:
                break

            print ('invest_loop_amount: ' + str(invest_loop_amount))


    else:



        request_body = {
        '_links': {
            'source': {
            'href': fundX_funding_source
            },
            'destination': {
            'href': investor_funding_source   
            }
        },
        'amount': {
            'currency': 'USD',
            'value': return_amount,
        },
        'metadata': {
            'note': 'GET Equity Partners ' + fund_name + ' investment'
        },
        'clearing': {
            'destination': 'next-available'
        },
        'correlationId': fund_ID,
        }

        transfer = dwolla_app_token.post('transfers', request_body, headers)
        transfer_url = transfer.headers['location'] 
        transfer = dwolla_app_token.get(transfer_url)
        transfer_status = transfer.body['status'] 

        transfer_list.append([transfer_url, transfer_status, return_amount])

        print('transfer_status: ' + transfer_status)

    return transfer_list













