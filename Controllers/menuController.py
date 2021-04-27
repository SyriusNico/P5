# coding : utf-8
import sys 
sys.path.append('C:\\Users\\Utilisateur\\Documents\\ExerciceOC\\Pur_Beurre')
import	Views.menuView as m

class MenuController():
	"""docstring for MenuController"""
	def __init__(self): 
		self.choice = None
		self.response = None
		self.pick = None

	def menuScreen(self):
		menu = m.MenuView()
		mainMenu = menu.screen()
		return mainMenu
	def menuBye(self):
		menu = m.MenuView()
		bye = menu.bye()
		return bye

	def makeChoice(self):
		self.choice = int(input("\nChoisissez une option : "))
		return self.choice

	def register(self):
		self.response = int(input("\nVoulez enregistrer ce produit dans votre liste ?\n1.oui\n2.non\n"))
		return self.response

	def pick(self):
		self.pick = int(input("\nChoisissez un produit en tapant son ID :\n"))
		return self.pick