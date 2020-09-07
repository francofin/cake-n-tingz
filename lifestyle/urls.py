from django.urls import path
from . import views

urlpatterns = [
    path('', views.lifestyle, name='lifestyle'),
    path('<int:id>', views.lifestyle_detail, name='lifestyle_detail'),
]
