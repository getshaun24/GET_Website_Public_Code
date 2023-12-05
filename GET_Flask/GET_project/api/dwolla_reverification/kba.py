from flask import Blueprint, session, url_for, request, redirect, jsonify
from flask_login import login_required
from flask_session import Session
import sys
import datetime
from datetime import datetime, timedelta
import time
import uuid
from GET_project.api.functions import takeSecond
from GET_project import db 
from GET_project.api.dwolla import dwolla_app_token, dwolla_check_verification_status



GET_dwolla_kba_Blueprint = Blueprint('GET_dwolla_kba', __name__)
@GET_dwolla_kba_Blueprint.route('/api/dwolla_reverification/kba/', methods=['GET', 'POST']) 


def GET_dwolla_kba():

    print('KBA 2')

    investor_ID = request.json.get("investor_ID", None)
    kba_action = request.json.get("kba_action", None)
    kba_answers = request.json.get("kba_answers", None)
    kba_url_return = request.json.get("kba_url_return", None)
    investor_info = db.investor_info.find_one({ "investor_ID": investor_ID },{"dwolla":1, "_id":0})
    dwolla_customer_url = investor_info['dwolla']['customer_url']



    if kba_action == 'start':
        dwolla_customer_status = None
        dwolla_beneficial_owner_status = None
        try:
            kba = dwolla_app_token.post('%s/kba' % dwolla_customer_url)
            kba_url = kba.headers['location'] 
            kba_response = dwolla_app_token.get(kba_url)
            kba_questions = kba_response.body['questions']
            status = 'kba_questions_recieved'
            message = 'KBA questions recieved'
        except:
            kba_url = None
            kba_questions = None
            status = 'kba_questions_error'
            message = 'KBA questions error'

            count = 0
            while count < 6:
                time.sleep(5)
                count += 1
                dwolla_customer_status, dwolla_beneficial_owner_status = dwolla_check_verification_status(dwolla_customer_url)
                if dwolla_customer_status != 'kba':
                    break

            dwolla_customer_status, dwolla_beneficial_owner_status = dwolla_check_verification_status(dwolla_customer_url)

    else:
        kba_url = None
        kba_questions = None
        try:
            request_body = {'answers' : kba_answers}
            send_kba_answers = dwolla_app_token.post (kba_url_return, request_body)
            status = 'kba_answers_recieved'
            message = 'KBA answers recieved'
        except:
            status = 'kba_answers_error'
            message = 'KBA answers error'


        count = 0
        while count < 6:
            time.sleep(5)
            count += 1
            dwolla_customer_status, dwolla_beneficial_owner_status = dwolla_check_verification_status(dwolla_customer_url)
            if dwolla_customer_status != 'kba':
                break



    return jsonify(
        kba_url=kba_url,
        kba_questions=kba_questions,
        dwolla_customer_status=dwolla_customer_status,
        dwolla_beneficial_owner_status=dwolla_beneficial_owner_status,
        status=status,
        message=message
    ), 200
