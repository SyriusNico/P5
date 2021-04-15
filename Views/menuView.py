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

	def display(self):

		# print("\n", self.title,"\n")
		# print(self.one)
		# print(self.two)
		# print("\nChoisissez une option :")
		choose = int(input())
		if choose == 1:
			number = 1
			for category in s.CATEGORIES:
				print(number, ":", category)
				number += 1
			print("\nChoisissez une catégorie :")
			prod = p.ProductView()
			print("\nChoisissez un produit :")
			prod.describe_product()
		if choose == 2:
			print("\nOn n'a pas encore l'option mais ça vient")
		# if choose != 1 or choose != 2:
		# 	print("\nVous devez saisir le chiffre associé à la proposition")
		# 	print("En plus {} n'est pas dans la liste.".format(choose))
	def printTitle(self):
		print(self.title)

	def printOption(self):
		print(self.one)
		print(self.two)