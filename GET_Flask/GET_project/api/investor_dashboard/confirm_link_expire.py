
from flask import Blueprint, request, jsonify
from GET_project.api.functions import confirm_password_token


GET_invest_flow_confirm_link_expire_Blueprint = Blueprint('GET_invest_flow_confirm_link_expire', __name__)
@GET_invest_flow_confirm_link_expire_Blueprint.route('/api/investor_dashboard/confirm_link_expire/', methods=['POST']) # <- from '/'
def GET_invest_flow_confirm_link_expire():
    token = request.json.get("ivid", None)
    if token is None:
        status='token_invalid'
    token_valid = confirm_password_token(token, expire_time=3600000000000)
    print(token_valid)
    if token_valid:
        status='token_valid'
    else:
        status='token_invalid'
    
    print(status)
    return jsonify(status=status), 200
