import mysql.connector
from mysql.connector.errors import *

class Connection:
	
	def __init__(self):
		self.conn = None
	
	def connect(self):
		try:
			db = mysql.connector.connect(
				host = "127.0.0.1",
				port = 3306,
				user = "dev",
				password = "sandbox",
				database="bakery",
				charset='utf8',
				collation="utf8_general_ci",
				use_unicode=True
			)
			
			self.conn = db
			return [1, db]
		except InterfaceError:
			return [0, "Error on trying to connect to the server"]
	
	def get_connection(self):
		return self.conn
		