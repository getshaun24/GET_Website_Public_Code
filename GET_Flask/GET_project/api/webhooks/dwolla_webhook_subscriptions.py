from flask import Blueprint, request, jsonify
import datetime
from datetime import datetime, timedelta
# from GET_project import db
from GET_project import db
from flask_jwt_extended import jwt_required
from flask_jwt_extended import current_user
from GET_project.api.dwolla import new_webhook_subscription, list_dwolla_webhook_subscriptions, delete_dwolla_webhook_sub

GET_dwolla_webhook_subscriptions_Blueprint = Blueprint('GET_dwolla_webhook_subscriptions', __name__)
@GET_dwolla_webhook_subscriptions_Blueprint.route('/api/webhooks/dwolla_webhook_subscriptions/', methods=['GET','POST']) # <- from '/'
# @jwt_required()
def GET_dwolla_webhook_subscriptions():


    add_new_webhook = request.json.get("add_new_webhook", None)
    new_webhook_url = request.json.get("new_webhook_url", None)
    delete_webhook_url = request.json.get("delete_webhook_url", None)
    delete_webhook = request.json.get("delete_webhook", None)


    if add_new_webhook == True:
        print('Adding new webhook subscription')
        new_webhook_subscription(new_webhook_url)

    if delete_webhook == True:
        print('Deleting webhook subscription')
        delete_dwolla_webhook_sub(delete_webhook_url)


    subscription_list, subscription_total = list_dwolla_webhook_subscriptions()

    subs_list = []
    for elm in subscription_list['_embedded']['webhook-subscriptions']:
        subs_list.append([elm['url'], elm['_links']['self']['href']])

        
    print(subs_list)







    return jsonify(
        subscription_list=subs_list,
        subscription_total=subscription_total,
        message="Transfers fetched."
    ), 200


