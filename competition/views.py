from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader
from django.conf import settings
from django.contrib.auth import get_user_model, logout
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required, permission_required
from django.contrib import messages
from django.shortcuts import get_object_or_404, render, redirect
from django.urls import reverse
from django import forms
from .models import Player, Competition, PlayerCompetition, Satay, Rating
from . import forms


# def admin(request):
#     return redirect('admin')

@login_required
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

# @permission_required("competition.view_competition")
@login_required
def competition_detail(request, pk):
    competition_selection = get_object_or_404(Competition, pk=pk)
    competition_list = Competition.objects.all()
    context = {"competition_selection": competition_selection,
               "competition_list": competition_list,          
    }
    return render(request, "competition/competition_detail.html", context)
    # return HttpResponse(response % competition_id)
    
# change competition names
# @permission_required("competition.change_competition")
@login_required  
def post_form(request, competition_id): 
    competition_list = Competition.objects.all()
    changed_names = 0
    for i in range(len(competition_list)):
        try:
            # new_name = request.POST[f"competition_{i+1}"].strip()
            new_name = request.POST.get(f"competition_{i+1}", "").strip()
            old_name = competition_list[i].name
            if new_name != old_name:
                changed_names += 1
                competition_list[i].name = new_name
                competition_list[i].save()
                messages.success(request, f"'{old_name}' is gewijzigd naar '{new_name}'")
        except:
            raise ValueError('failed to change competition names')
    if changed_names == 0:
        messages.error(request, "Geen wijzigingen gevonden")
    else:
        naam_or_namen = 'naam' if changed_names == 1 else 'namen'
        messages.info(request, f"{changed_names} {naam_or_namen} gewijzigd.")
    return HttpResponseRedirect(reverse("competition", args=(competition_id,)))

@login_required
def database(request):
    num_visits = request.session.get('num_visits', 0)
    num_visits += 1
    request.session['num_visits'] = num_visits
    
    User = get_user_model()
    user_list = User.objects.all()
    player_list = Player.objects.all()
    competition_list = Competition.objects.all()
    player_competition_list = PlayerCompetition.objects.all()
    satay_list = Satay.objects.all()
    rating_list = Rating.objects.all()
    
    context = {
        "user_list": user_list,
        "player_list": player_list,
        "competition_list": competition_list,
        "player_competition_list": player_competition_list,
        "satay_list": satay_list,
        "rating_list": rating_list,
        "num_visits": num_visits,
    }
    return render(request, "competition/db.html", context)

# def custom_login(request):
#     return render(request, 'registration/login.html')

def custom_logout(request):
    messages.success(request, f"Tot ziens {request.user.username}!")
    logout(request)
    return render(request, 'registration/logged_out.html')

def new_competition(request):
    form = forms.CreateCompetition()    
    if request.method == 'POST':
        form = forms.CreateCompetition(request.POST)
        if form.is_valid():
            newpost = form.save(commit=False)
            newpost.organiser = Player.objects.get(user=request.user)
            newpost.save()
            total_competitions = len(Competition.objects.all())
            messages.success(request, f"Nieuwe competitie toegevoegd: {newpost.name}.")
            messages.info(request, f"Organisator: {newpost.organiser}.")
            messages.info(request, f"Dit is de {total_competitions}e competitie.")
            messages.warning(request, f"Geen waarschuwingen.")
            messages.error(request, f"Geen errors.")
            return redirect('database')  
    else:
        form = forms.CreateCompetition()    # empty form for GET request
    context = {'form': form}
    return render(request, 'competition/competition_new.html', context)

def register(request):
    # create_player
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            new_user = form.save()
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password1') 
            messages.success(request, f"Gebruiker '{username}', wachtwoord '{password}' is geregistreerd!")
            add_player(new_user)
            return redirect("../accounts/login/")
        else:
            messages.error(request, f"Ongeldig fomulier!")
    else:
        form = UserCreationForm()
        messages.info(request, f"Vul het formulier in.")
    return render(request, 'registration/register.html', {'form': form})
    
def add_player(new_user):
    Player.objects.create(user=new_user, name=new_user.username)




    
def edit_player(request):
    pass

def edit_competition(request):
    pass

def delete_competition(request):
    pass

def rate_satay(request):
    pass

def edit_rating(request):
    pass

def request_to_join_competition(request):
    pass

def join_competition(request):
    # add_satay
    pass
