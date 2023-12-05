import plaid
from plaid.api import plaid_api
from plaid.model.item_public_token_exchange_request import ItemPublicTokenExchangeRequest
from plaid.model.processor_token_create_request import ProcessorTokenCreateRequest
import dwollav2
import uuid
from flask import current_app, g, jsonify
from werkzeug.local import LocalProxy
from GET_project import db 
from GET_project.api.plaid import plaid_client
import datetime
from datetime import datetime

def get_dwolla_token():

	if '_dwolla_token' not in g:

		dwolla_client = dwollav2.Client(key=current_app.config['DWOLLA_APP_KEY'], secret=current_app.config['DWOLLA_APP_SECRET'], environment=current_app.config['DWOLLA_APP_ENV']) # optional - defaults to production
		dwolla_app_token = g._dwolla_token = dwolla_client.Auth.client()

	return g._dwolla_token

dwolla_app_token = LocalProxy(get_dwolla_token)



# ------------------ WEBHOOKS ------------------------------
# ------------------ WEBHOOKS ------------------------------
# ------------------ WEBHOOKS ------------------------------

def list_dwolla_webhook_subscriptions():
		webhook_subscriptions = dwolla_app_token.get('webhook-subscriptions')
		webhook_subscriptions.body['total'] # => 1
		print(webhook_subscriptions.body)
		print(webhook_subscriptions.body['total'])
		return webhook_subscriptions.body, webhook_subscriptions.body['total']



def new_webhook_subscription(webhook_url):
    request_body = {
    'url': webhook_url,
    'secret': current_app.config['DWOLLA_WEBHOOK_SECRET'],
    }
    subscription = dwolla_app_token.post('webhook-subscriptions', request_body)
    subscription.headers['location']
    print(subscription.headers['location'])
    return subscription.headers['location']



def delete_dwolla_webhook_sub(webhook_url):
	dwolla_app_token.delete(webhook_url)


# ------------------ WEBHOOKS ------------------------------
# ------------------ WEBHOOKS ------------------------------
# ------------------ WEBHOOKS ------------------------------


def get_dwolla_acct_balance(dwolla_customer_url):

	funding_sources = dwolla_app_token.get('%s/funding-sources' % dwolla_customer_url)
	# print('funding_sources:', funding_sources.body)
	funding_source_account_url = funding_sources.body['_embedded']['funding-sources'][-1]['_links']['self']['href']
	print(funding_source_account_url)

	# funding_sources = dwolla_app_token.get('%s/funding-sources' % dwolla_customer_url)
	# print('dwolla 1')
	# customer_dwolla_funding_src = funding_sources.body['_embedded']['funding-sources'][1]['id']
	# print(customer_dwolla_funding_src)
	# customer_funding_url = "https://api-sandbox.dwolla.com/funding-sources/" + customer_dwolla_funding_src
	# # print(customer_funding_url)
	# customer_dwolla_balance = dwolla_app_token.get('%s/balance' % customer_funding_url)

	customer_dwolla_balance = dwolla_app_token.get('%s/balance' % funding_source_account_url)
	dwolla_balance = customer_dwolla_balance.body['balance']['value']
	print(dwolla_balance)
	return dwolla_balance


def dwolla_create_customer(investor_ID, institution_ID, create_customer_request_body, account_selected_value, new_fund):

	print('dwolla_create_customer')


	try:
		create_customer = dwolla_app_token.post('customers', create_customer_request_body)
		customer_url = create_customer.headers['location'] 
	except dwollav2.NotFoundError as e:
		print('get_on_dempand_auth - ', e.status)
		print('get_on_dempand_auth - ', e.body.code)
		customer_url = None



	# new_fund variable for creating a new GET Fund - not investor
	# if False then this is creating a new investor
	if new_fund == False:
		get_investor = db.investor_info.find_one({ "investor_ID": investor_ID })

		plaid_access_token = None
		insti_count = 0
		for intitution in get_investor["plaid"]["institutions"]:
			if intitution['institution_ID'] == institution_ID:
				plaid_access_token = intitution['plaid_access_token']
				break
			insti_count += 1


	# if True then this is creating a new GET fund
	if new_fund == True:
		print('this is a new fund -- ID = ', investor_ID)
		get_fund = db.fund_details.find_one({ "fund_ID": investor_ID })
		plaid_access_token = get_fund['plaid']['plaid_access_token']



	print('account_selected_value ----- > ', account_selected_value)
	funding_source_account = dwolla_link_new_account_funding_source(plaid_access_token, account_selected_value, customer_url)
	print('funding_source_account ----- > ', account_selected_value)


	return customer_url, funding_source_account



def dwolla_initiate_investment_transfer(fund_ID, investment_amount, investor_funding_source, fundX_funding_source, fund_name):


	TRANSACTION_LIMIT = current_app.config['TRANSACTION_LIMIT']
	print(investment_amount)

	transfer_list = []


	if float(investment_amount) > TRANSACTION_LIMIT:

		invest_loop_amount = float(investment_amount)

		while float(invest_loop_amount) >= 0:

			headers = {
    			'Idempotency-Key': str(uuid.uuid5(uuid.NAMESPACE_DNS, str(invest_loop_amount) + str(datetime.now().strftime("%m/%d/%Y, %H:%M:%S.%f"))))}

			if invest_loop_amount >= TRANSACTION_LIMIT:

				transfer_amount = TRANSACTION_LIMIT

				request_body = {
				'_links': {
					'source': {
					'href': investor_funding_source
					},
					'destination': {
					'href': fundX_funding_source
					}
				},
				'amount': {
					'currency': 'USD',
					'value': TRANSACTION_LIMIT,
				},
				'metadata': {
					'note': 'GET Equity Partners ' + fund_name + 'investment '
				},
				'clearing': {
					'destination': 'next-available'
				},
				'correlationId': fund_ID,
				}

			elif invest_loop_amount < TRANSACTION_LIMIT:

				transfer_amount = invest_loop_amount

				request_body = {
				'_links': {
					'source': {
					'href': investor_funding_source
					},
					'destination': {
					'href': fundX_funding_source
					}
				},
				'amount': {
					'currency': 'USD',
					'value': invest_loop_amount,
				},
				'metadata': {
					'note': 'GET Equity Partners ' + fund_name + ' investment'
				},
				'clearing': {
					'destination': 'next-available'
				},
				'correlationId': fund_ID,
				}

			try:
				transfer = dwolla_app_token.post('transfers', request_body, headers)
				transfer_url = transfer.headers['location'] 
				transfer = dwolla_app_token.get(transfer_url)
				transfer_status = transfer.body['status']
			except dwollav2.error.Error as e:
				return jsonify(code=e.body['code'], message=e.body['message']), 400
			 

			transfer_list.append([transfer_url, transfer_status, transfer_amount])

			invest_loop_amount -= TRANSACTION_LIMIT


			if invest_loop_amount <= 0:
				break

			print ('invest_loop_amount: ' + str(invest_loop_amount))


	else:


		headers = {
    	'Idempotency-Key': str(uuid.uuid5(uuid.NAMESPACE_DNS, str(investment_amount) + str(datetime.now().strftime("%m/%d/%Y, %H:%M:%S"))))}


		request_body = {
		'_links': {
			'source': {
			'href': investor_funding_source
			},
			'destination': {
			'href': fundX_funding_source
			}
		},
		'amount': {
			'currency': 'USD',
			'value': investment_amount,
		},
		'metadata': {
			'note': 'GET Equity Partners ' + fund_name + ' investment'
		},
		'clearing': {
			'destination': 'next-available'
		},
		'correlationId': fund_ID,
		}

		try:
			transfer = dwolla_app_token.post('transfers', request_body, headers)
			transfer_url = transfer.headers['location'] 
			transfer = dwolla_app_token.get(transfer_url)
			transfer_status = transfer.body['status'] 
		except dwollav2.error.Error as e:
			return jsonify(code=e.body['code'], message=e.body['message']), 400
		
		transfer_list.append([transfer_url, transfer_status, investment_amount])

		print('transfer_status: ' + transfer_status)

	return transfer_list






def dwolla_link_new_account_funding_source(plaid_access_token, account_selected_value, customer_url):


	# Create a processor token for a specific account id.
	create_request = ProcessorTokenCreateRequest(plaid_access_token, account_selected_value, "dwolla")
	create_response = plaid_client.processor_token_create(create_request)
	processor_token = create_response['processor_token']

	try:
		on_demand_authorization = dwolla_app_token.post('on-demand-authorizations')
		on_demand_authorization_accepted = on_demand_authorization.body['_links']['self']['href'] 
	except dwollav2.NotFoundError as e:
		print('get_on_dempand_auth - ', e.status)
		print('get_on_dempand_auth - ', e.body.code)
		on_demand_authorization_accepted = None


	dwolla_account_connect_request_body = {
		"_links": {
				"on-demand-authorization": {
					"href": on_demand_authorization_accepted
							}
					},
		'plaidToken': processor_token,
		  'name': 'GET_selected_funding_account'
	}


	try:
		dwolla_account_connect = dwolla_app_token.post('%s/funding-sources' % customer_url, dwolla_account_connect_request_body)
		funding_source_account = dwolla_account_connect.headers['location']
	except dwollav2.error.Error as e:
		print('connect_funding_source_account - ', e.status)
		print('connect_funding_source_account - ', e.body.code)
		funding_source_account = None

	return funding_source_account





def dwolla_check_verification_status(customer_url):

	customer = dwolla_app_token.get(customer_url)
	# print(customer.body)
	print(customer.body['status'])
	dwolla_customer_status = customer.body['status']

	try:
		beneficial_owners = dwolla_app_token.get('%s/beneficial-owners' % customer_url)
		beneficial_owner_id = beneficial_owners.body['_embedded']['beneficial-owners'][0]['id']
		beneficial_owner_url = 'https://api-sandbox.dwolla.com/beneficial-owners/' + beneficial_owner_id
		beneficial_owner = dwolla_app_token.get(beneficial_owner_url)
		dwolla_beneficial_owner_status = beneficial_owner.body['verificationStatus']
	except:
		dwolla_beneficial_owner_status = None

	print('dwolla_beneficial_owner_status: ' + str(dwolla_beneficial_owner_status))

	return dwolla_customer_status, dwolla_beneficial_owner_status





def dwolla_reverify_customer(customer_url, request_body):

	update_customer = dwolla_app_token.post(customer_url, request_body)

	return update_customer


def dwolla_reverify_owner(customer_url, request_body):

	beneficial_owners = dwolla_app_token.get('%s/beneficial-owners' % customer_url)
	beneficial_owner_id = beneficial_owners.body['_embedded']['beneficial-owners'][0]['id']
	beneficial_owner_url = 'https://api-sandbox.dwolla.com/beneficial-owners/' + beneficial_owner_id

	update_beneficial_owner = dwolla_app_token.post(beneficial_owner_url, request_body)

	return update_beneficial_owner
