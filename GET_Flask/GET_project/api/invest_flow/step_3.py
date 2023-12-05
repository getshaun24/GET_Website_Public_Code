from flask import Blueprint, session, url_for, request, redirect, jsonify
from flask_login import login_required
from flask_session import Session
import sys
import re
import datetime
from datetime import datetime, timedelta
import uuid
from GET_project.api.functions import takeSecond
from GET_project import db
from GET_project.api.dwolla import dwolla_app_token, dwolla_create_customer
from GET_project.api.plaid import get_plaid_identity_verification, create_individual_watchlist



GET_invest_flow_step_3_Blueprint = Blueprint('GET_invest_flow_step_3', __name__)
@GET_invest_flow_step_3_Blueprint.route('/api/invest_flow/step_3/', methods=['GET', 'POST']) # <- from '/'
def GET_invest_flow_step_3():



    print(request.json)

    investor_ID = request.json.get("investor_ID", None)
    fund_ID = request.json.get("fund_ID", None)
    institution_ID = request.json.get("institution_ID", None)
    email = request.json.get("email", None).rstrip()
    phone = request.json.get("phone", None)
    print('phone 0 -- > ', phone)
    format_phone = '+' + str(re.sub('\D', '', phone))
    print('phone 1 -- > ', format_phone)
    account_selected_value = str(request.json.get("account_selected_value", None)).rstrip()

    investing_as = request.json.get("investing_as", None).rstrip()
    is_accredited = request.json.get("is_accredited", None).rstrip()
    exempt_from_withholding = request.json.get("exempt_from_withholding", None).rstrip()

    industry_classification = request.json.get("industry_classification", None).rstrip()
    business_classification = request.json.get("business_classification", None).rstrip()
    business_name = request.json.get("business_name", None).rstrip()
    business_ein = request.json.get("business_ein", None)
    entity_purpose_to_invest = request.json.get("entity_purpose_to_invest", None).rstrip()

    controller_first_name = request.json.get("controller_first_name", None).rstrip()
    controller_last_name = request.json.get("controller_last_name", None).rstrip()
    controller_title = request.json.get("controller_title", None).rstrip()
    controller_dob = request.json.get("controller_dob", None)
    controller_ssn = request.json.get("controller_ssn", None)
    controller_address = request.json.get("controller_address", None).rstrip()
    controller_state = request.json.get("controller_state", None).rstrip()
    controller_city = request.json.get("controller_city", None).rstrip()
    controller_zip = request.json.get("controller_zip", None)
    controller_country = request.json.get("controller_country", None).rstrip()
    # controller_email = request.json.get("controller_email", None)

    owner_first_name = request.json.get("owner_first_name", None).rstrip()
    owner_last_name = request.json.get("owner_last_name", None).rstrip()
    owner_title = request.json.get("owner_title", None).rstrip()
    owner_dob = request.json.get("owner_dob", None)
    owner_ssn = request.json.get("owner_ssn", None)
    owner_address = request.json.get("owner_address", None).rstrip()
    owner_state = request.json.get("owner_state", None).rstrip()
    owner_city = request.json.get("owner_city", None).rstrip()
    owner_zip = request.json.get("owner_zip", None)
    owner_country = request.json.get("owner_country", None)
    # owner_email = request.json.get("owner_email", None)


    sole_prop_first_name = request.json.get("sole_prop_first_name", None).rstrip()
    sole_prop_last_name = request.json.get("sole_prop_last_name", None).rstrip()
    sole_prop_business_name = request.json.get("sole_prop_business_name", None).rstrip()
    sole_prop_business_ein = request.json.get("sole_prop_business_ein", None)
    sole_prop_dob = request.json.get("sole_prop_dob", None)
    sole_prop_ssn = request.json.get("sole_prop_ssn", None)
    sole_prop_business_classification = request.json.get("sole_prop_business_classification", None)
    sole_prop_industry_classification = request.json.get("sole_prop_industry_classification", None)
    sole_prop_address = request.json.get("sole_prop_address", None).rstrip()
    sole_prop_state = request.json.get("sole_prop_state", None).rstrip()
    sole_prop_city = request.json.get("sole_prop_city", None).rstrip()
    sole_prop_zip = request.json.get("sole_prop_zip", None)

    individual_first_name = request.json.get("individual_first_name", None).rstrip()
    individual_last_name = request.json.get("individual_last_name", None).rstrip()
    individual_dob = request.json.get("individual_dob", None)
    individual_ssn = request.json.get("individual_ssn", None)
    individual_address = request.json.get("individual_address", None).rstrip()
    individual_state = request.json.get("individual_state", None).rstrip()
    individual_city = request.json.get("individual_city", None).rstrip()
    individual_zip = request.json.get("individual_zip", None)
    empolyment_status = request.json.get("empolyment_status", None).rstrip()


    # variable for creating a new GET Fund - not investor
    new_fund = False

    print('investing_as: ', investing_as)



    if investing_as == 'individual':

        print(' Investing as Individual ------------------------------------------------>')


        create_customer_request_body = {
            'firstName': individual_first_name, 'lastName': individual_last_name, 'email': email,
            'type': 'personal', 'address1': individual_address, 'city': individual_city,
            'state': individual_state, 'postalCode': individual_zip, 'dateOfBirth': individual_dob, 
            'ssn': individual_ssn   #first 4 digits -- all digits accepted 
        }

        country = 'US'
        full_name = individual_first_name + ' ' + individual_last_name

        identity_verification_response, watchlist_screening_id = get_plaid_identity_verification(investor_ID, email, format_phone, individual_dob, individual_first_name, individual_last_name, individual_address, individual_city, individual_state, individual_zip, country, individual_ssn)


        # create_individual_watchlist(investor_ID, full_name, individual_dob, watchlist_screening_id)

        identity_var_path = 'plaid.identity_verification'
        db.investor_info.update({"investor_ID": investor_ID}, {"$set": { identity_var_path:identity_verification_response }})



        customer_url, funding_source_account = dwolla_create_customer(investor_ID, institution_ID, create_customer_request_body, account_selected_value, new_fund)

        # Add to Mongo DB
        db.investor_info.update({"investor_ID": investor_ID}, {"$set": { "KYC": { "investing_as":investing_as, "is_accredited":is_accredited, "exempt_from_withholding":exempt_from_withholding, "empolyment_status":empolyment_status, "individual_first_name":individual_first_name, "individual_last_name":individual_last_name, "individual_dob":individual_dob, "individual_ssn":individual_ssn, "individual_address":individual_address, 
        "individual_city":individual_city, "individual_state":individual_state, "individual_zip":individual_zip },
        "dwolla":{ "customer_url":customer_url }}})





    elif investing_as == 'soleProprietorship':

        print(' Investing as soleProp ------------------------------------------------>')


        create_customer_request_body = {
            'firstName': sole_prop_first_name, 'lastName': sole_prop_last_name, 'email': email, 'type': 'business','dateOfBirth': sole_prop_dob, 'ssn': sole_prop_ssn, 'address1': sole_prop_address, 'city': sole_prop_city,'state': sole_prop_state, 'postalCode': sole_prop_zip, 'businessClassification': sole_prop_business_classification, 'businessType': 'soleProprietorship', 'businessName': sole_prop_business_name, 'ein': sole_prop_business_ein
            }
        

        country = 'US'

        identity_verification_response, watchlist_screening_id = get_plaid_identity_verification(investor_ID, email, format_phone, sole_prop_dob, sole_prop_first_name, sole_prop_last_name, sole_prop_address, sole_prop_city, sole_prop_state, sole_prop_zip, country, sole_prop_ssn)

        identity_var_path = 'plaid.identity_verification'
        db.investor_info.update({"investor_ID": investor_ID}, {"$set": { identity_var_path:identity_verification_response }})

                    


        customer_url, funding_source_account = dwolla_create_customer(investor_ID, institution_ID, create_customer_request_body, account_selected_value, new_fund)

        db.investor_info.update({"investor_ID": investor_ID}, {"$set": { "KYC": { "investing_as":investing_as, "is_accredited":is_accredited, "exempt_from_withholding":exempt_from_withholding, "sole_prop_first_name":sole_prop_first_name, "sole_prop_last_name":sole_prop_last_name, "sole_prop_business_name":sole_prop_business_name, "sole_prop_business_ein":sole_prop_business_ein, "sole_prop_dob":sole_prop_dob, "sole_prop_ssn":sole_prop_ssn, "sole_prop_address": sole_prop_address, "sole_prop_state":sole_prop_state, "sole_prop_city":sole_prop_city, "sole_prop_zip":sole_prop_zip,
         "sole_prop_business_classification":sole_prop_business_classification, "sole_prop_industry_classification":sole_prop_industry_classification }, "dwolla":{ "customer_url":customer_url }}})



    else:



            create_customer_request_body = {
                'firstName': controller_first_name, 'lastName': controller_last_name, 'email': email,
                'type': 'business', 'address1': controller_address, 'city': controller_city,
                'state': controller_state, 'postalCode': controller_zip,
                'controller': {
                    'firstName': controller_first_name, 'lastName': controller_last_name, 'title': controller_title,'dateOfBirth': controller_dob, 'ssn': controller_ssn,
                    'address': {'address1': controller_address, 'city': controller_city,            'stateProvinceRegion': controller_state, 'postalCode': controller_zip, 'country': controller_country}
                      },
                      'businessClassification': business_classification,
                      'businessType': investing_as,
                      'businessName': business_name,
                      'ein': business_ein
                    }
            

        
            customer_url, funding_source_account = dwolla_create_customer(investor_ID, institution_ID, create_customer_request_body, account_selected_value, new_fund)


            owner_request_body = {
              'firstName': owner_first_name, 'lastName': owner_last_name, 'dateOfBirth': owner_dob, 'ssn': owner_ssn, 'address': { 'address1': owner_address, 'city': owner_city, 'stateProvinceRegion': owner_state, 'country': owner_country, 'postalCode': owner_zip
              }
            }

            post_beneficial_owner = dwolla_app_token.post('%s/beneficial-owners' % customer_url, owner_request_body)

            # is this redundant ?????
            owner_request_body_certification = { "status": "certified" }
            dwolla_app_token.post('%s/beneficial-ownership' % customer_url, owner_request_body_certification)




            print(' Investing as Entity ------------------------------------------------>')

            db.investor_info.update({"investor_ID": investor_ID}, {"$set": { "KYC": { "investing_as":investing_as, "is_accredited":is_accredited, "exempt_from_withholding":exempt_from_withholding, "industry_classification":industry_classification, "business_classification":business_classification, "business_name":business_name, "business_ein":business_ein, "entity_purpose_to_invest":entity_purpose_to_invest,
            "controller":{
                "controller_first_name":controller_first_name, "controller_last_name":controller_last_name, "controller_title":controller_title, "controller_dob":controller_dob, "controller_ssn":controller_ssn, "controller_address":controller_address, "controller_state":controller_state, "controller_city":controller_city, "controller_zip":controller_zip, "controller_country": controller_country},
                "beneficial_owner":{ 
                "owner_first_name":owner_first_name, "owner_last_name":owner_last_name, "owner_title":owner_title, "owner_dob":owner_dob, "owner_ssn":owner_ssn, "owner_address":owner_address, "owner_state":owner_state, "owner_city":owner_city, "owner_zip":owner_zip, "owner_country": owner_country} },"dwolla":{ "customer_url":customer_url }}})




           

            identity_verification_response_controller, watchlist_screening_id = get_plaid_identity_verification(investor_ID, email, format_phone, controller_dob, controller_first_name, controller_last_name, controller_address, controller_city, controller_state, controller_zip, controller_country, controller_ssn)

            identity_var_controller_path = 'plaid.identity_verification.controller'
            db.investor_info.update({"investor_ID": investor_ID}, {"$set": { identity_var_controller_path:identity_verification_response_controller }})

            if (owner_first_name + ' ' + owner_last_name) != (controller_first_name + ' ' + controller_last_name):
                # change investor_ID so plaid recognizes it as a different person
                identity_verification_response_owner, watchlist_screening_id_owner = get_plaid_identity_verification(investor_ID + '_owner', email, format_phone, owner_dob, owner_first_name, owner_last_name, owner_address, owner_city, owner_state, owner_zip, owner_country, owner_ssn)

                identity_var_owner_path = 'plaid.identity_verification.owner'
                db.investor_info.update({"investor_ID": investor_ID}, {"$set": { identity_var_owner_path:identity_verification_response_owner }})

    

    invest_url_path = 'investments.' + fund_ID + '.active_investor_dwolla_account_url'
    invest_id_path = 'investments.' + fund_ID + '.active_selected_bank_account_id'
    invest_insti_path = 'investments.' + fund_ID + '.active_institution_id'
    all_invest_url_path = 'dwolla.all_funding_source_accounts'
    db.investor_info.update({"investor_ID": investor_ID}, {"$set": { "signup_progress": 'step_3_completed', invest_url_path:funding_source_account, invest_id_path:account_selected_value, invest_insti_path:institution_ID, all_invest_url_path:[{'investor_dwolla_account_url':funding_source_account, 'selected_bank_account_id':account_selected_value, 'institution_ID':institution_ID}]}})





    return jsonify(
        status="Step_3_Complete",
        message="Step 3 info added to db."
    ), 200
