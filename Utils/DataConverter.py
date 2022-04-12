class DataConverter:
	
	@staticmethod
	def br_usa_date(br_date):
		parts = br_date.split("/")
		parts.reverse()
		
		return "-".join(parts)