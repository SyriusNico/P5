# coding : utf-8
import sys
sys.path.append('C:\\Users\\Utilisateur\\Documents\\ExerciceOC\\Pur_Beurre')
import Models.category as c

class CategoryController:
	"""register categories for database"""
	def __init__(self):

		#self.db = d.Database()
		self.cat = c.Category()

	def store_categories(self):
		categories = self.cat.read()
		return categories
