# coding: utf-8
import sys
sys.path.append('C:\\Users\\Utilisateur\\Documents\\ExerciceOC\\Pur_Beurre')
import mysql.connector
import Config.config as cf

"""

NE FAIT QUE GÉRER LA CONNEXION A LA BDD

"""
class Database():

	def __init__(self):

		self._cnx = mysql.connector.connect(**cf.config)
		self._cursor = self.cnx.cursor(buffered=True)
	
	@property
	def cnx(self):
		return self._cnx
	
	@property
	def cursor(self):
		return self._cursor
