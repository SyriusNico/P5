# coding : utf-8
import sys
sys.path.append('C:\\Users\\Utilisateur\\Documents\\ExerciceOC\\Pur_Beurre')
import Models.category as c
import Views.categoryView as v

class CategoryController:
	"""register categories for database"""
	def __init__(self):
		self.cat = c.Category()
		self.catView = v.CategoryView()

	def get_id_category(self):
		return self.cat.id_category

	def store_categories(self):
		categories = self.cat.read()
		return self.catView.show_categories(categories)
