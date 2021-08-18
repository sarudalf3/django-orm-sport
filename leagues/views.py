from django.shortcuts import render, redirect
from .models import League, Team, Player
from django.db.models import Q, Count
from . import team_maker

def index(request):
	context = {
		#"leagues": League.objects.all(),
		#"teams": Team.objects.all(),
		#"players": Player.objects.all(),
		"ans01": League.objects.filter(name__contains='baseball'),
		"ans02": League.objects.filter(name__contains='women'),
		"ans03": League.objects.filter(sport__contains='hockey'),
		"ans04": League.objects.exclude(sport__contains='football'),
		"ans05": League.objects.filter(name__contains='conference'),
		"ans06": League.objects.filter(name__contains='atlantic'),
		"ans07": Team.objects.filter(location='Dallas'),
		"ans08": Team.objects.filter(team_name__contains='Raptors'),
		"ans09": Team.objects.filter(location__contains='city'),
		"ans10": Team.objects.filter(team_name__startswith='T'),
		"ans11": Team.objects.order_by('location'),
		"ans12": Team.objects.order_by('-team_name'),
		"ans13": Player.objects.filter(last_name='Cooper'),
		"ans14": Player.objects.filter(first_name='Joshua'),
		"ans15": Player.objects.filter(last_name='Cooper').exclude(first_name="Joshua"),
		"ans16": Player.objects.filter(Q(first_name="Alexander") | Q(first_name="Wyatt")), ##first_name__in=["Alexander","Wyatt"]
	}
	return render(request, "leagues/index.html", context)

def make_data(request):
	team_maker.gen_leagues(10)
	team_maker.gen_teams(50)
	team_maker.gen_players(200)

	return redirect("index")

def advanced(request):
	context = {
		"ans01": Team.objects.filter(league__name='Atlantic Soccer Conference'),
		"ans02": Player.objects.filter(curr_team__team_name='Penguins', curr_team__location='Boston'),
		"ans03": Player.objects.filter(curr_team__league__name='International Collegiate Baseball Conference'),
		"ans04": Player.objects.filter(curr_team__league__name='American Conference of Amateur Football',last_name='Lopez'),
		"ans05": Player.objects.filter(curr_team__league__sport='Football'),
		"ans06": Team.objects.filter(curr_players__first_name='Sophia'),
		"ans07": League.objects.filter(teams__curr_players__first_name='Sophia'),
		"ans08": Player.objects.filter(last_name="Flores").exclude(curr_team__team_name="Roughriders",curr_team__location="Washington"),
		"ans09": Team.objects.filter(all_players__first_name="Samuel",all_players__last_name="Evans"),
		"ans10": Player.objects.filter(all_teams__team_name='Tiger-Cats', all_teams__location='Manitoba'),
		"ans11": Player.objects.filter(all_teams__team_name='Vikings', all_teams__location='Wichita').exclude(curr_team__team_name='Vikings', curr_team__location='Wichita'),
		"ans12": Team.objects.filter(all_players__first_name='Jacob', all_players__last_name='Gray').exclude(team_name='Colts', location='Oregon'),
		"ans13": Player.objects.filter(first_name="Joshua").filter(all_teams__league__name="Atlantic Federation of Amateur Baseball Players"),
		"ans14": Team.objects.annotate(num_players=Count('all_players')).filter(num_players__gte=12),#.order_by('num_players'),
		"ans15": Player.objects.annotate(num_teams=Count('all_teams')).order_by('-num_teams'),
}
	return render(request, "leagues/advanced.html", context)
