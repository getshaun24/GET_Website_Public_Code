from flask import Blueprint, jsonify, request, current_app
import sys
import json
import datetime
import uuid
import re
from datetime import date
from dateutil.tz import tzutc
from GET_project.api.plaid import plaid_client, create_plaid_user_id, update_plaid_link_token
from GET_project import db 
from GET_project.api.functions import json_serial
from flask_jwt_extended import jwt_required

GET_accred_linktoken_Blueprint = Blueprint('GET_accred_linktoken', __name__)
@GET_accred_linktoken_Blueprint.route('/api/get_accred/get_accred_linktoken/', methods=['GET', 'POST']) 
@jwt_required()
def GET_accred_linktoken():

    print('made it here --->')


    redirect_uri_3 = current_app.config['SITE_DOMAIN'] + current_app.config['PLAID_REDIRECT_URI_3']

    investor_ID = request.json.get("investor_ID", None)
    initialize_link_var = request.json.get("initialize_link_var", None)

    print('invest id', investor_ID)
    print('initialize_link_var', initialize_link_var)

    get_user = db.investor_info.find_one({ "investor_ID": investor_ID })
    print(get_user)
    plaid_access_token = get_user['plaid']['institutions'][-1]['plaid_access_token']
    institution_ID = get_user['plaid']['institutions'][-1]['institution_ID']
    plaid_user_token = get_user['plaid']['plaid_user_ids']['plaid_user_token']
    pre_format_phone = get_user['phone']
    phone = '+' + re.sub('\D', '', pre_format_phone)
    email = get_user['email']

    institution_array = []
    for institution in get_user['plaid']['institutions']:
        institution_array.append(institution['institution_ID'])



    # ----------------------------- INCOME Link Token   ------------------------------------------- 
        # ----------------------------- INCOME Link Token   ------------------------------------------- 
            # ----------------------------- INCOME Link Token   ------------------------------------------- 
                # ----------------------------- INCOME Link Token   ------------------------------------------- 
                    # ----------------------------- INCOME Link Token   ------------------------------------------- 


    # -------------- TEST SANDBOX -----------------------
    #To use the custom user, select a non-OAuth institution within Link 
    # and use username user_bank_income and password {}.


    if initialize_link_var == 'get_INCOME_link_token':
        plaid_income_product = ['income_verification']
        response = plaid_client.link_token_create(
            {
            'access_token':plaid_access_token,
            'user': {
                'client_user_id':investor_ID, 
                },
            'client_name': "Plaid Quickstart",
            'products': plaid_income_product,
            'country_codes': current_app.config['PLAID_COUNTRY_CODES'],
            'language': "en",
            'redirect_uri': redirect_uri_3,
            'user_token': plaid_user_token,
            'income_verification': {
                'income_source_types':['bank'],
                'bank_income':{ 'days_requested': 730, 'enable_multiple_items': True},
                },
            })
        link_token = response['link_token']



  # ----------------------------- INCOME Link Token   ------------------------------------------- 
        # ----------------------------- INCOME Link Token   ------------------------------------------- 
            # ----------------------------- INCOME Link Token   ------------------------------------------- 
                # ----------------------------- INCOME Link Token   ------------------------------------------- 
                    # ----------------------------- INCOME Link Token   ------------------------------------------- 


    if initialize_link_var == 'get_AUTH_link_token':

        # ---- RETURNING USER EXPEIENCE TEST ----
        if current_app.config['TEST_PLAID_RUX']:
            phone = "+1 415 555 0123"
            email = "example@plaid.com"


        plaid_products = ['auth'] 
        plaid_response = plaid_client.link_token_create({
            'client_name': "GET Website",
            'products': plaid_products,
            'country_codes': ["US", "CA"],
            'language': "en",
            'redirect_uri': redirect_uri_3,
            'user': {
                'client_user_id':investor_ID,
                'phone_number': phone,
                'email_address': email
                }})
        
        link_token = plaid_response['link_token']






    return jsonify(
        institution_ID=institution_ID,
        institution_array=institution_array,
        link_token=link_token,
        status="success",
        message="Link Token Created"
    ), 200


