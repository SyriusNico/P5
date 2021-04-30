# coding : utf-8
import sys
sys.path.append('C:\\Users\\Utilisateur\\Documents\\ExerciceOC\\Pur_Beurre')
import Controllers.categoryController as c


class CategoryView:

	def show_categories(self, datas):
		print("\n*****************************************")
		print("****          CATEGORIES             ****")
		print("*****************************************\n")
		for item in datas:
			print(item.id_category,item.name)