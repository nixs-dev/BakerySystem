class DeliveryModel:
	
	def __init__(self):
		self.id  = id
		self.cpf_client = cpf_client
		self.id_product = id_product
		self.amount = amount
		self.final_price = final_price
		self.address = address
		self.start_datetime = start_datetime
		self.end_datetime = end_datetime
		self.done = done
	    
	def get_id(self):
		return self.id
	
	def get_cpf_client(self):
		return self.cpf_client
	
	def get_id_product(self):
		return self.id_product
	
	def get_amount(self):
		return self.amount
	
	def get_final_price(self):
		return self.final_price
	
	def get_address(self):
		return self.get_address
	
	def get_start_datetime(self):
		return self.start_datetime
	
	def get_end_datetime(self):
		return self.end_datetime
		
	def get_done(self):
		return self.done