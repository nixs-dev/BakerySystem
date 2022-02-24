from Controllers import client_controller
from Controllers import views_controller
import os

class LoginView:
	
	def __init__(self):
		self.start()
	
	def start(self):
		state = ""
		
		while True:
			os.system("clear")
			
			print(state)
			cpf = input("CPF: ")
			password = input("Senha: ")
			
			result = client_controller.authentication(cpf, password)
			
			if not result[0]:
				state = result[1]
			else:
				views_controller.home()
				break