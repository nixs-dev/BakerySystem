from DAOs.Notifications import NotificationsDAO
from Models.Notification import NotificationModel
from Controllers import connection_controller
from Controllers import session_controller

def user_notifications():
	notifications = NotificationsDAO.get_by_user(connection_controller.get_connection(), session_controller.get().get_cpf())
	models = []
	
	for n in notifications:
		m = NotificationModel(n["id"], n["cpf_client"], n["text"], n["received"], n["timestamp"])
		models.append(m)
		
	return models