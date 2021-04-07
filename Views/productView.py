# coding : utf-8
import sys
sys.path.append('C:\\Users\\Utilisateur\\Documents\\ExerciceOC\\Pur_Beurre')
import Database.database as d
import Controllers.productController as p

class ProductView:

	def __init__(self):

		self.prodView = p.ProductController()
		self.show_products()


	def show_products(self):

		products = self.prodView.send_products()

		print("\n*****************************************")
		print("****          PRODUITS               ****")
		print("*****************************************\n")
		for product in products:
			print(product[0],product[1])

	def describe_product(self):
		count = 0
		product = self.prodView.send_product()
		attributes = ["ID:", "NOM:", "CODE:", "NUTRISCORE:", "MAGASIN:", "CATEGORIE:"]
		for attribute in product:
			print(attributes[count], attribute)
			print("___")
			count += 1