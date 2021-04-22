# coding : utf-8
import sys
sys.path.append('C:\\Users\\Utilisateur\\Documents\\ExerciceOC\\Pur_Beurre')
import Models.product as p

class Substitute(p.Product):

	"""Send alt product to the controller"""

	def __init__(self):
		super().__init__()
		self.subsitute_id = None
		self.bestProducts(2)

	def bestProducts(self, category):

		req = (" SELECT * FROM products WHERE category_id = '{}' AND nutrition_grade = 'a' ".format(category))
		self.cursor.execute(req)
		datas = self.cursor.fetchall()
		bestProducts = []
		for idx, data in enumerate(datas):
			subs = p.Product()
			subs.set_id(data[0])
			subs.set_name(data[1])
			subs.set_code(data[2])
			subs.set_nutrition_grade(data[3])
			subs.set_stores(data[4])
			subs.set_category_id(category)
			bestProducts.append(subs)

		return bestProducts







	