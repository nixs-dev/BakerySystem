import sqlite3


class SessionDAO:
	db_path = "LocalData/SESSION.db"
	db_source = (
							"CREATE TABLE IF NOT EXISTS session ("
							"	cpf BIGINT(11) NOT NULL,"
							"	password VARCHAR(500) NOT NULL"
							");"
	)
	
	@staticmethod
	def load_db():
		conn = sqlite3.connect(SessionDAO.db_path)
		SessionDAO.setup_db(conn)
		
		return conn
	
	@staticmethod
	def setup_db(conn):
		cursor = conn.cursor()
		
		cursor.execute(SessionDAO.db_source)
		conn.commit()
	
	@staticmethod
	def insert(conn, data):
		SessionDAO.clear_session(conn)
		
		cursor = conn.cursor()
		query = "INSERT INTO session VALUES (?, ?)"
		args = (data["cpf"], data["password"])
		
		cursor.execute(query, args)
		conn.commit()
	
	@staticmethod
	def clear_session(conn):
		cursor = conn.cursor()
		query = "DELETE FROM session"
		
		cursor.execute(query)
		conn.commit()
	
	@staticmethod
	def get_session(conn):
		cursor = conn.cursor()
		query = "SELECT * FROM session"
		
		cursor.execute(query)
		result = cursor.fetchall()
		
		return None if result == [] else result[0]