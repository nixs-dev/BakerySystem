class ProductModel:
	
	def __init__(self, id, name, price, amount, photo):
		self.id = None if id is None else int(id)
		self.name = name
		self.price = float(price)
		self.amount = int(amount)
		self.photo = photo
	
	def get_id(self):
		return self.id
		
	def get_name(self):
		return self.name
	
	def get_price(self):
		return float(self.price)
	
	def get_amount(self):
		return self.amount
	
	def get_photo(self):
		return self.photo