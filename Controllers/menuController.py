# coding : utf-8
import sys 
sys.path.append('C:\\Users\\Utilisateur\\Documents\\ExerciceOC\\Pur_Beurre')
import	Views.menuView as m

class MenuController():
	"""docstring for MenuController"""
	def __init__(self):
		self.menuScreen() 

	def menuScreen(self):
		menu = m.MenuView()
		return menu

	def makeChoice(self):
		choice = int(input("\nChoisissez une option : "))
		return choice

	def register(self):
		register = int(input("\nVoulez enregistrer ce produit dans votre liste ?"))
		return register