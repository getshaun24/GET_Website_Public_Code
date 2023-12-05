from flask import Blueprint, session, url_for, request, redirect, jsonify
from flask_login import login_required
from flask_session import Session
import sys
import datetime
from datetime import datetime, timedelta
import uuid
from GET_project.api.functions import takeSecond
from GET_project import db 
from GET_project.api.dwolla import dwolla_check_verification_status


GET_invest_flow_step_4_Blueprint = Blueprint('GET_invest_flow_step_4', __name__)
@GET_invest_flow_step_4_Blueprint.route('/api/invest_flow/step_4/', methods=['GET', 'POST']) # <- from '/'
def GET_invest_flow_step_4():



    fund_ID = request.json.get("fund_ID", None)
    agree_to_all = request.json.get("agree_to_all", None)
    signature_typed = request.json.get("signature_typed", None)
    investor_ID = request.json.get("investor_ID", None)

    print('fund_ID', fund_ID)

    if agree_to_all != 'yes':
        return jsonify(status="error", message="Please agree to all terms." ), 200


    agree_path = 'investments.' + fund_ID + '.agree_to_all'
    signature_typed_path = 'investments.' + fund_ID + '.signature_typed'
    datetime_signed_path = 'investments.' + fund_ID + '.datetime_signed'
    db.investor_info.update({"investor_ID": investor_ID}, {"$set": { "signup_progress": 'step_4_completed', agree_path:agree_to_all, signature_typed_path:signature_typed, datetime_signed_path:datetime.today()}})


    fund_info = db.fund_details.find_one({ "fund_ID": fund_ID },{"minimum_investment_amount":1, "_id":0})
    minimum_investment_amount = fund_info['minimum_investment_amount']

    investor_info = db.investor_info.find_one({ "investor_ID": investor_ID },{"dwolla":1, "_id":0})
    customer_url = investor_info['dwolla']['customer_url']

    try:
        dwolla_customer_status, dwolla_beneficial_owner_status = dwolla_check_verification_status(customer_url)
    except:
        dwolla_customer_status = 'error'
        dwolla_beneficial_owner_status = 'error'
        print('error getting customer status')


    print(' Signed & Agreed ------------------------------------------------>')



    return jsonify(
        minimum_investment_amount=minimum_investment_amount,
        dwolla_customer_status=dwolla_customer_status,
        dwolla_beneficial_owner_status=dwolla_beneficial_owner_status,
        status="Step_4_Complete",
        message="Step 4 info added to db."
    ), 200








