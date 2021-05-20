# coding : utf-8
import Views.menuView as m
# import sys
# # sys.path.append('C:\\Users\\Utilisateur\\Documents\\ExerciceOC\\Pur_Beurre')
# sys.path.append('Pur_Beurre')

class MenuController():

	def __init__(self):
		self.choice = None
		self.response = None

	def menuScreen(self):
		"""
		method used to display the main menu
		"""
		menu = m.MenuView()
		mainMenu = menu.screen()
		return mainMenu

	def substituteScreen(self):
		"""
		method used to display the substitute menu
		"""
		menu = m.MenuView()
		subsMenu = menu.substituteScreen()
		return subsMenu

	def menuBye(self):
		"""
		method used to signal that you are 
		quitting the application
		"""
		menu = m.MenuView()
		bye = menu.bye()
		return bye

	def makeChoice(self):
		"""
		method used to register
		the user's request
		"""
		self.choice = int(input("\nChoisissez une option : \n\n\n"))
		return self.choice

	def register(self):
		"""
		method used to register an product
		"""
		self.response = int(input(
			"\nVoulez enregistrer ce produit dans"
			" votre liste ?\n1.oui\n2.non\n\n\n")
		)
		return self.response
