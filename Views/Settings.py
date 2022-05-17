from kivy.uix.screenmanager import ScreenManager, Screen
from kivymd.app import MDApp
from kivy.lang import Builder
from kivymd.uix.selectioncontrol import MDCheckbox

from Views.Popup import AppPopup
from Utils.DataConverter import DataConverter
from Controllers import session_controller
from Controllers import settings_controller


class SettingsView(Screen):
	view = None
	user_settings_widgets = {}

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
		settings = settings_controller.user_settings()
		
		for s in settings:
			widget = self.user_settings_widgets[s]
			
			if isinstance(widget, MDCheckbox):
				widget.active = settings[s]
				widget.bind(active=lambda *args: settings_controller.checkbox_callback(*args, s))
				
	def add_settings(self, template):
		settings = settings_controller.available_settings()
		
		for i in settings:
			setting_type = settings[i][0]
			setting_text = settings[i][1]

			setting_template = Builder.load_file(f"Views/kv/{setting_type}.kv")
			setting_template.name = i
			setting_template.ids.setting_text.text = setting_text
			
			self.user_settings_widgets[i] = setting_template.ids.core
			template.ids.settings_list.add_widget(setting_template)
		
		# Default options 
		
		about_option = Builder.load_file("Views/kv/Button_setting.kv")
		about_option.ids.core.text = "Sobre"
		terms_option = Builder.load_file("Views/kv/Button_setting.kv")
		terms_option.ids.core.text = "Termos de uso"
		
		template.ids.settings_list.add_widget(about_option)
		template.ids.settings_list.add_widget(terms_option)