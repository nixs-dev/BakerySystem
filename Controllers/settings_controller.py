from DAOs.Settings import SettingsDAO
from Controllers import connection_controller
from Controllers import session_controller


def user_settings():
	settings = SettingsDAO.get_user_settings(connection_controller.get_connection(), session_controller.get().get_cpf())
	
	return settings

def available_settings():
	settings = SettingsDAO.get_available_settings()
	
	return settings

def checkbox_callback(elem, value, settings_name):
	SettingsDAO.update(connection_controller.get_connection(), session_controller.get().get_cpf(), settings_name, value)