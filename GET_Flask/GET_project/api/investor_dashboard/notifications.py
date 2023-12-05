from flask import Blueprint, request, jsonify
import datetime
from datetime import datetime, timedelta
from GET_project import db
from flask_jwt_extended import jwt_required

GET_user_notifications_Blueprint = Blueprint('GET_user_notifications', __name__)
@GET_user_notifications_Blueprint.route('/api/investor_dashboard/notifications/', methods=['GET', 'POST']) # <- from '/'
@jwt_required()
def GET_user_notifications():

    print('Notifications made it here --------------------------------------->')



    investor_ID = request.json.get("investor_ID", None)
    print('investor_ID: ', investor_ID)

    db.investor_info.update({"investor_ID": investor_ID}, {"$set": { 'notification_count':0 }})

    investor_info = db.investor_info.find_one({ "investor_ID": investor_ID },{"dwolla":1, "_id":0})

    print(investor_info['dwolla']['customer_url'])
    dwolla_customer_url = investor_info['dwolla']['customer_url']


    notification_info = db.dwolla_notifications.find({ "_links.customer.href": dwolla_customer_url },{"topic":1, "timestamp":1, "event_id":1, "_id":0})

    notifications_list = []
    for notify in notification_info:
        print(notify)
        print('x ----------------------- x')
        iso_x = datetime.strptime(notify['timestamp'], "%Y-%m-%dT%H:%M:%S.%f%z")
        print(iso_x.strftime("%d/%m/%Y H:%M:%S"))
        print('x ----------------------- x')
        notifications_list.append({'topic':notify['topic'], 'iso_x':iso_x.strftime("%d/%m/%Y %H:%M:%S"), 'event_id':notify['event_id']})


    print(notifications_list)


    return jsonify(
        table_data=notifications_list,
        message="Transfers fetched."
    ), 200


