from flask import Blueprint, request, jsonify
import sys

from plaid.model.item_public_token_exchange_request import ItemPublicTokenExchangeRequest
import datetime
from datetime import datetime
from flask import request
# from server import plaid_client, is_live_production_env



from GET_project.api.plaid import plaid_client, get_plaid_auth
from GET_project import db


GET_new_fund_setup_step_2_publictoken_Blueprint = Blueprint('GET_new_fund_setup_step_2_publictoken', __name__)
@GET_new_fund_setup_step_2_publictoken_Blueprint.route('/api/new_fund_setup/new_fund_step_2_publictoken/', methods=['GET', 'POST']) # 


def GET_new_fund_setup_step_2_publictoken():


    print('MADE IT HERE')



    fund_ID = request.json.get("fund_ID", None)
    public_token = request.json.get("public_token", None)
    meta_data = request.json.get("meta_data", None)

    print('meta_data: ', meta_data)
    # selected_account_id = meta_data['account']['id']
    # selected_account_id = 'xxx_test'
    # selected_account_name = 'yyy_test'

        
    exchange_response = plaid_client.item_public_token_exchange(ItemPublicTokenExchangeRequest(public_token=public_token))

    print('exchange_response -->', exchange_response)

    #pretty_print_response(exchange_response.to_dict())
    access_token = exchange_response['access_token']
    item_id = exchange_response['item_id']



            # Get Auth
    auth_response, account_ids_list, account_list = get_plaid_auth(access_token)
    institution_ID = auth_response['item']['institution_id']


            
    plaid_data_dict = {"Plaid": { institution_ID: {"plaid_access_token": access_token, "plaid_pull":{"Pull_date":'{:%Y-%m-%d}'.format(datetime.now()), "Auth":auth_response,}} }}






    plaid_data_dict = {"plaid": { "plaid_access_token": access_token, "institutions":[{"institution_ID":institution_ID, "plaid_pulls":[{"Pull_date":'{:%Y-%m-%d}'.format(datetime.now()), "Auth":auth_response}]}]
                                }}
     
  
     
    db.fund_details.update({"fund_ID": fund_ID}, {"$set": plaid_data_dict})

    print('Plaid Added --------------------------------------------------------------------------->')



    return jsonify(
        data=account_list,
        status="success",
        message="Public token received"
    ), 200


