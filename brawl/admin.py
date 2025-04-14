from django.contrib import admin
from brawl.models import Deck


class DeckAdmin(admin.ModelAdmin):
    list_display = ('name', 'event_date', 'player', 'place', 'deck_list')

admin.site.register(Deck, DeckAdmin)
