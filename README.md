[![ForTheBadge built-by-developers](http://ForTheBadge.com/images/badges/built-by-developers.svg)](https://GitHub.com/SyriusNico/)


# PROJECT 5 - FOOD APP

## DESCRIPTION

### architecture 

```
[x] - Database/
[x] ---- script.sql (script de création de la DB)
[x] ---- database.py (fichier qui gère la création des curseurs et envoie des requêtes)
[x] - Models/ (fichiers qui vont être créés à partir des données de la BDD)
[x] ---- Product.py
[x] ---- Category.py
[O] ---- Substitute.py
[x] - Config/
[x] ---- db_config.py (fichier de config des infos de la BDD)
[x] ---- settings.py (ton fichier actuel de config)
[x] - Api/
[x] ---- off.py (classe qui gère les requêtes d'OFF)
[x] - App/
[x] ---- main.py (point d'entrée de ton programme)
[x] - Controllers/
[x] ---- ProductController.py (gère le code métier des produits = requete BDD + traitements)
[O] ---- CategoryController.py (input)
[O] ---- SubstituteController.py (input la recup se fait par le controller)
[x] - Views/
[x] ---- ProductView.py (gère l'affichage des informations des produits)
[x] ---- CategoryView.py
[O] ---- SubstituteView.py
[x] ---- MenuView.py
```

## PROJECT'S UTILITY

## WHERE DOES IT START ?