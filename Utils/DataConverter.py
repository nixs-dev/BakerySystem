import datetime

class DataConverter:
	
	@staticmethod
	def br_usa_date(br_date):
		br_date = br_date.split("/")
		br_date.reverse()
		
		new_date = "-".join(br_date)
		
		return new_date
		
	@staticmethod
	def usa_br_date(usa_date):
		usa_date = usa_date.split("-")
		usa_date.reverse()
		
		new_date = "/".join(usa_date)
		
		return new_date