# coding : utf-8
import Models.substitute as s
# import sys
# # sys.path.append('C:\\Users\\Utilisateur\\Documents\\ExerciceOC\\Pur_Beurre')
# sys.path.append('Pur_Beurre')

class SubstituteController():

	def __init__(self):
		self.substitute = s.Substitute()

	def compare(self, productToCompare, product_list):
		"""
		compare the selected product 
		with the other products in the list
		"""
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
		"""
		used to register the substitute product
		"""
		self.substitute.save(product, substitute)

	def deleteAll(self):
		"""
		delete all the substitute list
		"""
		self.substitute.deleteAll()

	def myList(self):
		"""
		substitute list
		"""
		myList = self.substitute.readAll()
		return myList
