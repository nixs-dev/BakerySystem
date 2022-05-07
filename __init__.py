import kivy
from kivymd.app import MDApp
from kivy.uix.screenmanager import ScreenManager, NoTransition
from kivy.core.window import Window

from Views.Main import MainView
from Views.Login import LoginView
from Views.SignUp import SignUpView
from Views.Home import HomeView
from Views.Settings import SettingsView


class Manager(ScreenManager):
	def __init__(self):
		super().__init__()
		self.setup()

	def setup(self):
		self.add_widget(MainView(name="Main"))
		self.add_widget(LoginView(name="Login"))
		self.add_widget(SignUpView(name="SignUp"))
		self.add_widget(HomeView(name="Home"))
		self.add_widget(SettingsView(name="Settings"))
	
	def set_screen(self, screen_name):
		self.current = screen_name
		
class Application(MDApp):
	screen_manager = None
	on_back_screen = {
		"SignUp": "Login",
		"Settings": "Home"
	}
	
	def build(self):
		self.config_app()
		
		self.screen_manager = Manager()
		return self.screen_manager
	
	def config_app(self):
		Window.softinput_mode = "pan"
		Window.bind(on_keyboard=self.keyboard_handler)
		
	def keyboard_handler(self, window, key, *args):
		if key == 27:
			current_screen = self.screen_manager.current
        	
			if current_screen in self.on_back_screen.keys():
				new_screen = self.on_back_screen[current_screen]
				self.screen_manager.set_screen(new_screen)
				
				return True
			else:
				self.stop()

Application().run()