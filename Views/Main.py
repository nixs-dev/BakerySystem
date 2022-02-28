from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.lang import Builder

import time
from Controllers import connection_controller
from threading import Thread


class MainView(Screen):
	state = [None, None]
	
	def __init__(self, **kwargs):
		super(MainView, self).__init__(**kwargs)
		
		self.build()

	def build(self):
		view = Builder.load_file("Views/kv/Main.kv")
		self.add_widget(view)
	       
	def on_enter(self):
		Thread(target=self.connection_state).start()
		
	def connection_state(self):
		time.sleep(5)
		
		self.state = connection_controller.connect_to_database()
		
		if self.state[0] is not None:
			if self.state[0]:
				self.manager.set_screen("Login")
			else: 
				pass