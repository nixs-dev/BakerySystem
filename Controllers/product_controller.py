from DAOs.Product import ProductDAO
from Models.Product import ProductModel
from Controllers import connection_controller

def insert_product(args):
	'''
		Arguments:
			
			0 -> Name
			1 -> Price
			2 -> Amount
			
	'''
	
	product = ProductModel(None, args[0], args[1], args[2])
	sucess = ProductDAO.insert(connection_controller.database, product)
	
	if sucess:
		return True
	else:
		return False
	
def get_all_products():
	data_list = ProductDAO.get_all(connection_controller.database)
	products = []
		
	for p in data_list:
		product = ProductModel(p[0], p[1], p[2], p[3])
		products.append(product)
		
	return products