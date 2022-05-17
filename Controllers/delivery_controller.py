import datetime

from Models.Delivery import DeliveryModel
from DAOs.Delivery import DeliveryDAO
from DAOs.Product import ProductDAO
from Controllers import connection_controller


def make(cpf_client, id_product, product_name, amount, final_price, address):
	start_datetime = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
	delivery = DeliveryModel(None, cpf_client, id_product, product_name, amount, final_price, address, start_datetime, None, False)
	
	if ProductDAO.buy(connection_controller.get_connection(), id_product, amount):
		DeliveryDAO.insert(connection_controller.get_connection(), delivery)
	else:
		return f"No momento só temos {ProductDAO.get_amount(connection_controller.get_connection(), id_product)[0]['amount']} unidades"
	
	return None

def get_made_by_user(cpf_client):
	result = DeliveryDAO.get_by_user(connection_controller.get_connection(), cpf_client)
	models_list = []
	
	for i in result:
		address = {"city": i["city"], "district": i["district"], "street": i["street"], "num": i["num"]}
		model = DeliveryModel(i["id"], i["cpf_client"], i["id_product"], i["product_name"], i["amount"], i["final_price"], address, i["start_datetime"], i["end_datetime"], i["done"])
		models_list.append(model)
		
	return models_list