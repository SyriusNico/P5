# coding : utf-8
import Models.substitute as s

class SubstituteController():

	def __init__(self):
		self.substitute = s.Substitute()

	def compare(self, productToCompare, product_list):
		"""
		compare the selected product 
		with the other products in the list
		"""
		if productToCompare.nutrition_grade == 'a':
			return productToCompare
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

	def deleteOne(self, subsProd, mylist):
		"""
		delete one substitute
		"""
		if self.substitute._can_be_deleted(subsProd, mylist):
			self.substitute.deleteOne(subsProd)
			print("\n\nLe produit a été effacé\n\n")
		else:
			print("Aucun produit trouvé.")

	def deleteAll(self):
		"""
		delete all the substitute list
		"""
		self.substitute.deleteAll()

	def describe(self, subsProd):
		"""
		send more details
		"""
		prod = self.substitute.readInDetail(subsProd)
		return prod

	def myList(self):
		"""
		substitute list
		"""
		myList = self.substitute.readAll()
		return myList
