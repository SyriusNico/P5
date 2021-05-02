# coding : utf-8

class CategoryView:

	def show_categories(self, datas):
		print("\n*****************************************")
		print("****          CATEGORIES             ****")
		print("*****************************************\n")
		for item in datas:
			print(item.id_category,item.name)