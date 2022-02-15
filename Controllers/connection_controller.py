from Models.Connection import Connection

database = None

def connect_to_database():
	global database
	
	database = Connection()
	response = database.connect()
	
	if response[0] == 1:
		return [True, "Connected"]
	else:
		return [False, response[1]]