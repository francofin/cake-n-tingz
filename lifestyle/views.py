from django.shortcuts import render, redirect, get_object_or_404
from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator
from django.contrib import messages
from .models import Lifestyle

# Create your views here.

def lifestyle(request):
    featured_lifestyle = Lifestyle.objects.order_by('-created_date').filter(is_for_lifestyle_page=True)
    paginator = Paginator(featured_lifestyle, 3)
    page = request.GET.get('page')
    page_lifestyle = paginator.get_page(page)

    data = {
        'featured_lifestyle':page_lifestyle,
    }
    return render(request, 'pages/lifestyle.html', data)


def lifestyle_detail(request, id):
    lifestyle_article = get_object_or_404(Lifestyle, pk=id)

    data= {
        'lifestyle_article': lifestyle_article,
    }
    return render(request, 'pages/lifestyle_detail.html', data)
