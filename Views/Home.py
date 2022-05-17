from kivy.uix.screenmanager import ScreenManager, Screen
from kivymd.uix.menu import MDDropdownMenu
from kivymd.uix.bottomsheet import MDCustomBottomSheet
from kivy.app import App
from kivy.clock import Clock
from kivy.lang import Builder
from threading import Thread

from Views.Popup import AppPopup
from Views.FileChooser import AppFileChooser
from Utils.DataConverter import DataConverter
from Utils.Validations import Validations
from Controllers import client_controller
from Controllers import product_controller
from Controllers import delivery_controller
from Controllers import session_controller
from Controllers import notifications_controller


class HomeView(Screen):
	view = None
	products = []
	user_changes = {}
	
	def __init__(self, **kwargs):
		super().__init__(**kwargs)
		
		self.build()
		
	def build(self):
		template = Builder.load_file("Views/kv/Home.kv")
		template.ids.settings_button.bind(on_release=lambda x: self.manager.set_screen("Settings"))
		template.ids.search_bar.bind(text=self.search_product)
		template.ids.profile_user_password.bind(text=self.field_changed)
		template.ids.save_profile_button.bind(on_release=self.update_profile)
		template.ids.logout_button.bind(on_release=self.on_press_logout)
		
		self.view = template
		self.add_widget(self.view)
	
	def on_pre_enter(self):
		tabs_list = list(self.view.ids.tabs.get_tab_list())
		
		self.view.ids.tabs.switch_tab(tabs_list[0])
		self.view.ids.products_grid.clear_widgets()
		self.view.ids.profile_deliveries_list.clear_widgets()
		
	def on_enter(self):
		Clock.schedule_once(lambda x: self.setup_tabs())
		Clock.schedule_once(lambda x: self.add_notifications())
	
	
	# DATA SETUP
	
	def setup_tabs(self):
		self.add_products()
		self.set_user_info()
	
	def setup_product_frame(self, product_frame, product):
		product_frame.name = "PRODUCT_" + str(product.get_id())
		
		if product.get_photo() is not None:
			product_frame.ids.product_photo.texture = DataConverter.binary_to_texture(product.get_photo())
			
		product_frame.ids.product_name.text = product.get_name()
		product_frame.ids.product_price.text = format(product.get_price(), ".2f") + " R$"
		product_frame.ids.buy_button.name = product_frame.name
		product_frame.ids.buy_button.bind(on_release=self.show_product_info)
		
		return product_frame
	
	def set_user_info(self):
		user_info = session_controller.get()
		self.user_changes = {}
		
		profile_photo = user_info.get_profile_photo()
		
		if profile_photo is not None:
			self.view.ids.profile_photo.texture = DataConverter.binary_to_texture(profile_photo)
		else:
			self.view.ids.profile_photo.texture = None
			self.view.ids.profile_photo.source = "Resources/img/default_user_icon.png"
			self.view.ids.profile_photo.reload()
		
		self.view.ids.profile_photo.bind(on_release=AppFileChooser(selection_callback=self.change_profile_photo).open)
			
		self.view.ids.profile_user_name.text = user_info.get_name()
		self.view.ids.profile_user_cpf.text = Validations.format_cpf(user_info.get_cpf())
		self.view.ids.profile_user_email.text = user_info.get_email()
		self.view.ids.profile_user_p_phone.text = Validations.format_phone(str(user_info.get_phone_numbers()[0]))
		self.view.ids.profile_user_s_phone.text = Validations.format_phone(str(user_info.get_phone_numbers()[1])) if user_info.get_phone_numbers()[1] is not None else ""
		self.view.ids.profile_user_password.text = user_info.get_password()
		
		self.set_active_deliveries()
	
	def set_active_deliveries(self):
		deliveries = delivery_controller.get_made_by_user(session_controller.get().get_cpf())
		
		for d in deliveries:
			template = Builder.load_file("Views/kv/Delivery_listelem.kv")
			template.ids.amount_and_product.text = f"{d.get_amount()} unidades de {d.get_product_name()}"
			template.ids.delivery_time.text = DataConverter.get_datetime_delay(d.get_start_datetime(), d.get_end_datetime())
			template.ids.delivery_status.source = "Resources/img/done_icon.png" if d.get_done() else "Resources/img/not_done_icon.png"
			
			self.view.ids.profile_deliveries_list.add_widget(template)
		
	def add_products(self):
		self.products = []
		products = product_controller.get_all_products()
		
		for product_info in products:
			product_frame = Builder.load_file("Views/kv/ProductFrame.kv")
			product_frame = self.setup_product_frame(product_frame, product_info)
			self.view.ids.products_grid.add_widget(product_frame)
			self.products.append(product_frame)
	
	def add_notifications(self):
		notifications = [
            {
                "text": n.get_text(),
                "secondary_text": DataConverter.usa_br_datetime(n.get_timestamp()),
                "viewclass": "TwoLineListItem"
            } for n in notifications_controller.user_notifications()
        ]
        
		if len(notifications) == 0:
			notifications.append(
        		{
	                "text": "Vazio",
	                "viewclass": "OneLineListItem"
            	}
        	)
        	
		self.notifications_menu = MDDropdownMenu(
			caller=self.view.ids.notifications_button,
			items=notifications,
			width_mult=4,
			radius=[24, 0, 24, 0]
		)
		
		self.view.ids.notifications_button.bind(on_release=lambda x: self.notifications_menu.open())
		
	# ON PRESS
	
	def show_product_info(self, elem):
		bottom_sheet = Builder.load_file("Views/kv/BottomSheet.kv")
		
		product_id = int(elem.name.replace("PRODUCT_", ""))
		product_info = product_controller.get_product_by_id(product_id)
		
		if product_info.get_photo() is not None:
			bottom_sheet.ids.product_info_photo.texture = DataConverter.binary_to_texture(product_info.get_photo())
			
		bottom_sheet.ids.product_info_name.text += product_info.get_name()
		bottom_sheet.ids.product_info_price.text += format(product_info.get_price(), ".2f") + " R$"
		bottom_sheet.ids.product_info_available_amount.text += str(product_info.get_amount())
		bottom_sheet.ids.make_delivery_button.bind(on_release=lambda x: self.on_press_buy(bottom_sheet, {
			"product_id": product_id,
			"product_name": product_info.get_name(),
			"price": product_info.get_price(),
			"amount": int(bottom_sheet.screen.ids.product_info_amount.text)
		}))
		
		bottom_sheet = MDCustomBottomSheet(screen=bottom_sheet, animation=True, duration_opening=0.5)
		bottom_sheet.open()
	
	def on_press_buy(self, bottom_sheet, data):
		client_cpf = session_controller.get().get_cpf()
		client_address = session_controller.get().get_address()
		product_id = data["product_id"]
		product_name = data["product_name"]
		price = data["price"]
		amount = data["amount"]
		final_price = price * amount
		
		result = delivery_controller.make(client_cpf, product_id, product_name, amount, final_price, client_address)
		
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
		self.user_changes["photo"] = file_content
	
	def update_profile(self, elem):
		client_controller.updates(self.user_changes)
		session_controller.update()
		
	def field_changed(self, elem, value):
		self.user_changes[elem.name] = value

	
	# SEARCH BAR
	
	def search_product(self, elem, changes):
		value = changes.lower()
		results = []
		
		if value == "":
			results = self.products
		else:
			for p in self.products:
				if value in p.ids.product_name.text.lower():
					results.append(p)
		
		self.show_results(results)
		
	def show_results(self, results):
		self.view.ids.products_grid.clear_widgets()
		
		for r in results:
			self.view.ids.products_grid.add_widget(r)
		