# coding : utf-8
import sys
sys.path.append('C:\\Users\\Utilisateur\\Documents\\ExerciceOC\\Pur_Beurre')
import Controllers.controller as c
import Models.category as ca
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
"""
- généralités :
ok virer les "sys.path.append" si non utilisé
ok vérifier les imports (virer ceux en trop)
ok se servir de "config.py" pour les constantes modifiables par l'utilisateur.
Mettre les autres dans "settings.py"
- attention à ne faire QUE de l'affichage dans les views, ce sont les controller 
qui récupère les infos en BDD, puis les passent via des paramètres aux méthodes 
des vues pour affichage.
ok attention dans tes models, tu ne dois pas retourner les "datas" de tes 
requêtes SQL "en dur", mais bien retourner des OBJETS créés à partir de ces "datas".
- config.py :
- virer le import sys
- passer "config" en majuscule (CONSTANTE)
"""
if __name__ == '__main__':

	start = c.Controller()
	# cat = ca.Category()
	# cat.read()