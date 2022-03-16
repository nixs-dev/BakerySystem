from DAOs.Session import SessionDAO
from DAOs.Security import SecurityDAO
from Controllers import connection_controller, client_controller


SESSION = None

def session_authentication():
	global SESSION
	
	session = SessionDAO.get_session(SessionDAO.load_db())
	
	if session is None:
		return False
		
	
	cpf = session[0]
	hashed_password = session[1]
	
	correct_password = SecurityDAO.get_hashed_password(cpf, connection_controller.get_connection())
	
	if correct_password is None:
		return False
	elif correct_password != hashed_password:
		return False
	else:
		SESSION = client_controller.get_by_cpf(cpf)
		return True
