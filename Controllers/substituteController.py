# coding : utf-8
import sys
sys.path.append('C:\\Users\\Utilisateur\\Documents\\ExerciceOC\\Pur_Beurre')
import Models.substitute as s
import Views.substituteView as sv

class SubstituteController():

	def __init__(self):
		self.substitute = s.Substitute()

	def compare(self, productToCompare, product_list):

		print("\nVous pouvez remplacer ce produit par : ")
		for product in product_list:	
			if product.nutrition_grade != productToCompare.nutrition_grade :
				if product.nutrition_grade == 'a':
					print(product.product_name, product.nutrition_grade)
				if product.nutrition_grade == 'b':
					print(product.product_name, product.nutrition_grade)
			# else:
			# 	print("Aucun produit n'a de meilleur qualité nutritionnelle")

