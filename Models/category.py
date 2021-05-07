# coding : utf-8
import Database.database as d
import sys
sys.path.append('C:\\Users\\Utilisateur\\Documents\\ExerciceOC\\Pur_Beurre')


class Category(d.Database):

	"""Send category data to the controller"""

	def __init__(self, id_category=None, name=None):
		super().__init__()
		self.id_category = id_category
		self.name = name

	def set_id_category(self, _id):
		self.id_category = _id

	def set_name(self, name):
		self.name = name

	def create(self):
		if self._can_be_created():
			req = (
				"INSERT INTO categories (name) VALUES ('{}')".format(self.name)
			)
			self.cursor.execute(req)
			self.cnx.commit()
		else:
			print(
				"le nom", self.name, "n'est pas renseigné",
				self.name, "n'est pas enregistré en BDD"
			)

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
		# ici créer un objet et le renvoyer
		for data in datas:
			cat = Category()
			cat.set_id_category(data[0])
			cat.set_name(data[1])
			categories.append(cat)
		return categories
