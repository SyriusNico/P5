# coding : utf-8

class ProductView:

	def show_products(self, productController):

		try:
			print("\n*****************************************")
			print("****          PRODUITS               ****")
			print("*****************************************\n")

			for product in productController:
				print(product.id, "     ", product.product_name)
		except TypeError:
			print("Votre choix ne correspond à aucun produit.")

	def describe_product(self, productController):

		print("\n*****************************************")
		print("****     Description du produit      ****")
		print("*****************************************\n")
		print("\nNOM : ", productController.product_name)
		print("\nCODE : ", productController.code)
		print("\nNUTRISCORE : ", productController.nutrition_grade)
		print("\nSTORES : ", productController.stores)
		print("\nLIEN : ", productController.url)
