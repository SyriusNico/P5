# coding : utf-8
import Views.menuView as m


class MenuController():

	def __init__(self):
		self.choice = None
		self.response = None
		self.details = None

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

	def detail(self):
		"""
		method used to register
		the user's request
		"""
		self.details = int(input("\nVoulez vous plus de "
			"renseignement pour un produit ?\n1.oui\n2.non\n\n\n"))
		return self.details

	def register(self):
		"""
		method used to register an product
		"""
		self.response = int(input(
			"\nVoulez enregistrer ce produit dans"
			" votre liste ?\n1.oui\n2.non\n\n\n")
		)
		return self.response
