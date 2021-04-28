# coding : utf-8
import sys
sys.path.append('C:\\Users\\Utilisateur\\Documents\\ExerciceOC\\Pur_Beurre')
import Controllers.substituteController as s


class SubstituteView():


	def show_subs(self, substitute):
		try:
			print("\n###########################################")
			print("                                          ")
			print("  Vous pouvez remplacer ce produit par :  ")
			print("                                          ")
			print("     ", substitute.product_name,"         ")
			print("                                          ")
			print("  Pour un score égal à :                  ")
			print("                                          ")
			print("     ", substitute.nutrition_grade,"      ")
			print("                                          ")
			print("###########################################")
		except AttributeError:
			print("Il n'y a pas de substitut possible")

	def show_myList(self, myList):
		for item in myList:
			print("ID :", item.substitute_id,"|  Produit de substitution :",
			item.product_name)

	def details(self, choice, myList):
		for product in myList:
			if product.substitute_id == choice:
				print("###############################################")
				print("                                               ")
				print("            Description du produit :           ")
				print("                                               ")
				print("ID :   ", product.substitute_id, "             ")
				print("                                               ")
				print("Nom :  ", product.product_name,"               ")
				print("                                               ")
				print("Code : ", product.code, "                      ")
				print("                                               ")
				print("Score :", product.nutrition_grade, "           ")
				print("                                               ")
				print("Magasins : ", product.stores, "                ")
				print("                                               ")
				print("###############################################")