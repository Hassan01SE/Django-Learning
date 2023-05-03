from django.shortcuts import render

# Create your views here.

from django.http import HttpResponse

def drinks(request,drink_name):

    drink ={
        'mocha': 'type of coffee',
        'tea': 'type of beverage',      
        'lemonade':'type of refreshment',
    }

    if drink_name not in drink:
         choice_of_drink = "We have no description for it currently!"

    else:
        choice_of_drink = drink[drink_name]

    

    return HttpResponse(f"<h2> {drink_name} </h2>" + choice_of_drink)
