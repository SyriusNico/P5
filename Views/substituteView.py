# coding : utf-8
import sys
sys.path.append('C:\\Users\\Utilisateur\\Documents\\ExerciceOC\\Pur_Beurre')
import Controllers.substituteController as s


class SubstituteView():


	def show_subs(self, substitute):
		try:
			print("_______________________________________________")
			print("                                               ")
			print("   Vous pouvez remplacer ce produit par :      ")
			print("                                               ")
			print("ID :   ", substitute.id, "                     ")
			print("                                               ")
			print("Nom :  ", substitute.product_name,"            ")
			print("                                               ")
			print("Code : ", substitute.code, "                   ")
			print("                                               ")
			print("Nutriscore :", substitute.nutrition_grade, "   ")
			print("                                               ")
			print("Magasins : ", substitute.stores, "             ")
			print("                                               ")
			print("###############################################")
		except AttributeError:
			print("Il n'y a pas de substitut possible")

	def show_myList(self, myList):
		for item in myList:
			print("ID :", item.substitute.id,"|  Produit de substitution :",
			item.substitute.product_name)

	def details(self, myList):
		for product in myList:
			print("###############################################")
			print("                                               ")
			print("     Produit initialement sélectionné :        ")
			print("                                               ")
			print("ID :   ", product.product.id, "                ")
			print("                                               ")
			print("Nom :  ", product.product.product_name,"       ")
			print("                                               ")
			print("Code : ", product.product.code, "              ")
			print("                                               ")
			print("Nutriscore :", product.product.nutrition_grade  )
			print("                                               ")
			print("Magasins : ", product.product.stores, "        ")
			print("                                               ")
			print("_______________________________________________")
			print("                                               ")
			print("    Produit sélectionné comme substitut :      ")
			print("                                               ")
			print("ID :   ", product.substitute.id, "             ")
			print("                                               ")
			print("Nom :  ", product.substitute.product_name,"    ")
			print("                                               ")
			print("Code : ", product.substitute.code, "           ")
			print("                                               ")
			print("Nutriscore :", product.substitute.nutrition_grade)
			print("                                               ")
			print("Magasins : ", product.substitute.stores, "     ")
			print("                                               ")
			print("###############################################")