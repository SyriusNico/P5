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

	def send_product(self):

		correct = False
		while correct == False:
			product_id = int(input("\nChoisissez un produit : "))

			prod_from_db = self.prod.readOne(product_id)
			# # check if product exists in DB
			if prod_from_db:
				# check if product category correspond to our cat id
				if prod_from_db.id == product_id:
					# le produit chosi est OK
					correct = True
					return prod_from_db
