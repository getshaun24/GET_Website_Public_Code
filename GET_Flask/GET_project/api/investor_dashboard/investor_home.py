from flask import Blueprint, request, jsonify
import datetime
from datetime import datetime, timedelta
from GET_project import db 
from flask_jwt_extended import jwt_required
# from flask_jwt_extended import current_user


GET_investor_home_Blueprint = Blueprint('GET_investor_home', __name__)
@GET_investor_home_Blueprint.route('/api/investor_dashboard/investor_home/', methods=['GET', 'POST']) # <- from '/'
@jwt_required()
def GET_investor_home():

    print('Home made it here --------------------------------------->')

    # investor_ID = current_user['user_id']

    investor_ID = request.json.get("investor_ID", None)
    print('investor_ID: ', investor_ID)

    investor_info = db.investor_info.find_one({ "investor_ID": investor_ID },{"first_name":1, "last_name":1, "investments":1, 'notification_count':1, "_id":0})
    fund_info = db.fund_details.find({},{"fund_name":1, "fund_ID":1, "_id":0})

    notification_count = str(investor_info['notification_count'])
    full_name = investor_info['first_name'] + ' ' + investor_info['last_name']

    # funds = {}
    # for fund in fund_info:
    #     funds[fund['fund_ID']] = fund['fund_name']

    investment_array = []
    for fund in fund_info:
        fund_ID = fund['fund_ID']

        try:
            investment_amount = "${:,}".format(int(investor_info['investments'][fund_ID]['investment_amount']))
            status_split = investor_info['investments'][fund_ID]['investment_status'].split('-')
            status = status_split[0].replace(' ', '')
            print( investor_info['investments'][fund_ID]['investment_amount'])
            print(investor_info['investments'][fund_ID]['fund_name'])
            iso_x = (investor_info['investments'][fund_ID]['datetime_signed']).strftime("%d/%m/%Y")
            investment_array.append({'fund_name':investor_info['investments'][fund_ID]['fund_name'], 'status':status , 'iso_x':iso_x, 'investment_amount':investment_amount})
        except:
            print('no_fund')

        
    print(investment_array)
    print('notification_count -- - -- --- ->', notification_count)

    #                  print(get_user)
    # all_settlements_array = []
    # if get_user['all_settlements'] is not None:
    #     for settlement in get_user['all_settlements']:
    #         all_settlements_array.append({'recipient':settlement['counterparty_email'], 'status':settlement['status'], 'request_date':settlement['request_date']})




    return jsonify(
        full_name=full_name,
        notification_count=notification_count,
        table_data=investment_array,
        message="Transfers fetched."
    ), 200


