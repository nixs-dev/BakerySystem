import os.path
from kivymd.uix.filemanager import MDFileManager
from kivy.lang.builder import Builder


class AppFileChooser(MDFileManager):
	main_path = "/sdcard/"
	allow_ext = [".jpg", ".jpeg", ".png"]
	
	def __init__(self, selection_callback=None):
		super().__init__()
		
		self.selection_callback = selection_callback
		self.ext = self.allow_ext
	
	def select_path(self, path):
		if os.path.isdir(path):
			return
			
		file_content = open(path, "rb").read()
		
		self.close()
		self.selection_callback(path, file_content) if self.selection is not None else None
	
	def exit_manager(self, output):
		self.close()
	
	def open(self, elem):
		self.show(path=self.main_path)