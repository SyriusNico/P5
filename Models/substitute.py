# coding : utf-8
import Database.database as c
import Models.product as p
# import sys
# # sys.path.append('C:\\Users\\Utilisateur\\Documents\\ExerciceOC\\Pur_Beurre')
# sys.path.append('Pur_Beurre')

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

	def deleteAll(self):
		"""
		delete the substitute list 
		"""
		req = ("DELETE FROM substitutes")
		self.cursor.execute(req)
		self.cnx.commit()
