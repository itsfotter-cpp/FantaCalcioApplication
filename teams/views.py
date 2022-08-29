from django.db.models.query_utils import Q
from django.http.response import HttpResponseBadRequest, HttpResponseRedirect
from django.shortcuts import get_object_or_404, redirect, render
from .models import Players, Teams, Quotazioni
from leagues.models import Leagues
from django.urls import reverse
from django.contrib import messages

# Create your views here.

def MyTeams(request):

    team = Teams.objects.filter(Q(firstfantacoach=request.user.username) | Q(secondfantacoach=request.user.username))
    lista_team = []
    #controllo per evitare che lo stesso admin crei per più volte un team per una stessa lega
    for t in team:
        lista_team.append(t.id_league.pk)
    league = Leagues.objects.filter(id_auth_user=request.user.pk).exclude(pk__in=lista_team)

    context = {'team': team, 'league': league}
    
    return render(request, 'teams/MyTeams.html', context)

def addTeamToMyLeague(request):
    if request.method == "POST":

        league = get_object_or_404(Leagues, pk=request.POST.get("league"))

        Teams.objects.create(
            teamname = request.POST.get("team_name"),
            firstfantacoach = request.user.username,
            crediti = league.crediti,
            id_league = Leagues.objects.get(idleague=league.pk)
        )

        league.iscritti = str(int(league.iscritti)+1)
        league.save(update_fields=["iscritti"])

        url_return = reverse("my_teams")
        return HttpResponseRedirect(url_return)
    
    else:
        return HttpResponseBadRequest()

def ManageTeams(request, pk):
    league = get_object_or_404(Leagues, pk=pk)

    teams = Teams.objects.filter(id_league=pk)

    players = Players.objects.filter(id_team__id_league=pk).order_by("-idplayer")

    context = {"league": league, "teams": teams, "players": players}

    return render(request, 'teams/ManageTeam.html', context)

def LoadPlayer(request):
    quotazioni_players = Quotazioni.objects.filter(nome__icontains=request.GET.get("player"), ruolo=request.GET.get("ruolo")).values("nome", "ruolo")

    context = {"quotazioni_players": quotazioni_players}

    return render(request, 'ajax/Playerlist.html', context)

def addPlayerToTeam(request, id_league):
    
    if request.method == "POST":

        if Players.objects.filter(nome=request.POST.get("player_name"), id_team__id_league=id_league).count() > 0:
            messages.add_message(request, messages.ERROR, "Questo giocatore è già stato inserito per questa lega")

            url_return = reverse("manage_teams", kwargs={"pk": id_league})
            return HttpResponseRedirect(url_return)
        
        else:
            Players.objects.create(
                ruolo = request.POST.get("ruolo"),
                nome = request.POST.get("player_name"),
                costo = request.POST.get("player_cost"),
                id_team = Teams.objects.get(teamname=request.POST.get("fanta_team"), id_league=id_league)
            )

            team = Teams.objects.get(teamname=request.POST.get("fanta_team"), id_league=id_league)
            team.crediti = str(int(team.crediti)-int(request.POST.get("player_cost")))
            team.save(update_fields=["crediti"])

            url_return = reverse("manage_teams", kwargs={"pk": id_league})
            return HttpResponseRedirect(url_return)
    
    else:
        return HttpResponseBadRequest()

def deletePlayerFromTeam(request, pk):
    
    if request.method == "POST":
        player = Players.objects.get(pk=pk)
        id_league = player.id_team.id_league.idleague
        team = Teams.objects.get(idteam=player.id_team.idteam)
        team.crediti = str(int(team.crediti) + int(player.costo))
        team.save(update_fields=["crediti"])
        player.delete()
        url_return = reverse("manage_teams", kwargs={"pk": id_league})
        return HttpResponseRedirect(url_return)
    
    else:
        return HttpResponseBadRequest()

def DetailedTeam(request, pk):
    
    team = get_object_or_404(Teams, pk=pk) 
    players = Players.objects.filter(id_team=pk)
    context = {"team": team, "players": players}

    return render(request, 'teams/DetailedTeam.html', context)
    