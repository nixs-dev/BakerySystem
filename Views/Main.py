import time
import os
from Utils.Colors import Style
from Controllers import connection_controller
from Controllers import views_controller
from threading import Thread

class MainView:
	state = [None, ""]
	anim = ["\\", "|", "/", "-"]

	def __init__(self):
		self.start()
	
	def connection_state(self):
		self.state = connection_controller.connect_to_database()
		
	def start(self):
		i = 0
		
		Thread(target=self.connection_state).start()
		
		while True:
			if self.state[0] is not None:
				os.system("clear")
				print(f"{Style.GREEN if self.state[0] else Style.RED}{self.state[1]}{Style.RESET}")
				
				if self.state[0]:
					time.sleep(0.3)
					views_controller.login()
				
				break
			
			print(f"{self.anim[i]} Conectando...", end="\r", flush=True)
			
			if i == len(self.anim)-1:
				i = 0
			else:
				i += 1
			
			time.sleep(0.3)