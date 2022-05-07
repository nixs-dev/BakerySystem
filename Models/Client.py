class ClientModel:
	
	def __init__(self, cpf, name, birthdate, email, phone_numbers, profile_photo, address, password):
		self.cpf = cpf
		self.name = name
		self.birthdate = birthdate
		self.email = email
		self.phone_numbers = phone_numbers
		self.profile_photo = profile_photo
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
		phone_numbers = self.phone_numbers
		
		for i in range(0, 2):
			phone_numbers[i] = None if self.phone_numbers[i] == "" else self.phone_numbers[i]
			
		return phone_numbers
	
	def get_profile_photo(self):
		return self.profile_photo
		
	def get_address(self):
		return self.address
	
	def get_password(self):
		return self.password