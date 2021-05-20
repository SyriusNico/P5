# coding : utf-8
import Database.database as c
import Models.product as p


class Substitute(c.Database):

	"""Send alt product to the controller"""

	def __init__(self, product=None, substitute=None):
		super().__init__()
		self.product = product
		self.substitute = substitute

	def save(self, product, substitute):
		"""
		method which allows you to save a substitute
		"""
		try:
			req = ("INSERT INTO substitutes (product_id, substitute_id) \
			VALUES (%s,%s)")
			features = (product.id, substitute.id)
			self.cursor.execute(req, features)
			self.cnx.commit()
		except AttributeError:
			print("Le produit sera sauvegardé en tant que substitut.")
			req = ("INSERT INTO substitutes (product_id, substitute_id) \
			VALUES (%s,%s)")
			features = (product.id, product.id)
			self.cursor.execute(req, features)
			self.cnx.commit()

	def readAll(self):
		"""
		method wich allows you to read substitute liste
		"""
		req = "SELECT * FROM substitutes"
		self.cursor.execute(req)
		datas = self.cursor.fetchall()
		substitutes = []
		for data in datas:
			product = p.Product()
			product = product.readProd(data[0])
			product_2 = p.Product()
			product_2 = product_2.readProd(data[1])
			new_substitute = Substitute(product, product_2)
			substitutes.append(new_substitute)
		return substitutes

	def readInDetail(self, substitute_id):
		req = (
			"SELECT * FROM substitutes \
			WHERE substitute_id = '{}'".format(substitute_id)
		)
		self.cursor.execute(req)
		datas = self.cursor.fetchall()
		detail_list = []
		for data in datas:
			product = p.Product()
			product = product.readProd(data[0])
			product_2 = p.Product()
			product_2 = product_2.readProd(data[1])
			new_substitute = Substitute(product, product_2)
			detail_list.append(new_substitute)
		return detail_list

	def deleteOne(self, substitute_id):
		"""
		deletes an initial product and its substitute
		"""
		req = (
			"DELETE FROM substitutes \
			WHERE substitute_id = '{}'".format(substitute_id)
		)
		self.cursor.execute(req)
		self.cnx.commit()

	def _can_be_deleted(self, sub, mylist):
		"""
		check if you can
		delete its substitute
		"""
		for substitute in mylist:
			if  substitute.substitute.id == sub or substitute.product.id == sub:
				return True
		return False
	def deleteAll(self):
		"""
		delete the substitute list 
		"""
		req = ("DELETE FROM substitutes")
		self.cursor.execute(req)
		self.cnx.commit()
