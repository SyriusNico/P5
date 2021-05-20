# coding: utf-8
import mysql.connector
import Config.settings as s


class Database():

	def __init__(self):

		self._cnx = mysql.connector.connect(**s.SETTINGS)
		self._cursor = self.cnx.cursor(buffered=True)

	@property
	def cnx(self):
		""" connect to database """
		return self._cnx

	@property
	def cursor(self):
		"""
		allow python code to execute Mysql command in a database 
		"""
		return self._cursor
