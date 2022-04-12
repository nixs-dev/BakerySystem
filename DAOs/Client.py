
class ClientDAO:
	
	@staticmethod
	def get_all(conn):
		cursor = conn.cursor(dictionary=True)
		cursor.execute("SELECT * FROM clients")
		
		return cursor.fetchall()
		
	@staticmethod
	def get_by_cpf(cpf, conn):
		cursor = conn.cursor(dictionary=True)
		
		cursor.execute("SELECT * FROM clients WHERE cpf = %s", (cpf,))
		result = cursor.fetchall()
		
		return None if result == [] else result[0]
	
	@staticmethod
	def authenticate(conn, data):
		cursor = conn.cursor(dictionary=True)
		
		query = (
				    	"SELECT * FROM clients"
				    	" WHERE cpf = %s"
				    )
		args = (data["cpf"],)
		
		cursor.execute(query, args)
		result = cursor.fetchall()
		
		if len(result) == 0:
			return [False, "Nenhum usuário cadastrado com esse CPF"]
		else:
			if result[0]["password"] == data["password"]:
				return [True, None]
			else:
				return [False, "Senha incorreta"]
	
	@staticmethod
	def insert(conn, client):
		cursor = conn.cursor()
		
		query = (
				     	"INSERT INTO clients (cpf, _name, birthdate, email, p_phone, s_phone, cep, city, district, street, num, password)"
				     	"VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"
				    )
		args = (
				  	client.get_cpf(),
				        client.get_name(), 
				        client.get_birthdate(),
				        client.get_email(),
				        client.get_phone_numbers()[0],
				        client.get_phone_numbers()[1],
				        client.get_address()["cep"],
				        client.get_address()["city"],
				        client.get_address()["district"],
				        client.get_address()["street"],
				        client.get_address()["num"],
				        client.get_password()
				  )
		
		cursor.execute(query, args)
		conn.commit()
		
		return [True, None]