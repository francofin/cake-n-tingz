from django.shortcuts import render

# Create your views here.

def lifestyle(request):
    return render(request, 'pages/lifestyle.html')
