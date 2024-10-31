from django.contrib import admin
from .models import Player, Competition, Satay, Rating, PlayerCompetition

admin.site.register(Player)
admin.site.register(Competition)
admin.site.register(Satay)
admin.site.register(Rating)
admin.site.register(PlayerCompetition)