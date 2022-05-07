from kivy.uix.screenmanager import ScreenManager, Screen
from kivymd.app import MDApp
from kivy.lang import Builder

from Views.Popup import AppPopup
from Utils.DataConverter import DataConverter
from Controllers import session_controller
from DAOs.Settings import SettingsDAO


class SettingsView(Screen):
	view = None

	def __init__(self, **kwargs):
		super().__init__(**kwargs)
		self.build()
		
	def build(self):
		template = Builder.load_file("Views/kv/Settings.kv")
		self.add_settings(template)
		template.ids.back_button.bind(on_release=lambda x: self.manager.set_screen("Home"))
		
		self.view = template
		self.add_widget(self.view)
	
	def on_pre_enter(self):
		pass
		
	def on_enter(self):
		pass
	
	def add_settings(self, template):
		settings = SettingsDAO.get_available_settings()
		
		for i in settings:
			setting_type = settings[i][0]
			setting_text = settings[i][1]
			setting_callback = settings[i][2]
			
			setting_template = Builder.load_file(f"Views/kv/{setting_type}.kv")
			setting_template.ids.setting_text.text = setting_text
			
			template.ids.settings_list.add_widget(setting_template)
		
		# Default options 
		
		about_option = Builder.load_file("Views/kv/Button_setting.kv")
		about_option.ids.button.text = "Sobre"
		terms_option = Builder.load_file("Views/kv/Button_setting.kv")
		terms_option.ids.button.text = "Termos de uso"
		
		template.ids.settings_list.add_widget(about_option)
		template.ids.settings_list.add_widget(terms_option)