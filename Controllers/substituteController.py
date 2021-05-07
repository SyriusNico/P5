# coding : utf-8
import Models.substitute as s
import sys
sys.path.append('C:\\Users\\Utilisateur\\Documents\\ExerciceOC\\Pur_Beurre')


class SubstituteController():

	def __init__(self):
		self.substitute = s.Substitute()

	def compare(self, productToCompare, product_list):

		if productToCompare.nutrition_grade == 'a':
			pass
		else:
			for product in product_list:
				if product.nutrition_grade != productToCompare.nutrition_grade:
					if product.nutrition_grade == 'a':
						return product
					if product.nutrition_grade == 'b':
						return product

	def store(self, product, substitute):
		self.substitute.save(product, substitute)

	def deleteAll(self):
		self.substitute.deleteAll()

	def myList(self):
		myList = self.substitute.readAll()
		return myList
