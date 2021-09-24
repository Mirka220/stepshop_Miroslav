from django.shortcuts import render

from basketapp.models import Basket
from mainapp.models import Product


def index(request):
    title = 'главная'

    products = Product.objects.filter(category__is_active=True)

    basket = []

    if request.user.is_authenticated:
        basket = Basket.objects.filter(user=request.user)

    context = {
        'title': title,
        'products': products,
        'basket': basket,
    }

    return render(request, 'stepshop/index.html', context)


def contacts(request):
    title = 'контакты'

    basket = []

    if request.user.is_authenticated:
        basket = Basket.objects.filter(user=request.user)

    context = {
        'title': title,
        'basket': basket,
    }

    return render(request, 'stepshop/contact.html', context)


def about(request):
    title = 'о нас'

    basket = []

    if request.user.is_authenticated:
        basket = Basket.objects.filter(user=request.user)

    context = {
        'title': title,
        'basket': basket,
    }

    return render(request, 'stepshop/about.html', context)
