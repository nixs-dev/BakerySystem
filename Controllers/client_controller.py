from Controllers import connection_controller
from Controllers import session_controller
from Models.Client import ClientModel
from DAOs.Client import ClientDAO

def authentication(cpf, password):
	data = {
				"cpf": cpf,
				"password": password
			  }
	
	response = ClientDAO.authenticate(connection_controller.get_connection(), data)
	
	if response[0]:
		session_controller.create(response[1])
	
	return response

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