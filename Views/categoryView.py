# coding : utf-8
import sys
sys.path.append('C:\\Users\\Utilisateur\\Documents\\ExerciceOC\\Pur_Beurre')
import Database.database as d
import Controllers.categoryController as c

class CategoryView:

	def __init__(self):

		self.catView = c.CategoryController()
		self.show_categories()

	def show_categories(self):

		categories = self.catView.store_categories()

		print("\n*****************************************")
		print("****          CATEGORIES             ****")
		print("*****************************************\n")
		for i in categories:
			print(i[0],i[1])