from django.shortcuts import render

# Create your views here.
def foods(request):
    return render(request, 'pages/foods.html')
