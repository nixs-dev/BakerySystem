class NotificationModel:
	
	def __init__(self, id, cpf_client, text, received, timestamp):
		self.id  = int(id) if id is not None else None
		self.cpf_client = cpf_client
		self.text = text
		self.received = received
		self.timestamp = timestamp
	
	def get_id(self):
		return self.id
	
	def get_cpf_client(self):
		return self.cpf_client
	
	def get_text(self):
		return self.text
	
	def get_received(self):
		return self.received
	
	def get_timestamp(self):
		return self.timestamp