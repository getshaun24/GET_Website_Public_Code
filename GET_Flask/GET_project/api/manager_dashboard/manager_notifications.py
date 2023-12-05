from flask import Blueprint, request, jsonify
import datetime
from datetime import datetime, timedelta
from GET_project import db
from flask_jwt_extended import jwt_required

GET_manager_notifications_Blueprint = Blueprint('GET_manager_notifications', __name__)
@GET_manager_notifications_Blueprint.route('/api/manager_dashboard/manager_notifications/', methods=['GET', 'POST']) # <- from '/'
@jwt_required()
def GET_manager_notifications():

    print('Notifications made it here --------------------------------------->')



    manager_ID = request.json.get("manager_ID", None)
    print('manager_ID: ', manager_ID)




    notification_info = db.dwolla_notifications.find({})

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


