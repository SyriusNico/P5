# coding : utf-8
import sys
sys.path.append('C:\\Users\\Utilisateur\\Documents\\ExerciceOC\\Pur_Beurre')
import Database.database as c
# FAIRE PAREIL POUR CATEGORY
# KEVIN - EST CE QUE JE DOIS LE METTRE ICI ??
class Product(c.Database):

	"""Send product data to the controller"""

	def __init__(self, **product):
		super().__init__()
		self.product_name = product.get('product_name')
		self.code = product.get('code') 
		self.nutrition_grade = product.get('nutrition_grade_fr')
		self.stores = product.get('stores')
		self.category_id = ''


	def create(self):
		if self._can_be_created():
			req = (	
			"INSERT INTO products (product_name, code, nutrition_grade, stores, category_id) VALUES (%s, %s,"
			"%s, %s, %s)"
			)
			features = ( self.product_name, self.code, self.nutrition_grade, self.stores, self.category_id )
			self.cursor.execute(req, features)
			self.cnx.commit()
		else:
			print("le nom du produit n'est pas renseigné, le produit n'est pas enregistré en BDD")

	def _can_be_created(self):
		#TODO (vérification des données)
		if self.product_name is None:
			return False
		elif self.code is None:
			return False
		elif self.nutrition_grade is None:
			return False
		elif self.stores is None:
			return False
		return True

	def read(self, choice=int):
		req = "SELECT * FROM products WHERE category_id = '{}'".format(choice)
		self.cursor.execute(req)
		# fetchall a faire dans le model
		datas = self.cursor.fetchall()
		products = []
		for data in datas:
			products.append(data)
		return products

	def readOne(self, choice=int):
		req = "SELECT * FROM products WHERE id = '{}'".format(choice)
		self.cursor.execute(req)
		data = self.cursor.fetchone()
		attributes = []
		for attr in data:
			attributes.append(attr)
		return attributes

	def update(self):
		pass

	def delete(self):
		pass

