from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.app import App
from kivy.lang import Builder
from threading import Thread

from Controllers import product_controller


class HomeView(Screen):
	view = None

	def __init__(self, **kwargs):
		super().__init__(**kwargs)
		self.build()
		
	def build(self):
		self.view = Builder.load_file("Views/kv/Home.kv")
		self.add_widget(self.view)
		
	def setup_product_frame(self, product_frame, product):
		product_frame.id = "PRODUCT_" + str(product.get_id())
		product_frame.ids.product_name.text = product.get_name()
		product_frame.ids.product_price.text = str(product.get_price()) + " R$"
		
		return product_frame
	
	def on_enter(self):
		Thread(target=self.add_products).start()
	
	def add_products(self):
	      products = product_controller.get_all_products()
	      for product_info in products:
	      	product_frame = Builder.load_file("Views/kv/ProductFrame.kv")
	      	product_frame = self.setup_product_frame(product_frame, product_info)
	      	self.view.ids.products_grid.add_widget(product_frame)
	      	
	def on_press_buy(self, product_id):
		pass