# recipes

RECIPES OF KICHEN

Installation:

1)Open this project into your pyCharm 
2)create a database named recipes (MySQl)
3)migrate your data "python manage.py makemigrations"
4)create your admin user with "createsuperuser"

details:

In this project we made a page containes faqs, contact us for more information ,  home in which you find a button to add a recipe but to do that you must be authentified .
In all those pages we have a fix header and a fix footer in base.html file , in every file we extends the file base.html to maintain the form of tha page:
Home
![image](https://user-images.githubusercontent.com/106548290/236649993-0d80f41b-29a4-4288-8764-09ab6eb83121.png)
Our team
![image](https://user-images.githubusercontent.com/106548290/236650024-e997d419-c45f-46c6-ae71-4e5dc50b9b7e.png)
FAQS:
![image](https://user-images.githubusercontent.com/106548290/236650050-99c9dbc2-2bda-4d19-9083-af78ffbb7ccb.png)
Contact us:
![image](https://user-images.githubusercontent.com/106548290/236650070-c670a45c-e3ec-48e2-9bfd-65049fe1cc21.png)

In models.py we create a class named recette contain titre,ingredients ,description ,date_creation ,auteur.
Then we create a class RecetteForm.
In the file views.py we made functions:
recette_list: to list all recipes
create_recette: to create recipes
update_recette: to update a recipe 
delete_recette: to delete a recipe
search: to find a recipe 

then we add urls associate to the name of definitions in views.py 

![image](https://user-images.githubusercontent.com/106548290/236649972-0130e00b-24be-4368-8b18-531f87b91334.png)

