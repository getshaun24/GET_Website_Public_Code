from flask import Blueprint, request, jsonify
from GET_project import db

NDA_EnterPhoneMFA_Blueprint = Blueprint('NDA_EnterPhoneMFA', __name__)
@NDA_EnterPhoneMFA_Blueprint.route('/api/nda/enterPhoneMFA/', methods=['GET', 'POST']) # <- from '/'
def NDA_EnterPhoneMFA():

    print('made it here')

    
    phone = request.json.get("phone_number", None)
    investment = request.json.get("investment", None)
    mfa_code = request.json.get("mfa_code", None)

    print('mfa_code - ', mfa_code)

    if phone is None or mfa_code is None or investment is None:
        return jsonify(status="fieldError", message="No verification code was entered"), 400

    # Format phone number
    phone = "".join("".join("".join("".join("".join(phone.split('-')).split('(')).split(')')).split(' ')).split('+'))
    if len(phone) == 11:
        phone = "+" + phone

    print('phone ', phone)

    # Check to see if that phone number exists already. 
    contact = db.nda.find_one({"phone_number": phone})
    if contact is None:
        return jsonify(
            status="contactNotFound",
            message="Could not find contact."
        ), 400
    print(mfa_code)
    print(contact['mfa_code'])
    mfa_code_match = str(contact['mfa_code']) == str(mfa_code)

    if mfa_code_match:
        db.nda.update_one({"phone_number": phone}, {"$set": {"verified": True, "investments": { investment: "Signed"}}})
        return jsonify(
            status="success",
            message="Verification code matches."
        ), 200
    else:
        return jsonify(
            status="invalidCode",
            message="Verification code does not match."
        ), 406
    

