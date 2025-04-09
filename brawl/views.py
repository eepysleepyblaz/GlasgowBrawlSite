from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.urls import reverse
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.views import View
from django.utils.decorators import method_decorator

def home(request):
    context_dict = {}

    with open('static/txt/Banlist.txt', "r") as f:
        values = f.read()
        values = values.split("\n")
        
        values = set(values)
        values = list(values)

        values.sort()
        

        cards_dict = {}

        for i in range(len(values)):
            formatted = "+".join(values[i].split(" "))
            cards_dict[values[i]] = "https://api.scryfall.com/cards/named?exact={formatted}&format=image"

    with open('static/txt/BanlistAsCommander.txt', "r") as f:
        values2 = f.read()
        values2 = values2.split("\n")
        
        values2 = set(values2)
        values2 = list(values2)

        values.sort()
    
        for i in range(len(values2)):
            formatted = "+".join(values[i].split(" "))
            cards_dict[values[i]] = "https://api.scryfall.com/cards/named?exact={formatted}&format=image"
        
    context_dict['Cards'] = values
    context_dict['Commanders'] = values2
    context_dict['Images'] = cards_dict
    return render(request, 'brawl/home.html', context=context_dict)

class ValidateDecklistView(View):
    def get(self, request):

            decklist = request.GET['decklist']

            with open('static/txt/Banlist.txt', "r") as f:
                    values = f.read()
                    values = values.split("\n")
                    
                    values = set(values)
                    values = list(values)

                    values.sort()
                    banlist = values

            error_string = ""
            for card in decklist:
                card = card.split("(")[0][:-1]
                card_quantity = card.split(" ")[0]
                card_name = card.split(" ")[1:]

                if card_quantity > 1:
                    if card_name not in ["Mountain", "Island", "Plains", "Swamp", "Forest"]:
                        error_string = error_string + f"Too many copies of {card_name}.\n"

                if card_name in banlist:
                    error_string = error_string + f"{card_name} is banned.\n"
            
            if error_string == "":
                return HttpResponse("Nothing wrong with this deck list")
            else:
                return HttpResponse("Deck list not valid as:\n" + error_string)

