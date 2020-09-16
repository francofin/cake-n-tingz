from django.urls import path
from . import views

urlpatterns = [
    path('', views.lifestyle, name='lifestyle'),
    path('<int:id>', views.lifestyle_detail, name='lifestyle_detail'),
    path('lifestylecomment', views.lifestylecomment, name='lifestylecomment'),
    path('add_to_life_dash', views.add_to_life_dash, name='add_to_life_dash'),
    path('workouts', views.workouts, name='workouts'),
    path('travels', views.travels, name='travels'),
    path('health_and_well', views.health_and_well, name='health_and_well'),
    path('for_women', views.for_women, name='for_women'),
]
