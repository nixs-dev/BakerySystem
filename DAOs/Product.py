
class ProductDAO:
	
	@staticmethod
	def get_all(conn):
		cursor = conn.cursor(dictionary=True)
		cursor.execute("SELECT * FROM products")
		
		return cursor.fetchall()
	
	@staticmethod
	def insert(conn, product):
		cursor = conn.cursor()
		
		query = (
			          	"INSERT INTO products (_name, price, amount)"
			          	"VALUES (%s, %s, %s)"
			          )
		args = (
				  	product.get_name(),
				        product.get_price(), 
				        product.get_amount()
				  )
		
		cursor.execute(query, args)
		conn.commit()
		
		return True