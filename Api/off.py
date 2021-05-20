# coding: utf-8
import requests
import Config.config as cf
# import Database.database as dt
# import sys
# sys.path.append('C:\\Users\\Utilisateur\\Documents\\ExerciceOC\\Pur_Beurre')
sys.path.append('Pur_Beurre')

class Off():
	"""
	only send requests to the API
	"""
	def __init__(self):

		self.db = dt.Database()
		self.url = cf.URL

	def __get_payload(self, category):
		return {
			'action': 'process',
			'tagtype_0': 'categories',
			'tag_contains_0': 'contains',
			'tag_0': category,
			'tagtype_1': 'nutrition_grade_fr',
			'tag_contains_1': 'contains',
			'page_size': cf.NUMBER_PRODUCT,
			'json': 'true',
		}

	def get_products(self, category):
		"""
		send a request to the API to retrieve the products
		"""
		payload = self.__get_payload(category)
		req = requests.get(self.url, payload)
		products = req.json().get('products')
		self.db.cursor.close()
		self.db.cnx.close()
		return products
