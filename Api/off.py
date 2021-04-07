# coding: utf-8
import pprint
import sys
sys.path.append('C:\\Users\\Utilisateur\\Documents\\ExerciceOC\\Pur_Beurre')
import requests
import Config.settings as settings
import Database.database as dt

class Off():
	"""
	only send requests to the API
	"""
	def __init__(self):
		
		self.db = dt.Database()
		self.url = settings.URL


	def __get_payload(self, category):
		return {
			'action': 'process',
			'tagtype_0': 'categories',
			'tag_contains_0': 'contains',
			'tag_0': category,
			'tagtype_1': 'nutrition_grade_fr',
			'tag_contains_1': 'contains',
			'page_size': settings.NUMBER_PRODUCT, 
			'json': 'true',
		}

	def get_products(self, category):

		payload = self.__get_payload(category)
		req = requests.get(self.url, payload)
		products = req.json().get('products')
		self.db.cursor.close()
		self.db.cnx.close()	
		return products

