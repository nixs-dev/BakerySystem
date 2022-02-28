screen_manager = None

def main():
	global screen_manager
	screen_manager.current = "Main"

def signup():
	SignUpView()
	
def login():
	global screen_manager
	screen_manager.current = "Login"
	
def home():
	HomeView()