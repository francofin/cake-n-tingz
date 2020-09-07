from django.urls import path
from . import views


urlpatterns = [
    path('', views.index, name='index'),
    path('about/', views.about, name='about'),
    path('for_kids', views.for_kids, name='for_kids'),
    path('desserts', views.desserts, name='desserts'),
    path('dinner_meals', views.dinner_meals, name='dinner_meals'),
]
