from flask import Blueprint, session, url_for, request, redirect, jsonify, current_app
from flask_login import login_required
from flask_session import Session
import sys
import datetime
from datetime import datetime, timedelta
import uuid
from flask_mail import Mail
from flask_mail import Message
from GET_project.api.mail import mail
from GET_project.api.functions import GET_fundX_ID
from GET_project.api.dwolla import dwolla_check_verification_status
from GET_project import db
import re
from random import randint


GET_instant_invest_step_1_Blueprint = Blueprint('GET_instant_invest_step_1', __name__)
@GET_instant_invest_step_1_Blueprint.route('/api/investor_dashboard/instant_invest/instant_invest_step_1/', methods=['GET', 'POST']) # <- from '/'
def GET_instant_invest_step_1():



    investment_amount = request.json.get("investment_amount", None)
    selected_fund = request.json.get("instant_selected_fund", None)
    investor_ID = request.json.get("investor_ID", None)


    print('selected fund ------------------->', selected_fund)
    fundX_ID, fundX_name = GET_fundX_ID(selected_fund)


    get_investor = db.investor_info.find_one({ "investor_ID": investor_ID })

    for key, value in get_investor["investments"].items():
        print('KEY ---- >', key, value)
        if key == fundX_ID:
            if value['investment_status'] == 'invested' or value['investment_status'] == 'invested_payment_pending':
                print('investor already invested in this fund')
                return jsonify(
                    status="investor_already_invested",
                    message="Investor already invested in this fund."
                ), 200

    fund_name_path = "investments." + str(fundX_ID) + ".fund_name"
    investment_amount_path = "investments." + str(fundX_ID) + ".investment_amount"
    investment_status_path = "investments." + str(fundX_ID) + ".investment_status"
    additional_invest_path = 'investments.' + str(fundX_ID) + '.additional_investments'
    db.investor_info.update({"investor_ID": investor_ID}, {"$set": { fund_name_path:fundX_name, investment_amount_path:investment_amount, investment_status_path:"not_invested", additional_invest_path:[]}})
    print('instant invest step one done')


    return jsonify(
        fund_ID=fundX_ID,
        status="Step_1_Complete",
        message="Step 1 info added to db."
    ), 200


