from django.shortcuts import render, redirect, get_object_or_404
from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator
from django.contrib import messages
from .models import Lifestyle, LifestyleComment, LifestyleDashboard
from pages.models import Ashley

# Create your views here.

def lifestyle(request):
    featured_lifestyle = Lifestyle.objects.order_by('-created_date').filter(is_for_lifestyle_page=True)
    ashley_info = Ashley.objects.all()
    paginator = Paginator(featured_lifestyle, 3)
    page = request.GET.get('page')
    page_lifestyle = paginator.get_page(page)

    data = {
        'featured_lifestyle':page_lifestyle,
        'ashley_info': ashley_info,
    }
    return render(request, 'pages/lifestyle.html', data)


def lifestyle_detail(request, id):
    lifestyle_article = get_object_or_404(Lifestyle, pk=id)
    new_lifestyle = Lifestyle.objects.order_by('-created_date').filter(is_new_for_blog=True)
    lifestyle_id = id
    all_comments = LifestyleComment.objects.order_by('-create_date').filter(lifestyle_id=lifestyle_id)
    ashley_info = Ashley.objects.all()

    data= {
        'lifestyle_article': lifestyle_article,
        'all_comments': all_comments,
        'ashley_info': ashley_info,
        'new_lifestyle': new_lifestyle,
    }
    return render(request, 'pages/lifestyle_detail.html', data)

def add_to_life_dash(request):

    if request.method == 'POST':
        user_id = request.POST['user_id']
        lifestyle_id = request.POST['lifestyle_id']
        lifestyles = Lifestyle.objects.order_by('-created_date').filter(pk=lifestyle_id)
        life_photo_url = request.POST['life_photo']
        lifestyle_title = request.POST['lifestyle_title']
        life_des = request.POST['lifestyle_description']

        life_article = LifestyleDashboard(user_id=user_id, life_id=lifestyle_id, life_photo=life_photo_url, lifestyle_title=lifestyle_title, life_description=life_des)
        life_article.save()
        messages.success(request, 'Article has Been Successfully Added To Your Dashboard')
        return redirect('/lifestyle/'+lifestyle_id)

def lifestylecomment(request):
    if request.method == 'POST':
        user_id = request.POST['user_id']
        first_name = request.POST['first_name']
        email = request.POST['email']
        lifestyle_id = request.POST['lifestyle_id']
        website = request.POST['website']
        message = request.POST['message']

        comment = LifestyleComment(user_id =user_id, first_name=first_name, email=email, comments=message, lifestyle_id=lifestyle_id)

        comment.save()
        return redirect('/lifestyle/'+lifestyle_id)

def workouts(request):
    workout = Lifestyle.objects.order_by('-created_date').filter(is_workout=True)
    paginator = Paginator(workout, 3)
    page = request.GET.get('page')
    page_food = paginator.get_page(page)
    ashley_info = Ashley.objects.all()

    data = {
        'workout':workout,
        'ashley_info': ashley_info,
    }

    return render(request, 'pages/workouts.html', data)

def travels(request):
    travel = Lifestyle.objects.order_by('-created_date').filter(is_travel=True)
    paginator = Paginator(travel, 3)
    page = request.GET.get('page')
    page_food = paginator.get_page(page)
    ashley_info = Ashley.objects.all()

    data = {
        'travel':travel,
        'ashley_info': ashley_info,
    }

    return render(request, 'pages/travel.html', data)

def health_and_well(request):
    health = Lifestyle.objects.order_by('-created_date').filter(is_health=True)
    paginator = Paginator(health, 3)
    page = request.GET.get('page')
    page_food = paginator.get_page(page)
    ashley_info = Ashley.objects.all()

    data = {
        'health':health,
        'ashley_info': ashley_info,
    }

    return render(request, 'pages/health_and_well_being.html', data)

def for_women(request):
    women = Lifestyle.objects.order_by('-created_date').filter(is_for_women=True)
    paginator = Paginator(women, 3)
    page = request.GET.get('page')
    page_food = paginator.get_page(page)
    ashley_info = Ashley.objects.all()

    data = {
        'women':women,
        'ashley_info': ashley_info,
    }

    return render(request, 'pages/for_women.html', data)
