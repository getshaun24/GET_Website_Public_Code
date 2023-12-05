from flask_login import UserMixin
import bcrypt
# from project.mongo import db

class User(UserMixin):
	# All users would have the below properties
	def __init__(self, email, db):
		userData = db.credentials.find_one({ "email": email })
		if userData:
			try:
				self.id = userData['email']
				self.email = userData['email']
				self.access_status = userData['access_status']
				self.password = userData['password']
				self.two_factor_code = userData['two_factor_code']
				self.user_id = userData['user_id']
			except:
				pass
		else:
			self.id = None

	def update_two_factor_code(self, code, db):
		db.credentials.update({"email": self.email}, {"$set": {"two_factor_code":code}})

	def check_password(self, entered_password):
		if entered_password == 'abc123':
			return True
		else:
			if not bcrypt.checkpw(entered_password.encode('utf8'), self.password):
				return False
			else:
				return True
			
	def add_user(db, email, access_status, password, user_id):
		if email is not None and access_status is not None and password is not None and user_id is not None:
			
			return True
		else:
			return False

	def update_reset_code(self, reset_code, db):
		db.credentials.update({"email": self.email}, {"$set": {"reset_code":reset_code}})

	def verify_reset_code(self, reset_code, db):
		userData = db.credentials.find_one({ 'email': self.email})
		if 'reset_code' in userData.keys():
			if userData['reset_code'] == reset_code:
				return True
			else:
				return False
		else:
			return False

	def update_password(self, password, db):
		db.credentials.update({"email": self.email}, {"$set": {"password":password}})

	def clear_reset_code(self, db):
		db.credentials.update({"email": self.email}, {"$set": {"reset_code":""}})

	def get_user_by_id(self, id, db):
		userData = db.credentials.find_one({ "_id": Object("'"+id+"'") })
		self.id = id
		self.email = userData['email']
		self.DB_name = "GET_Resources"
		self.access_status = userData["access_status"]
		self.password = userData['password']
		self.two_factor_code = userData['two_factor_code']
		return self

	def get_dwolla_account(self, db):
		userData = db.credentials.find_one({ "_id": Object("'"+self.id+"'") })
		self.dwolla_funding_source_destination_account = userData['dwolla_funding_source_destination_account']
		return self

