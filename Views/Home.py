from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.uix.tabbedpanel import TabbedPanel
from kivy.app import App
from kivy.lang import Builder
from threading import Thread

from Views.Popup import AppPopup
from Controllers import product_controller
from Controllers import delivery_controller
from Controllers import session_controller


class HomeView(Screen):
	view = None

	def __init__(self, **kwargs):
		super().__init__(**kwargs)
		self.build()
		
	def build(self):
		template = Builder.load_file("Views/kv/Home.kv")
		template.ids.logout_button.bind(on_release=self.on_press_logout)
		
		self.view = template
		self.add_widget(self.view)
	
	def on_pre_enter(self):
		self.view.ids.tabs.switch_to(self.view.ids.tabs.tab_list[1])
		self.view.ids.products_grid.clear_widgets()
		
	def on_enter(self):
		self.setup_tabs()
	
	
	# DATA SETUP
	
	def setup_tabs(self):
		self.add_products()
		self.set_user_info()
	
	def setup_product_frame(self, product_frame, product):
		product_frame.name = "PRODUCT_" + str(product.get_id())
		product_frame.ids.product_name.text = product.get_name()
		product_frame.ids.product_price.text = str(product.get_price()) + " R$"
		product_frame.ids.buy_button.name = product_frame.name
		product_frame.ids.buy_button.bind(on_release=self.on_press_buy)
		
		return product_frame
	
	def set_user_info(self):
		user_info = session_controller.get()
		
		self.view.ids.profile_user_name.text = user_info.get_name()
		self.view.ids.profile_user_cpf.text = str(user_info.get_cpf())
		
	def add_products(self):
		products = product_controller.get_all_products()
		
		for product_info in products:
			product_frame = Builder.load_file("Views/kv/ProductFrame.kv")
			product_frame = self.setup_product_frame(product_frame, product_info)
			self.view.ids.products_grid.add_widget(product_frame)
	
	
	# ON PRESS
	
	def on_press_buy(self, elem):
		client_cpf = session_controller.get().get_cpf()
		client_address = session_controller.get().get_address()
		product_id = int(elem.name.replace("PRODUCT_", ""))
		price = product_controller.get_product_by_id(product_id).get_price()
		amount = 1
		final_price = price * amount
		
		delivery_controller.make(client_cpf, product_id, amount, final_price, client_address)
		AppPopup(title="X", content=str(elem.name)).open()
	
	def on_press_logout(self, elem):
		if session_controller.logout():
			self.manager.set_screen("Login")
		else:
			AppPopup(title="X", content="X").open()