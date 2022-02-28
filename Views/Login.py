from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.lang import Builder

from Controllers import client_controller

class LoginView(Screen):
    
	def __init__(self, **kwargs):
		super(LoginView, self).__init__(**kwargs)
		
		self.build()

	def build(self):
	       view = Builder.load_file("Views/kv/Login.kv")
	       self.add_widget(view)

	def login(self):
	       cpf = self.root.ids.cpf.text
	       password = self.root.ids.password.text
	       
	       result = client_controller.authentication(cpf, password)
	       
	       if not result[0]:
	       	self.root.ids.response.text = result[1]
	       else:
	       	self.manager.set_screen("Home")