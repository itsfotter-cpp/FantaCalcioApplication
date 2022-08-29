from django.db.models.query_utils import Q
from leagues.models import Leagues
from django.shortcuts import get_object_or_404, render
from django.urls import reverse
from django.http import HttpResponseRedirect, HttpResponseBadRequest
from .models import Leagues
from teams.models import Players, Teams, Quotazioni
from core.models import Coach
from django.contrib.auth.models import User
from django.contrib.auth.hashers import make_password, check_password

# Create your views here.
def CreateNewLeague(request):
    if request.method == 'POST':
        league = Leagues.objects.filter(leaguename=request.POST.get('league_name'), password=make_password(request.POST.get('password_league'))).count()
        if league == 1:
            status = "Esiste già una lega con questo nome!"
            context = {"status": status}
            return render(request, 'leagues/CreateLeague.html', context)
        else:
            league = Leagues.objects.create(
                        leaguename = request.POST.get('league_name'),
                        teamnumber = request.POST.get('number_partecipants'),
                        password = make_password(request.POST.get('password_league')),
                        crediti = request.POST.get('credits'),
                        id_auth_user = User.objects.get(id=request.user.pk)
                    )
            
            coach = Coach.objects.create(
                        id_auth_user = User.objects.get(id=request.user.pk),
                        id_league = Leagues.objects.get(idleague=league.pk),
                        rank = "Admin"
                )
            
            if request.POST.get('team_name'):
                team = Teams.objects.create(
                            teamname = request.POST.get('team_name'),
                            firstfantacoach = request.POST.get('coach_name'),
                            crediti = request.POST.get('credits'),
                            id_league = Leagues.objects.get(idleague=league.pk)
                        )
                coach.id_team = team.pk
                coach.save(update_fields=['id_team'])
                

            url_return = reverse("homepage")
            return HttpResponseRedirect(url_return)

    else:
        return render(request, 'leagues/CreateLeague.html')

def JoinLeague(request):
    if request.method == 'POST':
        league = Leagues.objects.get(leaguename=request.POST.get('league_name'))

        if league is None:
            status = "Non esiste nessuna lega con queste credenziali"
            context = {"status": status}
            return render(request, 'leagues/JoinLeague.html', context)

        elif request.user.pk == league.id_auth_user.pk:
            status = "Non ti puoi unire ad una lega di cui sei proprietario"
            context = {"status": status}
            return render(request, 'leagues/JoinLeague.html', context)
        
        elif Teams.objects.filter(Q(firstfantacoach=request.user.username) | Q(secondfantacoach=request.user.username), id_league=league.pk).count() > 0:
            status = "Hai già iscritto una squadra a questa Lega"
            context = {"status": status}
            return render(request, 'leagues/JoinLeague.html', context)

        else:
            if check_password(request.POST.get('password_league'), league.password):

                context = {"league": league}

                return render(request, 'leagues/JoinLeagueCreateTeam.html', context)

            else:
                status = "Non esiste nessuna lega con queste credenziali"
                context = {"status": status}
                return render(request, 'leagues/JoinLeague.html', context)
               
    else:
        return render(request, 'leagues/JoinLeague.html')

def CreateTeamForLeague(request):
    if request.method == 'POST':
        league = get_object_or_404(Leagues, pk=request.POST.get('league_pk'))
    
        team = Teams.objects.create(
                teamname = request.POST.get('team_name'),
                firstfantacoach = request.POST.get('coach_name'),
                crediti = league.crediti,
                id_league = Leagues.objects.get(idleague=league.pk)
            )

        coach = Coach.objects.create(
                    id_auth_user = User.objects.get(id=request.user.pk),
                    rank = "User",
                    id_team = Teams.objects.get(idteam=team.pk),
                    id_league = Leagues.objects.get(idleague=league.pk)
                )
        
        league.iscritti = str(int(league.iscritti) + 1)
        league.save(update_fields=["iscritti"])
        
        url_return = reverse("homepage")
        return HttpResponseRedirect(url_return)
    
    else:
        HttpResponseBadRequest()

def DetailedLeague(request, pk):
    teams = Teams.objects.filter(id_league=pk)
    context = {'teams': teams}

    return render(request, 'leagues/DetailedLeague.html', context)

def MyLeagues(request):
    teams = Teams.objects.filter(firstfantacoach=request.user.username)

    context = {'teams': teams}

    return render(request, 'leagues/MyLeagues.html', context)
