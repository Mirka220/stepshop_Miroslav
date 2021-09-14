from django.shortcuts import render, get_object_or_404

from mainapp.models import Product, ProductCategory


def products(request, pk=None):
    title = 'продукты | каталог'

    links_menu = ProductCategory.objects.all()

    products_all = Product.objects.all()
    category = {'name': 'продукты'}

    if pk is not None:
        products_all = Product.objects.filter(category__id=pk)
        category = get_object_or_404(ProductCategory, id=pk)

    context = {
        'title': title,
        'links_menu': links_menu,
        'products': products_all,
        'category': category,
        'pk': pk,
    }

    return render(request, 'mainapp/products.html', context)


def product(request):
    title = 'продукт'

    context = {
        'title': title,
    }

    return render(request, 'mainapp/product.html', context)
