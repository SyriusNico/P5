import Controllers.menuController as c
import Controllers.categoryController as ctrl
import Controllers.productController as pc
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
		"""
		method used to process the user's 
		request as long as the user does 
		not enter a correct option the menu is displayed
		"""
		menu = c.MenuController()
		itsGood = False
		while itsGood == False:
			try:
				menu.menuScreen()
				menu.makeChoice()
				# Find a product
				if menu.choice == 1:
					itsGood = True
					self.category_demand.store_categories()
					select_category = self.product_demand.choose_cat()
					if select_category > 5:
						itsGood = False
					else:
						product_list = self.product_demand.send_products()
						product = self.product_demand.send_product()
						self.products.describe_product(product)
						substitute = self.substitute_demand.compare(product, product_list)
						if product == substitute:
							print("Ce produit est le meilleur")
						else:
							self.subView.show_subs(substitute)
						menu.register()

					# User choose yes
					if menu.response == 1:
						self.substitute_demand.store(product, substitute)
						itsGood = False
					# User choose no
					elif menu.response == 2:
						itsGood = False
					else:
						print("Ce choix ne correspond à aucune option")
						itsGood = False
				# substitute menu
				elif menu.choice == 2:
					correct = False
					itsGood = True
					while correct == False:
						menu.substituteScreen()
						menu.makeChoice()
						# view my substitute list
						if menu.choice == 1:
							correct = True
							subs_list = self.substitute_demand.myList()
							if subs_list != []:
								self.subView.show_list(subs_list)
								menu.detail()
								if menu.details == 1:
									sub_number = int(input("Choisissez un produit :"))
									sub = self.substitute_demand.describe(sub_number)
									self.subView.details(sub)
									correct = False
								if menu.details == 2:
									itsGood = False
								else:
									correct = False
							else:
								print("\n\nLa liste est vide.\n\n")
								correct = True
						# delete one product from the list
						if menu.choice == 2:
							subs_list = self.substitute_demand.myList()
							if subs_list != []:
								self.subView.show_list(subs_list)
								print("\n\nSelectionner le produit " 
								"à supprimer\n")
								subProd = int(input("\n\nEntrer le numéro"
									" du produit de substitution : "))
								self.substitute_demand.deleteOne(subProd, subs_list)
							else:
								print("\n\nLa liste est vide.\n\n")
								correct = True
						# delete all the list
						if menu.choice == 3:
							self.substitute_demand.deleteAll()
							print("\n\nLa liste à été vidé.\n\n")
							correct = True
						# return to the main menu
						if menu.choice == 4:
							correct = True
							itsGood = False
						else:
							print("\n\nRetour au menu substituts.\n\n")
							correct = False
				# exit the program
				elif menu.choice == 3:
					menu.menuBye()
					itsGood = True
				else:
					print("Ce choix ne correspond à aucune option.")
			except ValueError:
				print("Vous devez entrer un numéro.Retour un menu principal.")
				itsGood = False
