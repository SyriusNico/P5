[![ForTheBadge built-by-developers](http://ForTheBadge.com/images/badges/built-by-developers.svg)](https://GitHub.com/SyriusNico/)


# PROJECT 5 - FOOD APP

## DESCRIPTION
```
This program allow you to replace a product selected by another with better nutritional quality.
Products come from to the database of the open food fact website.
```
### architecture 

```
 - Database/
 ---- script.sql 
 ---- database.py 
 - Models/ 
 ---- Product.py
 ---- Category.py
 ---- Substitute.py
 - Config/
 ---- db_config.py 
 ---- settings.py
 - Api/
 ---- off.py 
 - App/
 ---- main.py 
 - Controllers/
 ---- ProductController.py 
 ---- CategoryController.py 
 ---- SubstituteController.py 
 - Views/
 ---- ProductView.py 
 ---- CategoryView.py
 ---- SubstituteView.py
 ---- MenuView.py
```

## PROJECT'S UTILITY
```
This project aims to allow you to eat more healty. 
For any suggestion you're welcome.
```
## HOW THIS WORKS ?
```
In the project folder run the file main.py and follow the instructions.
```
## PROGRAM INSTALLATION

**Requirements**
```
- Mysql
- python3
- requests
- mysql.connector
```
**Steps**
```
- Fork this repository to your Github account.
- Clone or download the project to a local folder.
```
## CONFIGURATION

**Configure your Database**
```
- Run the Mysql Command Line.
- Copy the Mysql script "myData.sql".
- Paste in the Mysql Command Line.
- Close the Client.
```
**Set up your food Database**
```
- In the Config folder write 5 categories in config file in the constant "CATEGORIES".
- Categories must correspond to the categories of the open food fact website.
- Enter the number of products to scan in the constant "NUMBER_PRODUCT".

```
**Initialize your Database**
```
- In the Controllers folder
- Go to the offController.py file
- At the end of the script, instantiate an object from the offController class example : 
	ObjectName = OffController()
- Use the class method "init_datas" example :
	ObjectName.init_datas()
- Run on your terminal : offController.py
```
## PROGRAM LAUNCH
```
- On your terminal run main.py file.
```