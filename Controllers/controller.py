import sys
sys.path.append('C:\\Users\\Utilisateur\\Documents\\ExerciceOC\\Pur_Beurre')
import Controllers.menuController as c
import Controllers.categoryController as ctrl
import Controllers.productController as  pc
import Controllers.substituteController as sc
import Views.categoryView as cat
import Views.productView as p


class Controller():

	
	def __init__(self):

		self.category_demand = ctrl.CategoryController()
		self.product_demand = pc.ProductController()
		self.categories = cat.CategoryView()
		self.products = p.ProductView()
		self.substitute = sc.SubstituteController()
		self.launch()

	def launch(self):

		menu = c.MenuController()
		if menu.makeChoice() == 1:
			self.category_demand.store_categories()
			product_list = self.product_demand.send_products()
			self.products.show_products(product_list)
			product = self.product_demand.send_product()
			self.products.describe_product(product)
			self.substitute.compare(product, product_list)
			# if menu.register() == 1:
			# 	print("\nproduit enregistré")
		# A REVOIR A RETRAVAILLER