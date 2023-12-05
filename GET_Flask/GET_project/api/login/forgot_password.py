from flask import Blueprint, session, url_for, request, redirect, render_template, flash, current_app, jsonify
from flask_session import Session
import pymongo
import sys
from GET_project.api.mail import mail, get_html_forgot_pw
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

from GET_project.api.functions import confirm_password_token, get_token_data, generate_password_token


GET_forgot_password_Blueprint = Blueprint('GET_forgot_password', __name__)

@GET_forgot_password_Blueprint.route('/api/login/forgot_password/', methods=['GET', 'POST']) # <- from '/'
def GET_forgot_password():


    pass_method = request.json.get("pass_method", None)

    if pass_method == 'email':

        email = request.json.get("email", None)

        user = User(email, db)
        if email is None:
            return jsonify({'msg':"Email is missing"}), 401
        if user.id is None:
            return jsonify({'msg':"Account does not exist"}), 401

        TEST_EMAIL_RECIPIENTS = current_app.config['TEST_EMAIL_RECIPIENTS']
        MAIL_USERNAME = current_app.config['MAIL_USERNAME']
        SITE_DOMAIN = current_app.config['SITE_DOMAIN']

        data_to_load = {'user_ID': user.id, 'email': email} 
        email_url_link = SITE_DOMAIN + '/login_pages/forgot_password/?ivid=' + generate_password_token(data_to_load)

        new_investor_email = get_html_forgot_pw(email_url_link)

        if TEST_EMAIL_RECIPIENTS == True:
            email_to = current_app.config['EMAIL_LIST']
        else:
            email_to = [email]

        msg = Message(
                    sender=MAIL_USERNAME,
                    recipients=email_to,
                    subject="GET Equity Partners - Update Password",
                    html=new_investor_email
                    )
        mail.send(msg)


        return jsonify({'msg':"email_sent"}), 200

    elif pass_method == 'update_the_pass':

        token = request.json.get('ivid', None)
        password = request.json.get('password', None)

        print('------------------------------------- xxx ---------------------------------------------------')
        print(token)
        print(password)
        print('------------------------------------- xxx ---------------------------------------------------')

        if token is None:
            return jsonify(msg='No token provided as a parameter', status='token_error'), 400
        token_valid = confirm_password_token(token, expire_time=10000000)

        if password is None:
            return jsonify(msg='Did not recieve passwords', status='token_error')
        
        if token_valid:
            
            token_data = get_token_data(token, expire_time=10000000)

            user = User(email=token_data['user_ID'], db=db)
            investor_ID = user.user_id

            password = request.json.get("password", None)

        db.credentials.update({"user_id": investor_ID}, {"$set": { "password": bcrypt.hashpw(password.encode('utf8'), bcrypt.gensalt())}})

        return jsonify({'msg':"password_updated", "investor_ID": investor_ID}), 200




