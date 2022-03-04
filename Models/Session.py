from datetime import datetime


class SessionModel:

	def __init__(self, data):
		self.data = data
		self.start = datetime.now().strftime("%d/%m/%Y %H:%M:%S")
	
	def get_data(self):
		return self.data
	
	def get_start_date(self):
		return self.start.split(' ')[0]
		
	def get_start_time(self):
		return self.start.split(' ')[1]