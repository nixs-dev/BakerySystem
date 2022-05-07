from Models.Delivery import DeliveryModel


class DeliveryDAO:
	
	@staticmethod
	def insert(conn, delivery):
		cursor = conn.cursor()
		query = (
						"INSERT INTO deliveries"
						"(cpf_client, id_product, amount, final_price, city, district, street, num, start_datetime, end_datetime, done)"
						"VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"
		)
		args = (
						delivery.get_cpf_client(),
						delivery.get_id_product(),
						delivery.get_amount(),
						delivery.get_final_price(),
						delivery.get_address()["city"],
						delivery.get_address()["district"],
						delivery.get_address()["street"],
						delivery.get_address()["num"],
						delivery.get_start_datetime(),
						delivery.get_end_datetime(),
						delivery.get_done(),
		)
		
		cursor.execute(query, args)
		conn.commit()
		
		return [True, None]
		
	@staticmethod
	def get_all(conn):
		cursor = conn.cursor(dictionary=True)
		query = "SELECT * FROM deliveries"
		
		cursor.execute(query)
		
		return cursor.fetchall()
	
	@staticmethod
	def get_by_user(conn, cpf_client):
		cursor = conn.cursor(dictionary=True)
		query = "SELECT * FROM deliveries WHERE cpf_client = %s"
		
		cursor.execute(query, (cpf_client,))
		
		return cursor.fetchall()