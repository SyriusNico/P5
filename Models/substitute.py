# coding : utf-8
import sys
sys.path.append('C:\\Users\\Utilisateur\\Documents\\ExerciceOC\\Pur_Beurre')
import Models.product as p

class Substitute(p.Product):

	"""Send alt product to the controller"""

	def __init__(self):
		super().__init__()
		# useless attributes
		self.product_id = None
		self.substitute_id = None

	def set_product_id(self, product_id):
		self.product_id = product_id

	def set_substitute_id(self, substitute_id):
		self.substitute_id = substitute_id


		# useless function i have to rework them
	def create(self, product, substitute):

		req = ("INSERT INTO substitutes (product_id, substitute_id) VALUES (%s,%s)")
		features = (product.id, substitute.id)
		self.cursor.execute(req, features)
		self.cnx.commit()

	def readSubList(self):
		# req = ("SELECT * FROM products  JOIN substitutes ON products.id = substitutes.product_id AND products.id = substitutes.substitute_id")
		# req = ("SELECT product_id, substitute_id,  product_name FROM substitutes JOIN products ON substitutes.product_id = products.id AND substitutes.product_name = products.product_name")
		req = ("SELECT * \
  		FROM products \
  		INNER JOIN substitutes ON products.id = substitutes.substitute_id")
		self.cursor.execute(req)
		datas = self.cursor.fetchall()
		substitutes = []
		for data in datas:
			substitute = Substitute()
			substitute.set_name(data[1])
			substitute.set_nutrition_grade(data[3])
			substitute.set_product_id(data[6])
			substitute.set_substitute_id(data[7])
			substitutes.append(substitute)
		return substitutes
		#select

	def update(self):
		req = ()
		#alter

	def delete(self):
		pass
		#drop

	def save(self, product):
		self.save_list.append(product)

		# TODO :
		# Make a request to insert substitute in subtitute table for database

