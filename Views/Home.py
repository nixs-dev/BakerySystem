from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.uix.tabbedpanel import TabbedPanel
from kivymd.uix.bottomsheet import MDCustomBottomSheet
from kivy.app import App
from kivy.lang import Builder
from threading import Thread

from Views.Popup import AppPopup
from Views.FileChooser import AppFileChooser
from Utils.DataConverter import DataConverter
from Utils.Validations import Validations
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
		template.ids.settings_button.bind(on_release=lambda x: self.manager.set_screen("Settings"))
		template.ids.profile_photo.bind(on_release=AppFileChooser(selection_callback=self.change_profile_photo).open)
		template.ids.logout_button.bind(on_release=self.on_press_logout)
		
		self.view = template
		
		self.add_widget(self.view)
	
	def on_pre_enter(self):
		tabs_list = list(self.view.ids.tabs.get_tab_list())
		
		self.view.ids.tabs.switch_tab(tabs_list[0])
		self.view.ids.products_grid.clear_widgets()
		
	def on_enter(self):
		self.setup_tabs()
	
	
	# DATA SETUP
	
	def setup_tabs(self):
		self.add_products()
		self.set_user_info()
	
	def setup_product_frame(self, product_frame, product):
		product_frame.name = "PRODUCT_" + str(product.get_id())
		
		if product.get_photo is not None:
			product_frame.ids.product_photo.texture = DataConverter.binary_to_texture(product.get_photo())
			
		product_frame.ids.product_name.text = product.get_name()
		product_frame.ids.product_price.text = str(product.get_price()) + " R$"
		product_frame.ids.buy_button.name = product_frame.name
		product_frame.ids.buy_button.bind(on_release=self.show_product_info)
		
		return product_frame
	
	def set_user_info(self):
		user_info = session_controller.get()
		
		profile_photo = user_info.get_profile_photo()
		
		if profile_photo is not None:
			self.view.ids.profile_photo.texture = DataConverter.binary_to_texture(profile_photo)
		else:
			self.view.ids.profile_photo.source = "Resources/img/default_user_icon.png"
			
		self.view.ids.profile_user_name.text = user_info.get_name()
		self.view.ids.profile_user_cpf.text = Validations.format_cpf(user_info.get_cpf())
		self.view.ids.profile_user_email.text = user_info.get_email()
		self.view.ids.profile_user_p_phone.text = Validations.format_phone(str(user_info.get_phone_numbers()[0]))
		self.view.ids.profile_user_s_phone.text = Validations.format_phone(str(user_info.get_phone_numbers()[1])) if user_info.get_phone_numbers()[1] is not None else ""
		self.view.ids.profile_user_password.text = user_info.get_password()
		
		self.set_active_deliveries()
	
	def set_active_deliveries(self):
		deliveries = delivery_controller.get_made_by_user(session_controller.get().get_cpf())
		
		i = 0
		
		for d in deliveries:
			template = Builder.load_file("Views/kv/Delivery_listelem.kv")
			template.ids.amount_and_product.text = f"{d.get_amount()} unidades de X"
			template.ids.delivery_time.text = f"{i}"
			template.ids.delivery_status.source = "Resources/img/done_icon.png" if d.get_done() else "Resources/img/not_done_icon.png"
			
			self.view.ids.profile_deliveries_list.add_widget(template)
			
			i += 1
		
	def add_products(self):
		products = product_controller.get_all_products()
		
		for product_info in products:
			product_frame = Builder.load_file("Views/kv/ProductFrame.kv")
			product_frame = self.setup_product_frame(product_frame, product_info)
			self.view.ids.products_grid.add_widget(product_frame)
	
	
	# ON PRESS
	
	def show_product_info(self, elem):
		bottom_sheet = Builder.load_file("Views/kv/BottomSheet.kv")
		
		product_id = int(elem.name.replace("PRODUCT_", ""))
		product_info = product_controller.get_product_by_id(product_id)
		
		bottom_sheet.ids.product_info_name.text += product_info.get_name()
		bottom_sheet.ids.product_info_price.text += str(product_info.get_price())
		bottom_sheet.ids.product_info_available_amount.text += str(product_info.get_amount())
		bottom_sheet.ids.make_delivery_button.bind(on_release=lambda x: self.on_press_buy(bottom_sheet, {
			"product": product_id,
			"price": product_info.get_price(),
			"amount": int(bottom_sheet.screen.ids.product_info_amount.text)
		}))
		
		bottom_sheet = MDCustomBottomSheet(screen=bottom_sheet, animation=True, duration_opening=0.5)
		bottom_sheet.open()
	
	def on_press_buy(self, bottom_sheet, data):
		client_cpf = session_controller.get().get_cpf()
		client_address = session_controller.get().get_address()
		product_id = data["product"]
		price = data["price"]
		amount = data["amount"]
		final_price = price * amount
		
		result = delivery_controller.make(client_cpf, product_id, amount, final_price, client_address)
		
		if result is None:
			AppPopup(title="X", content="Pronto").open()
			bottom_sheet.dismiss()
		else:
			AppPopup(title="X", content=result).open()
	
	def on_press_logout(self, elem):
		if session_controller.logout():
			self.manager.set_screen("Login")
		else:
			AppPopup(title="X", content="X").open()
		
	# PROFILE UPDATE
	
	def change_profile_photo(self, file, file_content):
		img = DataConverter.binary_to_texture(file_content)
		
		self.view.ids.profile_photo.texture = img
		self.profile_photo = file_content
		