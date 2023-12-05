from flask import Flask, render_template, session, redirect, url_for
from flask_session import Session
from flask_cors import CORS
import secrets 
# from . import mongo
import os

from flask_login import LoginManager, login_required, logout_user
from GET_project.api.models import User
# from GET_project import db, close_mongo_db
# from GET_project.api.mongo import close_mongo_db
import sys

from datetime import datetime
from datetime import timedelta
from datetime import timezone

from flask import Flask
from flask import jsonify

from flask_jwt_extended import create_access_token
from flask_jwt_extended import get_jwt
from flask_jwt_extended import get_jwt_identity
from flask_jwt_extended import jwt_required
from flask_jwt_extended import JWTManager
from flask_jwt_extended import set_access_cookies
from flask_jwt_extended import unset_jwt_cookies

import pymongo

# from rq import Queue, get_current_job
# from rq.job import Job
# from GET_project.api.worker import redis_conn, redis_queue

from flask import request
# Change this depending on the config you want to use.
# from config import DevelopmentConfig
import config

from dotenv import load_dotenv
load_dotenv()

# def create_app():
app = Flask(__name__, template_folder="", instance_relative_config=True)
app.config.from_object(os.environ['APP_SETTINGS'])
# app.config['SECRET_KEY'] = secrets.token_hex()
app.config['SECRET_KEY'] = 'GET_Vamire'

CORS(app, origins=["https://thewallstreetnetwork.com", "https://www.thewallstreetnetwork.com", "www.thewallstreetnetwork.com", "https://www.dev.thisisget.com", "https://dev.thisisget.com", "www.dev.thisisget.com" "www.thisisget.com", "www.thisisget.com", "http://www.thisisget.com", "https://www.thisisget.com", "http://thisisget.com", "https://thisisget.com", "http://localhost:3000", "http://127.0.0.1:3000", "http://localhost:3001", "http://127.0.0.1:3001"], headers=['Content-Type'], expose_headers=['Access-Control-Allow-Origin', 'Access-Control-Allow-Credentials'], supports_credentials=True)

try:
	os.makedirs(app.instance_path)
except OSError:
	pass



# Initialize MongoDB
class MongoSingleton:
	print('Initializing Mongo - Singleton...', file=sys.stderr)
	_instance = None
	def __new__(cls):
		if cls._instance is None:
			cls._instance = super().__new__(cls)
			cls._instance.client = pymongo.MongoClient(app.config['MONGO_CLI'], tls=True)
			print('Mongo initialized - Singleton')
		return cls._instance

global mongo	
mongo = MongoSingleton().client
app.db = mongo
global db
db = mongo[app.config['MONGO_DB']]

# Initialize the Redis connection
# q = Queue(connection=redis_conn)
# app.q = q



# Load user in current session

# login_manager = LoginManager()
# login_manager.login_view = 'GET_login.GET_login'
# login_manager.init_app(app)

# Load user in current session
# @login_manager.user_loader
# def load_user(investor_ID):
#   user = User(email=investor_ID, db=db)
#   if user:
#     return user
#   return None

""" 
Clear user session and redirect to homepage.
In all of our pages all we have to do is if the logout button is clicked we just route to this endpoint. i.e.

if form_data['logout'] == 'logout':
	return redirect(url_for('/logout'))

"""
# @app.route('/logout', methods=['GET', 'POST'])
# @login_required
# def logout():
# 	logout_user()
# 	session.clear()
# 	return redirect(url_for('GET_home'))



# ------------------------------- TEARDOWN APP CONTEXT ----------------------------------------->
# This is executed using the teardown_appcontext signal 

@app.teardown_appcontext
def teardown_db(exception):
	# close_mongo_db()
	mongo.close()




# --------------------------------- JWT --------------------------------------------------->
# --------------------------------- JWT --------------------------------------------------->
# --------------------------------- JWT --------------------------------------------------->




jwt = JWTManager(app)

# Register a callback function that takes whatever object is passed in as the
# identity when creating JWTs and converts it to a JSON serializable format.
@jwt.user_identity_loader
def user_identity_lookup(user):
	print(user.id)
	return user.id


# Register a callback function that loads a user from your database whenever
# a protected route is accessed. This should return any python object on a
# successful lookup, or None if the lookup failed for any reason (for example
# if the user has been deleted from the database).
@jwt.user_lookup_loader
def user_lookup_callback(_jwt_header, jwt_data):
	identity = jwt_data["sub"]
	return User(identity, db)

# Using an `after_request` callback, we refresh any token that is within 30
# minutes of expiring. Change the timedeltas to match the needs of your application.
@app.after_request
def refresh_expiring_jwts(response):
	try:
		exp_timestamp = get_jwt()["exp"]
		now = datetime.now(timezone.utc)
		target_timestamp = datetime.timestamp(now + timedelta(minutes=30))
		if target_timestamp > exp_timestamp:
			access_token = create_access_token(identity=get_jwt_identity())
			set_access_cookies(response, access_token)
		return response
	except (RuntimeError, KeyError):
		# Case where there is not a valid JWT. Just return the original response
		return response

""" 
Clear user session and redirect to homepage.
In all of our pages all we have to do is if the logout button is clicked we just route to this endpoint. i.e.
"""
@app.route('/api/logout/', methods=['GET', 'POST'])
@jwt_required()
def logout():
	response = jsonify({"msg": "logout successful"})
	unset_jwt_cookies(response)
	mongo.close()
	# session.clear()
	return response

# @app.route("/login_test", methods=["POST"])
# def login_test():

	
# 	email = request.json.get("email", None)
# 	password = request.json.get("password", None)
# 	print(email, password)
# 	# if email != "test" or password != "test":
# 	# 	return jsonify({"msg": "Bad email or password"}), 401

# 	print('CORRECT!!!')
# 	# You can use the additional_info argument to either add
# 	# custom info or override default info in the JWT.
# 	additional_info = {"aud": "some_audience", "foo": "bar"}
# 	access_token = create_access_token(email, additional_claims=additional_info)

# 	print('access_token: ', access_token)

# 	response = jsonify({"msg": "login successful"})
# 	set_access_cookies(response, access_token)
# 	return jsonify(access_token=access_token)


# @app.route("/logout_test", methods=["POST"])
# def logout_test():
# 	response = jsonify({"msg": "logout successful"})
# 	unset_jwt_cookies(response)
# 	return response


# In a protected view, get the claims you added to the jwt with the
# get_jwt() method
# @app.route("/protected", methods=["GET"])
# @jwt_required()
# def protected():
# 	claims = get_jwt()
# 	return jsonify(foo=claims["foo"])








	# --------------------------------- BLUEPRINTS ------------------------------------------------->



	# --------------------------------- Fund Forms --------------------------------------------------->

from GET_project.api.invest_flow.step_1 import GET_invest_flow_step_1_Blueprint
app.register_blueprint(GET_invest_flow_step_1_Blueprint)

# from GET_project.api.invest_flow.step_2 import GET_invest_flow_step_2_Blueprint
# app.register_blueprint(GET_invest_flow_step_2_Blueprint)

from GET_project.api.invest_flow.step_3 import GET_invest_flow_step_3_Blueprint
app.register_blueprint(GET_invest_flow_step_3_Blueprint)

from GET_project.api.invest_flow.step_4 import GET_invest_flow_step_4_Blueprint
app.register_blueprint(GET_invest_flow_step_4_Blueprint)

from GET_project.api.invest_flow.step_5 import GET_invest_flow_step_5_Blueprint
app.register_blueprint(GET_invest_flow_step_5_Blueprint)



from GET_project.api.invest_flow.step_2_linktoken import GET_invest_flow_step_2_linktoken_Blueprint
app.register_blueprint(GET_invest_flow_step_2_linktoken_Blueprint)

from GET_project.api.invest_flow.step_2_publictoken import GET_invest_flow_step_2_publictoken_Blueprint
app.register_blueprint(GET_invest_flow_step_2_publictoken_Blueprint)

from GET_project.api.invest_flow.step_5_publictoken import GET_invest_flow_step_5_publictoken_Blueprint
app.register_blueprint(GET_invest_flow_step_5_publictoken_Blueprint)


from GET_project.api.invest_flow.accred_and_investments import GET_check_accredidation_and_get_plaid_investments_Blueprint
app.register_blueprint(GET_check_accredidation_and_get_plaid_investments_Blueprint)


# --------------------------------- Get Plaid Accredidation --------------------------------------------------->

from GET_project.api.get_accred.get_accred_linktoken import GET_accred_linktoken_Blueprint
app.register_blueprint(GET_accred_linktoken_Blueprint)

from GET_project.api.get_accred.get_accred_publictoken import GET_accred_publictoken_Blueprint
app.register_blueprint(GET_accred_publictoken_Blueprint)



# --------------------------------- Dwolla Return Money --------------------------------------------------->

from GET_project.api.returns import GET_returns_Blueprint
app.register_blueprint(GET_returns_Blueprint)


# --------------------------------- Dwolla Reverify --------------------------------------------------->


from GET_project.api.dwolla_reverification.reverify_customer import GET_dwolla_reverify_customer_Blueprint
app.register_blueprint(GET_dwolla_reverify_customer_Blueprint)

from GET_project.api.dwolla_reverification.documents_needed import GET_dwolla_documents_needed_Blueprint
app.register_blueprint(GET_dwolla_documents_needed_Blueprint)

from GET_project.api.dwolla_reverification.kba import GET_dwolla_kba_Blueprint
app.register_blueprint(GET_dwolla_kba_Blueprint)



# --------------------------------- Login & Signup --------------------------------------------------->



  
from GET_project.api.login.login import GET_login_Blueprint
app.register_blueprint(GET_login_Blueprint)

from GET_project.api.login.forgot_password import GET_forgot_password_Blueprint
app.register_blueprint(GET_forgot_password_Blueprint)

from GET_project.api.login.two_factor import GET_two_factor_Blueprint
app.register_blueprint(GET_two_factor_Blueprint)

from GET_project.api.login.create_user import GET_create_user_Blueprint
app.register_blueprint(GET_create_user_Blueprint)

# from GET_project.api.signup.signup import GET_signup_Blueprint
# app.register_blueprint(GET_signup_Blueprint)





# --------------------------------- NEW Fund Setup --------------------------------------------------->



from GET_project.api.new_fund_setup.new_fund_step_1 import GET_new_fund_setup_step_1_Blueprint
app.register_blueprint(GET_new_fund_setup_step_1_Blueprint)

from GET_project.api.new_fund_setup.new_fund_step_2_linktoken import GET_new_fund_setup_step_2_linktoken_Blueprint
app.register_blueprint(GET_new_fund_setup_step_2_linktoken_Blueprint)

from GET_project.api.new_fund_setup.new_fund_step_2_publictoken import GET_new_fund_setup_step_2_publictoken_Blueprint
app.register_blueprint(GET_new_fund_setup_step_2_publictoken_Blueprint)

from GET_project.api.new_fund_setup.new_fund_step_3 import GET_new_fund_setup_step_3_Blueprint
app.register_blueprint(GET_new_fund_setup_step_3_Blueprint)


from GET_project.api.new_fund_setup.new_fund_docs_needed import GET_dwolla_new_fund_documents_needed_Blueprint
app.register_blueprint(GET_dwolla_new_fund_documents_needed_Blueprint)


# --------------------------------- Investor Dashboard --------------------------------------------------->

from GET_project.api.investor_dashboard.investor_home import GET_investor_home_Blueprint
app.register_blueprint(GET_investor_home_Blueprint)

from GET_project.api.investor_dashboard.transactions import GET_user_transactions_Blueprint
app.register_blueprint(GET_user_transactions_Blueprint)

from GET_project.api.investor_dashboard.notifications import GET_user_notifications_Blueprint
app.register_blueprint(GET_user_notifications_Blueprint)

from GET_project.api.investor_dashboard.agreements import GET_investor_agreements_Blueprint
app.register_blueprint(GET_investor_agreements_Blueprint)

from GET_project.api.investor_dashboard.confirm_link_expire import GET_invest_flow_confirm_link_expire_Blueprint
app.register_blueprint(GET_invest_flow_confirm_link_expire_Blueprint)

from GET_project.api.investor_dashboard.instant_invest.instant_invest_step_1 import GET_instant_invest_step_1_Blueprint
app.register_blueprint(GET_instant_invest_step_1_Blueprint)

from GET_project.api.investor_dashboard.instant_invest.instant_invest_step_2 import GET_instant_invest_step_2_Blueprint
app.register_blueprint(GET_instant_invest_step_2_Blueprint)

from GET_project.api.investor_dashboard.instant_invest.instant_invest_step_3 import GET_instant_invest_step_3_Blueprint
app.register_blueprint(GET_instant_invest_step_3_Blueprint)

# --------------------------------- NDA ------------------------------------------------------------->

from GET_project.api.nda.enterInfo import NDA_EnterInfo_Blueprint
app.register_blueprint(NDA_EnterInfo_Blueprint)

from GET_project.api.nda.enterPhoneMFA import NDA_EnterPhoneMFA_Blueprint
app.register_blueprint(NDA_EnterPhoneMFA_Blueprint)

# --------------------------------- Dwolla Webook --------------------------------------------------->

from GET_project.api.webhooks.dwolla_webhook_subscriptions import GET_dwolla_webhook_subscriptions_Blueprint
app.register_blueprint(GET_dwolla_webhook_subscriptions_Blueprint)

from GET_project.api.webhooks.dwolla_webhook import Dwolla_Webhook_Blueprint
app.register_blueprint(Dwolla_Webhook_Blueprint)

# from GET_project.api.webhooks.dwolla_webhook import Dwolla_Running_Jobs_Blueprint 
# app.register_blueprint(Dwolla_Running_Jobs_Blueprint)

# from GET_project.api.webhooks.dwolla_webhook import Dwolla_Expired_Jobs_Blueprint 
# app.register_blueprint(Dwolla_Expired_Jobs_Blueprint)




# --------------------------------- Dashboard Config ------------------------------------------------------------->

from GET_project.api.dashboard_config.upload_profile import GET_upload_profile_config_Blueprint
app.register_blueprint(GET_upload_profile_config_Blueprint)







# --------------------------------- Contact and Subscribe --------------------------------------------------->

from GET_project.api.contact_and_subscribe import GET_contact_and_subscribe_Blueprint
app.register_blueprint(GET_contact_and_subscribe_Blueprint)

from GET_project.api.WALLSTREET_conatcat_and_sub import WALLSTREET_conatcat_and_sub_Blueprint
app.register_blueprint(WALLSTREET_conatcat_and_sub_Blueprint)


from GET_project.api.reserve_seat import GET_reserve_seat_Blueprint
app.register_blueprint(GET_reserve_seat_Blueprint)


# --------------------------------- Manager Dashboard ------------------------------------------------>

from GET_project.api.manager_dashboard.manager_signup import Manager_Signup_Blueprint
app.register_blueprint(Manager_Signup_Blueprint)

from GET_project.api.manager_dashboard.manager_home import Manager_Home_Blueprint
app.register_blueprint(Manager_Home_Blueprint)

from GET_project.api.manager_dashboard.manager_transactions import GET_manager_transactions_Blueprint
app.register_blueprint(GET_manager_transactions_Blueprint)

from GET_project.api.manager_dashboard.manager_notifications import GET_manager_notifications_Blueprint
app.register_blueprint(GET_manager_notifications_Blueprint)

from GET_project.api.manager_dashboard.manager_agreements import GET_manager_agreements_Blueprint
app.register_blueprint(GET_manager_agreements_Blueprint)

from GET_project.api.manager_dashboard.manager_update_agreements import GET_manager_update_agreements_Blueprint
app.register_blueprint(GET_manager_update_agreements_Blueprint)

from GET_project.api.manager_dashboard.manager_upsell import Manager_Upsell_Blueprint
app.register_blueprint(Manager_Upsell_Blueprint)

from GET_project.api.manager_dashboard.manager_upsell_received import Manager_Upsell_Received_Blueprint
app.register_blueprint(Manager_Upsell_Received_Blueprint)





# Session(app)

# if __name__ == '__main__':

# 	app.run()

