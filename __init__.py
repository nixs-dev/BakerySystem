import kivy
from kivy.app import App
from kivy.uix.screenmanager import ScreenManager, NoTransition

from Views.Main import MainView
from Views.Login import LoginView
from Views.Home import HomeView


class Manager(ScreenManager):
	def __init__(self):
		super().__init__()
		self.setup()
		
	def setup(self):
		self.add_widget(MainView(name="Main"))
		self.add_widget(LoginView(name="Login"))
		self.add_widget(HomeView(name="Home"))
	
	def set_screen(self, screen_name):
		self.current = screen_name
		
class Application(App):
	def build(self):
		return Manager()

Application().run()