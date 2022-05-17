from Utils.Validations import Validations

class InputFormatter:
	
	@staticmethod
	def cpf_field(elem, changes):
		elem.text = Validations.format_cpf(changes)