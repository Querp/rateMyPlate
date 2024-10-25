from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader
from django.conf import settings
from django.contrib.auth import get_user_model
from django.shortcuts import get_object_or_404, render
from django.urls import reverse

from .models import Player, Competition, Satay, Rating



def index(request):
    User = get_user_model()
    user_list = User.objects.all()
    player_list = Player.objects.all()
    competition_list = Competition.objects.all()
    satay_list = Satay.objects.all()
    rating_list = Rating.objects.all()
    
    context = {
        "user_list": user_list,
        "player_list": player_list,
        "competition_list": competition_list,
        "satay_list": satay_list,
        "rating_list": rating_list,
    }
    return render(request, "competition/index.html", context)

def competition(request, pk):
    competition_selection = get_object_or_404(Competition, pk=pk)
    competition_list = Competition.objects.all()
    context = {"competition_selection": competition_selection,
               "competition_list": competition_list,          
    }
    return render(request, "competition/competition-detail.html", context)
    # return HttpResponse(response % competition_id)
    
    
def post_form(request, competition_id):
    competition_list = Competition.objects.all()
    for i in range(len(competition_list)):
        try:
            new_name = request.POST[f"competition_{i+1}"]
            competition_list[i].name = new_name
            competition_list[i].save()
        except:
            raise ValueError('NOO')
   
    return HttpResponseRedirect(reverse("competition", args=(competition_id,)))