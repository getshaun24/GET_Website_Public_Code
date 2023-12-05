from flask import Blueprint, session, url_for, request, redirect, render_template, flash, jsonify
from flask_session import Session
import pymongo
import sys
# from server import mongo_client, mongoDB_master_access
# from GET_project.api.mongo import mongo as db
from GET_project import db
from random import randint
from GET_project.api.models import User
import flask_login
from flask_jwt_extended import create_access_token, set_access_cookies
from GET_project.api.functions import confirm_password_token, get_token_data
import bcrypt

GET_create_user_Blueprint = Blueprint('GET_create_user', __name__)
@GET_create_user_Blueprint.route('/api/login/create_user/', methods=['POST']) # <- from '/'
def GET_create_user():

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

        investor_ID = token_data['user_ID']
        print('------------------------------------- xxx ---------------------------------------------------')
        print(token_data['email'])
        print(investor_ID)
        print('------------------------------------- xxx ---------------------------------------------------')
        

        if token_data is not None:
            if token_data['email'] is not None and token_data['user_ID']:
                user = None
                user = User(email=token_data['email'], db=db)
                if user.id is not None:
                    print('User already exists')
                    return jsonify(msg='User already exists',  status='token_error'), 403
                else:
                    db.credentials.insert_one({
                        "email": token_data['email'],
                        "password": bcrypt.hashpw(password.encode('utf8'), bcrypt.gensalt()),
                        "access_status": 'investor',
                        "user_id": token_data['user_ID'],
                    })
                    
                user = User(email=token_data['email'], db=db)
                investor = db.investor_info.find_one({'investor_ID': token_data['user_ID']}, {'accredation_status': 1})
                print(investor['accredation_status'])
                if 'accredation_status' in investor:
                    accredation_status = investor['accredation_status']
                    access_token = create_access_token(identity=user)
                    response = jsonify({'msg':'User added', 'access_status':user.access_status, 'accredation_status':accredation_status, 'investor_ID':investor_ID})
                    set_access_cookies(response, access_token)
                    print('ACCRED')
                    return response, 200
                else:
                    access_token = create_access_token(identity=user)
                    response = jsonify({'msg':'User added but could not determine accrediation status.', 'access_status':user.access_status, 'investor_ID':investor_ID})
                    set_access_cookies(response, access_token)
                    return response, 200
            else:
                print('Token was corrupted')
                return jsonify(msg='Token was corrupted', status='token_error'), 403
        else:
            print('Could not retrieve token data')
            return jsonify(msg='Could not retrieve token data',  status='token_error'), 403
    else:
        print('Token is not valid')
        return jsonify(msg='Token is not valid',  status='token_error'), 403

    