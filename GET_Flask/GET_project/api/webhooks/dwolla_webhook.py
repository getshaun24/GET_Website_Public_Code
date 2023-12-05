from GET_project import db
# from GET_project import db
from flask import jsonify, Blueprint, request, current_app
# from rq import get_current_job
# from rq.registry import StartedJobRegistry
import time
# from GET_project.api.worker import redis_queue, redis_conn
# from GET_project import process_webhook_result
from flask_mail import Message
from GET_project.api.mail import mail, get_html_documents_needed, get_html_reverify_customer, get_html_reverify_funding_source, get_html_reverify_owner, get_html_documents_failed, get_html_documents_approved, get_html_investment_processed
from GET_project.api.functions import generate_generic_token
from GET_project.api.plaid import get_plaid_balance_for_account
from GET_project.api.dwolla import dwolla_initiate_investment_transfer

def process_webhook_result(body):
    
    # Step 1: see if the event is already in the dwolla_nofications collection (Dwolla recommendation)
    eventID = body['id']
    resourceID = body['resourceId']
    topic = body['topic']
    customerURL = body['_links']['customer']['href']
    eventExists = db.dwolla_notifications.find_one({"event_id": eventID})
    customer = None

    print('customerURL ----->', customerURL)


    # Step 2: if the event does not exist then add it to the collection
    if eventExists is None:
        db.dwolla_notifications.insert_one({
            "event_id": eventID,
            "resourceId": resourceID,
            "topic": topic,
            "timestamp": body['timestamp'],
            "_links": body['_links']
        })

    transfer_list = ['customer_transfer_created', 'customer_transfer_cancelled', 'customer_transfer_failed', 'customer_transfer_completed']
    transfer_bank_list = ['customer_bank_transfer_created', 'customer_bank_transfer_creation_failed', 'customer_bank_transfer_cancelled', 'customer_bank_transfer_failed', 'customer_bank_transfer_completed']
    documents_needed = ['customer_verification_document_needed', 'customer_beneficial_owner_verification_document_needed']
    reverify_customer = ['customer_reverification_needed']
    reverify_funding_source = ['customer_funding_source_unverified']
    reverify_owner = ['customer_beneficial_owner_reverification_needed']

    # Step 3: check to see if the topic was a transfer
    if topic in transfer_bank_list or topic in transfer_list:
        transferURL = body['_links']['resource']['href']
        # Try to update the transfer status
        if "cancelled" in topic:
            from GET_project.api.functions import transfer_failure_retrieve
            from GET_project.api.dwolla import get_dwolla_token
            transferURL = body['_links']['resource']['href']
            transfer_failure_code, failure_reason, transfer_status = transfer_failure_retrieve(transfer_url=transferURL, dwolla_token=get_dwolla_token)
            db.tranfers.update({"transfer_url": transferURL}, {"$set": {
                "transfer_status": topic,
                "transfer_failure_code": transfer_failure_code,
                "failure_reason": failure_reason,
                "transfer_status": transfer_status
            }})
        else:
            db.tranfers.update({"transfer_url": transferURL}, {"$set": {"transfer_status": topic}})

        if "completed" in topic:
            customer = db.investor_info.find_one({"dwolla.customer_url": customerURL})
            # Step 4: check to see if all of the funding is completed for that customer and fund and if so then update the investment status
            try:
                correlationID = body['correlationId']
                totalInvestmentAmount = customer['investments'][correlationID]['investment_amount']
                fund_investor_transfers = db.transfers.find({"dwolla_customer_url": customerURL, "fund_ID": correlationID})
                totalTransferCompleted = 0
                for record in fund_investor_transfers:
                    if "completed" in record.status:
                        totalTransferCompleted += record['transfer_amount']
                if totalTransferCompleted == totalInvestmentAmount:
                    db.investor_info.update({"dwolla.customer_url": customerURL}, {"$set": {"investments."+correlationID+".investment_status": "Completed"}})
            except Exception as e:
                print(f'Could not update the investment status for customer ', customerURL, ': ', e)

    TEST_EMAIL_RECIPIENTS = current_app.config['TEST_EMAIL_RECIPIENTS']
    MAIL_USERNAME = current_app.config['MAIL_USERNAME']
    SITE_DOMAIN = current_app.config['SITE_DOMAIN']

    # If document upload failed, generate encrypted email and send link
    if topic == 'customer_verification_document_failed':
        investor_info = db.investor_info.find_one({"dwolla.customer_url": customerURL}, {'email': 1, 'investor_ID': 1, 'signup_progress': 1, 'investments': 1, '_id': 0})
        signup_progress = None

        if investor_info is not None:
            email = investor_info['email']
            investments = investor_info['investments']
            investor_id = investor_info['investor_ID']
            signup_progress = investor_info['signup_progress']

            if signup_progress == 'Documents Pending':

                db.investor_info.update_one({"dwolla.customer_url": customerURL}, {'$set': {'signup_progress': 'Document Verification Failed'}})

                for investment_name, investment_data in investments.items():
                    if investment_data['investment_status'] == 'documents_pending_transaction_confirmed':
                        db.investor_info.update_one({"dwolla.customer_url": customerURL}, {'$set': {'investments.'+investment_name+'.investment_status': 'document_verification_failed_transaction_confirmed'}})

            email_url_link = SITE_DOMAIN + '/login_pages/login'
            
            email_internal = email_to = current_app.config['EMAIL_LIST']

            msg = Message(
                sender=MAIL_USERNAME,
                recipients=[email],
                subject="GET Equity Partners - Document Verification Failed",
                html=get_html_documents_failed(email_url_link)
            )
            mail.send(msg)

            msg = Message(
                sender=MAIL_USERNAME,
                recipients=email_internal,
                subject="GET Equity Partners - Document Verification Failed",
                body="Dwolla customer verification document failed for investor ID: " + investor_id + " with email: " + email
            )
            mail.send(msg)
        
        else:
            print("Could not find the matching investor record in the investor_info collection with the Dwolla customer URL: " + customerURL)

    # If document upload was approved, generate encrypted email and send link
    if topic == 'customer_verification_document_approved':
        investor_info = db.investor_info.find_one({"dwolla.customer_url": customerURL}, {'email': 1, 'investor_ID': 1, 'signup_progress': 1, 'investments': 1, 'plaid': 1, '_id': 0})
        fund_id = None
        investor_funding_source = None
        account_id = None
        investment_amount = None
        signup_progress = None

        if investor_info is not None:
            email = investor_info['email']
            investments = investor_info['investments']
            investor_id = investor_info['investor_ID']
            signup_progress = investor_info['signup_progress']

            if signup_progress == 'Documents Pending':

                db.investor_info.update_one({"dwolla.customer_url": customerURL}, {'$set': {'signup_progress': 'Signup Successful'}})

                for investment_name, investment_data in investments.items():
                    if investment_data['investment_status'] == 'documents_pending_transaction_confirmed':
                        fund_id = investment_name
                        investor_funding_source = investment_data["active_investor_dwolla_account_url"]
                        account_id = investment_data['active_selected_bank_account_id']
                        investment_amount = investment_data['investment_amount']
                        break
                        
        
        fundX_funding_source = None
        fund_name = None
        if fund_id is not None:
            get_fund = db.fund_details.find_one({ "fund_ID": fund_id })
            if get_fund is not None:
                fund_name = get_fund["fund_name"]
                fundX_funding_source = get_fund['dwolla']['GET_fund_dwolla_account_url']

        plaid_access_token = None
        plaid = investor_info['plaid']
        if account_id is not None:
            for institution in plaid['institutions']:
                plaid_access_token = institution['plaid_access_token']
                for pull in institution['plaid_pulls']['Auth']:
                    for account in pull['auth_response']['accounts']:
                        if account_id == account['account_id']:
                            break

        # Found the correct account ID and plaid access token
        if plaid_access_token is not None and account_id is not None and fund_id is not None and investment_amount is not None and investor_funding_source is not None and fundX_funding_source is not None and fund_name is not None:
            balance = get_plaid_balance_for_account(plaid_access_token=plaid_access_token, selected_bank_account_id=account_id)
            print(balance)
            if balance is not None and balance > investment_amount:
                # Process Dwolla transaction
                transfer_list = dwolla_initiate_investment_transfer(fund_ID=fund_id, investment_amount=investment_amount, investor_funding_source=investor_funding_source, fundX_funding_source=fundX_funding_source, fund_name=fund_name)
                db.investor_info.update_one({"dwolla.customer_url": customerURL}, {'$set': {'investments.'+investment_name+'.investment_status': 'invested_payment_pending'}})
                # Send notification email
                if TEST_EMAIL_RECIPIENTS == True:
                    email_to = current_app.config['EMAIL_LIST']
                else:
                    email_to = [email]

                email_url_link = SITE_DOMAIN + '/login_pages/login'
                msg = Message(
                    sender=MAIL_USERNAME,
                    recipients=email_to,
                    subject="GET Equity Partners - Investment Processed",
                    html=get_html_investment_processed(email_url_link)
                )
                mail.send(msg)

            else: 
                # Send notification email
                email_to = current_app.config['EMAIL_LIST']

                msg = Message(
                    sender=MAIL_USERNAME,
                    recipients=email_to,
                    subject="GET Equity Partners - Dwolla Webhook Notification",
                    body="Either the balance was not sufficient or plaid returned no account on the balance pull for investor " + investor_id
                )
                mail.send(msg)

        else:
            # Send notification email
            email_to = current_app.config['EMAIL_LIST']

            msg = Message(
                sender=MAIL_USERNAME,
                recipients=email_to,
                subject="GET Equity Partners - Dwolla Webhook Notification",
                body="Something went wrong for the dwolla_document_verification_approved webook processing transfer for investor " + investor_id
            )
            mail.send(msg)


        # investor = db.investor_info.find_one({"dwolla.customer_url": customerURL}, {'email': 1, 'investor_ID': 1, '_id': 0})
        # if investor is not None:
        #     email = investor['email']
        #     email_url_link = SITE_DOMAIN + '/login_pages/login'
            
        #     if TEST_EMAIL_RECIPIENTS == True:
        #         email_to = email_to = current_app.config['EMAIL_LIST']
        #     else:
        #         email_to = email

        #     msg = Message(
        #         sender=MAIL_USERNAME,
        #         recipients=email_to,
        #         subject="GET Equity Partners - Document Verification Approved",
        #         html=get_html_documents_failed(email_url_link)
        #     )
        #     mail.send(msg)
        
        # else:
        #     print("Could not find the matching investor record in the investor_info collection with the Dwolla customer URL: " + customerURL)

    # If documents are needed, generate encrypted email and send link
    # if topic in documents_needed:
    #     investor = db.investor_info.find_one({"dwolla.customer_url": customerURL}, {'email': 1, 'investor_ID': 1, '_id': 0})
    #     if investor is not None:
    #         investor_ID = investor['investor_ID']
    #         email = investor['email']
    #         # data_to_load = {'user_ID': investor_ID, 'email': email} # Anything else to add???
    #         # email_url_link = SITE_DOMAIN + '/investor_dashboard/dwolla_reverification/documents_needed/?token=' + generate_generic_token(data_to_load)
    #         email_url_link = SITE_DOMAIN + '/login_pages/login'
            
    #         if TEST_EMAIL_RECIPIENTS == True:
    #             email_to = email_to = current_app.config['EMAIL_LIST']
    #         else:
    #             email_to = email

    #         msg = Message(
    #             sender=MAIL_USERNAME,
    #             recipients=email_to,
    #             subject="GET Equity Partners - Dwolla Documents Required",
    #             html=get_html_documents_needed(email_url_link)
    #         )
    #         mail.send(msg)
        
    #     else:
    #         print("Could not find the matching investor record in the investor_info collection with the Dwolla customer URL: " + customerURL)

    # If customer reverification is needed, generate encrypted email and send link
    # if topic in reverify_customer:
    #     investor = db.investor_info.find_one({"dwolla.customer_url": customerURL}, {'email': 1, 'investor_ID': 1, '_id': 0})
    #     if investor is not None:
    #         investor_ID = investor['investor_ID']
    #         email = investor['email']
    #         # data_to_load = {'user_ID': investor_ID, 'email': email} # Anything else to add???
    #         # email_url_link = SITE_DOMAIN + '/investor_dashboard/dwolla_reverification/reverify_customer/?token=' + generate_generic_token(data_to_load)
    #         email_url_link = SITE_DOMAIN + '/login_pages/login'

    #         if TEST_EMAIL_RECIPIENTS == True:
    #             email_to = email_to = current_app.config['EMAIL_LIST']
    #         else:
    #             email_to = email

    #         msg = Message(
    #             sender=MAIL_USERNAME,
    #             recipients=email_to,
    #             subject="GET Equity Partners - Reverify Dwolla Customer",
    #             html=get_html_reverify_customer(email_url_link)
    #         )
    #         mail.send(msg)
        
    #     else:
    #         print("Could not find the matching investor record in the investor_info collection with the Dwolla customer URL: " + customerURL)

    # If funding source reverification is needed, generate encrypted email and send link
    # if topic in reverify_funding_source:
    #     investor = db.investor_info.find_one({"dwolla.customer_url": customerURL}, {'email': 1, 'investor_ID': 1, '_id': 0})
    #     if investor is not None:
    #         investor_ID = investor['investor_ID']
    #         email = investor['email']
    #         # data_to_load = {'user_ID': investor_ID, 'email': email} # Anything else to add???
    #         # email_url_link = SITE_DOMAIN + '/investor_dashboard/dwolla_reverification/reverify_funding_source/?token=' + generate_generic_token(data_to_load)
    #         email_url_link = SITE_DOMAIN + '/login_pages/login'
            
    #         if TEST_EMAIL_RECIPIENTS == True:
    #             email_to = email_to = current_app.config['EMAIL_LIST']
    #         else:
    #             email_to = email

    #         msg = Message(
    #             sender=MAIL_USERNAME,
    #             recipients=email_to,
    #             subject="GET Equity Partners - Dwolla Reverify Funding Source Required",
    #             html=get_html_reverify_funding_source(email_url_link)
    #         )
    #         mail.send(msg)
        
    #     else:
    #         print("Could not find the matching investor record in the investor_info collection with the Dwolla customer URL: " + customerURL)

    # If documents are needed generate encrypted email and send link
    # if topic in reverify_owner:
    #     investor = db.investor_info.find_one({"dwolla.customer_url": customerURL}, {'email': 1, 'investor_ID': 1, '_id': 0})
    #     if investor is not None:
    #         investor_ID = investor['investor_ID']
    #         email = investor['email']
    #         # data_to_load = {'user_ID': investor_ID, 'email': email} # Anything else to add???
    #         # email_url_link = SITE_DOMAIN + '/investor_dashboard/dwolla_reverification/reverify_owner/?token=' + generate_generic_token(data_to_load)
    #         email_url_link = SITE_DOMAIN + '/login_pages/login'
            
    #         if TEST_EMAIL_RECIPIENTS == True:
    #             email_to = current_app.config['EMAIL_LIST'].split(';')
    #         else:
    #             email_to = email

    #         msg = Message(
    #             sender=MAIL_USERNAME,
    #             recipients=email_to,
    #             subject="GET Equity Partners - Dwolla Owner Reverification Needed",
    #             html=get_html_reverify_owner(email_url_link)
    #         )
    #         mail.send(msg)
        
    #     else:
    #         print("Could not find the matching investor record in the investor_info collection with the Dwolla customer URL: " + customerURL)


    # Step 5: update the notification count
    if customer is None:
        customer = db.investor_info.find_one({"dwolla.customer_url": customerURL})
    if customer is not None:
        if 'notification_count' not in customer:
            db.investor_info.update({"dwolla.customer_url": customerURL}, {"$set": {"notification_count": 1}})
        elif customer['notification_count'] is None:
            db.investor_info.update({"dwolla.customer_url": customerURL}, {"$set": {"notification_count": 1}})
        else:
            db.investor_info.update({"dwolla.customer_url": customerURL}, {"$set": {"notification_count": customer['notification_count']+1}})

    
    
        
    # This is for Redis. Don't uncomment below if not using Redis
    # Return job information
    # job = get_current_job()
    # time.sleep(10)

    # return {
    #     "job_id": job.id,
    #     "job_enqueued_at": job.enqueued_at.isoformat(),
    #     "job_started_at": job.started_at.isoformat(),
    #     "input": body,
    #     "result": "Success"
    # }

def isSignatureValid(body=None, signature=None):
    # Create a HMAC thing
    import hmac
    import hashlib
    # Comment out this line when testing with requests from Dwolla and leave uncommented in production.
    # return signature == hmac.new(current_app.config['DWOLLA_WEBHOOK_SECRET'], body, hashlib.sha256).hexdigest()
    return True

def response(statusCode=400, message=None):
    return jsonify(body=message, statusCode=statusCode)

Dwolla_Webhook_Blueprint = Blueprint('Dwolla_Webhook', __name__)
@Dwolla_Webhook_Blueprint.route('/api/webhooks/dwolla_webhook/', methods=['GET','POST']) # <- from '/'
def dwolla_webhook():
    
    if request.method == "POST":
        print("Request recieved")
        print(request.url)
        body = request.json

        signature = request.headers["X-Request-Signature-SHA-256"]
        print(f'${signature}: Received webhook. Validating request...')

        if signature is None:
            print("No signature found in request headers")
            return response(400, "No signature found")

        print(body)
        print(current_app.config['DWOLLA_WEBHOOK_SECRET'])

        if not (isSignatureValid(body=body, signature=signature)):
            print("Signature from headers could not be validated against secret")
            return response(400, "Invalid signature")
        
        # try:  
            # get url that the person has entered
            # from GET_project.api.webhooks.dwolla_webhook import process_webhook_result
            # job = current_app.q.enqueue_call(process_webhook_result, body)
            # job = redis_queue.enqueue(process_webhook_result, body)
        job = process_webhook_result(body)
            # print(job.get_id())
        return response(200, "Success")
            
        # except Exception as e:
        #     print(f'[${signature}]: Failed to place webhook in queue for processing', e)
        #     return response(500, "Failed to place webhook in queue")

    return response(400, 'Only POST requests are supported')



# Dwolla_Running_Jobs_Blueprint = Blueprint('Dwolla_Jobs_Running', __name__)
# @Dwolla_Running_Jobs_Blueprint.route('/api/webhooks/dwolla_webhook/jobs_running', methods=['GET']) # <- from '/'
# def dwolla_running_jobs():

#     registry = StartedJobRegistry('default', connection=redis_conn)
#     for job in registry.get_queue().get_jobs():
#         print(job.get_status())
#     return jsonify(200, registry.get_queue().job_ids)

# Dwolla_Expired_Jobs_Blueprint = Blueprint('Dwolla_Jobs_Expired', __name__)
# @Dwolla_Expired_Jobs_Blueprint.route('/api/webhooks/dwolla_webhook/jobs_expired', methods=['GET']) # <- from '/'
# def dwolla_expired_jobs():

#     registry = StartedJobRegistry('default', connection=redis_conn)
#     for job in registry.get_queue().finished_job_registry.get_job_ids():
#         print(job)
#     return jsonify(200, str(registry.get_queue().finished_job_registry.get_job_ids()))