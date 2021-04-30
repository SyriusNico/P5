import sys
sys.path.append('C:\\Users\\Utilisateur\\Documents\\ExerciceOC\\Pur_Beurre')

import Models.product as p

class ProductController:

	def __init__(self):
		self.prod = p.Product()
		self.catNumber = None
		self.prodNumber = None

	def send_products(self):
		self.catNumber = int(input("\nChoisissez une categorie : "))
		products = self.prod.read(self.catNumber)
		return products

	def send_product(self, categories):

		correct = False
		while correct == False:
			try:
				product_id = int(input("\nChoisissez un produit : "))
				prod_from_db = self.prod.readOne(product_id)
				correct = True
				return prod_from_db
			except TypeError:
				print("Ce choix ne correspond à aucun produit")
				correct = False
