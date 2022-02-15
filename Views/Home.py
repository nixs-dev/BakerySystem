from Controllers import connection_controller

class HomeView:
	
	def __init__(self):
		self.start()
	
	def start(self):
		print("WELCOME")
		print(connection_controller.database)