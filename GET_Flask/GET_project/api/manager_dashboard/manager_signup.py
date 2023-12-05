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
from flask_jwt_extended import create_access_token, set_access_cookies


Manager_Signup_Blueprint = Blueprint('Manager_Signup', __name__)
@Manager_Signup_Blueprint.route('/api/manager_dashboard/manager_signup/', methods=['POST']) # <- from '/'
def Manager_Signup():

    email = request.json.get("email", None)
    password = request.json.get("password", None)
    token = request.json.get("manager_access_token", None)


    # Here we do some code to make sure the username and password is correct.
    if email is None or password is None or token is None:
        return jsonify({'msg':"Email, password or token is missing"}), 401
    if email.split('@')[-1] != 'thisisget.com':
        return jsonify({'msg':"Email must be a GET email"}), 401
    if token != current_app.config['REGISTER_MANAGER_TOKEN']:
        return jsonify({'msg':"Token is incorrect"}), 401
    
    user = None
    user = User(email=email, db=db)
    if hasattr(user, 'email'):
        return jsonify(msg='User already exists'), 403
    else:
        db.credentials.insert_one({
            "email": email,
            "password": bcrypt.hashpw(password.encode('utf8'), bcrypt.gensalt()),
            "access_status": 'manager',
            "user_id": str(uuid.uuid1())
        })

        user = User(email=email, db=db)
        # Set cookies so that we have an identity to check the two factor code for in the next step.
        access_token = create_access_token(identity=user)
        response = jsonify({"msg": "create_user_success"})
        set_access_cookies(response, access_token)
    
        return response, 200
