import sys
sys.path.append('C:\\Users\\Utilisateur\\Documents\\ExerciceOC\\Pur_Beurre')

import Models.product as p

class ProductController:

	def __init__(self):

		#self.db = d.Database()
		self.prod = p.Product()
		self.catNumber = None
		self.prodNumber = None

	def send_products(self):
		
		self.catNumber = int(input("\nChoisissez une categorie : "))
		products = self.prod.read(self.catNumber)
		return products

	def send_product(self):

		self.prodNumber = int(input("\nChoisissez un produit : "))
		product = self.prod.readOne(self.prodNumber)
		return product
