from flask import Blueprint, session, url_for, request, redirect, jsonify
from flask_login import login_required
from flask_session import Session
import sys
import datetime
from datetime import datetime, timedelta
import uuid
from GET_project.api.functions import takeSecond
from GET_project import db
from GET_project.api.dwolla import dwolla_app_token, dwolla_create_customer, dwolla_check_verification_status



GET_new_fund_setup_step_3_Blueprint = Blueprint('GET_new_fund_setup_step_3', __name__)
@GET_new_fund_setup_step_3_Blueprint.route('/api/new_fund_setup/new_fund_step_3/', methods=['GET', 'POST']) # <- from '/'
def GET_new_fund_setup_step_3():





    fund_ID = request.json.get("fund_ID", None)
    plaid_skipped = request.json.get("plaid_skipped", None)
    email = request.json.get("email", None)

    account_selected_value = request.json.get("account_selected_value", None)

    investing_as = request.json.get("investing_as", None)

    industry_classification = request.json.get("industry_classification", None)
    business_classification = request.json.get("business_classification", None)
    business_name = request.json.get("business_name", None)
    business_ein = request.json.get("business_ein", None)

    controller_first_name = request.json.get("controller_first_name", None)
    controller_last_name = request.json.get("controller_last_name", None)
    controller_title = request.json.get("controller_title", None)
    controller_dob = request.json.get("controller_dob", None)
    controller_ssn = request.json.get("controller_ssn", None)
    controller_address = request.json.get("controller_address", None)
    controller_state = request.json.get("controller_state", None)
    controller_city = request.json.get("controller_city", None)
    controller_zip = request.json.get("controller_zip", None)
    controller_country = request.json.get("controller_country", None)

    owner_first_name = request.json.get("owner_first_name", None)
    owner_last_name = request.json.get("owner_last_name", None)
    owner_title = request.json.get("owner_title", None)
    owner_dob = request.json.get("owner_dob", None)
    owner_ssn = request.json.get("owner_ssn", None)
    owner_address = request.json.get("owner_address", None)
    owner_state = request.json.get("owner_state", None)
    owner_city = request.json.get("owner_city", None)
    owner_zip = request.json.get("owner_zip", None)
    owner_country = request.json.get("owner_country", None)


    sole_prop_first_name = request.json.get("sole_prop_first_name", None)
    sole_prop_last_name = request.json.get("sole_prop_last_name", None)
    sole_prop_business_name = request.json.get("sole_prop_business_name", None)
    sole_prop_business_ein = request.json.get("sole_prop_business_ein", None)
    sole_prop_dob = request.json.get("sole_prop_dob", None)
    sole_prop_ssn = request.json.get("sole_prop_ssn", None)
    sole_prop_business_classification = request.json.get("sole_prop_business_classification", None)
    sole_prop_industry_classification = request.json.get("sole_prop_industry_classification", None)
    sole_prop_address = request.json.get("sole_prop_address", None)
    sole_prop_state = request.json.get("sole_prop_state", None)
    sole_prop_city = request.json.get("sole_prop_city", None)
    sole_prop_zip = request.json.get("sole_prop_zip", None)

    individual_first_name = request.json.get("individual_first_name", None)
    individual_last_name = request.json.get("individual_last_name", None)
    individual_dob = request.json.get("individual_dob", None)
    individual_ssn = request.json.get("individual_ssn", None)
    individual_address = request.json.get("individual_address", None)
    individual_state = request.json.get("individual_state", None)
    individual_city = request.json.get("individual_city", None)
    individual_zip = request.json.get("individual_zip", None)
    empolyment_status = request.json.get("empolyment_status", None)

    # new_fund variable for creating a new GET Fund - not investor
    new_fund = True

    print('investing_as: ', investing_as)
    print('Plaid Skipped: ', plaid_skipped)



    if investing_as == 'individual':

        print(' Investing as Individual ------------------------------------------------>')


        create_customer_request_body = {
            'firstName': individual_first_name, 'lastName': individual_last_name, 'email': email,
            'type': 'personal', 'address1': individual_address, 'city': individual_city,
            'state': individual_state, 'postalCode': individual_zip, 'dateOfBirth': individual_dob, 
            'ssn': individual_ssn   #first 4 digits -- all digits accepted 
        }


        if plaid_skipped == False:
            customer_url, funding_source_account = dwolla_create_customer(fund_ID, '', create_customer_request_body, account_selected_value, new_fund)
        else:
            create_customer = dwolla_app_token.post('customers', create_customer_request_body)
            customer_url = create_customer.headers['location'] 

            funding_sources = dwolla_app_token.get('%s/funding-sources' % customer_url)
            funding_source_account = funding_sources.body['_embedded']['funding-sources'][0]['_links']['self']['href']
            print(funding_source_account)

            
        # Add to Mongo DB

        db.fund_details.update({"fund_ID": fund_ID}, {"$set": { "KYC": { "fund_entity_type":investing_as, "empolyment_status":empolyment_status, "individual_first_name":individual_first_name, "individual_last_name":individual_last_name, "individual_dob":individual_dob, "individual_ssn":individual_ssn, "individual_address":individual_address, 
        "individual_city":individual_city, "individual_state":individual_state, "individual_zip":individual_zip },
        "dwolla":{ "customer_url":customer_url, "GET_fund_dwolla_account_url":funding_source_account, "selected_bank_account_id":account_selected_value }}})



    elif investing_as == 'soleProprietorship':

        print(' Investing as soleProp ------------------------------------------------>')


        create_customer_request_body = {
            'firstName': sole_prop_first_name, 'lastName': sole_prop_last_name, 'email': email, 'type': 'business','dateOfBirth': sole_prop_dob, 'ssn': sole_prop_ssn, 'address1': sole_prop_address, 'city': sole_prop_city,'state': sole_prop_state, 'postalCode': sole_prop_zip, 'businessClassification': sole_prop_business_classification, 'businessType': 'soleProprietorship', 'businessName': sole_prop_business_name, 'ein': sole_prop_business_ein
            }

                    

        if plaid_skipped == False:
            customer_url, funding_source_account = dwolla_create_customer(fund_ID, '', create_customer_request_body, account_selected_value, new_fund)
        else:
            create_customer = dwolla_app_token.post('customers', create_customer_request_body)
            customer_url = create_customer.headers['location'] 

            funding_sources = dwolla_app_token.get('%s/funding-sources' % customer_url)
            funding_source_account = funding_sources.body['_embedded']['funding-sources'][0]['_links']['self']['href']
            print(funding_source_account)



        


        db.fund_details.update({"fund_ID": fund_ID}, {"$set": { "KYC": { "fund_entity_type":investing_as, "sole_prop_first_name":sole_prop_first_name, "sole_prop_last_name":sole_prop_last_name, "sole_prop_business_name":sole_prop_business_name, "sole_prop_business_ein":sole_prop_business_ein, "sole_prop_dob":sole_prop_dob, "sole_prop_ssn":sole_prop_ssn, "sole_prop_address": sole_prop_address, "sole_prop_state":sole_prop_state, "sole_prop_city":sole_prop_city, "sole_prop_zip":sole_prop_zip,
         "sole_prop_business_classification":sole_prop_business_classification, "sole_prop_industry_classification":sole_prop_industry_classification },
         "dwolla":{ "customer_url":customer_url, "GET_fund_dwolla_account_url":funding_source_account, "selected_bank_account_id":account_selected_value }}})



    else:

            print(' Investing as Entity ------------------------------------------------>')



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


            if plaid_skipped == False:
                print('plaid skipped is false')
                customer_url, funding_source_account = dwolla_create_customer(fund_ID, '', create_customer_request_body, account_selected_value, new_fund)
            else:
                create_customer = dwolla_app_token.post('customers', create_customer_request_body)
                customer_url = create_customer.headers['location'] 

                funding_sources = dwolla_app_token.get('%s/funding-sources' % customer_url)
                funding_source_account = funding_sources.body['_embedded']['funding-sources'][0]['_links']['self']['href']
                print('plaid skipped is True')
                print(funding_source_account)

            

            owner_request_body = {
              'firstName': owner_first_name, 'lastName': owner_last_name, 'dateOfBirth': owner_dob, 'ssn': owner_ssn, 'address': { 'address1': owner_address, 'city': owner_city, 'stateProvinceRegion': owner_state, 'country': owner_country, 'postalCode': owner_zip
              }
            }

            post_beneficial_owner = dwolla_app_token.post('%s/beneficial-owners' % customer_url, owner_request_body)

            # is this redundant ?????
            owner_request_body_certification = { "status": "certified" }
            dwolla_app_token.post('%s/beneficial-ownership' % customer_url, owner_request_body_certification)




            db.fund_details.update({"fund_ID": fund_ID}, {"$set": { "KYC": { "fund_entity_type":investing_as, "industry_classification":industry_classification, "business_classification":business_classification, "business_name":business_name, "business_ein":business_ein,
            "controller":{
                "controller_first_name":controller_first_name, "controller_last_name":controller_last_name, "controller_title":controller_title, "controller_dob":controller_dob, "controller_ssn":controller_ssn, "controller_address":controller_address, "controller_state":controller_state, "controller_city":controller_city, "controller_zip":controller_zip, "controller_country": controller_country},
                "beneficial_owner":{ 
                "owner_first_name":owner_first_name, "owner_last_name":owner_last_name, "owner_title":owner_title, "owner_dob":owner_dob, "owner_ssn":owner_ssn, "owner_address":owner_address, "owner_state":owner_state, "owner_city":owner_city, "owner_zip":owner_zip, "owner_country": owner_country} },
                "dwolla":{ "customer_url":customer_url, "GET_fund_dwolla_account_url":funding_source_account, "selected_bank_account_id":account_selected_value }}})



    try:
        dwolla_customer_status, dwolla_beneficial_owner_status = dwolla_check_verification_status(customer_url)
    except:
        dwolla_customer_status = 'error'
        dwolla_beneficial_owner_status = 'error'
        print('error getting customer status')



    return jsonify(
        dwolla_customer_status=dwolla_customer_status,
        dwolla_beneficial_owner_status=dwolla_beneficial_owner_status,
        status="Step_3_Complete",
        message="Step 3 info added to db."
    ), 200
