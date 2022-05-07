
		
		
		
		
			
			MDBoxLayout:
				id: specific_info
				orientation: "horizontal"
				
				MDTextField:
					id: street
					hint_text: "Rua"
					multiline: False
					
				MDTextField:
					id: num
					hint_text: "Número"
					multiline: False
		
		MDTextField:
			id: password
			name: "password"
			hint_text: "Senha"
			multiline: False
			password: True
	
		MDLabel:
			id: response
			text: ""
			font_name: "Resources/font/main.ttf"
			size_hint_x: .3                
			text_size: self.size
			halign: 'left'
			valign: 'middle'
			color: get_color_from_hex('#FF0000')
			
		MDRaisedButton:
			id: ok_button
			text: "Ok"
			font_name: "Resources/font/main.ttf"
