from flask import Blueprint, session, url_for, request, redirect, jsonify
from flask_login import login_required
from flask_session import Session
import sys
import datetime
from datetime import datetime, timedelta
import uuid
from GET_project.api.functions import takeSecond
from GET_project import db
from GET_project.api.dwolla import dwolla_app_token, dwolla_check_verification_status
import gridfs
import time
import codecs
from werkzeug.datastructures import ImmutableMultiDict
import json
import io
import dwollav2



GET_dwolla_new_fund_documents_needed_Blueprint = Blueprint('GET_dwolla_new_funds_documents_needed', __name__)
@GET_dwolla_new_fund_documents_needed_Blueprint.route('/api/new_fund_setup/new_fund_docs_needed/', methods=['GET', 'POST']) 

def GET_dwolla_new_funds_documents_needed():

    print('made it to new fund docs needed')

    file_list = []
    for filename, file in request.files.items():
        file_list.append(filename)
        print(filename)
        print(file)
    fund_ID = request.form['fund_ID']
    investing_as = request.form['investing_as']
    individual_verification_type = request.form['individual_verification_type']
    sole_prop_verification_type = request.form['sole_prop_verification_type']
    controller_verification_type = request.form['controller_verification_type']
    owner_verification_type = request.form['owner_verification_type']


    print('fund_ID : ' + fund_ID)


    fund_details = db.fund_details.find_one({ "fund_ID": fund_ID },{"dwolla":1, "_id":0})
    customer_url = fund_details['dwolla']['customer_url']

    if investing_as == 'individual':

        uploaded_document = request.files['file_1']
        
        uploaded_document_name = individual_verification_type
        uploaded_document_uuid = str(uuid.uuid1())
        document_path = 'KYC.uploaded_documents'
        db.fund_details.update({"fund_ID": fund_ID}, {"$push": { document_path: {uploaded_document_name: uploaded_document_uuid}}})

        fs = gridfs.GridFS(db)
        fs.put(uploaded_document, filename=uploaded_document_uuid)

        uploaded_document.stream.seek(0)                    
        uploaded_document = io.BytesIO(uploaded_document.read())

        try:
            dwolla_app_token.post('%s/documents' % customer_url, file = uploaded_document, documentType = uploaded_document_name)
        except dwollav2.error.Error as e:
            print('dwolla_error_code', e.body['code'])
            print('dwolla_error_message', e.body['message'])


    elif investing_as == 'soleProprietorship':

        uploaded_document_1 = request.files['file_1']
        uploaded_document_2 = request.files['file_2']

        uploaded_document_name_1 = sole_prop_verification_type
        uploaded_document_uuid_1 = str(uuid.uuid1())
        uploaded_document_name_2 = 'other'
        uploaded_document_uuid_2 = str(uuid.uuid1())

        document_path = 'KYC.uploaded_documents'
        db.fund_details.update({"fund_ID": fund_ID}, {"$push": { document_path: { "$each": [{uploaded_document_name_1: uploaded_document_uuid_1}, {uploaded_document_name_2: uploaded_document_uuid_2}]} }})

        fs = gridfs.GridFS(db)
        fs.put(uploaded_document_1, filename=uploaded_document_uuid_1)
        fs.put(uploaded_document_2, filename=uploaded_document_uuid_2)

        uploaded_document_1.stream.seek(0)                    
        uploaded_document_1 = io.BytesIO(uploaded_document_1.read())
        try:
            dwolla_app_token.post('%s/documents' % customer_url, file = uploaded_document_1, documentType = uploaded_document_name_1)
        except dwollav2.error.Error as e:
            print('dwolla_error_code', e.body['code'])
            print('dwolla_error_message', e.body['message'])
        
        uploaded_document_2.stream.seek(0)                    
        uploaded_document_2 = io.BytesIO(uploaded_document_2.read())
        try:
            dwolla_app_token.post('%s/documents' % customer_url, file = uploaded_document_2, documentType = uploaded_document_name_2)
        except dwollav2.error.Error as e:
            print('dwolla_error_code', e.body['code'])
            print('dwolla_error_message', e.body['message'])
        
        if "file_3" in file_list:
            uploaded_document_3 = request.files['file_3']
            uploaded_document_name_3 = 'other'
            uploaded_document_uuid_3 = str(uuid.uuid1())

            db.fund_details.update({"fund_ID": fund_ID}, {"$push": { document_path: {uploaded_document_name_3: uploaded_document_uuid_3}}})
            fs.put(uploaded_document_3, filename=uploaded_document_uuid_3)

            uploaded_document_3.stream.seek(0)                    
            uploaded_document_3 = io.BytesIO(uploaded_document_3.read())
            try:
                dwolla_app_token.post('%s/documents' % customer_url, file = uploaded_document_3, documentType = uploaded_document_name_3)
            except dwollav2.error.Error as e:
                print('dwolla_error_code', e.body['code'])
                print('dwolla_error_message', e.body['message'])

    else:
        print('entity docs')
        uploaded_document_1 = request.files['file_1']
        uploaded_document_2 = request.files['file_2']
        uploaded_document_3 = request.files['file_3']
        
        uploaded_document_name_1 = controller_verification_type
        uploaded_document_uuid_1 = str(uuid.uuid1())
        uploaded_document_name_2 = owner_verification_type 
        uploaded_document_uuid_2 = str(uuid.uuid1())
        uploaded_document_name_3 = 'other'
        uploaded_document_uuid_3 = str(uuid.uuid1())


        document_path = 'KYC.uploaded_documents'
        db.fund_details.update({"fund_ID": fund_ID}, {"$push": { document_path: { "$each": [{uploaded_document_name_1: uploaded_document_uuid_1}, {uploaded_document_name_2: uploaded_document_uuid_2}, {uploaded_document_name_3: uploaded_document_uuid_3}]} }})
        
        fs = gridfs.GridFS(db)
        fs.put(uploaded_document_1, filename=uploaded_document_uuid_1)
        fs.put(uploaded_document_2, filename=uploaded_document_uuid_2)
        fs.put(uploaded_document_3, filename=uploaded_document_uuid_3)

        uploaded_document_1.stream.seek(0)                    
        uploaded_document_1 = io.BytesIO(uploaded_document_1.read())
        try:
            dwolla_app_token.post('%s/documents' % customer_url, file = uploaded_document_1, documentType = uploaded_document_name_1)
        except dwollav2.error.Error as e:
            print('dwolla_error_code', e.body['code'])
            print('dwolla_error_message', e.body['message'])
        
        uploaded_document_2.stream.seek(0)                    
        uploaded_document_2 = io.BytesIO(uploaded_document_2.read())
        try:
            dwolla_app_token.post('%s/documents' % customer_url, file = uploaded_document_2, documentType = uploaded_document_name_2)
        except dwollav2.error.Error as e:
            print('dwolla_error_code', e.body['code'])
            print('dwolla_error_message', e.body['message'])
        
        uploaded_document_3.stream.seek(0)                    
        uploaded_document_3 = io.BytesIO(uploaded_document_3.read())
        try:
            dwolla_app_token.post('%s/documents' % customer_url, file = uploaded_document_3, documentType = uploaded_document_name_3)
        except dwollav2.error.Error as e:
            print('dwolla_error_code', e.body['code'])
            print('dwolla_error_message', e.body['message'])
     

        if "file_4" in file_list:
            uploaded_document_4 = request.files['file_4']
            uploaded_document_name_4 = 'other'
            uploaded_document_uuid_4 = str(uuid.uuid1())

            db.fund_details.update({"fund_ID": fund_ID}, {"$push": { document_path: {uploaded_document_name_4: uploaded_document_uuid_4}}})
            fs.put(uploaded_document_4, filename=uploaded_document_uuid_4)

            uploaded_document_4.stream.seek(0)                    
            uploaded_document_4 = io.BytesIO(uploaded_document_4.read())
            try:
                dwolla_app_token.post('%s/documents' % customer_url, file = uploaded_document_4, documentType = uploaded_document_name_4)
            except dwollav2.error.Error as e:
                print('dwolla_error_code', e.body['code'])
                print('dwolla_error_message', e.body['message'])





    db.fund_details.update({"fund_ID": fund_ID}, {"$set": {
        "signup_progress": 'Documents Pending'
    }})
    

    count = 0
    while count < 6:
        time.sleep(5)
        count += 1
        dwolla_customer_status, dwolla_beneficial_owner_status = dwolla_check_verification_status(customer_url)
        if dwolla_customer_status != 'retry' and dwolla_beneficial_owner_status != 'retry':
            break

    dwolla_customer_status, dwolla_beneficial_owner_status = dwolla_check_verification_status(customer_url)

    print('document upload success')

    return jsonify(
        dwolla_customer_status=dwolla_customer_status,  
        dwolla_beneficial_owner_status=dwolla_beneficial_owner_status,
        status="Document_Complete",
        message="Documents uploaded successfully"
    ), 200










