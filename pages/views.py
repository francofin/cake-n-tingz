from django.shortcuts import render
from pages.models import Team
# Create your views here.

def index(request):

    return render(request, 'pages/index.html')

def about(request):
    teams = Team.objects.all()
    data = {
        'teams': teams,
    }
    return render(request, 'pages/about.html', data)
