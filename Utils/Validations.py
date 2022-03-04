import requests
import json

class Validations:
	__cep_api = "https://viacep.com.br/ws/{}/json/"
	
	@staticmethod
	def get_numeric(string):
		numeric = string
		
		for i in range(0, len(string)):
			if not string[i].isnumeric():
				numeric = numeric.replace(string[i], '')
		
		return numeric
	
	@staticmethod
	def validate_cep(cep):
		if len(numeric_cep) == 8:
			return True
		else:
			return False
			
	@staticmethod
	def validate_cpf(cpf):
		def check_verifier(cpf, index):
			result = 0
			
			for i in range(index, 1, -1):
				result += int(cpf[index-i]) * i
				
			rest = result % 11
			
			if rest in (0, 1):
				result = 0
			elif rest >= 2 and rest <= 10:
				result = 11 - rest
				
			return result == int(cpf[index-1])
		
		if len(cpf) != 11:
			return False
		else:
			if check_verifier(cpf, 10) and check_verifier(cpf, 11):
				return True
			else:
				return False
		
	@staticmethod
	def get_cep_info(cep):
		formatted_cep = Validations.validate_cep(cep)
		
		if formatted_cep is None:
			return None
		
		url = Validations.__cep_api.format(cep)
		response = requests.get(url).text
		
		return json.loads(response) if "erro" not in json.loads(response).keys() else None