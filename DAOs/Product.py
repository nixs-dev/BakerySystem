
class ProductDAO:
	
	@staticmethod
	def get_one(conn, id):
		cursor = conn.cursor(dictionary=True)
		cursor.execute("SELECT * FROM products WHERE id = %s", (id,))
		
		return cursor.fetchall()
	
	@staticmethod
	def get_amount(conn, id):
		cursor = conn.cursor(dictionary=True)
		cursor.execute("SELECT amount FROM products WHERE id = %s", (id,))
		
		return cursor.fetchall()
		
	@staticmethod
	def get_all(conn):
		cursor = conn.cursor(dictionary=True)
		cursor.execute("SELECT * FROM products")
		
		return cursor.fetchall()
	
	@staticmethod
	def insert(conn, product):
		cursor = conn.cursor()
		
		query = (
			          	"INSERT INTO products (_name, price, amount, photo)"
			          	"VALUES (%s, %s, %s, %s)"
			          )
		args = (
				  		product.get_name(),
				      	product.get_price(),
				      	product.get_amount(),
				      	product.get_photo()
				  )
		
		cursor.execute(query, args)
		conn.commit()
		
		return True
	
	@staticmethod
	def buy(conn, id, amount):
		cursor = conn.cursor()
		
		query = (
			          	"UPDATE products SET amount = amount - %s WHERE `id` = %s"
			          )
		args = (
				  		amount,
				  		id,
				  )
		
		try:
			cursor.execute(query, args)
			conn.commit()
		except:
			return False
		
		return True