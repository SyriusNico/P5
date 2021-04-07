# coding: utf-8
import sys
sys.path.append('C:/Users/Utilisateur/Documents/ExerciceOC/Pur_Beurre')

# Mettre un commentaire qui explique comment trouver les catégories
# quelles sont les valeurs par défaut
# + infos nécessaires
CATEGORIES = [
	'surgeles',
	'viandes', 
	'sauces', 
	'fromages', 
	'legumineuses'
]


# The number of products scan in the query
NUMBER_PRODUCT = 50

# Request parameters

URL = 'https://fr.openfoodfacts.org/cgi/search.pl'
