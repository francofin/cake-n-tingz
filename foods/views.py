from django.shortcuts import render, get_object_or_404, redirect
from foods.models import Food, Dashboard, Comment
from pages.models import Ashley
from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator
from django.contrib import messages

# Create your views here.
def foods(request):
    featured_foods = Food.objects.order_by('-created_date').filter(is_featured=True)
    paginator = Paginator(featured_foods, 6)
    page = request.GET.get('page')
    page_food = paginator.get_page(page)
    ashley_info = Ashley.objects.all()

    data = {
        'featured_foods':page_food,
        'ashley_info': ashley_info,
    }

    return render(request, 'pages/foods.html', data)


def food_detail(request, id):
    food_recipe = get_object_or_404(Food, pk=id)
    featured_posts = Food.objects.order_by('-created_date').filter(is_featured_for_home_page=True)
    food_id = id
    all_comments = Comment.objects.order_by('-create_date').filter(food_id=food_id)
    ashley_info = Ashley.objects.all()

    data= {
        'food_recipe': food_recipe,
        'featured_posts': featured_posts,
        'all_comments': all_comments,
        'ashley_info': ashley_info,
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
        messages.success(request, 'Article has Been Successfully Added To Your Dashboard')
        return redirect('/foods/'+food_id)

# def dashboard(request):
#     user_food_article = Food.objects.all().filter(user_id=request.user.id)
#
#     articles = {
#         'food_article':user_food_article,
#     }

    return render(request, 'pages/dashboard.html', articles)



def comment(request):
    if request.method == 'POST':
        user_id = request.POST['user_id']
        first_name = request.POST['first_name']
        email = request.POST['email']
        food_id = request.POST['food_id']
        website = request.POST['website']
        message = request.POST['message']

        comment = Comment(user_id =user_id, first_name=first_name, email=email, comments=message, food_id=food_id)

        comment.save()
        return redirect('/foods/'+food_id)
