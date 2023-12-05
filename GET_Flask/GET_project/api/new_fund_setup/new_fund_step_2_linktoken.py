from flask import Blueprint, jsonify, current_app, request
import sys
from GET_project.api.plaid import plaid_client


GET_new_fund_setup_step_2_linktoken_Blueprint = Blueprint('GET_new_fund_setup_step_2_linktoken', __name__)
@GET_new_fund_setup_step_2_linktoken_Blueprint.route('/api/new_fund_setup/new_fund_step_2_linktoken/', methods=['GET', 'POST']) 

def GET_new_fund_setup_step_2_linktoken():


    print('MADE IT HERE FUND SETUP LINK')

    redirect_uri_4 = current_app.config['SITE_DOMAIN'] + current_app.config['PLAID_REDIRECT_URI_4']

    fund_ID = request.json.get("fund_ID", None)


    plaid_products = ['auth']

    response = plaid_client.link_token_create(
        {
        'user': {
            'client_user_id': fund_ID,
            },
        'client_name': "GET Website",
        'products': plaid_products,
        'country_codes': current_app.config['PLAID_COUNTRY_CODES'],
        'language': "en",
        'redirect_uri': redirect_uri_4,
        })



    link_token = response['link_token']

    print('LINK TOKEN', link_token)


    return jsonify(
        link_token=link_token,
        status="success",
        message="Link Token Created"
    ), 200


