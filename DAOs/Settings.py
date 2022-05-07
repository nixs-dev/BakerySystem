class SettingsDAO:
	available_settings = {
		"notifications": ["Checkbox_setting", "Notificações", None]
	}
	
	@staticmethod
	def get_available_settings():
		return SettingsDAO.available_settings