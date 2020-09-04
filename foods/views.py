from django.shortcuts import render, get_object_or_404
from foods.models import Food
from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator

# Create your views here.
def foods(request):
    featured_foods = Food.objects.order_by('-created_date').filter(is_featured=True)
    paginator = Paginator(featured_foods, 3)
    page = request.GET.get('page')
    page_food = paginator.get_page(page)

    data = {
        'featured_foods':page_food,
    }

    return render(request, 'pages/foods.html', data)


def food_detail(request, id):
    food_recipe = get_object_or_404(Food, pk=id)

    data= {
        'food_recipe': food_recipe,
    }
    return render(request, 'pages/food_detail.html', data)

def comment(request):

    return render(request, 'pages/contact.html')
