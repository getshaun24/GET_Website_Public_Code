


# from server import mongo_client, mongoDB_master_access, app
# from project.mongo import mongo_client, mongoDB_master_access
# from project.mongo import db
import sys
from flask import session, current_app
import json
import re
import dwollav2
from datetime import date, datetime

from GET_project import db
from itsdangerous import URLSafeTimedSerializer, SignatureExpired, BadSignature












def transfer_failure_retrieve(transfer_url, dwolla_token):

    # client = dwollav2.Client(key = current_app['DWOLLA_APP_KEY'], secret = current_app['DWOLLA_APP_SECRET'], environment = 'sandbox') # optional - defaults to production
    # dwolla_app_token = client.Auth.client()
    dwolla_app_token = dwolla_token


    transfer_retrieve = dwolla_app_token.get(transfer_url)
    transfer_status = transfer_retrieve.body['status']

    try:
        get_transfer_failure_status = dwolla_app_token.get('%s/failure' % transfer_url)
        transfer_failure_code = get_transfer_failure_status.body['code']
        if transfer_failure_code == 'R01':
            failure_reason = "Insufficient Funds. Available balance is not sufficient to cover the dollar value of the debit entry."
        elif transfer_failure_code == 'R02':
            failure_reason = "Bank Account Closed. Previously active account has been closed."
        elif transfer_failure_code == 'R03':
            failure_reason = "No Account/Unable to Locate Account. Account number structure is valid, but doesn’t match individual identified in entry or is not an open account."
        elif transfer_failure_code == 'R04':
            failure_reason = "Invalid Bank Account Number Structure. Account number structure is not valid."
        elif transfer_failure_code == 'R05':
            failure_reason = "Unauthorized debit to consumer account. A debit entry was transmitted to a consumer account that was not authorized by the Receiver. Written Statement is required."
        elif transfer_failure_code == 'R06':
            failure_reason = "Returned per ODFI’s request. The ODFI has requested that the RDFI return the ACH entry as an erroneous entry. If the RDFI agrees to return the entry, the ODFI must indemnify the RDFI in accordance with guidelines."
        elif transfer_failure_code == 'R07':
            failure_reason = "Authorization revoked by customer. The receiver who previously authorized an entry has revoked authorization with the originator for this debit entry."
        elif transfer_failure_code == 'R08':
            failure_reason = "Payment stopped. The Receiver has placed a stop payment order on this debit entry, which may be placed on one or more debit entries."
        elif transfer_failure_code == 'R09':
            failure_reason = "Uncollected funds. A sufficient book or ledger balance exists to satisfy the dollar value of the transaction  (i.e., uncollected checks), but the available balance is below the dollar value of the debit entry."
        elif transfer_failure_code == 'R10':
            failure_reason = "Customer advises unauthorized, improper,  ineligible, or part of an incomplete transaction. The RDFI has been notified by the receiver (ie. customer that the entry is unauthorized, improper or ineligible)."
        elif transfer_failure_code == 'R11':
            failure_reason = "Check truncation entry return. To be used when returning a check truncation entry. This reason for return should be used only if no other return reason code is applicable."
        elif transfer_failure_code == 'R12':
            failure_reason = "Branch sold to another DFI. A financial institution received an entry to an account that was sold to another FI."
        elif transfer_failure_code == 'R13':
            failure_reason = "Invalid ACH routing number. Entry contains a receiving DRI identification or gateway identification that is not a valid ACH routing number."
        elif transfer_failure_code == 'R14':
            failure_reason = "Representative payee deceased or unable to continue in that capacity. The representative payee is a person either deceased or no longer able to continue in original capacity (ie. legally incapacitated adults or minors), while the beneficiary is not deceased."
        elif transfer_failure_code == 'R15':
            failure_reason = "Beneficiary or account holder deceased. (1) The beneficiary is deceased. The beneficiary may or may not be the account holder; (2) The account holder (acting in a non-representative payee capacity) is an owner of the account and is deceased."
        elif transfer_failure_code == 'R16':
            failure_reason = "Account frozen/Entry returned per OFAC instruction. 1) Access to account is restricted due to specific action taken by the RDFI or legal action 2) OFAC has instructed the RDFI or gateway to return the entry."
        elif transfer_failure_code == 'R17':
            failure_reason = "File record edit criteria. Fields can’t be processed by RDFI."
        elif transfer_failure_code == 'R18':
            failure_reason = "Improper effective entry date. The effective entry date for a credit entry is more than two banking days after the banking day of processing as established by the originating ACH operator or the effective date is after window of processing."
        elif transfer_failure_code == 'R19':
            failure_reason = "Amount field error. Amount field is non-numeric, zero, or exceeding $25,000."
        elif transfer_failure_code == 'R20':
            failure_reason = "Non-transaction account. The ACH entry destined for a non-transaction account, for example, an account against which transactions are prohibited or limited."
        elif transfer_failure_code == 'R21':
            failure_reason = "Invalid company identification. The company identification information not valid."
        elif transfer_failure_code == 'R22':
            failure_reason = "Invalid individual ID number. In CIE and MET entries, when the original ID number isn’t used, the receiver has indicated to the RDFI that the number with which the Originator was identified is not correct."
        elif transfer_failure_code == 'R23':
            failure_reason = "Credit entry refused by receiver.  Receiver returned entry because, for instance,  minimum or exact amount not remitted. Any credit entry that is refused by the receiver may be returned by the RDFI."
        elif transfer_failure_code == 'R24':
            failure_reason = "Duplicate entry. The RDFI has received what appears to be a duplicate entry; i.e., the trace number, date, dollar amount and/or other data matches another transaction."
        elif transfer_failure_code == 'R25':
            failure_reason = "Addenda error. Addenda record indicator value is incorrect, with code invalid, out of sequence,  or missing."
        elif transfer_failure_code == 'R26':
            failure_reason = "Mandatory field error. Erroneous data or missing data in a mandatory field."
        elif transfer_failure_code == 'R27':
            failure_reason = "Trace number error. Original entry trace number is not present or does not correspond correctly in the addenda record on a return or notification of change entry."
        elif transfer_failure_code == 'R28':
            failure_reason = "Routing number check digit error. The check digit for the routing number is invalid."
        elif transfer_failure_code == 'R29':
            failure_reason = "Corporate customer advises not authorized. The RDFI has been notified by receiver (non-consumer) that a specific transaction is unauthorized."
        elif transfer_failure_code == 'R30':
            failure_reason = "RDFI not participant in check truncation program. The RDFI does not participate in a check truncation program."
        elif transfer_failure_code == 'R31':
            failure_reason = "Permissible return entry (CCD and CTX only). The REFI may return a CCD or CTX entry that the ODFI agrees to accept."
        elif transfer_failure_code == 'R32':
            failure_reason = "RDFI non-settlement. The RDFI is not able to settle the entry."
        elif transfer_failure_code == 'R33':
            failure_reason = "Return of XCK entry. The RDFI determines at its sole discretion to return an XCK entry."
        elif transfer_failure_code == 'R34':
            failure_reason = "Limited participation DFI. The RDFI participation has been limited by a federal or state supervisor."
        elif transfer_failure_code == 'R35':
            failure_reason = "Return of improper debit entry. Debit entries are not permitted for CIE entries or to loan accounts."
        elif transfer_failure_code == 'R36':
            failure_reason = "Return of improper credit entry. ACH credit entries are not permitted for use with ARC, BOC, POP, RCK, TEL, XCK."
        elif transfer_failure_code == 'R37':
            failure_reason = "Source document presented for payment. The source document to which an ARC, BOX, or POP entry relates has been presented for payment."
        elif transfer_failure_code == 'R38':
            failure_reason = "Stop payment on source document"
        elif transfer_failure_code == 'R39':
            failure_reason = "Improper source document/source document presented for payment"
        elif transfer_failure_code == 'R40':
            failure_reason = "Return of ENR entry by federal government agency"
        elif transfer_failure_code == 'R41':
            failure_reason = "Invalid transaction code"
        elif transfer_failure_code == 'R42':
            failure_reason = "Routing number/check digit error"
        elif transfer_failure_code == 'R43':
            failure_reason = "Invalid DFI account number"
        elif transfer_failure_code == 'R44':
            failure_reason = "Invalid individual ID number/identification number"
        elif transfer_failure_code == 'R45':
            failure_reason = "Invalid individual name/company name"
        elif transfer_failure_code == 'R46':
            failure_reason = "Invalid representative payee indicatort"
        elif transfer_failure_code == 'R47':
            failure_reason = "Duplicate enrollment"
        elif transfer_failure_code == 'R50':
            failure_reason = "State law affecting RCK acceptance"
        elif transfer_failure_code == 'R51':
            failure_reason = "Item related to RCK entry is ineligible or RCK entry is improper"
        elif transfer_failure_code == 'R52':
            failure_reason = "Stop payment on item related to RCK entry"
        elif transfer_failure_code == 'R53':
            failure_reason = "Item and RCK entry presented for payment"
        elif transfer_failure_code == 'R61':
            failure_reason = "Misrouted return"
        elif transfer_failure_code == 'R62':
            failure_reason = "Return of erroneous or reversing debt"
        elif transfer_failure_code == 'R67':
            failure_reason = "Duplicate return"
        elif transfer_failure_code == 'R68':
            failure_reason = "Untimely return"
        elif transfer_failure_code == 'R69':
            failure_reason = "Field error(s)"
        elif transfer_failure_code == 'R70':
            failure_reason = "Permissible return entry not accepted/return not requested by ODFI"
        elif transfer_failure_code == 'R71':
            failure_reason = "Misrouted dishonored return"
        elif transfer_failure_code == 'R72':
            failure_reason = "Untimely dishonored return"
        elif transfer_failure_code == 'R73':
            failure_reason = "Timely original return"
        elif transfer_failure_code == 'R74':
            failure_reason = "Corrected return"
        elif transfer_failure_code == 'R75':
            failure_reason = "Return not duplicate"
        elif transfer_failure_code == 'R76':
            failure_reason = "No errors found"
        elif transfer_failure_code == 'R77':
            failure_reason = "Non-acceptance of R62 dishonored return"
        elif transfer_failure_code == 'R80':
            failure_reason = "IAT entry coding errors"
        elif transfer_failure_code == 'R81':
            failure_reason = "Non-participant in IAT program"
        else:
            transfer_failure_code = "Failure Unknown - Contact Admin"
            failure_reason = "Failure Unknown - Contact Admin"
            print('Failure Reason --> ', failure_reason, file=sys.stderr)
    except:
        transfer_failure_code = "None"
        failure_reason = "None"
        print('No Failure', file=sys.stderr)

    return transfer_failure_code, failure_reason, transfer_status



#---------------------------------------------------------------------------------------------------------------------->
#---------------------------------------------------------------------------------------------------------------------->
#---------------------------------------------------------------------------------------------------------------------->


def takeSecond(elem):
    return elem[1]



#---------------------------------------------------------------------------------------------------------------------->
#---------------------------------------------------------------------------------------------------------------------->
#---------------------------------------------------------------------------------------------------------------------->


def GET_fundX_ID(selected_fund):

    NANO_FUND_ID = current_app.config['NANO_FUND_ID']
    ECO_FUND_ID = current_app.config['ECO_FUND_ID']
    NEXT_FUND_ID = current_app.config['NEXT_FUND_ID']

    fundX_ID = ''
    fundX_name = ''
    if 'Nanotechnology' in selected_fund:
        fundX_ID = NANO_FUND_ID
        fundX_name = 'US Nanotechnology Fund A'
    if 'Eco_Energy' in selected_fund:
        fundX_ID = ECO_FUND_ID
        fundX_name = 'Eco Energy Fund'
    if 'NEXT_AI' in selected_fund:
        fundX_ID = NEXT_FUND_ID
        fundX_name = 'NEXT AI Fund'
    
    return fundX_ID, fundX_name




def pretty_print_response(response):
  print(json.dumps(response, indent=2, sort_keys=True), file=sys.stderr)


def format_error(e):
  return {'error': {'display_message': e.display_message, 'error_code': e.code, 'error_type': e.type, 'error_message': e.message } }



def find_between(s, first, last):
    try:
        start = s.index(first) + len(first)
        end = s.index(last, start)
        return s[start:end]
    except ValueError:
        return ""



def json_serial(obj):
    """JSON serializer for objects not serializable by default json code"""

    if isinstance(obj, (datetime, date)):
        return str(obj)
    raise TypeError ("Type %s not serializable" % type(obj))

def generate_password_token(data): 
    serializer = URLSafeTimedSerializer(current_app.config['ITS_DANGEROUS_SECRET'], salt="createpasswordsalt")
    token = serializer.dumps(data)
    return token

def generate_generic_token(data): 
    serializer = URLSafeTimedSerializer(current_app.config['ITS_DANGEROUS_SECRET'], salt="gEner!C")
    token = serializer.dumps(data)
    return token

def confirm_password_token(token, expire_time=3600):
    serializer = URLSafeTimedSerializer(current_app.config['ITS_DANGEROUS_SECRET'])
    try:
        confirmed_token = serializer.loads(token, max_age=expire_time, salt="createpasswordsalt")
    except Exception:
        return False
    return True

def get_token_data(token, expire_time=4000):
    serializer = URLSafeTimedSerializer(current_app.config['ITS_DANGEROUS_SECRET'])
    try:
        confirmed_token = serializer.loads(token, max_age=expire_time, salt="createpasswordsalt")
        return confirmed_token
    except Exception:
        return None