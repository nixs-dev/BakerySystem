class ProductModel:
	
	def __init__(self, id, name, price, amount):
		self.id = None if id is None else int(id)
		self.name = name
		self.price = float(price)
		self.amount = int(amount)
	
	def get_id(self):
		return self.id
		
	def get_name(self):
		return self.name
	
	def get_price(self):
		return "{0:.2f}".format(self.price)
	
	def get_amount(self):
		return self.amount