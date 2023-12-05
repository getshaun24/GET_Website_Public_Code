from flask import Blueprint, session, url_for, request, redirect, render_template, flash, current_app, jsonify
from flask_session import Session
import pymongo
import sys
from GET_project.api.mail import mail
# from GET_project.api.mongo import mongo as db
from GET_project import db 
from flask_jwt_extended import jwt_required

Manager_Home_Blueprint = Blueprint('Manager_Home', __name__)
@Manager_Home_Blueprint.route('/api/manager_dashboard/manager_home/', methods=['POST']) # <- from '/'
@jwt_required()
def Manager_Home():

    manager_ID = request.json.get("manager_ID", None)

    get_manager = db.credentials.find_one({ "user_id": manager_ID })
    manager_email = get_manager["email"]

    
    return jsonify(
            manager_email=manager_email
        ), 200
