import os
from Views.Main import MainView
from Views.Home import HomeView

def startApplication():
	os.system("clear")
	MainView()

def home():
	os.system("clear")
	HomeView()