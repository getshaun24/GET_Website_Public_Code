
from flask import current_app, g
from werkzeug.local import LocalProxy
from datetime import datetime, date, timedelta
import json
from GET_project.api.functions import json_serial

import plaid
from plaid.api import plaid_api
from plaid.model.identity_get_request import IdentityGetRequest
from plaid.model.auth_get_request import AuthGetRequest
from plaid.model.transactions_recurring_get_request import TransactionsRecurringGetRequest
from plaid.model.transactions_get_request import TransactionsGetRequest
from plaid.model.transactions_get_request_options import TransactionsGetRequestOptions
from plaid.api import plaid_api
from plaid.model.investments_holdings_get_request import InvestmentsHoldingsGetRequest
from plaid.model.user_create_request import UserCreateRequest
from plaid.model.credit_bank_income_get_request import CreditBankIncomeGetRequest
from plaid.model.credit_bank_income_get_request_options import CreditBankIncomeGetRequestOptions
from plaid.model.institutions_get_by_id_request import InstitutionsGetByIdRequest
from plaid.model.country_code import CountryCode
# from plaid.model.credit_sessions_get_request import CreditSessionsGetRequest
from plaid.model.link_token_create_request import LinkTokenCreateRequest
from plaid.model.link_token_create_request_user import LinkTokenCreateRequestUser
from plaid.model.asset_report_create_request import AssetReportCreateRequest
from plaid.model.asset_report_create_request_options import AssetReportCreateRequestOptions
from plaid.model.asset_report_user import AssetReportUser
from plaid.model.asset_report_get_request import AssetReportGetRequest

from plaid.model.identity_verification_create_request import IdentityVerificationCreateRequest
from plaid.model.identity_verification_request_user import IdentityVerificationRequestUser
# from plaid.model.identity_verification_user_phone_number import IdentityVerificationUserPhoneNumber
from plaid.model.client_user_id import ClientUserID
from plaid.model.user_name import UserName
from plaid.model.user_address import UserAddress
from plaid.model.generic_country_code import GenericCountryCode
from plaid.model.user_id_number import UserIDNumber
from plaid.model.id_number_type import IDNumberType

from plaid.model.watchlist_screening_individual_create_request import WatchlistScreeningIndividualCreateRequest
from plaid.model.watchlist_screening_request_search_terms import WatchlistScreeningRequestSearchTerms
from plaid.model.watchlist_screening_individual_name import WatchlistScreeningIndividualName
from plaid.model.watchlist_screening_document_value_nullable import WatchlistScreeningDocumentValueNullable
from plaid.model.generic_country_code_nullable import GenericCountryCodeNullable
from plaid.model.client_user_id_nullable import ClientUserIDNullable

from plaid.model.accounts_balance_get_request import AccountsBalanceGetRequest


def get_plaid_client():

    if '_plaid_client' not in g:


        if current_app.config['ENV'] == 'production':
            host = plaid.Environment.Production
        elif current_app.config['ENV'] == 'development':
            host = plaid.Environment.Development
        else:
            host = plaid.Environment.Sandbox



        plaid_configuration = plaid.Configuration(
            host=host,
            api_key={
                'clientId': current_app.config['PLAID_CLIENT_ID'],
                'secret': current_app.config['PLAID_SECRET']
            }
        )
        plaid_api_client = plaid.ApiClient(plaid_configuration)
        plaid_client = g._plaid_client = plaid_api.PlaidApi(plaid_api_client)

        return plaid_client

    return g._plaid_client

plaid_client = LocalProxy(get_plaid_client)





def format_plaid_error(e):
    response = json.loads(e.body)
    return {'error': {'status_code': e.status, 'display_message': response['error_message'], 'error_code': response['error_code'], 'error_type': response['error_type']}}





def create_plaid_user_id(investor_ID):
    user_id_request = UserCreateRequest(client_user_id=investor_ID)
    user_id_response = plaid_client.user_create(user_id_request)

    plaid_user_token = user_id_response['user_token']
    plaid_user_id  = user_id_response['user_id']
    plaid_request_id  = user_id_response['request_id']

    print("Plaid user token: 1 ___--------------------------- >", plaid_user_token)


    return plaid_user_token, plaid_user_id, plaid_request_id





def get_plaid_auth(plaid_access_token):

    auth_response = None
    try:
        print('Starting Auth pull')
        auth_response = plaid_client.auth_get(AuthGetRequest(access_token=plaid_access_token))
    except plaid.ApiException as e:
        error_response = format_plaid_error(e)
        print('Auth error: ' + error_response)


    account_ids_list = []
    account_list = []
    for ii in auth_response["accounts"]:
        iso_code = ii['balances']['iso_currency_code']
        if iso_code == 'USD':
            account_ids_list.append(ii["account_id"])
            account_list.append([ii["name"], ii["official_name"], ii["account_id"]])
        else:
            print('Currency not USD')


    return auth_response.to_dict(), account_ids_list, account_list





def get_plaid_balance_for_account(plaid_access_token, selected_bank_account_id):

    request = AccountsBalanceGetRequest(access_token=plaid_access_token)
    response = plaid_client.accounts_balance_get(request)
    accounts = response['accounts']
    for account in accounts:
        if account['account_id'] == selected_bank_account_id:
            return account['balances']['available']

    return None
    





def get_plaid_identity(plaid_access_token):

    identity_response = None
    try:
        print("Starting identity GET request")
        identity_response = plaid_client.identity_get(IdentityGetRequest(access_token=plaid_access_token))
        #pretty_print_response(identity_response.to_dict())
    except plaid.ApiException as e:
        error_response = format_plaid_error(e)
        print('Identity response error: ' + error_response)

    return identity_response.to_dict()






def get_plaid_transactions(plaid_access_token):


    transactions_clean = []
    transactions = None
    try:
        print('Starting first transactions pull')
        today = date.today()
        days = timedelta(days = 730) # 2 years
        transactions_request = TransactionsGetRequest(
            access_token=plaid_access_token,
            start_date=today-days,
            end_date=today,
            options=TransactionsGetRequestOptions()
        )
        transactions_response = plaid_client.transactions_get(transactions_request)
        transactions = transactions_response['transactions']

        # the transactions in the response are paginated, so make multiple calls while incrementing the cursor to
        # retrieve all transactions
        transaction_pull_count = 1
        while len(transactions) < transactions_response['total_transactions']:
            transactions_request = TransactionsGetRequest(
                access_token=plaid_access_token,
                start_date=today-days,
                end_date=today,
                options=TransactionsGetRequestOptions(
                    offset=len(transactions)
                )
            )
            transactions_response = plaid_client.transactions_get(transactions_request)
            transactions.extend(transactions_response['transactions'])
            transaction_pull_count += 1
            print('Transaction pull count: ' + str(transaction_pull_count))


# ------------------ clean and organize transactions for mongo ------------------


        # print("First transaction: " + str(transactions[0]))
        account_names = {}
        for account in transactions_response['accounts']:
            account_names[account.account_id] = account.name

        for transaction in transactions:
            try:
                t = {
                    "account_id": transaction['account_id'],
                    "account_name": account_names[transaction['account_id']],
                    "account_owner": transaction['account_owner'],
                    "amount": transaction['amount'],
                    "authorized_date": transaction['authorized_date'].strftime('%Y-%m-%d'),
                    "date": transaction['date'].strftime('%Y-%m-%d'),
                    "merchant_name": transaction['merchant_name'],
                    "payment_channel": transaction['payment_channel'],
                    "pending": transaction['pending'],
                    "iso_currency_code": transaction['iso_currency_code'],
                    "transaction_id": transaction['transaction_id'],
                    "transaction_type": transaction['transaction_type']
                }

                transactions_clean.append(t)
            except:
                print("Error with transaction: ")


    
    except plaid.ApiException as e:
        error_response = format_plaid_error(e)
        print('Transaction error: ' + str(error_response))


    return transactions_clean




def get_plaid_recurring_transactions(plaid_access_token, account_ids_list):
    try:
        recurring_request = TransactionsRecurringGetRequest(
        access_token=plaid_access_token,
        account_ids=account_ids_list,
        )
        recurring_response = plaid_client.transactions_recurring_get(recurring_request)
        inflow_streams = recurring_response.inflow_streams
        outflow_streams = recurring_response.outflow_streams
    except:
        inflow_streams = 'No Access Yet'
        outflow_streams = 'No Acess Yet'

    return inflow_streams, outflow_streams




def get_plaid_investment_holdings(plaid_access_token):
    

    holdings = None
    securities = None

    try:
        # Pull Holdings for an Item
        investments_request = InvestmentsHoldingsGetRequest(access_token=plaid_access_token)
        investment_response = plaid_client.investments_holdings_get(investments_request)
        investment_response = json.loads(json.dumps(investment_response.to_dict(), default=json_serial))

        # Handle Holdings response
        holdings = investment_response['holdings']

        # Handle Securities response
        securities = investment_response['securities']

        print('holdings --- > ', holdings)

    except plaid.ApiException as e:
        error_response = format_plaid_error(e)
        print('Investment error: ' + str(error_response))



    return holdings, securities















def get_plaid_income(plaid_access_token, plaid_user_token, plaid_request_id):


    plaid_income_request = CreditBankIncomeGetRequest(
        user_token=plaid_user_token,
        options=CreditBankIncomeGetRequestOptions(
            count=100
        )
        )

    plaid_income_response = plaid_client.credit_bank_income_get(plaid_income_request)

    try:
        institution_ID = plaid_income_response['bank_income'][0]['items'][0]['institution_id']
    except:
        institution_ID = 'xxx'

    plaid_income_response = json.loads(json.dumps(plaid_income_response.to_dict(), default=json_serial))
    return plaid_income_response, institution_ID





# def get_plaid_link_session(plaid_user_token):

        # session_request = CreditSessionsGetRequest(
        # user_token=plaid_user_token)

        # session_response = plaid_client.credit_sessions_get(session_request)




def get_institution_info(institution_ID):

    PLAID_COUNTRY_CODES=[CountryCode('US'), CountryCode('GB'), CountryCode('ES'), CountryCode('NL'), CountryCode('FR'), CountryCode('IE'), CountryCode('CA'), CountryCode('DE'), CountryCode('IT'), CountryCode('PL'), CountryCode('DK'), CountryCode('NO'), CountryCode('SE'), CountryCode('EE'), CountryCode('LT'), CountryCode('LV')]

    institution_request = InstitutionsGetByIdRequest(
        institution_id=institution_ID,
        country_codes=PLAID_COUNTRY_CODES
    )
    institution_response = plaid_client.institutions_get_by_id(institution_request)

    return institution_response












# -------------------------------------------------------------------------------


def update_plaid_link_token(plaid_client_user_id, plaid_access_token):
    # Create a one-time use link_token for the Item.
    # This link_token can be used to initialize Link
    # in update mode for the user.
    # Create a link_token for the given user
    request = LinkTokenCreateRequest(
            client_name="GET",
            country_codes=[CountryCode('US')],
            # additional_consented_products=['assets', 'income_verification'],
            language='en',
            access_token = plaid_access_token,
            webhook='https://webhook.sample.com',
            user=LinkTokenCreateRequestUser(
                client_user_id=plaid_client_user_id
            )
        )
    response = plaid_client.link_token_create(request)


    print(response)

    return response

# -------------------------------------------------------------------------------







def create_asset_report(plaid_client_user_id, plaid_access_token):
    # access_tokens is a list of Item access tokens.
# Note that the assets product must be enabled for all Items.
# All fields on the options object are optional.
    request = AssetReportCreateRequest(
        access_tokens=[plaid_access_token],
        days_requested=90,
        options=AssetReportCreateRequestOptions(
            webhook='https://www.example.com',
            client_report_id='123',
        )
    )
    response = plaid_client.asset_report_create(request)
    asset_report_id = response['asset_report_id']
    asset_report_token = response['asset_report_token']

    return asset_report_id, asset_report_token




def get_asset_report(asset_report_token):
    # asset_report_token is the token from the AssetReport.create response.
    try:
        request = AssetReportGetRequest(asset_report_token=asset_report_token)
        response = plaid_client.asset_report_get(request)
        report = response['report']
    except plaid.ApiException as e:
        if e.code == 'PRODUCT_NOT_READY':
            print('Asset report is not ready yet. Try again later.')
        else:
            print('error')











def get_plaid_identity_verification(investor_ID, email, phone, dob, given_name, family_name, street_address, city, state, zip_code, CountryCode, ssn):



    #test vars

    # phone =	"+19876543212"
    # given_name = "Leslie"
    # family_name = "Knope"
    # # Verification_code = "11111"
    # street_address = "123 Main St."
    # city = "Pawnee"
    # state = "IN"
    # zip_code = "46001"
    # month = "January"
    # day = "18"
    # year = "1975"
    # ssn = "123-45-6789"
    # dob = "1975-01-18"

    print('phone ---- > ', phone)



    identity_template_id = current_app.config['PLAID_IDENTITY_VERIFICATION_TEMPLATE_ID']

    identity_verification_request = IdentityVerificationCreateRequest(
        is_idempotent= True,
        is_shareable=True,
        template_id=identity_template_id,
        gave_consent=True,
        user=IdentityVerificationRequestUser(
            client_user_id=ClientUserID(investor_ID),
            email_address=str(email),
            phone_number=str(phone),
            date_of_birth=datetime.strptime(dob, "%Y-%M-%d").date(),
            name=UserName(
                given_name=str(given_name),
                family_name=str(family_name)
            ),
            address=UserAddress(
                street=str(street_address),
                city=str(city),
                region=str(state),
                postal_code=str(zip_code),
                country=GenericCountryCode(CountryCode)
            ),
            id_number=UserIDNumber(
            value=ssn.replace('-',''),
            type=IDNumberType('us_ssn')
            )
        )
    )
    
    try:
        identity_verification_response = plaid_client.identity_verification_create(identity_verification_request)
        watchlist_screening_id = identity_verification_response['watchlist_screening_id']
        print(identity_verification_response)
        return json.loads(json.dumps(identity_verification_response.to_dict(), default=json_serial)), watchlist_screening_id
    except plaid.ApiException as e:
        print('plaid identity verification failed')
        print(e)
        identity_verification_response = 'plaid_identity_verification_failed'
        watchlist_screening_id = 'plaid_identity_verification_failed'
        print(identity_verification_response)
        return identity_verification_response, watchlist_screening_id





def create_individual_watchlist(investor_ID, full_name, dob, watchlist_screening_id):
    
    request = WatchlistScreeningIndividualCreateRequest(
    search_terms=WatchlistScreeningRequestSearchTerms(
        watchlist_program_id=watchlist_screening_id,
        legal_name=WatchlistScreeningIndividualName(full_name),
        date_of_birth=datetime.strptime(dob, "%Y-%M-%d").date(),
        # document_number=WatchlistScreeningDocumentValueNullable('C31195855'),
        country=GenericCountryCode('US'),
    ),
    client_user_id=ClientUserID(investor_ID),
    )
    response = plaid_client.watchlist_screening_individual_create(request)









