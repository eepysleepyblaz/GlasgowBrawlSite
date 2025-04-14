from django.db import models

class Deck(models.Model):
    name = models.CharField(max_length=100, null=False)
    event_date = models.DateField(null=False)

    place = models.IntegerField(null=False)

    player = models.CharField(max_length=101, null=False)

    # Use \n as the delimiter to split the deck list
    # Put the number of commanders as the first entry (include partners)
    # Then have the commanders and partners next
    deck_list = models.CharField(max_length=99999, null=False)

    def __str__(self):
        return self.name