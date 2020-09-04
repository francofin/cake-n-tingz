from django.shortcuts import render
from pages.models import Team
from foods.models import Food
# Create your views here.

def index(request):
    featured_foods = Food.objects.order_by('-created_date').filter(is_featured=True)
    all_food = Food.objects.order_by('-created_date').filter(is_for_home_page=True)
    data = {
        'featured_foods':featured_foods,
        'all_food':all_food,
    }

    return render(request, 'pages/index.html', data)

def about(request):
    teams = Team.objects.all()
    data = {
        'teams': teams,
    }
    return render(request, 'pages/about.html', data)
