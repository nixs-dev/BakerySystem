
class ProductDAO:
	
	@staticmethod
	def get_all(conn):
		cursor = conn.get_connection().cursor()
		cursor.execute("SELECT * FROM products")
		
		return cursor.fetchall()
	
	@staticmethod
	def insert(conn, product):
		conn = conn.get_connection()
		cursor = conn.cursor()
		query = f"INSERT INTO products (_name, price, amount) VALUES (%s, %s, %s)"
		args = (product.get_name(), product.get_price(), product.get_amount())
		
		cursor.execute(query, args)
		conn.commit()
		
		return True