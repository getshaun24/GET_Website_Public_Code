from flask import Blueprint, session, url_for, request, redirect, jsonify
from flask_login import login_required
from flask_session import Session
import sys
import datetime
from datetime import datetime, timedelta
import time
import uuid
from GET_project.api.functions import takeSecond
from GET_project import db 
from GET_project.api.dwolla import dwolla_app_token, dwolla_reverify_customer, dwolla_check_verification_status, dwolla_reverify_owner



GET_dwolla_reverify_customer_Blueprint = Blueprint('GET_dwolla_reverify_customer', __name__)
@GET_dwolla_reverify_customer_Blueprint.route('/api/dwolla_reverification/reverify_customer/', methods=['GET', 'POST']) 


def GET_dwolla_reverify_customer():



    print(request.json)

    investor_ID = request.json.get("investor_ID", None)
    fund_ID = request.json.get("fund_ID", None)
    institution_ID = request.json.get("institution_ID", None)
    reverify_email = request.json.get("reverify_email", None)


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

    dwolla_customer_status = request.json.get("dwolla_customer_status", None)
    dwolla_beneficial_owner_status = request.json.get("dwolla_customer_status", None)

 


    # variable for creating a new GET Fund - not investor
    new_fund = False

    print('investing_as: ', investing_as)

    investor_info = db.investor_info.find_one({ "investor_ID": investor_ID },{"dwolla":1, "_id":0})
    dwolla_customer_url = investor_info['dwolla']['customer_url']
    reverify_path = 'KYC.reverify' #path for mongo db update

    if investing_as == 'individual':

        print(' Investing as Individual ------------------------------------------------>')


        create_customer_request_body = {
            'firstName': individual_first_name, 'lastName': individual_last_name, 'email': reverify_email,
            'type': 'personal', 'address1': individual_address, 'city': individual_city,
            'state': individual_state, 'postalCode': individual_zip, 'dateOfBirth': individual_dob, 
            'ssn': individual_ssn 
        }

        dwolla_reverify_customer(dwolla_customer_url, create_customer_request_body)

                # Add to Mongo DB
        db.investor_info.update({"investor_ID": investor_ID}, {"$set": { "reverified_email": reverify_email, reverify_path: { "individual_first_name":individual_first_name, "individual_last_name":individual_last_name, "individual_dob":individual_dob, "individual_ssn":individual_ssn, "individual_address":individual_address, 
        "individual_city":individual_city, "individual_state":individual_state, "individual_zip":individual_zip }}})



    elif investing_as == 'soleProprietorship':

        print(' Investing as soleProp ------------------------------------------------>')


        create_customer_request_body = {
            'firstName': sole_prop_first_name, 'lastName': sole_prop_last_name, 'email': reverify_email, 'type': 'business','dateOfBirth': sole_prop_dob, 'ssn': sole_prop_ssn, 'address1': sole_prop_address, 'city': sole_prop_city,'state': sole_prop_state, 'postalCode': sole_prop_zip, 'businessClassification': sole_prop_business_classification, 'businessType': 'soleProprietorship', 'businessName': sole_prop_business_name, 'ein': sole_prop_business_ein
            }

                    
        dwolla_reverify_customer(dwolla_customer_url, create_customer_request_body)

        
        db.investor_info.update({"investor_ID": investor_ID}, {"$set": { "reverified_email": reverify_email, reverify_path: { "sole_prop_first_name":sole_prop_first_name, "sole_prop_last_name":sole_prop_last_name, "sole_prop_business_name":sole_prop_business_name, "sole_prop_business_ein":sole_prop_business_ein, "sole_prop_dob":sole_prop_dob, "sole_prop_ssn":sole_prop_ssn, "sole_prop_address": sole_prop_address, "sole_prop_state":sole_prop_state, "sole_prop_city":sole_prop_city, "sole_prop_zip":sole_prop_zip,
         "sole_prop_business_classification":sole_prop_business_classification, "sole_prop_industry_classification":sole_prop_industry_classification }}})



    else:

        if dwolla_customer_status == 'retry':

            create_customer_request_body = {
                'firstName': controller_first_name, 'lastName': controller_last_name, 'email': reverify_email, 
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

            dwolla_reverify_customer(dwolla_customer_url, create_customer_request_body)

            db.investor_info.update({"investor_ID": investor_ID}, {"$set": { "reverified_email": reverify_email, reverify_path: { "industry_classification":industry_classification, "business_classification":business_classification, "business_name":business_name, "business_ein":business_ein,
            "controller":{
                "controller_first_name":controller_first_name, "controller_last_name":controller_last_name, "controller_title":controller_title, "controller_dob":controller_dob, "controller_ssn":controller_ssn, "controller_address":controller_address, "controller_state":controller_state, "controller_city":controller_city, "controller_zip":controller_zip, "controller_country": controller_country}}}})


        if dwolla_beneficial_owner_status == 'retry':
            owner_request_body = {
              'firstName': owner_first_name, 'lastName': owner_last_name, 'dateOfBirth': owner_dob, 'ssn': owner_ssn, 'address': { 'address1': owner_address, 'city': owner_city, 'stateProvinceRegion': owner_state, 'country': owner_country, 'postalCode': owner_zip
              }
            }

            dwolla_reverify_owner(dwolla_customer_url, owner_request_body)

            
            db.investor_info.update({"investor_ID": investor_ID}, {"$set": { "reverified_email": reverify_email, reverify_path: {"beneficial_owner":{ 
                "owner_first_name":owner_first_name, "owner_last_name":owner_last_name, "owner_title":owner_title, "owner_dob":owner_dob, "owner_ssn":owner_ssn, "owner_address":owner_address, "owner_state":owner_state, "owner_city":owner_city, "owner_zip":owner_zip, "owner_country": owner_country} }}})


       


            print(' Investing as Entity ------------------------------------------------>')



    count = 0
    while count < 6:
        time.sleep(5)
        count += 1
        dwolla_customer_status, dwolla_beneficial_owner_status = dwolla_check_verification_status(dwolla_customer_url)
        if dwolla_customer_status != 'retry' and dwolla_beneficial_owner_status != 'retry':
            break

    dwolla_customer_status, dwolla_beneficial_owner_status = dwolla_check_verification_status(dwolla_customer_url)


    return jsonify(
        dwolla_customer_status=dwolla_customer_status,
        dwolla_beneficial_owner_status=dwolla_beneficial_owner_status,
        status="reverification_complete",
        message="Reverification Complete"
    ), 200
