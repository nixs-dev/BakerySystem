import requests
import json
import datetime

class Validations:
	__cep_api = "https://viacep.com.br/ws/{}/json/"
	__allowed_emails = ("gmail", "yahoo", "outlook")
	
	@staticmethod
	def format_phone(phone):
		phone = str(Validations.get_numeric(phone))
		length = len(phone)
		ddd = ""
		rest = ""
		
		if length >= 2:
			ddd = phone[slice(2)]
		else:
			 return f"({phone})"
		
		if length >= 3:
			rest = phone[slice(2, length+1)]
			
		return f"({ddd}) {rest}"
	
	@staticmethod
	def format_date(date):
		date = Validations.get_numeric(date)
		edited_date = ""
		
		separators = 2
		counter = 0
		for i in date:
			edited_date += str(i)
			counter += 1
			
			if counter == 2 and separators > 0:
				edited_date += "/"
				counter = 0
				separators -= 1
		
		return edited_date
		
	@staticmethod
	def get_numeric(string):
		string = str(string)
		numeric = string
		
		for i in range(0, len(string)):
			if not string[i].isnumeric():
				numeric = numeric.replace(string[i], '')
		
		return numeric
	
	@staticmethod
	def validate_cep(cep):
		cep = Validations.get_numeric(cep)
		
		if len(cep) == 8:
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
	def validate_phone(phone):
		phone = Validations.get_numeric(phone)
		body = phone[slice(2, len(phone)+1)] if len(phone) >= 3 else ""
		
		return True if (len(body) == 8 or len(body) == 9) and len(body) + 2 == len(phone) else False
	
	@staticmethod
	def validate_email(email):
		parts = []
		
		if "@" not in email:
			return False
		else:
			parts = email.split("@")
			
			if "." not in parts[1]:
				return False
			
			subparts = parts[1].split(".")
			
			if len(subparts) > 2:
				return False
				
			if subparts[0] not in Validations.__allowed_emails:
				return False
			
			if subparts[1] != "com":
				return False
				
		return True
	
	@staticmethod
	def validate_date(date):
		date = Validations.get_numeric(date)
		splitted_date = []
		
		if len(date) != 8:
			return False
		
		part_temp = ""
		for i, j in enumerate(date):
			part_temp += str(j)
			
			if len(splitted_date) == 2:
				splitted_date.append(date[slice(i, len(date)+1)])
				break
			elif len(part_temp) == 2:
				splitted_date.append(part_temp)
				part_temp = ""
				
		return True if 31 >= int(splitted_date[0]) > 0 and 12 >= int(splitted_date[1]) > 0 and datetime.datetime.today().year > int(splitted_date[2]) > 0 else False
			
	@staticmethod
	def get_cep_info(cep):
		if not Validations.validate_cep(cep):
			return None
		
		url = Validations.__cep_api.format(cep)
		response = requests.get(url).text
		
		return json.loads(response) if "erro" not in json.loads(response).keys() else None