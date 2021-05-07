# coding : utf-8
import Config.config as cf
import Api.off as off
import Models.category as c
import Models.product as p
import sys
sys.path.append('C:\\Users\\Utilisateur\\Documents\\ExerciceOC\\Pur_Beurre')


class OffController:

	def __init__(self):
		self.off = off.Off()

	def init_datas(self):
		index = 1
		for category in cf.CATEGORIES:
			products = self.off.get_products(category)
			self.__store_category(category)
			for product in products:
				self.__store_product(index, **product)
			index += 1

	def read(self):
		for category in cf.CATEGORIES:
			products = self.off.get_products(category)
			return products

	def __store_category(self, category):
		cat = c.Category()
		cat.name = category
		cat.create()

	def __store_product(self, idx, **product):
		prod = p.Product(**product)
		prod.category_id = idx
		prod.create()
