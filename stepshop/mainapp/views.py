from django.shortcuts import render

from mainapp.models import Product


def products(request):
    title = 'продукты | каталог'

    links_menu = [
        {'href': 'products_all', 'name': 'все'},
        {'href': 'products_shoes', 'name': 'обувь'},
        {'href': 'products_pants', 'name': 'штаны'},
        {'href': 'products_phones', 'name': 'смартфоны'},
        {'href': 'products_parts', 'name': 'автозапчасти'},
    ]

    products_all = Product.objects.all()

    context = {
        'title': title,
        'links_menu': links_menu,
        'products': products_all,
    }

    return render(request, 'mainapp/products.html', context)


def product(request):
    title = 'продукт'

    context = {
        'title': title,
    }

    return render(request, 'mainapp/product.html', context)
