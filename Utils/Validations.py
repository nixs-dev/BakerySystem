import requests
import json

class Validations:
	__cep_api = "https://viacep.com.br/ws/{}/json/"
	
	@staticmethod
	def validate_cep(cep):
		numeric_cep = cep
		
		for i in range(0, len(cep)):
			if not cep[i].isnumeric():
				numeric_cep = numeric_cep.replace(cep[i], '')
		
		if len(numeric_cep) == 8:
			return numeric_cep
		else:
			return None
			
	@staticmethod
	def get_cep_info(cep):
		formatted_cep = Validations.validate_cep(cep)
		
		if formatted_cep is None:
			return None
		
		url = Validations.__cep_api.format(cep)
		response = requests.get(url).text
		
		return json.loads(response) if "erro" not in json.loads(response).keys() else None