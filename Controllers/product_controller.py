from DAOs.Product import ProductDAO
from Models.Product import ProductModel
from Controllers import connection_controller

def insert_product(name, price, amount):
	product = ProductModel(None, name, price, amount)
	sucess = ProductDAO.insert(connection_controller.get_connection(), product)
	
	if sucess:
		return True
	else:
		return False
	
def get_all_products():
	data_list = ProductDAO.get_all(connection_controller.get_connection())
	products = []
		
	for p in data_list:
		product = ProductModel(p["id"], p["_name"], p["price"], p["amount"])
		products.append(product)
		
	return products