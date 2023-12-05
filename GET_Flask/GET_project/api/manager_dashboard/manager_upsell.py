from flask import Blueprint, session, url_for, request, redirect, render_template, flash, current_app, jsonify
from flask_session import Session
import pymongo
import sys
from GET_project.api.mail import mail
# from GET_project.api.mongo import mongo as db
from GET_project import db 
from flask_jwt_extended import jwt_required
from GET_project.api.functions import GET_fundX_ID
from GET_project.api.functions import generate_password_token
from GET_project.api.mail import mail, get_upsell_template
from flask_mail import Mail
from flask_mail import Message

Manager_Upsell_Blueprint = Blueprint('Manager_Upsell', __name__)
@Manager_Upsell_Blueprint.route('/api/manager_dashboard/manager_upsell/', methods=['POST']) # <- from '/'
@jwt_required()
def Manager_Upsell():


    investor_email = request.json.get("investor_email", None)
    selected_fund = request.json.get("selected_fund", None)

    print('selected fund ------------------->', selected_fund)
    fundX_ID, fundX_name = GET_fundX_ID(selected_fund)

    try:
        investor_info = db.investor_info.find_one({ "email": investor_email },{"investor_ID":1, "_id":0})
        investor_ID = investor_info['investor_ID']
    except:
        return jsonify(status='email_does_not_exist'), 200

         # ----------------------------- investor_email --------------------------------

    TEST_EMAIL_RECIPIENTS = current_app.config['TEST_EMAIL_RECIPIENTS']
    MAIL_USERNAME = current_app.config['MAIL_USERNAME']
    SITE_DOMAIN = current_app.config['SITE_DOMAIN']
    # SITE_DOMAIN = 'http://127.0.0.1:3000'
    EMAIL_LIST = current_app.config['EMAIL_LIST']
    # email_url_link = EMAIL_DOMAIN + '/investor_dashboard/investor_welcome/?ivid=' + investor_ID
    data_to_load = {'investor_ID': investor_ID, 'fundX_ID': fundX_ID} # Anything else to add???
    email_url_link = SITE_DOMAIN + '/investor_dashboard/solidify_investment/?ivid=' + generate_password_token(data_to_load)

    new_investor_email = get_upsell_template(email_url_link)

    if TEST_EMAIL_RECIPIENTS == True:
        email_to = EMAIL_LIST
    else:
        email_to = [investor_email]

    msg = Message(

                sender=MAIL_USERNAME,
                recipients=email_to,
                subject="GET Equity Partners - Solidifying Your Investment",
                html=new_investor_email
                )
    mail.send(msg)

    status='success'

    
    return jsonify(
            status=status
        ), 200
