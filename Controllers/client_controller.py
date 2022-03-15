from Controllers import connection_controller
from Controllers import session_controller
from Models.Client import ClientModel
from DAOs.Client import ClientDAO
from DAOs.Session import SessionDAO
from DAOs.Security import SecurityDAO

def authentication(cpf, password):
	data = {
				"cpf": cpf,
				"password": password
	 }
	
	response = ClientDAO.authenticate(connection_controller.get_connection(), data)
	
	if response[0]:
		session_controller.create(response[1])
	
	return response

def session_authentication():
	session = SessionDAO.get_session(SessionDAO.load_db())
	
	if session is None:
		return None
		
	
	cpf = session[0]
	hashed_password = session[1]
	
	correct_password = SecurityDAO.get_hashed_password(cpf, connection_controller.get_connection())
	
	if correct_password is None:
		return False
	elif correct_password != hashed_password:
		return False
	else:
		return True

def signup(cpf, name, birthdate, email, p_phone, s_phone, cep, city, district, street, num, password):
	phone_numbers = [p_phone, s_phone]
	address = {
			         	"cep":  cep,
			         	"city": city,
			         	"district": district,
			         	"street": street,
			         	"num": num
				   }
	
	client = ClientModel(cpf, name, birthdate, email, phone_numbers, address, password)
	response = ClientDAO.insert(connection_controller.get_connection(), client)
	
	return response