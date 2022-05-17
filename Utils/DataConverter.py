import io
from datetime import datetime
from kivy.uix.image import CoreImage


class DataConverter:
	
	@staticmethod
	def br_usa_datetime(br_date):
		new_date = usa_date.strftime("%Y/%m/%d %H:%M:%S")
		
		return new_date
		
	@staticmethod
	def usa_br_datetime(usa_date):
		new_date = usa_date.strftime("%d/%m/%Y %H:%M:%S")
		
		return new_date
	
	@staticmethod
	def br_usa_strdate(br_date_str):
		parts = br_date_str.split("/")
		parts.reverse()
		
		return "-".join(parts)
		
	@staticmethod
	def binary_to_texture(binary):
		data = io.BytesIO(binary)
		img = CoreImage(data, ext="png").texture
		
		return img
	
	@staticmethod
	def get_datetime_delay(start, end=None):
		end = datetime.now() if end is None else end
		delay_secs = (end-start).total_seconds()
		days = 0
		hrs = 0
		mins = 0
		secs = 0
		
		if delay_secs >= 60:
			mins = int(delay_secs // 60)
			delay_secs -= 60 * mins
		
		secs = delay_secs
		
		if mins >= 60:
			hrs = int(mins // 60)
			mins -= 60 * hrs
		
		if hrs >= 24:
			days = int(hrs // 24)
			hrs -= 24 * days
		
		return f"{days} Dias, {hrs} horas, {mins} minutos e {round(secs)} segundos"
		