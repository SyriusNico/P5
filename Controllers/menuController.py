# coding : utf-8
import sys 
sys.path.append('C:\\Users\\Utilisateur\\Documents\\ExerciceOC\\Pur_Beurre')
import	Views.menuView as m

class MenuController():
	"""docstring for MenuController"""
	def __init__(self): 
		self.choice = None
		self.response = None


	def menuScreen(self):
		menu = m.MenuView()
		mainMenu = menu.screen()
		return mainMenu

	def substituteScreen(self):
		menu = m.MenuView()
		subsMenu = menu.substituteScreen()
		return subsMenu
		
	def menuBye(self):
		menu = m.MenuView()
		bye = menu.bye()
		return bye

	def makeChoice(self):
		self.choice = int(input("\nChoisissez une option : \n\n\n"))
		return self.choice

	def register(self):
		self.response = int(input("\nVoulez enregistrer ce produit dans votre liste ?\n1.oui\n2.non\n\n\n"))
		return self.response



