# coding : utf-8
import sys
sys.path.append('C:\\Users\\Utilisateur\\Documents\\ExerciceOC\\Pur_Beurre')
import Models.substitute as s

class SubstituteController():

	def __init__(self):
		self.substitute = s.Substitute()

	def compare(self, productToCompare, product_list):

		for product in product_list:
			if product.nutrition_grade != productToCompare.nutrition_grade :
				if product.nutrition_grade == 'a':
					return product
				if product.nutrition_grade == 'b':
					return product
				if product.nutrition_grade == productToCompare.nutrition_grade:
					print("Il n'a pas de meilleur produit à proposer")


	def store(self, product, substitute):
		self.substitute.save(product, substitute)

	def deleteAll(self):
		self.substitute.deleteAll()

	def myList(self):
		myList = self.substitute.readAll()
		return myList