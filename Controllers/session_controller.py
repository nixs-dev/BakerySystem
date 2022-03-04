from Models.Session import SessionModel


current = None

def logout():
	global current
	
	current = None

def create(client):
	global current
	
	current = SessionModel(client)

def get_session_data():
	global current
	
	if current is not None:
		return current.get_data()
	else:
		return None