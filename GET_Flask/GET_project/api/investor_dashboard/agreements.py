from flask import Blueprint, request, jsonify, current_app
import datetime
from datetime import datetime, timedelta
from GET_project import db
from flask_jwt_extended import jwt_required

GET_investor_agreements_Blueprint = Blueprint('GET_investor_agreements', __name__)
@GET_investor_agreements_Blueprint.route('/api/investor_dashboard/agreements/', methods=['GET', 'POST']) # <- from '/'
@jwt_required()
def GET_investor_agreements():

    print('Home made it here --------------------------------------->')



    investor_ID = request.json.get("investor_ID", None)
    print('investor_ID: ', investor_ID)


    NANO_FUND_ID = current_app.config['NANO_FUND_ID']
    ECO_FUND_ID = current_app.config['ECO_FUND_ID']

    investor_info = db.investor_info.find_one({ "investor_ID": investor_ID },{"investments":1, "_id":0})
    fund_info = db.fund_details.find({},{"fund_name":1, "fund_ID":1, "_id":0})

    # funds = {}
    # for fund in fund_info:
    #     funds[fund['fund_ID']] = fund['fund_name']

    legal_array = []
    for fund in fund_info:
        fund_ID = fund['fund_ID']

        try:
            fund_name = investor_info['investments'][fund_ID]['fund_name']
            print(fund_name)
            iso_x = (investor_info['investments'][fund_ID]['datetime_signed']).strftime("%d/%m/%Y")
            print('x ----------------------- x')
            if fund_ID == NANO_FUND_ID:
                print('x ----------------------- fund_ID -   ', fund_ID)
                sub_agreement_url = 'https://thisisget.com/legal_ag/nano/Subscription_Agreement_&_Accredited_Cert__US_Nano_Fund_A.pdf'
                ppm_url = 'https://thisisget.com/legal_ag/nano/PPM_for_US_Nanotechnology_Fund_A.pdf'
                operating_url = 'https://thisisget.com/legal_ag/nano/US_Nano_Fund_A_Operating_Agreement.pdf'
            elif fund_ID == ECO_FUND_ID:
                print('x ----------------------- fund_ID -   ', fund_ID)
                sub_agreement_url = 'https://thisisget.com/legal_ag/eco/Subscription_Agreement_Only_Eco_Energy.pdf'
                ppm_url = 'https://thisisget.com/legal_ag/eco/PPM_for_Eco_Energy_Partners.pdf'
                operating_url = 'https://thisisget.com/legal_ag/eco/Operating_Agreement_Eco_Energy_Partners.pdf'
            legal_array.append({'fund_name':fund_name, 'iso_x':iso_x, 'sub_agreement_url':sub_agreement_url, 'ppm_url':ppm_url, 'operating_url':operating_url})
        except:
            print('no_fund')

    print(legal_array)

        
    print(legal_array)


    return jsonify(
        table_data=legal_array,
        message="Transfers fetched."
    ), 200


