from brawl.models import Deck
from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.urls import reverse
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.views import View
from django.utils.decorators import method_decorator
import datetime

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

def events(request):
    events_dates_final = []
    events_dates = Deck.objects.order_by('event_date').values_list('event_date').distinct()
    for i in range(len(events_dates)):
        events_dates_final.append(str(events_dates[i][0].strftime('%d-%m-%Y')))
    context_dict = {}
    context_dict['event_dates'] = events_dates_final
    

    return render(request, 'brawl/events.html', context=context_dict)

def show_event(request, event_date):

    event_date = datetime.datetime.strptime(event_date, '%d-%m-%Y').date()

    context_dict = {}
    context_dict['date'] = event_date

    decks = Deck.objects.filter(event_date=event_date)
    return_decks = []
    for deck in decks:
        player = deck.player
        name = deck.name
        place = deck.place
        wins = deck.wins
        loses = deck.loses
        deck = deck.deck_list.split("£")
        commander_count = int(deck.pop(0))
        commander1 = " ".join(deck.pop(0).split(" ")[1:])
        commander1imagename = "+".join(commander1.split(" "))
        if commander_count == 2:
            commander2 = " ".join(deck.pop(0).split(" ")[1:])
            commander2imagename = "+".join(commander2.split(" "))
        else:
            commander2 = None
            commander2imagename = None

        deck_cards = []        
        for card in deck:
            deck_cards.append({'name': " ".join(card.split(" ")[1:]), 'imgname': "+".join(card.split(" ")[1:]), 'quantity': int(card.split(" ")[0])})
        return_decks.append({'name': name, 'player': player, 'wins': wins, 'loses': loses, 'place': place, 'commander1': commander1, 'commander2': commander2,
                              'cards': deck_cards, 'commander1imgname': commander1imagename, 'commander2imgname': commander2imagename})

    context_dict['decks'] = return_decks

    return render(request, 'brawl/show_event.html', context=context_dict)

class ValidateDecklistView(View):
    def get(self, request):
        try:
            decklist = request.GET['deck']

            if decklist == "":
                return

            decklist = decklist.split("\n")
            with open('static/txt/Banlist.txt', "r") as f:
                    values = f.read()
                    values = values.split("\n")
                    
                    values = set(values)
                    values = list(values)

                    values.sort()
                    banlist = values

            error_string = ""
            deck_size = 0
            for card in decklist:
                if card == "":
                    continue
                
                card = card.split("(")[0][:-1]
                card_quantity = int(card.split(" ")[0])
                deck_size += card_quantity
                card_name = " ".join(card.split(" ")[1:])

                if card_quantity > 1:
                    if card_name not in ["Mountain", "Island", "Plains", "Swamp", "Forest"]:
                        error_string = error_string + f"Too many copies of {card_name}.\n"

                if card_name in banlist:
                    error_string = error_string + f"{card_name} is banned.\n"
            
            if error_string == "":
                return HttpResponse("Decklist valid")
            else:
                return HttpResponse("Deck list not valid as:\n" + error_string)
        except:
            return HttpResponse("Something went wrong.")
