import sys
sys.path.append('C:\\Users\\Utilisateur\\Documents\\ExerciceOC\\Pur_Beurre')
import Controllers.menuController as c
import Controllers.categoryController as ctrl
import Controllers.productController as  pc
import Controllers.substituteController as sc
import Views.categoryView as cat
import Views.productView as p
import Views.substituteView as s


class Controller():

	
	def __init__(self):

		self.category_demand = ctrl.CategoryController()
		self.product_demand = pc.ProductController()
		self.substitute_demand = sc.SubstituteController()
		self.categories = cat.CategoryView()
		self.products = p.ProductView()
		self.subView = s.SubstituteView()
		self.launch()

	def launch(self):

		menu = c.MenuController()
		itsGood = False
		while itsGood == False:
			menu.menuScreen()
			menu.makeChoice()
			if menu.choice == 1:
				itsGood = True
				self.category_demand.store_categories()
				product_list = self.product_demand.send_products()
				self.products.show_products(product_list)
				product = self.product_demand.send_product()
				self.products.describe_product(product)
				substitute = self.substitute_demand.compare(product, product_list)
				self.subView.show_subs(substitute)
				menu.register()
				# User choose yes
				if menu.response == 1:
					self.substitute_demand.store(product, substitute)
					itsGood = False
				# User choose no
				elif menu.response == 2:
					menu.menuScreen()
					itsGood = False
				else:
					print("Ce choix ne correspond à aucune option")
					itsGood = False

			elif menu.choice == 2:
				subs_list = self.substitute_demand.myList()
				self.subView.show_myList(subs_list)


			elif menu.choice == 3:
				menu.menuBye()
				itsGood = True
			else:
				print("Ce choix ne correspond à aucune option")
