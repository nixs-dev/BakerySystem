from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.lang import Builder

from Controllers import client_controller

class LoginView(Screen):
	view = None
	
	def __init__(self, **kwargs):
		super().__init__(**kwargs)
		self.build()

	def build(self):
		template = Builder.load_file("Views/kv/Login.kv")
		template.ids.ok_button.bind(on_release=self.login)
		template.ids.signup_link.bind(on_ref_press=self.go_signup_view)
	       
		self.view = template
		self.add_widget(self.view)
	
	def go_signup_view(self, elem, link):
		self.manager.set_screen("SignUp")

	def login(self, elem):
		cpf = self.view.ids.cpf.text
		password = self.view.ids.password.text
	       
		result = client_controller.authentication(cpf, password)
	       
		if  result is not None:
			self.view.ids.response.text = result
		else:
			self.manager.set_screen("Home")