from django.urls import path
from . import views


urlpatterns = [
    path('', views.foods, name='foods'),
    path('<int:id>', views.food_detail, name='food_detail'),
    path('comment', views.comment, name='comment'),
]
