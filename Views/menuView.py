import sys
sys.path.append('C:\\Users\\Utilisateur\\Documents\\ExerciceOC\\Pur_Beurre')
import Config.settings as s
import Views.productView as p

class MenuView:

	def __init__(self):

		self.screen()

	def screen(self):
		print(" __________________________________________________")
		print("|                                                  |")
		print("|           BIENVENUE SUR PUR BEURRE               |")
		print("|                   ****                           |")
		print("|                                                  |")
		print("|                 * MENU *                         |")
		print("|                                                  |")
		print("|  1. Aliment à remplacer                          |")
		print("|                                                  |")
		print("|  2. Retrouver mes aliments substitués            |")
		print("|                                                  |")
		print("|__________________________________________________|")

