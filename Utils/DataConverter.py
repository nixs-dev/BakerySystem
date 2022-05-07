import io
import datetime
from kivy.uix.image import CoreImage


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
	
	@staticmethod
	def binary_to_texture(binary):
		data = io.BytesIO(binary)
		img = CoreImage(data, ext="png").texture
		
		return img