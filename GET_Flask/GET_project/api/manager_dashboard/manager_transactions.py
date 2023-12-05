from flask import Blueprint, request, jsonify
import datetime
from datetime import datetime, timedelta
# from GET_project import db
from GET_project import db
from flask_jwt_extended import jwt_required
from flask_jwt_extended import current_user
from GET_project.api.dwolla import get_dwolla_acct_balance

GET_manager_transactions_Blueprint = Blueprint('GET_manager_transactions', __name__)
@GET_manager_transactions_Blueprint.route('/api/manager_dashboard/manager_transactions/', methods=['GET','POST']) # <- from '/'
@jwt_required()
def GET_manager_transactions():


    # if current_user.access_status != 'investor':
    #     return jsonify({'msg': 'Access denied'}), 403

    # investor_ID = current_user.user_id


    print('Transactions made it here --------------------------------------->')


    manager_ID = request.json.get("manager_ID", None)
    print('manager_ID: ', manager_ID)



    transfers = db.transfers.find({})
    print('Transactions >', transfers)



    if transfers is None:
        return jsonify(message="There are currently no transfer records for this investor."), 202



    fund_info = db.fund_details.find({},{"fund_name":1, "fund_ID":1, "_id":0})
    print(transfers.count())

    funds = {}
    for fund in fund_info:
        funds[fund['fund_ID']] = fund['fund_name']

    transfer_list = []
    for transfer in transfers:
        try:
            td = transfer['transfer_datetime'].strftime("%d/%m/%Y")
        except:
            td = None

        fund_name = 'Undefined'
        if transfer['fund_ID'] in funds:
            fund_name = funds[transfer['fund_ID']]

        transfer_amount = "${:,}".format(int(transfer['transfer_amount']))


        investor_ID_trans = transfer['investor_ID']
        investor_info = db.investor_info.find_one({ "investor_ID": investor_ID_trans })
        investor_name = investor_info['first_name'] + ' ' + investor_info['last_name']
        investor_email = investor_info['email']
        investor_phone = investor_info['phone']
                
        # transfer_list.append([str(transfer['_id'])[-7:], td, fund_name, transfer['transfer_status'], transfer['transfer_amount']])
        transfer_list.append({'investor_name':investor_name, 'investor_email':investor_email, 'investor_phone':investor_phone, 'transaction_datetime':td, 'fund_name':fund_name, 'transfer_status':transfer['transfer_status'], 'transfer_amount':transfer_amount, 'transfer_id':str(transfer['_id'])[-7:]})




    return jsonify(
        table_data=transfer_list,
        message="Transfers fetched."
    ), 200


