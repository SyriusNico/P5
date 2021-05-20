# coding : utf-8



class SubstituteView():

	def show_subs(self, substitute):
		try:
			print("_______________________________________________\n")
			print("   Vous pouvez remplacer ce produit par :  \n")
			print("ID :   ", substitute.id, "\n")
			print("Nom :  ", substitute.product_name, "\n")
			print("Code : ", substitute.code, "\n")
			print("Nutriscore :", substitute.nutrition_grade, "\n")
			print("Magasins : ", substitute.stores, "\n")
			print("Lien :", substitute.url, "\n")
			print("###############################################")
		except AttributeError:
			print("Il n'y a pas de substitut possible")
	def show_list(self,mylist):
		print("\n\n ***Mes produits substitués***\n\n")
		for product in mylist:
			print(product.substitute.id, product.substitute.product_name)

	def details(self, myList):
		for product in myList:
			print("###############################################\n")
			print("     Produit initialement sélectionné :       \n")
			print("ID :   ", product.product.id, "\n")
			print("Nom :  ", product.product.product_name, "\n")
			print("Code : ", product.product.code, "\n")
			print("Nutriscore :", product.product.nutrition_grade, "\n")
			print("Magasins : ", product.product.stores, "\n")
			print("Lien :", product.product.url, "\n")
			print("_______________________________________________\n")
			print("    Produit sélectionné comme substitut :     \n")
			print("ID :   ", product.substitute.id, "\n")
			print("Nom :  ", product.substitute.product_name, "\n")
			print("Code : ", product.substitute.code, "\n")
			print("Nutriscore :", product.substitute.nutrition_grade, "\n")
			print("Magasins : ", product.substitute.stores, "\n")
			print("Lien :", product.substitute.url, "\n")
			print("###############################################")
