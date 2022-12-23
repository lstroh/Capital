# Capital
I implemented a capital city quiz.

I used the provided API: https://countriesnow.space/api/v0.1/countries/capital and added all the data into the capital table in Django.
The function to update DB based on the API is implemented in capital app views.py

Of course, we could use the API directly without storing the information in the DB, but since the data will not change, I prefer to add the data.

I used the latest Django version and requests packages.

pip install requests

pip install django

and to run the Django server I used pip install django.
