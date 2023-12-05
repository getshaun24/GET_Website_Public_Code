from flask import Blueprint, session, url_for, request, redirect, jsonify
from flask_login import login_required
from flask_session import Session
import sys
import datetime
from datetime import datetime, timedelta
import uuid
from GET_project.api.functions import takeSecond
from GET_project import db 
from GET_project.api.dwolla import dwolla_check_verification_status


GET_instant_invest_step_2_Blueprint = Blueprint('GET_instant_invest_step_2', __name__)
@GET_instant_invest_step_2_Blueprint.route('/api/investor_dashboard/instant_invest/instant_invest_step_2/', methods=['GET', 'POST']) # <- from '/'
def GET_instant_invest_step_2():




    fund_ID = request.json.get("fund_ID", None)
    agree_to_all = request.json.get("agree_to_all", None)
    signature_typed = request.json.get("signature_typed", None)
    investor_ID = request.json.get("investor_ID", None)

    if agree_to_all != 'yes':
        return jsonify(status="error", message="Please agree to all terms." ), 200


    agree_path = 'investments.' + fund_ID + '.agree_to_all'
    signature_typed_path = 'investments.' + fund_ID + '.signature_typed'
    datetime_signed_path = 'investments.' + fund_ID + '.datetime_signed'
    db.investor_info.update({"investor_ID": investor_ID}, {"$set": { "signup_progress": 'step_4_completed', agree_path:agree_to_all, signature_typed_path:signature_typed, datetime_signed_path:datetime.today()}})





    get_investor = db.investor_info.find_one({ "investor_ID": investor_ID })
    # print(get_investor["dwolla"]['all_funding_source_accounts'])
    account_list = []
    for fs in get_investor["dwolla"]['all_funding_source_accounts']:
        for intitution in get_investor["plaid"]["institutions"]:
                for auth_obj in intitution["plaid_pulls"]["Auth"]:
                    for acct in auth_obj['auth_response']['accounts']:
                        iso_code = acct['balances']['iso_currency_code']
                        if iso_code == 'USD':
                            if fs["selected_bank_account_id"] == acct['account_id']:
                                account_list.append([acct["name"], acct["official_name"], fs["investor_dwolla_account_url"]])
                        else:
                            print('Currency not USD')




    fund_info = db.fund_details.find_one({ "fund_ID": fund_ID },{"minimum_investment_amount":1, "_id":0})
    minimum_investment_amount = fund_info['minimum_investment_amount']


    return jsonify(
        minimum_investment_amount=minimum_investment_amount,
        account_list=account_list,
        status="Step_4_Complete",
        message="Step 4 info added to db."
    ), 200








