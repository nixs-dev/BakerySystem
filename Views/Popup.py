from kivy.lang import Builder
from kivy.uix.popup import Popup
from kivy.uix.label import Label
from kivymd.uix.button.button import MDIconButton
from kivymd.uix.floatlayout import MDFloatLayout
from kivy.graphics.instructions import Canvas
from kivy.graphics import Rectangle

class AppPopup(Popup):
	ok_button_callback = None
	
	def __init__(self, **kwargs):
		super().__init__(title=kwargs.get("title"), content=None, auto_dismiss=False)
		self.size_hint = (None, 0.5)
		self.separator_height = 0
		self.title_align = "center"
		self.title_font = "Resources/font/main.ttf"
		possible_width = ((len(kwargs.get("content")) * 20) / 2) + 20
		
		if possible_width >= 200:
			self.width = possible_width
		else:
			self.width = 200
		
		self.ok_button_callback = kwargs.get("ok_button_callback")
		
		self.build_content(kwargs.get("content"))
		
	def build_content(self, content_text):
		template = Builder.load_file("Views/kv/Popup.kv")
		template.ids.content.text = content_text
		template.ids.ok_button.bind(on_release=self.ok_button_press)
		
		self.content = template
		
		self.background = "Resources/img/popup_background.png"
		
	def ok_button_press(self, elem):
		self.dismiss()
		self.ok_button_callback() if self.ok_button_callback is not None else None
		