from django.shortcuts import render
from pages.models import Team, Ashley
from foods.models import Food
from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator
# Create your views here.

def index(request):
    featured_foods = Food.objects.order_by('-created_date').filter(is_featured=True)
    all_food = Food.objects.order_by('-created_date').filter(is_for_home_page=True)
    sliders = Food.objects.order_by('-created_date').filter(is_for_slider=True)
    sliders2 = Food.objects.order_by('-created_date').filter(is_for_slider2=True)
    holiday_recipes = Food.objects.order_by('-created_date').filter(is_holiday_recipe=True)
    featured_posts = Food.objects.order_by('-created_date').filter(is_featured_for_home_page=True)
    home_page_side_article = Food.objects.order_by('-created_date').filter(is_for_home_page_side=True)
    ashley_info = Ashley.objects.all()
    data = {
        'featured_foods':featured_foods,
        'all_food':all_food,
        'slider_foods':sliders,
        'slide_food2':sliders2,
        'holiday_recipes':holiday_recipes,
        'featured_posts': featured_posts,
        'home_page_side_article':home_page_side_article,
        'ashley_info': ashley_info,
    }

    return render(request, 'pages/index.html', data)

def about(request):
    teams = Team.objects.all()
    ashley_info = Ashley.objects.all()
    data = {
        'teams': teams,
        'ashley_info': ashley_info,
    }
    return render(request, 'pages/about.html', data)

def for_kids(request):
    kid_meals = Food.objects.order_by('-created_date').filter(is_for_kids=True)
    paginator = Paginator(kid_meals, 6)
    page = request.GET.get('page')
    page_food = paginator.get_page(page)

    data = {
        'kids_meals':page_food,
    }

    return render(request, 'pages/kids_meals.html', data)

def desserts(request):
    sweet_treat = Food.objects.order_by('-created_date').filter(is_dessert=True)
    paginator = Paginator(sweet_treat, 6)
    page = request.GET.get('page')
    page_food = paginator.get_page(page)

    data = {
        'sweet_treat':page_food,
    }

    return render(request, 'pages/desserts.html', data)

def dinner_meals(request):
    dinner = Food.objects.order_by('-created_date').filter(is_dinner=True)
    paginator = Paginator(dinner, 6)
    page = request.GET.get('page')
    page_food = paginator.get_page(page)

    data = {
        'dinner':page_food,
    }

    return render(request, 'pages/dinners.html', data)

def footer(request):
    ashley_info = Ashley.objects.all()

    data = {
        'ashley_info': ashley_info,
    }
    return render(request, 'includes/_footer.html', data)
