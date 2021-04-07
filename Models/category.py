# coding : utf-8
import sys
sys.path.append('C:\\Users\\Utilisateur\\Documents\\ExerciceOC\\Pur_Beurre')
import Database.database as d

class Category(d.Database):

	"""Send category data to the controller"""

	def __init__(self, id_category = None, name = None):
		super().__init__()
		self.id_category = id_category
		self.name = name

	def create(self):
		if self._can_be_created():
			req =("INSERT INTO categories (name) VALUES ('{}')".format(self.name)
				)
			self.cursor.execute(req)
			self.cnx.commit()
		else:
			print("le nom du produit n'est pas renseigné, le produit n'est pas enregistré en BDD")
		
	def _can_be_created(self):
		if self.name is None:
			return False
		return True

	def read(self):
		req = "SELECT * FROM categories"
		self.cursor.execute(req)
		self.cnx.commit()
		# fetchall a faire dans le model
		datas = self.cursor.fetchall()
		categories = []
		for data in datas:
			categories.append(data)
		return categories

	def update(self):
		pass

	def delete(self):
		pass