import os
from Views.Main import MainView
from Views.Login import LoginView
from Views.SignUp import SignUpView
from Views.Home import HomeView

def startApplication():
	os.system("clear")
	MainView()

def signup():
	os.system("clear")
	SignUpView()
	
def login():
	os.system("clear")
	LoginView()
	
def home():
	os.system("clear")
	HomeView()