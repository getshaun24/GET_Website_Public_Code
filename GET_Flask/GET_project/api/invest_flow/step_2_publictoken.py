from flask import Blueprint, request, jsonify
import sys

from plaid.model.item_public_token_exchange_request import ItemPublicTokenExchangeRequest
import datetime
from datetime import datetime
from flask import request
# from server import plaid_client, is_live_production_env



from GET_project.api.plaid import plaid_client, get_plaid_auth, get_plaid_income, create_plaid_user_id
from GET_project import db 


GET_invest_flow_step_2_publictoken_Blueprint = Blueprint('GET_invest_flow_step_2_publictoken', __name__)
@GET_invest_flow_step_2_publictoken_Blueprint.route('/api/invest_flow/step_2_publictoken/', methods=['GET', 'POST']) # 


def GET_invest_flow_step_2_publictoken():


    print('MADE IT HERE')



    investor_ID = request.json.get("investor_ID", None)
    public_token = request.json.get("public_token", None)
    meta_data = request.json.get("meta_data", None)


    print('meta_data: ', meta_data, file=sys.stderr)

        
    exchange_response = plaid_client.item_public_token_exchange(ItemPublicTokenExchangeRequest(public_token=public_token))

    print('exchange_response -->', exchange_response)

    #pretty_print_response(exchange_response.to_dict())
    access_token = exchange_response['access_token']
    item_id = exchange_response['item_id']


      #      Get Auth
    auth_response, account_ids_list, account_list = get_plaid_auth(access_token)

    institution_ID = auth_response['item']['institution_id']


    try:
      plaid_user_token, plaid_user_id, plaid_request_id = create_plaid_user_id(investor_ID)

      plaid_data_dict = {"signup_progress": 'step_2_completed', "plaid": {"plaid_user_ids":{"plaid_user_token":plaid_user_token, "plaid_user_id":plaid_user_id, "plaid_request_id":plaid_request_id},"institutions":[{"institution_ID":institution_ID, "plaid_access_token": access_token, "plaid_pulls": {"Auth": [{"Pull_date":'{:%Y-%m-%d}'.format(datetime.now()), "auth_response":auth_response}]}}] }}
     
      db.investor_info.update({"investor_ID": investor_ID}, {"$set": plaid_data_dict})


    except:
      plaid_data_dict = {"plaid.institutions":{"institution_ID":institution_ID, "plaid_access_token": access_token, "plaid_pulls": {"Auth": [{"Pull_date":'{:%Y-%m-%d}'.format(datetime.now()), "auth_response":auth_response}]}} }

      db.investor_info.update({"investor_ID": investor_ID}, {"$push": plaid_data_dict})


    print('Plaid Added --------------------------------------------------------------------------->')
    


    return jsonify(
        data=account_list,
        institution_ID=institution_ID,
        status="success",
        message="Public token received"
    ), 200


