from flask import Blueprint, request, jsonify, current_app
import sys
import datetime
from datetime import datetime
from plaid.model.item_public_token_exchange_request import ItemPublicTokenExchangeRequest
from flask import request

from flask_mail import Mail
from flask_mail import Message
from GET_project.api.mail import mail, get_html_email_template
# from server import plaid_client, is_live_production_env


from GET_project.api.functions import generate_password_token
from GET_project.api.plaid import get_plaid_transactions, get_plaid_identity, get_plaid_investment_holdings, get_plaid_income, get_plaid_recurring_transactions, get_institution_info
from GET_project import db


GET_check_accredidation_and_get_plaid_investments_Blueprint = Blueprint('GET_check_accredidation_and_get_plaid_investments', __name__)
@GET_check_accredidation_and_get_plaid_investments_Blueprint.route('/api/invest_flow/accred_and_investments/', methods=['GET', 'POST']) # 


def GET_check_accredidation_and_get_plaid_investments():


    print('GET Bank Investments & Check Accredidation Status --------------------------------------------------------------------------->')


    investor_ID = request.json.get("investor_ID", None)
    fund_ID = request.json.get("fund_ID", None)
    get_investor = db.investor_info.find_one({ "investor_ID": investor_ID })



    investing_as = get_investor['KYC']['investing_as']
    first_last = get_investor["first_name"] + ' ' + get_investor["last_name"]
    investor_email = get_investor["email"]
    investment_amount = get_investor["investments"][fund_ID]['investment_amount']
    fund_name = get_investor["investments"][fund_ID]['fund_name']
    pre_formated_phone = get_investor['phone']
    email = get_investor['email']
    signup_progress = get_investor['signup_progress']
    try:
        entity_purpose = get_investor['KYC']['entity_purpose_to_invest']
    except:
        entity_purpose = 'N/A'

    if investing_as == 'corporation' or investing_as == 'llc' or investing_as == 'partnership':
        if get_investor['plaid']['identity_verification']['controller'] == 'plaid_identity_verification_failed':
            identity_verification_controller = 'Submission Failed'
        else:
            identity_verification_controller = 'Successfully Submitted'
        try:
            if get_investor['plaid']['identity_verification']['owner'] == 'plaid_identity_verification_failed':
                identity_verification_owner = 'Submission Failed'
            else:
                identity_verification_owner = 'Successfully Submitted'
        except:
            identity_verification_owner = 'N/A'
        identity_verification = "Controller: " + identity_verification_controller + " | Owner: " + identity_verification_owner
    else:
        if get_investor['plaid']['identity_verification'] == 'plaid_identity_verification_failed':
            identity_verification = 'Submission Failed'
        else:
            identity_verification = 'Successfully Submitted'


    insti_count = 0
    assets_total = 0
    for intitution in get_investor["plaid"]["institutions"]:
        investments_path = 'plaid.institutions.' + str(insti_count) + '.plaid_pulls.Investments'
        institution_ID =  intitution['institution_ID']
        plaid_access_token = intitution['plaid_access_token']
        institution_info = get_institution_info(institution_ID)
        supported_institution_products = institution_info['institution']['products']
        print(supported_institution_products)
        if 'investments' in str(supported_institution_products):
            print('getting holdings')
            holdings, securities = get_plaid_investment_holdings(plaid_access_token)
            if holdings != None:
                db.investor_info.update({"investor_ID": investor_ID}, {"$push": {investments_path:[{ "Pull_date":'{:%Y-%m-%d}'.format(datetime.now()), 'holdings':holdings, 'securities':securities}] }})
                for ii in holdings:
                    assets_total += (float(ii["institution_value'"]) * float(ii["quantity"]))
        for auth_obj in intitution["plaid_pulls"]["Auth"]:
            for acct in auth_obj['auth_response']['accounts']:
                current_balance = acct['balances']['current']
                assets_total += current_balance
        insti_count += 1
                   


    if investing_as == 'individual' or 'soleProprietorship':
        asset_limit = 1000000
    else:
        asset_limit = 5000000

    if assets_total >= asset_limit:
        accredation_status = "Is Accredited"
    else:
        accredation_status = "Not Accredited"


    print("Account assets_total: " + str(assets_total))
    print("Account accredation_status: " + str(accredation_status))


    if signup_progress == 'Signup Successful':
        db.investor_info.update({"investor_ID": investor_ID}, {"$set":{'accredation_status':accredation_status}})
    else:
        investment_status_path = 'investments.' + fund_ID + '.investment_status'
        db.investor_info.update({"investor_ID": investor_ID}, {"$set":{'accredation_status':accredation_status,             investment_status_path:"documents_pending_transaction_confirmed"}})


     # ----------------------------- investor_email --------------------------------

    TEST_EMAIL_RECIPIENTS = current_app.config['TEST_EMAIL_RECIPIENTS']
    MAIL_USERNAME = current_app.config['MAIL_USERNAME']
    SITE_DOMAIN = current_app.config['SITE_DOMAIN']
    EMAIL_LIST = current_app.config['EMAIL_LIST']
    # email_url_link = EMAIL_DOMAIN + '/investor_dashboard/investor_welcome/?ivid=' + investor_ID
    data_to_load = {'user_ID': investor_ID, 'email': investor_email} # Anything else to add???
    email_url_link = SITE_DOMAIN + '/investor_dashboard/investor_welcome/?ivid=' + generate_password_token(data_to_load)

    new_investor_email = get_html_email_template(email_url_link)

    if TEST_EMAIL_RECIPIENTS == True:
        email_to = EMAIL_LIST
    else:
        email_to = [email]

    msg = Message(

                sender=MAIL_USERNAME,
                recipients=email_to,
                subject="GET Equity Partners - Account Validate & Login",
                html=new_investor_email
                )
    mail.send(msg)

     # ----------------------------- Internal Info Email --------------------------------

    
    new_investor_update_info = "<br> <b>signup_status - </b> " + str(signup_progress) + "<br> <b>fund_name - </b> " + str(fund_name) + "<br> <b>investment_amount - </b> " + str(investment_amount) + "<br> <b>investing_as - </b> " + str(investing_as) + "<br> <b>investor_name - </b> " + str(first_last) +  "<br> <b>email - </b> " + str(email) + "<br> <b>phone - </b> " + str(pre_formated_phone) + "<br> <b>accredation_status - </b> " + str(accredation_status) + "<br><b>entity_purpose - </b> " + str(entity_purpose) + "<br><b>plaid_identity_verification - </b> " + str(identity_verification) + "<br><b>investor_ID - </b> " + str(investor_ID) + "<br> <b>fund_ID - </b> " + str(fund_ID)

    msg = Message(
                sender=MAIL_USERNAME,
                recipients=EMAIL_LIST,
                subject="New Investor Update",
                html=new_investor_update_info
                )
    mail.send(msg)




    print('ACCRED DONE --------------------------------------------------------------------------->', file=sys.stderr)

   



    return jsonify(
        data='none',
        status="success",
        message="extra_plaid"
    ), 200


