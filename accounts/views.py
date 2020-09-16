from django.shortcuts import render, redirect
from django.contrib import messages, auth
from django.contrib.auth.models import User
from foods.models import Dashboard, Food
from pages.models import Ashley
from lifestyle.models import LifestyleDashboard
from django.contrib.auth.decorators import login_required


# Create your views here.
def login(request):
    if request.method=='POST':
        username = request.POST['username']
        password = request.POST['password']

        user = auth.authenticate(username=username, password=password)

        if user is not None:
            auth.login(request, user)
            messages.success(request, 'You Are Successfully Logged In! Welcome')
            return redirect('dashboard')
        else:
            messages.error(request, 'Invalid LogIn Credentials')
            return redirect('login')
    return render(request, 'pages/login.html')

def register(request):
    if request.method=='POST':
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        password2 = request.POST['password2']

        if password == password2:
            if User.objects.filter(username=username).exists():
                messages.error(request, 'Username Already Exists')
                return redirect('register')
            else:
                if User.objects.filter(email=email).exists():
                    messages.error(request, 'Email Already Exists!')
                    return redirect('register')
                else:
                    user = User.objects.create_user(first_name=first_name, last_name=last_name, username=username, password=password)
                    auth.login(request, user)
                    messages.success(request, 'you are now logged in')
                    return redirect('dashboard')
                    user.save()
                    messages.succes(request, 'Account Successfully Created. Welcome')
                    return redirect('index')
        else:
            messages.error(request, 'Passwords Do Not Match!')
            return redirect('register')
    else:
        return render(request, 'pages/register.html')
@login_required(login_url='login')
def dashboard(request):
    user_foods = Dashboard.objects.all().filter(user_id=request.user.id)
    ashley_info = Ashley.objects.all()
    # user_lifestyle = LifestyleDashboard.object.all().filter(user_id=request.user.id)

    articles = {
        'food_article':user_foods,
        'ashley_info': ashley_info,
        # 'user_lifestyle': user_lifestyle,
    }

    return render(request, 'pages/dashboard.html', articles)


def logout(request):
    if request.method=='POST':
        auth.logout(request)
        return redirect('index')
    return redirect('index')
