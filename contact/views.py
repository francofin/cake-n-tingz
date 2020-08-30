from django.shortcuts import render
from pages.models import Team

# Create your views here.
def contact(request):
    teams = Team.objects.all()
    data = {
        'teams': teams,
    }
    return render(request, 'pages/contact.html', data)
