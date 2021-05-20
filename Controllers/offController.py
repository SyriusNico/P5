# coding : utf-8
import Config.config as cf
import Api.off as off
import Models.category as c
import Models.product as p

class OffController:

	def __init__(self):
		self.off = off.Off()

	def init_datas(self):
		"""
		method used to initialize the database
		"""
		index = 1
		for category in cf.CATEGORIES:
			products = self.off.get_products(category)
			self.__store_category(category)
			for product in products:
				self.__store_product(index, **product)
			index += 1

	def read(self):
		"""
		method that returns the products for each categories
		"""
		for category in cf.CATEGORIES:
			products = self.off.get_products(category)
			return products

	def __store_category(self, category):
		"""
		method which saves a category
		"""
		cat = c.Category()
		cat.name = category
		cat.create()

	def __store_product(self, idx, **product):
		"""
		method that registers a product
		"""
		prod = p.Product(**product)
		prod.category_id = idx
		prod.create()
