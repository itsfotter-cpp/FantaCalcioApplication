from django.urls import path
from . import views

urlpatterns = [
    path('create-league/', views.CreateNewLeague, name='create_new_league'),
    path('join-a-league/', views.JoinLeague, name='join_a_league'),
    path('create-a-team-for-league/', views.CreateTeamForLeague, name='create_team_for_league'),
    path('detailed-league/<int:pk>/', views.DetailedLeague, name='detailed_league'),
    path('my-leagues/', views.MyLeagues, name='my_leagues'),
    
]