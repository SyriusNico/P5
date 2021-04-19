# coding : utf-8
import sys
sys.path.append('C:\\Users\\Utilisateur\\Documents\\ExerciceOC\\Pur_Beurre')
import Models.product as p

class Substitute(p.Product):

	"""Send alt product to the controller"""

	def __init__(self):
		super().__init__()
		self.subsitute_id = None 

	def bestProducts(self):

		req = (" SELECT * FROM products WHERE nutrition_grade = 'a'")
		self.cursor.execute(req)
		bestProducts = self.cursor.fetchall()
		return bestProducts







	