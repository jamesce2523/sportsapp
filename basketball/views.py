# Create your views here.

from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404
from basketball.models import Team, Player


def home(request):
	male_teams = Team.objects.filter(gender='m')
	female_teams = Team.objects.filter(gender='f')
	return render(request, "basketball/home.html", {
		'male_teams': male_teams,
		'female_teams': female_teams
	})

def team(request, pk):
	team = get_object_or_404(Team, id=pk)
	players = team.players.all()
	return render(request, "basketball/team.html", {
		'team': team, 
		'players':players
	})

def player(request, pk):
	player = get_object_or_404(Player, id=pk)
	return render(request, "basketball/player.html", {'player':player})