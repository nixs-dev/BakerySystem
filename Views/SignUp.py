import io
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.lang import Builder
from kivy.uix.textinput import TextInput
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.image import CoreImage

from Views.Popup import AppPopup
from Views.FileChooser import AppFileChooser
from Utils.Validations import Validations
from Utils.DataConverter import DataConverter
from Controllers import client_controller


class SignUpView(Screen):
	view = None
	profile_photo = None
	optional_fields = ["s_phone"]
	validated_fields = {
										"cpf": {"status": False, "hint": "CPF"},
										"cep": {"status": False, "hint": "CEP"},
										"birthdate": {"status": False, "hint": "Data de nascimento"},
										"email": {"status": False, "hint": "Email"},
										"p_phone": {"status": False, "hint": "Telefone 1"},
										"s_phone": {"status": True, "hint": "Telefone 2"},
	}
	
	
	def __init__(self, **kwargs):
		super().__init__(**kwargs)
		self.build()

	def build(self):
		template = Builder.load_file("Views/kv/SignUp.kv")
		'''template.ids.back_button.bind(on_release=lambda x: self.manager.set_screen("Login"))
		template.ids.profile_photo.bind(on_release=AppFileChooser(selection_callback=self.set_profile_photo).open)
		template.ids.cpf.bind(text=self.validate_cpf)
		template.ids.cep.bind(text=self.complete_address)
		template.ids.birthdate.bind(text=self.validate_birthdate)
		template.ids.email.bind(text=self.validate_email)
		template.ids.p_phone.bind(text=self.validate_phone)
		template.ids.s_phone.bind(text=self.validate_phone)
		template.ids.ok_button.bind(on_release=self.signup)'''
		
		self.view = template
		self.add_widget(self.view)
	
	def check_fields(self, layout):
		for elem in layout:
			if isinstance(elem, TextInput):
				field_content = elem.text.replace(" ", "")
				
				if field_content == "" and elem.name not in self.optional_fields:
					return False
			elif isinstance(elem, BoxLayout):
				result = self.check_fields(elem.children)
				
				if not result:
					return False
				
		return True
	
	def check_validations(self):
		for key in self.validated_fields:
			if not self.validated_fields[key]["status"]:
				return self.validated_fields[key]["hint"]
		
	def signup(self, elem):
		fields_state = self.check_fields(self.view.ids.form.children)
		validations_state = self.check_validations()
		
		if validations_state is not None:
			AppPopup(title="Erro", content=f"Campo {validations_state} inválido").open()
		elif not fields_state:
			AppPopup(title="Erro", content="Campos vazios").open()
		else:
			response = client_controller.signup(self.view.ids.cpf.text, 
													   self.view.ids.name.text,
													   self.view.ids.birthdate.text,
													   self.view.ids.email.text, 
													   Validations.get_numeric(self.view.ids.p_phone.text),
													   Validations.get_numeric(self.view.ids.s_phone.text),
													   self.profile_photo,
													   self.view.ids.cep.text,
													   self.view.ids.city.text,
													   self.view.ids.district.text,
													   self.view.ids.street.text, 
													   self.view.ids.num.text,
													   self.view.ids.password.text)
			if response is None:
				self.manager.set_screen("Login")
			else:
				AppPopup(title="Erro", content=response).open()
			
	
	# Data integrity section
	
	def set_profile_photo(self, file, file_content):
		img = DataConverter.binary_to_texture(file_content)
		
		self.view.ids.profile_photo.texture = img
		self.profile_photo = file_content
		
	def validate_cpf(self, elem, changes):
		status_cpf = Validations.validate_cpf(changes)
		
		self.validated_fields["cpf"]["status"] = status_cpf
		self.view.ids.cpf.foreground_color = (255, 0, 0) if not status_cpf else (0, 0, 0)
	
	def validate_birthdate(self, elem, changes):
		formated_date = Validations.format_date(changes)
		status_date = Validations.validate_date(formated_date)
		self.view.ids.birthdate.text= formated_date
		
		self.validated_fields["birthdate"]["status"] = status_date
		self.view.ids.birthdate.foreground_color = (255, 0, 0) if not status_date else (0, 0, 0)
	
	def validate_phone(self, elem, changes):
		formated_phone = Validations.format_phone(changes)
		status_phone = Validations.validate_phone(formated_phone)
		
		if formated_phone.replace(" ", "") == "()":
			formated_phone = ""
		if formated_phone.replace(" ", "") == "" and elem.name in self.optional_fields:
			status_phone = True
			
		elem.text = formated_phone
		elem.cursor = (0, 0)
		self.validated_fields[elem.name]["status"] = status_phone
		elem.foreground_color = (255, 0, 0) if not status_phone else (0, 0, 0)
		
	def validate_email(self, elem, changes):
		status_email = Validations.validate_email(changes)
					
		self.validated_fields["email"]["status"] = status_email
		self.view.ids.email.foreground_color = (255, 0, 0) if not status_email else (0, 0, 0)
		
	def complete_address(self, elem, changes):
		cep_info = Validations.get_cep_info(changes)
		
		if cep_info is not None:
			self.validated_fields["cep"]["status"] = True
			self.view.ids.cep.foreground_color = (0, 0, 0)
			
			self.view.ids.city.text = cep_info["localidade"]
			self.view.ids.district.text = cep_info["bairro"]
			self.view.ids.street.text = cep_info["logradouro"]
		else:
			self.validated_fields["cep"]["status"] = False
			self.view.ids.cep.foreground_color = (255, 0, 0)
	       