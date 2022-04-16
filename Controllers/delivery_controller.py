import datetime

from Models.Delivery import DeliveryModel
from DAOs.Delivery import DeliveryDAO
from Controllers import connection_controller


def make(cpf_client, id_product, amount, final_price, address):
	start_datetime = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
	delivery = DeliveryModel(None, cpf_client, id_product, amount, final_price, address, start_datetime, None, False)
	
	DeliveryDAO.insert(connection_controller.get_connection(), delivery)
	
	return True