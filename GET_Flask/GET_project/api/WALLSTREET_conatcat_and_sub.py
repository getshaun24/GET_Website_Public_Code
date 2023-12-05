from flask import Blueprint, session, url_for, request, redirect, jsonify, current_app
from flask_login import login_required
from flask_session import Session
import sys
import datetime
from datetime import datetime, timedelta
import uuid
from GET_project.api.functions import GET_fundX_ID
from GET_project import db
from flask_mail import Message
from GET_project.api.mail import mail
import re



WALLSTREET_conatcat_and_sub_Blueprint = Blueprint('WALLSTREET_conatcat_and_sub', __name__)
@WALLSTREET_conatcat_and_sub_Blueprint.route('/api/WALLSTREET_conatcat_and_sub/', methods=['GET', 'POST']) # <- from '/'
def WALLSTREET_conatcat_and_sub():



    subscribe_email = request.json.get("subscribe_email", None)
    subscribe_name = request.json.get("subscribe_name", None)

    first_name = request.json.get("first_name", None)
    last_name = request.json.get("last_name", None)
    contact_email = request.json.get("contact_email", None)
    phone = request.json.get("phone", None)
    message = request.json.get("message", None)



    MAIL_USERNAME = current_app.config['MAIL_USERNAME']
    EMAIL_LIST = current_app.config['EMAIL_LIST']

    if subscribe_email:
        if db.WALLSTREET_email_subscriber_list.find_one({ "subscribe_email": subscribe_email }):
            status = "email_already_subscribed"
            message = "This Email Has Already Been Subscribed"
        else:
            db.WALLSTREET_email_subscriber_list.insert_one({
                    "subscriber_email": subscribe_email,
                    "subscribe_name": subscribe_name,
                    "datetime_subscribed": datetime.now().strftime("%m/%d/%Y, %H:%M:%S")
            })


            # ----------------------------- Internal Info Email --------------------------------

            
            new_email_sub = "New Subscriber - " + str(subscribe_name) + "<br> " + "Email - " + str(subscribe_email)

            msg = Message(
                        sender=MAIL_USERNAME,
                        recipients=EMAIL_LIST,
                        subject="WALLSTREET New Email Subscriber",
                        html=new_email_sub
                        )
            mail.send(msg)

            status="success_email_added",
            message="Success, You Have Been Added To The Email List"


    elif contact_email:

        # ----------------------------- Internal Info Email --------------------------------

            
            new_contact = "Fist Name - " + str(first_name) + "<br>" + "Last Name - " + str(last_name) + "<br>" + "Contact Email - " + str(contact_email) + "<br>" + "Phone - " + str(phone) + "<br>" + "Message - " + str(message)


            msg = Message(
                        sender=MAIL_USERNAME,
                        recipients=EMAIL_LIST,
                        subject="WALLSTREET Contact Form",
                        html=new_contact
                        )
            mail.send(msg)

            status="success_contact_sent",
            message="Success, Your Message Has Been Sent and We Will Be In Touch Shortly"

    else:
        status="error",
        message="Error, Please Try Again"



    return jsonify(
        status=status,
        message=message
    ), 200

