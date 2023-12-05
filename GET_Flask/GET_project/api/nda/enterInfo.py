from flask import Blueprint, request, current_app, jsonify
from GET_project import db
from random import randint
from datetime import datetime
from twilio.rest import Client
from GET_project.api.functions import GET_fundX_ID


NDA_EnterInfo_Blueprint = Blueprint('NDA_EnterInfo', __name__)
@NDA_EnterInfo_Blueprint.route('/api/nda/enterInfo/', methods=['GET', 'POST']) # <- from '/'
def NDA_EnterInfo():

    
    name = request.json.get("name", None)
    email = request.json.get("email", None)
    phone = request.json.get("phone_number", None)
    investment = request.json.get("investment", None)

    if phone is None or name is None or email is None or investment is None:
        return jsonify(status="error", message="At least one field is not entered."), 400

    if len(email.split('@')[-1].split('.')) != 2:
        return jsonify(status="error", message="Email is invalid."), 400

    # Format phone number
    phone = "".join("".join("".join("".join("".join(phone.split('-')).split('(')).split(')')).split(' ')).split('+'))
    print(phone)
    if len(phone) == 11:
        phone = "+" + phone
    else: 
        return jsonify(status="error", message="Phone number is invalid."), 400

    print(phone)

    # Check to see if that phone number exists already. 
    contactVerified = False
    contact = db.nda.find_one({"phone_number": phone})
    if contact is not None:
        contactVerified = contact['verified']
        if contactVerified:
            db.nda.update_one({"phone_number": phone}, {"$set": {"investments": { investment: "Signed"}}})
            return jsonify(
                status="contactVerified",
                message="Contact already added and verified.",
                name=contact['name'],
                email=contact['email'],
                phone=contact['phone_number']
            ), 200

    # Set access token. 
    two_factor_code = randint(100000, 999999)
    print("Contact verified ", contactVerified)
    if not contactVerified and contact is not None:
        db.nda.update_one({"phone_number": phone}, {"$set": {"investments": { investment: "Not Signed"}, "mfa_code": two_factor_code}})
    else:
        print("Made it here")
        db.nda.insert_one({
            "date_created": datetime.today(),
            "name": name,
            "email": email,
            "phone_number": phone,
            "investments": {
                investment: "Not Signed"
            },
            "mfa_code": two_factor_code,
            "verified": False
        })
    print(phone)

    fundX_ID, fundX_name = GET_fundX_ID(investment)

    # Format text message
    body = f"We appreciate your interest in the GET Equity Partners {fundX_name} Fund. Your part of the Non-Disclosure Agreement is complete - Thank You! \n\nYour verification code is: \n\n {two_factor_code}"
   


# ----------------------- TWILIO -----------------------

    client = Client(current_app.config['TWILIO_AUTH_ID'],current_app.config['TWILIO_AUTH_TOKEN'])
    message = client.messages.create(
        to=phone, 
        from_=current_app.config['TWILIO_SENDER_NUMBER'],
        body=body
    )

# ----------------------- TWILIO -----------------------
    
    return jsonify(
        status="contactAdded",
        message=phone
    ), 200