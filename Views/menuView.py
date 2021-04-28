# coding : utf-8
import sys
sys.path.append('C:\\Users\\Utilisateur\\Documents\\ExerciceOC\\Pur_Beurre')
import Config.settings as s
import Views.productView as p

class MenuView:

	def screen(self):
		print(" __________________________________________________")
		print("|                                                  |")
		print("|           BIENVENUE SUR PUR BEURRE               |")
		print("|                   ****                           |")
		print("|                                                  |")
		print("|                 * MENU *                         |")
		print("|                                                  |")
		print("|  1. Aliment à remplacer                          |")
		print("|                                                  |")
		print("|  2. Retrouver mes aliments substitués            |")
		print("|                                                  |")
		print("|  3. Quitter l'application                        |")
		print("|__________________________________________________|")

	def substituteScreen(self):
		print(" __________________________________________________")
		print("|                                                    |")
		print("|                 * MENU *                           |")
		print("|                                                    |")
		print("|  1. Sélectionner un produit                        |")
		print("|                                                    |")
		print("|  2. Effacer tous les éléments (Choix irréversible) |")
		print("|                                                    |")
		print("|  3. Retour                                         |")
		print("|____________________________________________________|")

	def bye(self):
		print( """   ##     ##  ##            #####    ######   ##  ##    ####     ####    #####
  ####    ##  ##            ##  ##   ##       ##  ##   ##  ##     ##     ##  ##
 ##  ##   ##  ##            ##  ##   ##       ##  ##   ##  ##     ##     ##  ##
 ######   ##  ##            #####    ####     ##  ##   ##  ##     ##     #####
 ##  ##   ##  ##            ####     ##       ##  ##   ##  ##     ##     ####
 ##  ##   ##  ##            ## ##    ##         ###    ##  ##     ##     ## ##
 ##  ##    ####             ##  ##   ######     ##      ####     ####    ##  ##""")
