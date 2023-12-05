from flask import Blueprint, session, url_for, request, redirect, jsonify
from flask_login import login_required
from flask_session import Session
import sys
import datetime
from datetime import datetime, timedelta
import uuid
from GET_project.api.functions import takeSecond
from GET_project import db
import gridfs
import time
import codecs
from werkzeug.datastructures import ImmutableMultiDict
import json
import io
from tempfile import TemporaryFile
from PIL import Image
from flask_jwt_extended import jwt_required

GET_upload_profile_config_Blueprint = Blueprint('GET_upload_profile_config', __name__)
@GET_upload_profile_config_Blueprint.route('/api/dashboard_config/upload_profile/', methods=['GET', 'POST']) 
@jwt_required()
def GET_upload_profile_config():

    print('made it to profile img upload')


    file_list = []
    for filename, file in request.files.items():
        print('test')
        file_list.append(filename)
        print(filename)
        print(file)
    manager_ID = request.form['manager_ID']

    print('manager_ID : ' + manager_ID)


    user_info = db.credentials.find_one({ "user_id": manager_ID },{"dashboard_config":1})
    current_profile_imgae = user_info['dashboard_config']['profile_img'] # <-- Image to be deleted


    uploaded_document = request.files['file_1']
    orig_image = Image.open(uploaded_document)
    rgb_image = orig_image.convert('RGB')
    new_width = 150
    width, height = rgb_image.size   # Get dimensions
    aspect_ratio = height / width
    new_height = int(new_width * aspect_ratio)
    resized_image = rgb_image.resize((new_width, new_height), Image.ANTIALIAS)


    temp_file = TemporaryFile()
    resized_image.save(temp_file, 'jpeg')
    temp_file.seek(0)
    resized = temp_file.read()

    
    profile_uuid = str(uuid.uuid1())
    db.credentials.update({"user_id": manager_ID}, {"$set": { 'dashboard_config': {'profile_img': profile_uuid}}})
    fs = gridfs.GridFS(db)
    fs.put(resized, filename=profile_uuid)
    temp_file.close()


    #delete old profile image
    fs.delete(current_profile_imgae)

    #send image back to client
    profile_image = fs.get_last_version(profile_uuid)
    base64_data = codecs.encode(profile_image.read(), 'base64')
    profile_image = base64_data.decode('utf-8')


    return jsonify(
        status="Document_Complete",
        message="Documents uploaded successfully",
        profile_image=profile_image
    ), 200










