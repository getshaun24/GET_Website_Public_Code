from flask import Blueprint, session, url_for, request, redirect, jsonify, current_app
from flask_login import login_required
from flask_session import Session
import sys
import datetime
from datetime import datetime, timedelta
import uuid
from flask_mail import Mail
from flask_mail import Message
from GET_project.api.mail import mail
from GET_project.api.functions import GET_fundX_ID
from GET_project.api.dwolla import dwolla_check_verification_status
from GET_project import db
import re
from random import randint


GET_invest_flow_step_1_Blueprint = Blueprint('GET_invest_flow_step_1', __name__)
@GET_invest_flow_step_1_Blueprint.route('/api/invest_flow/step_1/', methods=['GET', 'POST']) # <- from '/'
def GET_invest_flow_step_1():


    first_name = request.json.get("first_name", None)
    last_name = request.json.get("last_name", None)
    email = request.json.get("email", None)
    phone = request.json.get("phone", None)
    investment_amount = request.json.get("investment_amount", None)
    selected_fund = request.json.get("selected_fund", None)
    submitted_two_factor_code = request.json.get("submitted_two_factor_code", None)
    investor_ID = request.json.get("investor_ID", None)


    print('selected fund ------------------->', selected_fund)
    fundX_ID, fundX_name = GET_fundX_ID(selected_fund)
    print('fundX_ID ------------------->', fundX_ID)


    get_investor = db.investor_info.find_one({ "email": email })

    if submitted_two_factor_code != None:
         

        two_factor_code = get_investor['two_factor_code']
        if int(submitted_two_factor_code) == int(two_factor_code):
            investor_ID = get_investor['investor_ID']
            institution_ID = get_investor['investments'][fundX_ID]['active_institution_id']
            account_selected_value = get_investor['investments'][fundX_ID]['active_selected_bank_account_id']
            db.investor_info.update({"email": email}, {"$unset": {"two_factor_code": ''}})
            return jsonify(
                    investor_ID=investor_ID,
                    fund_ID=fundX_ID,
                    institution_ID=institution_ID,
                    account_selected_value=account_selected_value,
                    status="code_correct",
                    message="Two Factor Code Correct."
                ), 200
        else:
            db.investor_info.update({"email": email}, {"$unset": {"two_factor_code": ''}})
            return jsonify(
                    status="incorrect_code",
                    message="Incorrect Two Factor Code."
                ), 200


    if get_investor:
        if (
            get_investor['signup_progress'] == 'step_3_completed' or
            get_investor['signup_progress'] == 'step_4_completed' or
            get_investor['signup_progress'] == 'Document Verification Failed' or
            (
                'investments' in get_investor and 
                fundX_ID in get_investor['investments'] and 
                get_investor['investments'][fundX_ID]['investment_status'] == 'documents_pending_no_transaction_confirmation'
            )
        ):
     
            two_factor_code = randint(100000, 999999)
            db.investor_info.update({"email": email}, {"$set": {'two_factor_code': two_factor_code }})

            TEST_EMAIL_RECIPIENTS = current_app.config['TEST_EMAIL_RECIPIENTS']
            MAIL_USERNAME = current_app.config['MAIL_USERNAME']

            if TEST_EMAIL_RECIPIENTS == True:
                email_to = current_app.config['EMAIL_LIST']
            else:
                email_to = [email]

            msg = Message(
                        sender=MAIL_USERNAME,
                        recipients=email_to,
                        subject="GET Equity Partners - Temporary Two Factor Code",
                        html="<br> <b>Investment Process Temporary Two Factor Code - </b> " + str(two_factor_code)
                        )
            mail.send(msg)
            
            return jsonify(
                status="email_exists",
                message="This Email Already Exists."
            ), 200

        elif get_investor['signup_progress'] == 'Signup Successful' or get_investor['signup_progress'] == 'Documents Pending':

            return jsonify(
                status="already_invested",
                message="You already have an account, Please login to invest or signup with a new unique email"
            ), 200



    if investor_ID == '':
        investor_ID = str(uuid.uuid5(uuid.NAMESPACE_DNS, email + str(datetime.now().strftime("%m/%d/%Y, %H:%M:%S"))))
        db.investor_info.insert_one({
                "investor_ID": investor_ID,
                "date_user_created": datetime.today(),
                "signup_progress": 'step_1_completed',
                "first_name": first_name,
                "last_name": last_name,
                "email": email,
                "phone": phone,
                "investments": {
                fundX_ID: {
                        "fund_name": fundX_name,
                        "investment_amount": investment_amount,
                        "investment_status": "not_invested",
                        'additional_investments': []
                    }}})

    else:
        db.investor_info.update({"investor_ID": investor_ID}, {"$set": { 
                "date_user_created": datetime.today(),
                "signup_progress": 'step_1_completed',
                "first_name": first_name,
                "last_name": last_name,
                "email": email,
                "phone": phone,
                "investments": {
                fundX_ID: {
                        "fund_name": fundX_name,
                        "investment_amount": investment_amount,
                        "investment_status": "not_invested",
                        'additional_investments': []
                    }}}})
        



    return jsonify(
        fund_ID=fundX_ID,
        investor_ID=investor_ID,
        status="Step_1_Complete",
        message="Step 1 info added to db."
    ), 200


