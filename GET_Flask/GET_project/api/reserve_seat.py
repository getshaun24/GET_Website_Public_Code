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



GET_reserve_seat_Blueprint = Blueprint('GET_reserve_seat', __name__)
@GET_reserve_seat_Blueprint.route('/api/reserve_seat/', methods=['GET', 'POST']) # <- from '/'
def GET_reserve_seat():



    first_name = request.json.get("first_name", None)
    last_name = request.json.get("last_name", None)
    email = request.json.get("email", None)
    phone = request.json.get("phone", None)
    investment_amount = request.json.get("investment_amount", None)
    fund_reserved: str = request.json.get("fund_reserved", None)
    datetime_reserved = datetime.now().strftime("%m/%d/%Y, %H:%M:%S")


    MAIL_USERNAME = current_app.config['MAIL_USERNAME']
    EMAIL_LIST = current_app.config['EMAIL_LIST']

    if email:
        if db.fund_reserve_list.find_one({ "email": email }):
            status = "email_already_reserved"
            message = "A Seat Has Already Been Reserved With This Email"
        else:
            db.fund_reserve_list.insert_one({
                    "email": email,
                    "datetime_reserved": datetime_reserved,
                    "fund_reserved": fund_reserved,
                    "first_name": first_name,
                    "last_name": last_name,
                    "phone": phone,
                    "investment_amount": investment_amount
            })



        # ----------------------------- Internal Info Email --------------------------------

            
            new_reserve = "Fist Name - " + str(first_name) + "<br>" + "Last Name - " + str(last_name) + "<br>" + "Email - " + str(email) + "<br>" + "Phone - " + str(phone) + "<br>" + "Investment Amount - " + str(investment_amount) + "<br>" + "Fund Reserved - " + str(fund_reserved) + "<br>" + "DateTime Reserved - " + str(datetime_reserved)


            msg = Message(
                        sender=MAIL_USERNAME,
                        recipients=EMAIL_LIST,
                        subject="GET Contact Form",
                        html=new_reserve
                        )
            mail.send(msg)

            status="success_reserved",
            message="Success, your seat has been reserved and we will be in touch shortly."

    else:
        status="error",
        message="Error, Please Try Again"



    return jsonify(
        status=status,
        message=message
    ), 200

