from Controllers import connection_controller
from Controllers import session_controller
from Models.Client import ClientModel
from DAOs.Client import ClientDAO
from DAOs.Security import SecurityDAO
from Utils.DataConverter import DataConverter


def authentication(cpf, password):
	data = {
				"cpf": cpf,
				"password": password
	 }
	
	response = ClientDAO.authenticate(connection_controller.get_connection(), data)
	
	if response[0]:
		session_controller.create(data)
	
	return response[1]

def signup(cpf, name, birthdate, email, p_phone, s_phone, profile_photo, cep, city, district, street, num, password):
	phone_numbers = [p_phone, s_phone]
	birthdate = DataConverter.br_usa_date(birthdate)
	address = {
			         	"cep":  cep,
			         	"city": city,
			         	"district": district,
			         	"street": street,
			         	"num": num
				   }
	
	client = ClientModel(cpf, name, birthdate, email, phone_numbers, profile_photo, address, password)
	response = ClientDAO.insert(connection_controller.get_connection(), client)
	
	if response[0]:
		SecurityDAO.insert(cpf, connection_controller.get_connection())
		
	return response[1]

def get_by_cpf(cpf):
	response = ClientDAO.get_by_cpf(cpf, connection_controller.get_connection())
	
	name = response["_name"]
	birthdate = response["birthdate"]
	email = response["email"]
	phone_numbers = [response["p_phone"], response["s_phone"]]
	profile_photo = response["photo"]
	address = {
			         	"cep":  response["cep"],
			         	"city": response["city"],
			         	"district": response["district"],
			         	"street": response["street"],
			         	"num": response["num"]
	}
	password = response["password"]
	
	client = ClientModel(cpf, name, birthdate, email, phone_numbers, profile_photo, address, password)
	
	return client