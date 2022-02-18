from Controllers import product_controller
from Controllers import commands_controller

class HomeView:
	products_list = []
	
	def __init__(self):
		self.start()
	
	def start(self):
		print("WELCOME\n\n")
		self.products_list = product_controller.get_all_products()
		
		self.show_products()
		
		while True:
			command = input("Operation: ")
			response = commands_controller.execute(command)
			
			print(response)
	
	def show_products(self):
		if len(self.products_list) == 0:
			print("Any product available!")
			return
		
		for prod in self.products_list:
			print((
				f"ID: {prod.get_id()}\n"
				f"Name: {prod.get_name()}\n"
				f"Price: {prod.get_price()}\n"
				"\n"
			))