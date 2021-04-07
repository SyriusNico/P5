# coding : utf-8
import sys
sys.path.append('C:\\Users\\Utilisateur\\Documents\\ExerciceOC\\Pur_Beurre')
import Api.off as api
import Controllers.offController as o
import Controllers.categoryController as ctrl
import Views.menuView as m
"""
1 - Quel aliment souhaitez-vous remplacer ?
	L'utilisateur sélectionne 1. 
	Le programme pose les questions suivantes à l'utilisateur et ce dernier sélectionne les réponses :
	Sélectionnez la catégorie. [Plusieurs propositions associées à un chiffre. L'utilisateur entre le chiffre correspondant et appuie sur entrée]
	Sélectionnez l'aliment. [Plusieurs propositions associées à un chiffre. L'utilisateur entre le chiffre correspondant à l'aliment choisi et appuie sur entrée]
	Le programme propose un substitut, sa description, un magasin ou l'acheter (le cas échéant) et un lien vers la page d'Open Food Facts concernant cet aliment.
	L'utilisateur a alors la possibilité d'enregistrer le résultat dans la base de données.
2 - Retrouver mes aliments substitués.
"""

if __name__ == '__main__':

	start = m.MenuView()