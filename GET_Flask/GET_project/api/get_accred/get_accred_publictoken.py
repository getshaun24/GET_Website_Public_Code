from flask import Blueprint, request, jsonify
import sys
import json
from plaid.model.item_public_token_exchange_request import ItemPublicTokenExchangeRequest
from flask import request

import datetime
from datetime import datetime, date
from dateutil.tz import tzutc
# from server import plaid_client, is_live_production_env



from GET_project.api.plaid import plaid_client, get_plaid_income, get_plaid_auth, get_plaid_investment_holdings, get_institution_info
from GET_project import db
from flask_jwt_extended import jwt_required

GET_accred_publictoken_Blueprint = Blueprint('GET_accred_publictoken', __name__)
@GET_accred_publictoken_Blueprint.route('/api/get_accred/get_accred_publictoken/', methods=['GET', 'POST']) # 
@jwt_required()
def GET_accred_publictoken():


    investor_ID = request.json.get("investor_ID", None)
    institution_ID = request.json.get("institution_ID", None)
    public_token = request.json.get("public_token", None)
    meta_data = request.json.get("meta_data", None)
    product_public_var = request.json.get("product_public_var", None)
    print('00------------------- product_public_var ------> ', product_public_var)

    get_user = db.investor_info.find_one({ "investor_ID": investor_ID })
    plaid_access_token = get_user['plaid']['institutions'][-1]['plaid_access_token']
    plaid_user_token = get_user['plaid']['plaid_user_ids']['plaid_user_token']
    plaid_request_id = get_user['plaid']['plaid_user_ids']['plaid_request_id']
    investing_as = get_user['KYC']['investing_as']

    #get index of matching institution
    insti_count = 0
    for insti in get_user['plaid']['institutions']:
        if institution_ID == insti['institution_ID']:
            break
        else:
            insti_count += 1
            


# ----------------------------- INCOME ------------------------------------------- 
    # ----------------------------- INCOME  ------------------------------------------- 
        # ----------------------------- INCOME  ------------------------------------------- 
            # ----------------------------- INCOME ------------------------------------------- 
                # ----------------------------- INCOME ------------------------------------------- 


    if product_public_var == 'get_INCOME_public_token':


        plaid_income_response, institution_ID = get_plaid_income(plaid_access_token, plaid_user_token, plaid_request_id)


        bank_total_amount = 0
        for obj in plaid_income_response['bank_income']:
            try:
                if obj['bank_income_summary']['iso_currency_code'] == 'USD':
                    print('amt -- ', float(obj['bank_income_summary']['total_amount']))
                    bank_total_amount += float(obj['bank_income_summary']['total_amount'])
            except:
                print('probably no currency code')

        
        print('bank_total_amount: ', bank_total_amount)

        monthly_amounts = {}
        bank_total_qualifies = False
        if bank_total_amount > 1000:

            bank_total_qualifies = True
            print('doing next step')

            for obj in plaid_income_response['bank_income']:
                if obj['bank_income_summary']['iso_currency_code'] == 'USD':
                    for summary in obj['bank_income_summary']['historical_summary']:
                        try:
                            year_month = (datetime.strptime(summary['start_date'], '%Y-%m-%d')).strftime("'%Y_%m'")
                            if year_month in monthly_amounts.keys():
                                monthly_amounts[year_month] += float(summary['total_amount'])
                            else:
                                monthly_amounts[year_month] = float(summary['total_amount'])
                        except:
                            print(summary)
        

        print('monthly amts -', monthly_amounts)


        accredation_status = 'Not Accredited'
        status = "income_not_accredited"
        for key, value in monthly_amounts.items():

            if value > 1:
            #if value < 5000:
                accredation_status = 'Not Accredited'
                break
            else:
                accredation_status = 'Accredited'
                status = "income_is_accredited"

        print( 'ACCRED ---------- >', accredation_status)
        print( 'ACCRED status ---------- >', status)


        # ------------------------ Add In Institution Array ------------------
        #plaid_income_path = 'plaid.institutions.' + str(insti_count) + '.plaid_pulls.Bank_Income'

        # ------------------------ Add In Outer Plaid Object ------------------
        plaid_income_path = 'plaid.bank_income'


        db.investor_info.update({"investor_ID": investor_ID}, {"$push": { 
            plaid_income_path:{"Pull_date":'{:%Y-%m-%d}'.format(datetime.now()), 
            'bank_income':plaid_income_response}}})
        

        db.investor_info.update({"investor_ID": investor_ID}, {"$set": { 
            'accredation_status': accredation_status}})
        








# ----------------------------- AUTH ------------------------------------------- 
    # ----------------------------- AUTH  ------------------------------------------- 
        # ----------------------------- AUTH  ------------------------------------------- 
            # ----------------------------- AUTH ------------------------------------------- 
                # ----------------------------- AUTH ------------------------------------------- 


    if product_public_var == 'get_AUTH_public_token':

        exchange_response = plaid_client.item_public_token_exchange(ItemPublicTokenExchangeRequest(public_token=public_token))

        #pretty_print_response(exchange_response.to_dict())
        access_token = exchange_response['access_token']
        item_id = exchange_response['item_id']

        # -------- Get Auth -----------------
        auth_response, account_ids_list, account_list = get_plaid_auth(access_token)

        institution_ID = auth_response['item']['institution_id']


        institution_info = get_institution_info(institution_ID)
        supported_institution_products = institution_info['institution']['products']
        print(supported_institution_products)
        if 'investments' in str(supported_institution_products):
            print('getting holdings')
            holdings, securities = get_plaid_investment_holdings(plaid_access_token)
            plaid_data_dict = {"plaid.institutions":{"institution_ID":institution_ID, "plaid_access_token": access_token, "plaid_pulls": {"Auth": [{"Pull_date":'{:%Y-%m-%d}'.format(datetime.now()), "auth_response":auth_response}], 'Investments': [{'holdings':holdings, 'securities':securities}] } } }

        plaid_data_dict = {"plaid.institutions":{"institution_ID":institution_ID, "plaid_access_token": access_token, "plaid_pulls": {"Auth": [{"Pull_date":'{:%Y-%m-%d}'.format(datetime.now()), "auth_response":auth_response}] } } }

        db.investor_info.update({"investor_ID": investor_ID}, {"$push": plaid_data_dict})



        print('GET Bank Investments & Check Accredidation Status --------------------------------------------------------------------------->')

        investor_ID = request.json.get("investor_ID", None)
        get_investor = db.investor_info.find_one({ "investor_ID": investor_ID })

        insti_count = 0
        assets_total = 0
        for intitution in get_investor["plaid"]["institutions"]:
            investments_path = 'plaid.institutions.' + str(insti_count) + '.plaid_pulls.Investments'
            plaid_access_token = intitution['plaid_access_token']
            if "Investments" in intitution["plaid_pulls"]:
                for invest_obj in intitution["plaid_pulls"]["Investments"]:
                    if holdings != None:
                        for ii in holdings:
                            assets_total += (float(ii["institution_value'"]) * float(ii["quantity"]))
            for auth_obj in intitution["plaid_pulls"]["Auth"]:
                for acct in auth_obj['auth_response']['accounts']:
                    current_balance = acct['balances']['current']
                    assets_total += current_balance
            insti_count += 1
                

        if investing_as == 'individual' or 'soleProprietorship':
            asset_limit = 1000000


        if assets_total >= asset_limit:
            accredation_status = "Is Accredited"
            status = "auth_is_accredited"
        else:
            accredation_status = "Not Accredited"
            status = "auth_not_accredited"

        print("Account assets_total: " + str(assets_total))
        print("Account accredation_status: " + str(accredation_status))



        db.investor_info.update({"investor_ID": investor_ID}, {"$set":{'accredation_status':accredation_status}})
    

    

        bank_total_qualifies = False


    print('Plaid Added --------------------------------------------------------------------------->')

    return jsonify(
        bank_total_qualifies=bank_total_qualifies,
        status=status,
        message="Public token received"
    ), 200


