from random import randint

from django.shortcuts import render
import requests
from django.http import HttpResponse
from .models import Capital
from .forms import QuizForm

# a function to get country and capital from the API and add to the DB
def updateDB():
    response = requests.get('https://countriesnow.space/api/v0.1/countries/capital')
    response_data = response.json()
    print(response_data["data"])
    capital_data = list(response_data["data"])
    for id in range(len(capital_data)):
        country = capital_data[id]['name']
        capital = capital_data[id]['capital']
        capital_model = Capital(country=country, capital=capital, id= id+1)
        capital_model.save()
        print("Added " + str(country) + " " + str(capital) + " " + str(id+1))

def quiz(request):
    if request.method == "POST":
        form = QuizForm(request.POST)
        print("form-" + str(form))
        if form.is_valid():
            print("valid")
            user_data = form.cleaned_data
            capital_ref = Capital.objects.get(country=user_data.get('country_hidden'))
            if str(user_data.get('capital')).lower() == str(capital_ref.capital).lower():
                return render(request, "quiz/correct.html", {'capital_ref': capital_ref})
            else:
                return render(request, "quiz/wrong.html" , {'capital_ref': capital_ref})
        else:
            print("not valid")
            print(form.errors)
            return render(request, "quiz/wrong.html")
    else:
        max_number = Capital.objects.count()
        print(max_number)
        number = randint(1, max_number)
        print(number)
        #updateDB()
        country = Capital.objects.get(id=number).country
        form = QuizForm(initial={'country': country,
                                 'country_hidden':country})
        form.fields['country_hidden'].widget = form.fields['country_hidden'].hidden_widget()
        print(Capital.objects.get(id=number).capital)
        return render(request, "quiz/quiz.html", {"form" : form})


