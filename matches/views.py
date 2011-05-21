from django.shortcuts import render,get_object_or_404
from matches.models import *

def index(request):
    matches = Match.objects.order_by('card__date')
    return render(request,'matches/index.html',locals())

def match_details(request,match_id):
    match = get_object_or_404(Match,pk=match_id)
    return render(request,'matches/match_details.html',locals())
