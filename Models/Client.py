class ClientModel:
	
	def __init__(self, cpf, name, birthdate, email, phone_numbers, address, password):
		self.cpf = cpf
		self.name = name
		self.birthdate = birthdate
		self.email = email
		self.phone_numbers = phone_numbers
		self.address = address
		self.password = password
	
	def get_cpf(self):
		return self.cpf
	
	def get_name(self):
		return self.name
	
	def get_birthdate(self):
		return self.birthdate
	
	def get_email(self):
		return self.email
	
	def get_phone_numbers(self):
		return self.phone_numbers
	
	def get_address(self):
		return self.address
	
	def get_password(self):
		return self.password