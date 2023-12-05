from flask import Blueprint, session, url_for, request, redirect, render_template, flash, current_app, jsonify
from flask_session import Session
import pymongo
import sys
from GET_project.api.mail import mail
# from GET_project.api.mongo import mongo as db
from GET_project import db 
from random import randint
from flask_mail import Mail
from flask_mail import Message
import bcrypt
import uuid
import datetime
from datetime import datetime, timedelta
from GET_project.api.models import User



GET_login_Blueprint = Blueprint('GET_login', __name__)
@GET_login_Blueprint.route('/api/login/login/', methods=['POST']) # <- from '/'
def GET_login():

    email = request.json.get("email", None)
    password = request.json.get("password", None)

    # Here we do some code to make sure the username and password is correct.
    if email is None or password is None:
        return jsonify({'msg':"Email or password is missing"}), 401
    user = User(email, db)
    print(str(user))
    if user.id is None:
        return jsonify({'msg':"Account not registered"}), 401
    if not user.check_password(password):
        return jsonify({'msg':"Wrong password"}), 401

    # Set access token. 
    two_factor_code = '111'
    two_factor_recipient = current_app.config['EMAIL_LIST']

    if current_app.config['ENV'] == 'production':
        two_factor_code = randint(100000, 999999)
        two_factor_recipient = [user.email]

    user.update_two_factor_code(code=two_factor_code, db=db)

    # Send access token to via email
    msg = Message(sender=current_app.config['MAIL_USERNAME'],
        recipients=two_factor_recipient,
        subject="GET - 2 Factor Code",
        body="Please Use The Following Code: \n \n " + str(two_factor_code)
    )
    mail.send(msg)

    # Set cookies so that we have an identity to check the two factor code for in the next step.
    # access_token = create_access_token(identity=user.email)
    response = jsonify({"msg": "Credentials are good"})
    # set_access_cookies(response, access_token)
   
    return response, 200
