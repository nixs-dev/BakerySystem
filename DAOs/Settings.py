class SettingsDAO:
	available_settings = {
		"notifications": ["Checkbox_setting", "Notificações"]
	}
	
	@staticmethod
	def get_available_settings():
		return SettingsDAO.available_settings
	
	@staticmethod
	def insert(conn, user):
		cursor = conn.cursor()
		query = "INSERT INTO settings (cpf_client) VALUES (%s)"
		
		cursor.execute(query, (user,))
		conn.commit()
		
		return True
	
	@staticmethod
	def update(conn, user, setting, value):
		cursor = conn.cursor()
		query = f"UPDATE settings SET {setting} = %s WHERE cpf_client = %s"
		
		cursor.execute(query, (value, user,))
		conn.commit()
		
		return True
		
	@staticmethod
	def get_user_settings(conn, user):
		cursor = conn.cursor(dictionary=True)
		query = f"SELECT {','.join(SettingsDAO.available_settings.keys())} FROM settings WHERE cpf_client = %s"
		cursor.execute(query, (user,))
		
		return cursor.fetchall()[0]