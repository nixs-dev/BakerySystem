class NotificationsDAO:
	
	@staticmethod
	def get_by_user(conn, user):
		cursor = conn.cursor(dictionary=True)
		query = "SELECT * FROM notifications WHERE cpf_client = %s ORDER BY timestamp"
		args = (user, )
		
		cursor.execute(query, args)
		
		return cursor.fetchall()