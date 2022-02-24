from Controllers import client_controller
from Controllers import views_controller
from Utils.Validations import Validations

class SignUpView:
	
	def __init__(self):
		self.start()
	
	def start(self):
		self.show_form()
	
	def show_form(self):
		cpf = input("CPF: ")
		name = input("Nome: ")
		birthdate = input("Data de Nascimento (dd/mm/AAAA): ")
		email = input("Email: ")
		p_phone = input("Telefone (primário): ")
		s_phone = input("Telefone (secundário): ")
		
		while True:
			cep = input("CEP: ")
			a_info = Validations.get_cep_info(cep)
			
			if a_info is not None:
				city = a_info["localidade"]
				district = a_info["bairro"]
				street = a_info["logradouro"]
				num = int(input("Número: "))
				
				break
			else:
				print("CEP inválido")
		
		password = input("Senha: ")
		
		
		response = client_controller.signup(cpf, name, birthdate, email, p_phone, s_phone, cep, city, district, street, num, password)
		
		if response[0]:
			pass
		else:
			print(response[1])