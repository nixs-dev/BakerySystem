from kivy.lang import Builder
from kivy.uix.popup import Popup
from kivy.uix.label import Label


class AppPopup(Popup):
	
	def __init__(self, **kwargs):
		super().__init__(title=kwargs.get("title"), content=None, auto_dismiss=False)
		self.size_hint = (0.5, 0.5)
		
		self.build_content(kwargs.get("content"))
	
	def build_content(self, content_text):
		template = Builder.load_file("Views/kv/Popup.kv")
		template.ids.content.text = content_text
		template.ids.ok_button.bind(on_release=self.dismiss)
		
		self.content = template