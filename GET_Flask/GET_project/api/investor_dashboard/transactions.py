from flask import Blueprint, request, jsonify
import datetime
from datetime import datetime, timedelta
# from GET_project import db
from GET_project import db
from flask_jwt_extended import jwt_required
from flask_jwt_extended import current_user
from GET_project.api.dwolla import get_dwolla_acct_balance

GET_user_transactions_Blueprint = Blueprint('GET_user_transactions', __name__)
@GET_user_transactions_Blueprint.route('/api/investor_dashboard/transactions/', methods=['GET','POST']) # <- from '/'
@jwt_required()
def GET_user_transactions():


    # if current_user.access_status != 'investor':
    #     return jsonify({'msg': 'Access denied'}), 403

    # investor_ID = current_user.user_id


    print('Transactions made it here --------------------------------------->')


    investor_ID = request.json.get("investor_ID", None)
    print('investor_ID: ', investor_ID)


    transfers = db.transfers.find({"investor_ID": investor_ID}, {"investor_ID":1, "fund_ID":1, "transfer_status":1, "transfer_amount":1, "transfer_datetime":1})



    if transfers is None:
        return jsonify(message="There are currently no transfer records for this investor."), 202



    fund_info = db.fund_details.find({},{"fund_name":1, "fund_ID":1, "_id":0})
    print(transfers.count())

    funds = {}
    for fund in fund_info:
        funds[fund['fund_ID']] = fund['fund_name']

    transfer_list = []
    for transfer in transfers:
        print("Transfer fund ID: ", transfer['fund_ID'])
        try:
            td = transfer['transfer_datetime'].strftime("%d/%m/%Y")
        except:
            td = None

        fund_name = 'Undefined'
        if transfer['fund_ID'] in funds:
            fund_name = funds[transfer['fund_ID']]

        transfer_amount = "${:,}".format(int(transfer['transfer_amount']))


        transfer_list.append({'transaction_datetime': td, 'fund_name':fund_name, 'transfer_status':transfer['transfer_status'], 'transfer_amount':transfer_amount, 'transfer_id':str(transfer['_id'])[-7:]})



    investor_info = db.investor_info.find_one({ "investor_ID": investor_ID },{"dwolla":1, "_id":0})

    print(investor_info['dwolla']['customer_url'])
    dwolla_customer_url = investor_info['dwolla']['customer_url']

    dwolla_balance = get_dwolla_acct_balance(dwolla_customer_url)

    print(dwolla_balance)

    return jsonify(
        table_data=transfer_list,
        dwolla_balance=dwolla_balance,
        message="Transfers fetched."
    ), 200


