# coding : utf-8
import sys
sys.path.append('C:\\Users\\Utilisateur\\Documents\\ExerciceOC\\Pur_Beurre')

import Config.config as cf
import Api.off as off
import Models.category as c
import Models.product as p
# Prends en compte l'interrogation du client
class OffController:

	def __init__(self):

		self.off = off.Off()
		# self.init_datas()

	def init_datas(self):
		index = 1
		for category in cf.CATEGORIES:
			products = self.off.get_products(category)
			self.__store_category(category)
			for product in products:
				self.__store_product(index, **product)
			index += 1



	def __store_category(self, category):
		cat = c.Category()
		cat.name = category
		cat.create()

	def __store_product(self, idx, **product):
		prod = p.Product(**product)
		prod.category_id = idx
		prod.create()
