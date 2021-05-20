# coding : utf-8
import Database.database as c
# import sys
# # sys.path.append('C:\\Users\\Utilisateur\\Documents\\ExerciceOC\\Pur_Beurre')
# sys.path.append('Pur_Beurre')

class Product(c.Database):

	"""Send product data to the controller"""

	def __init__(self, **product):
		super().__init__()
		self.id = None
		self.product_name = product.get('product_name')
		self.code = product.get('code')
		self.nutrition_grade = product.get('nutrition_grade_fr')
		self.stores = product.get('stores')
		self.url = product.get('url')
		self.category_id = ''

	def set_id(self, _id):
		self.id = _id

	def set_name(self, name):
		self.product_name = name

	def set_code(self, code):
		self.code = code

	def set_nutrition_grade(self, grade):
		self.nutrition_grade = grade

	def set_stores(self, stores):
		self.stores = stores

	def set_url(self, url):
		self.url = url

	def set_category_id(self, _id):
		self.category_id = _id

	def create(self):
		if self._can_be_created():
			req = (
				"INSERT INTO products \
				(product_name, code, nutrition_grade, stores, url, category_id) \
				VALUES (%s, %s,%s, %s, %s, %s)"
			)
			features = (
				self.product_name, self.code, self.nutrition_grade,
				self.stores, self.url, self.category_id
			)
			self.cursor.execute(req, features)
			self.cnx.commit()
		else:
			print(
				self.product_name,
				"n'est pas renseigné, le produit n'est pas enregistré en BDD"
			)

	def _can_be_created(self):
		"""
		check if you can register
		this data in your datatabase
		"""
		if self.product_name is None:
			return False
		elif self.code is None:
			return False
		elif self.nutrition_grade is None:
			return False
		elif self.stores is None:
			return False
		elif self.url is None:
			return False
		return True

	def read(self, choice=int):
		"""
		select all products when you enter an id
		"""
		req = "SELECT * FROM products WHERE category_id = '{}'".format(choice)
		self.cursor.execute(req)
		datas = self.cursor.fetchall()
		products = []
		for idx, data in enumerate(datas):
			prod = Product()
			prod.set_id(data[0])
			prod.set_name(data[1])
			prod.set_code(data[2])
			prod.set_nutrition_grade(data[3])
			prod.set_stores(data[4])
			prod.set_url(data[5])
			prod.set_category_id(choice)
			products.append(prod)
		return products

	def readOne(self, prod_id, cat_id):
		""" 
		select a product when you
		enter its id and its category
		"""
		req = "SELECT * FROM products WHERE id = '{}' \
		AND category_id = '{}'".format(prod_id, cat_id)
		self.cursor.execute(req)
		data = self.cursor.fetchone()
		oneProd = Product()
		oneProd.set_id(data[0])
		oneProd.set_name(data[1])
		oneProd.set_code(data[2])
		oneProd.set_nutrition_grade(data[3])
		oneProd.set_stores([data[4]])
		oneProd.set_url(data[5])
		oneProd.set_category_id(cat_id)
		return oneProd

	def readProd(self, prod_id):
		""" 
		select a product when you enter its id
		"""
		req = "SELECT * FROM products WHERE id = '{}'".format(prod_id)
		self.cursor.execute(req)
		data = self.cursor.fetchone()
		oneProd = Product()
		oneProd.set_id(data[0])
		oneProd.set_name(data[1])
		oneProd.set_code(data[2])
		oneProd.set_nutrition_grade(data[3])
		oneProd.set_stores(data[4])
		oneProd.set_url(data[5])
		oneProd.set_category_id(data[6])
		return oneProd
