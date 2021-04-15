import sys
sys.path.append('C:\\Users\\Utilisateur\\Documents\\ExerciceOC\\Pur_Beurre')
import Controllers.menuController as c
import Controllers.categoryController as ctrl
import Controllers.productController as  pc
import Views.categoryView as cat
import Views.productView as p

catCtrl = ctrl.CategoryController()
prodCtrl = pc.ProductController()
categories = cat.CategoryView()

class Controller():

	
	def __init__(self):

		self.category_demand = ctrl.CategoryController()
		self.product_demand = pc.ProductController()
		self.categories = cat.CategoryView()
		self.products = p.ProductView()
		self.launch()

	def launch(self):

		menu = c.MenuController()
		if menu.makeChoice() == 1:
			datas = catCtrl.store_categories()
			categories.show_categories(datas)
		# category = input("Choisissez une catégorie")
			product_list = self.product_demand.send_products()
			self.products.show_products(product_list)
			product = self.product_demand.send_product()
			# self.products.describe_product(product)
			for prod in product_list:
				if prod.id == product.id:
					self.products.describe_product(product)
				else:
					print("le produit n'est pas dans la liste")