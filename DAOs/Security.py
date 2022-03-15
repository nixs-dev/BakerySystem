import hashlib
import os


class SecurityDAO():
	
	@staticmethod
	def get_salt(cpf_client, conn):
		cursor = conn.cursor()
		query = "SELECT salt FROM security WHERE cpf_client = %s"
		args = (cpf_client,)
		
		cursor.execute(query, args)
		result = cursor.fetchall()
		
		if len(result) == 0:
			return None
		else:
			return result[0][0]
	
	def get_hashed_password(cpf_client, conn):
		cursor = conn.cursor()
		password_query = "SELECT password FROM clients WHERE cpf = %s"
		password_args = (cpf_client,)
		
		cursor.execute(password_query, password_args)
		result  = cursor.fetchall()
		password = ""
		
		if result == []:
			return None
		else:
			password = result[0][0]
		
		
		salt = SecurityDAO.get_salt(cpf_client, conn)
		digested = hashlib.pbkdf2_hmac('sha256', password.encode("utf-8"), salt, 10000)
		
		return digested.hex()
	
	def insert(cpf_client, conn):
		cursor = conn.cursor()
		query = "INSERT INTO security (cpf_client, salt) VALUES (%s, %s)"
		args = (cpf_client, os.urandom(32))
		
		cursor.execute(query, args)
		conn.commit()
		
		return True