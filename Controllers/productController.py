# coding : utf-8
import Models.product as p
import Views.productView as v
import sys
sys.path.append('C:\\Users\\Utilisateur\\Documents\\ExerciceOC\\Pur_Beurre')


class ProductController:

	def __init__(self):
		self.prod = p.Product()
		self.prodView = v.ProductView()
		self.catNumber = None
		self.prodNumber = None

	def choose_cat(self):
		self.catNumber = int(input("\nChoisissez une categorie : "))
		print("Veuillez patienter ...")
		return self.catNumber

	def send_products(self):
		products = self.prod.read(self.catNumber)
		return products

	def send_product(self):
		product_list = self.send_products()
		self.prodView.show_products(product_list)
		correct = False
		while correct == False:
			try:
				product_id = int(input("\nChoisissez un produit : "))
				prod_from_db = self.prod.readOne(product_id, self.catNumber)
				if prod_from_db.category_id != self.catNumber:
					print(
						"Il n'y a aucun produit avec l'ID : {} "
						"pour cette categorie".format(prod_from_db.id)
					)
				else:
					correct = True
					return prod_from_db

			except TypeError:
				print("Ce choix ne correspond à aucun produit")
				correct = False
