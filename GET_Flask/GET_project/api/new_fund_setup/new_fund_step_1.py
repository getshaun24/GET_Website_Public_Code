from flask import Blueprint, session, url_for, request, redirect, jsonify
from flask_login import login_required
from flask_session import Session
import sys
import datetime
from datetime import datetime, timedelta
import uuid
from GET_project import db
import re
from flask_jwt_extended import jwt_required


GET_new_fund_setup_step_1_Blueprint = Blueprint('GET_new_fund_setup_step_1', __name__)
@GET_new_fund_setup_step_1_Blueprint.route('/api/new_fund_setup/new_fund_step_1/', methods=['GET', 'POST']) # <- from '/'
@jwt_required()
def GET_new_fund_setup_step_1():

    print('FUND STEP 1')
    print('request.json ------------------->', request.json)

    first_name = request.json.get("first_name", None)
    last_name = request.json.get("last_name", None)
    email = request.json.get("email", None)
    phone = request.json.get("phone", None)
    new_fund_name = request.json.get("new_fund_name", None)
    fund_ID = request.json.get("fund_ID", None)
    minimum_investment_amount = int(request.json.get("minimum_investment_amount", None))


    if fund_ID == None or fund_ID == '':
        fund_ID = str(uuid.uuid5(uuid.NAMESPACE_DNS, email + str(datetime.now().strftime("%m/%d/%Y, %H:%M:%S"))))

        print('fund_ID ------------------->', fund_ID)

        db.fund_details.insert_one({
                "fund_name": new_fund_name,
                "fund_ID": fund_ID,
                "date_fund_created": datetime.today(),
                "first_name": first_name,
                "last_name": last_name,
                "email": email,
                "phone": phone,
                "minimum_investment_amount":minimum_investment_amount
            })
    else:
        db.fund_details.update({"fund_ID": fund_ID}, {"$set": { 
                "fund_name": new_fund_name,
                "fund_ID": fund_ID,
                "date_fund_created": datetime.today(),
                "first_name": first_name,
                "last_name": last_name,
                "email": email,
                "phone": phone,
                "minimum_investment_amount":minimum_investment_amount
            }})


    return jsonify(
        fund_ID=fund_ID,
        status="Step_1_Complete",
        message="Step 1 info added to db."
    ), 200


