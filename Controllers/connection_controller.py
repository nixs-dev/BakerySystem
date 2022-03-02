from Models.Connection import Connection

database = None

def connect_to_database():
	global database
	
	database = Connection()
	response = database.connect()
	
	if response[0] == 1:
		return [True, "Conectado"]
	else:
		return [False, response[1]]

def get_connection():
	global database
	
	response = database.get_connection()
	
	return response