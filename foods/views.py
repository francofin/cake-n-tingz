from django.shortcuts import render, get_object_or_404, redirect
from foods.models import Food, Dashboard
from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator
from django.contrib import messages

# Create your views here.
def foods(request):
    featured_foods = Food.objects.order_by('-created_date').filter(is_featured=True)
    paginator = Paginator(featured_foods, 6)
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

def add_to_dash(request):

    if request.method == 'POST':
        user_id = request.POST['user_id']
        food_id = request.POST['food_id']
        foods = Food.objects.order_by('-created_date').filter(pk=food_id)
        food_photo_url = request.POST['food_photo']
        food_title = request.POST['food_title']
        food_des = request.POST['food_description']

        food_article = Dashboard(user_id=user_id, food_id=food_id, food_photo=food_photo_url, food_title=food_title, food_description=food_des)
        food_article.save()
        messages.success(request, 'Article has Been Successfully Added To Your Database')
        return redirect('/foods/'+food_id)

# def dashboard(request):
#     user_food_article = Food.objects.all().filter(user_id=request.user.id)
#
#     articles = {
#         'food_article':user_food_article,
#     }

    return render(request, 'pages/dashboard.html', articles)



def comment(request):

    return render(request, 'pages/contact.html')
