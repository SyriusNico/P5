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
			


	def store(self, product, substitute):
		self.substitute.create(product, substitute)

	def myList(self):
		myList = self.substitute.readSubList()
		return myList