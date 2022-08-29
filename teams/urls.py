from django.urls import path
from . import views

urlpatterns = [
    path('my-teams/', views.MyTeams, name='my_teams'),
    path('add-team-to-my-league/', views.addTeamToMyLeague, name='add_team_to_my_league'),
    path('add-player-to-team/<id_league>/', views.addPlayerToTeam, name='add_player_to_team'),
    path('manage-teams/<int:pk>/', views.ManageTeams, name='manage_teams'),
    path('ajax/load-player/', views.LoadPlayer, name="load_player"),
    path('delete-player-from-team/<pk>/', views.deletePlayerFromTeam, name='delete_player_from_team'),
    path('detailed-team/<int:pk>/', views.DetailedTeam, name='detailed_team')
]