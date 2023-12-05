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
import io
import gridfs
import codecs
import json
from tempfile import TemporaryFile
from PIL import Image

GET_two_factor_Blueprint = Blueprint('GET_two_factor', __name__)

@GET_two_factor_Blueprint.route('/api/login/two_factor/', methods=['POST']) # <- from '/'
def GET_two_factor():

    email = request.json.get('email', None)
    two_factor = request.json.get('two_factor', None)

    if two_factor is None:
        return jsonify({'msg':'Two factor code not entered'}), 401

    user = User(email=email, db=db)
    if int(two_factor) != int(user.two_factor_code):
        return jsonify({'msg': 'Code is not correct'}), 401

        
    try:
        fs = gridfs.GridFS(db)
        get_user = db.credentials.find_one({ "email": email })
        dashboard_config = get_user['dashboard_config']
        print('profile_img: ' + dashboard_config['profile_img'])
        profile_image = fs.get_last_version(dashboard_config['profile_img'])
        base64_data = codecs.encode(profile_image.read(), 'base64')
        profile_image = base64_data.decode('utf-8')
    except:
        dashboard_config = 'None'
        profile_image = 'None'

    print('profile_image: ' + str(profile_image))


    access_token = create_access_token(identity=user)
    response = jsonify({'msg':'Login successful', 'access_status':user.access_status, 'user_id':user.user_id, 'dashboard_config':dashboard_config, 'profile_image':profile_image })
    set_access_cookies(response, access_token)


    return response, 200




