from django.shortcuts import render


def products(request):
    title = 'продукты | каталог'

    links_menu = [
        {'href': 'products_all', 'name': 'все'},
        {'href': 'products_shoes', 'name': 'обувь'},
        {'href': 'products_pants', 'name': 'штаны'},
        {'href': 'products_phones', 'name': 'смартфоны'},
        {'href': 'products_parts', 'name': 'автозапчасти'},
    ]

    context = {
        'title': title,
        'links_menu': links_menu,
    }

    return render(request, 'mainapp/products.html', context)


def product(request):
    return render(request, 'mainapp/product.html')
