from flask import Blueprint, jsonify, request, current_app
import re
import sys
import uuid
import datetime
from datetime import datetime
from GET_project.api.plaid import plaid_client, create_plaid_user_id
from GET_project import db


GET_invest_flow_step_2_linktoken_Blueprint = Blueprint('GET_invest_flow_step_2_linktoken', __name__)
@GET_invest_flow_step_2_linktoken_Blueprint.route('/api/invest_flow/step_2_linktoken/', methods=['GET', 'POST']) 

def GET_invest_flow_step_2_linktoken():


    print('MADE IT HERE')

    redirect_uri = current_app.config['SITE_DOMAIN'] + current_app.config['PLAID_REDIRECT_URI']

    investor_ID = request.json.get("investor_ID", None)
    email = request.json.get("email", None)
    pre_format_phone = request.json.get("phone", None)
    phone = '+' + re.sub('\D', '', pre_format_phone)

    print('phone: ------------------------_> ', phone)
    print('investor_ID: ------------------------_> ', investor_ID)


    #plaid wont allow duplicate client_user_id's
    # investor_ID = investor_ID + '___' + str(uuid.uuid5(uuid.NAMESPACE_DNS, str(datetime.now())))[:4]
    # print('investor_ID: ------------------------_> ', investor_ID)


    #plaid_products = ['auth','transactions','identity', 'investments'] 
    # plaid_products = ['income_verification']

    # If you know at the point of Link initialization that you will want to use Transactions with the linked Item, initialize Link with Transactions in order to start the product initialization process ahead of time.





    # ---- RETURNING USER EXPEIENCE TEST ----
    if current_app.config['TEST_PLAID_RUX']:
        print('TEST_PLAID_RUX')
        phone = "+1 415 555 0123"
        email = "example@plaid.com"

    # plaid_products = ['auth', 'income_verification']
    plaid_products = ['auth'] 

    plaid_response = plaid_client.link_token_create({
        'client_name': "GET",
        'products': plaid_products,
        'country_codes': current_app.config['PLAID_COUNTRY_CODES'],
        'language': "en",
        'redirect_uri': redirect_uri,
        'user': {
            'client_user_id':investor_ID,
            'phone_number': phone,
            'email_address': email
            }


            # for income testing only
            # user -- user_bank_income
            # pass -- "{}"
            # get income and mongo on public_token page
            # 'user_token': plaid_user_token,
            # 'income_verification': {
            # 'income_source_types':['bank'],
            # 'bank_income':{ 'days_requested': 730, 'enable_multiple_items': True},
            # },

        })
    
    link_token = plaid_response['link_token']
    print('LINK TOKEN', link_token)






    return jsonify(
        link_token=link_token,
        status="success",
        message="Link Token Created"
    ), 200


