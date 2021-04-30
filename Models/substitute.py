# coding : utf-8
import sys
sys.path.append('C:\\Users\\Utilisateur\\Documents\\ExerciceOC\\Pur_Beurre')
import Database.database as c
import Models.product as p

# class Substitute(p.Product):

# 	"""Send alt product to the controller"""

# 	def __init__(self):
# 		super().__init__()
# 		# useless attributes
# 		self.product_id = None
# 		self.substitute_id = None

# 	def set_product_id(self, product_id):
# 		self.product_id = product_id

# 	def set_substitute_id(self, substitute_id):
# 		self.substitute_id = substitute_id


# 		# useless function i have to rework them
# 	def create(self, product, substitute):

# 		req = ("INSERT INTO substitutes (product_id, substitute_id) VALUES (%s,%s)")
# 		features = (product.id, substitute.id)
# 		self.cursor.execute(req, features)
# 		self.cnx.commit()

# 	def readSubList(self):
# 		# req = ("SELECT * FROM products  JOIN substitutes ON products.id = substitutes.product_id AND products.id = substitutes.substitute_id")
# 		# req = ("SELECT product_id, substitute_id,  product_name FROM substitutes JOIN products ON substitutes.product_id = products.id AND substitutes.product_name = products.product_name")
# 		req = ("SELECT * \
#   		FROM products \
#   		INNER JOIN substitutes ON products.id = substitutes.substitute_id")
# 		self.cursor.execute(req)
# 		datas = self.cursor.fetchall()
# 		substitutes = []
# 		for data in datas:
# 			substitute = Substitute()
# 			substitute.set_name(data[1])
# 			substitute.set_code(data[2])
# 			substitute.set_nutrition_grade(data[3])
# 			substitute.set_stores(data[4])
# 			substitute.set_product_id(data[6])
# 			substitute.set_substitute_id(data[7])
# 			substitutes.append(substitute)
# 		return substitutes
# 		#select


# 	def update(self):
# 		pass
# 		#alter

	
# 	def deleteOne(self):
# 		req = ("DELETE FROM substitutes WHERE ")
# 		# TODO :
# 		# Make a request to insert substitute in subtitute table for database

class Substitute(c.Database):

	"""Send alt product to the controller"""

	def __init__(self, product = None, substitute = None):
		super().__init__()
		self.product = product
		self.substitute = substitute

	def save(self, product_id, substitute_id):
		# enregistrement du substitute
		# self.product.id
		# self.substitute.id
		req = ("INSERT INTO substitutes (product_id, substitute_id) VALUES (%s,%s)")
		features = (product_id, substitute_id)
		self.cursor.execute(req, features)
		self.cnx.commit()
		

	# @staticmethod
	def readAll(self):
		# récupération de tous les substitutes
		req = "SELECT * FROM substitutes"
		self.cursor.execute(req)
		datas = self.cursor.fetchall()
		substitutes = []

		for idx, data in enumerate(datas):
			product = p.Product()
			product = product.readOne(data[0])
			product_2 = p.Product()
			product_2 = product_2.readOne(data[1])
			new_substitute = Substitute(product, product_2)
			substitutes.append(new_substitute)
		
		return substitutes

	def deleteAll(self):
		req = ("DELETE FROM substitutes")
		self.cursor.execute(req)
		self.cnx.commit()
		

# # récupération des substituts
# ma_variable_tableau_de_substituts = Substitute.all(