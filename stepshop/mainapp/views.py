from django.shortcuts import render, get_object_or_404

from mainapp.models import Product, ProductCategory
from basketapp.models import Basket


def get_basket(user_):
    if user_.is_authenticated:
        return Basket.objects.filter(user=user_)
    else:
        return []


def get_same_product(current_product):
    return Product.objects.filter(category=current_product.category).exclude(id=current_product.id)


def products(request, pk=None):
    title = 'продукты | каталог'

    links_menu = ProductCategory.objects.all()

    products_all = Product.objects.all()
    category = {'name': 'продукты'}

    if pk is not None:
        products_all = Product.objects.filter(category__id=pk)
        category = get_object_or_404(ProductCategory, id=pk)

    basket = get_basket(request.user)

    context = {
        'title': title,
        'links_menu': links_menu,
        'products': products_all,
        'category': category,
        'pk': pk,
        'basket': basket,
    }

    return render(request, 'mainapp/products.html', context)


def product(request, pk):
    title = 'продукт'

    links_menu = ProductCategory.objects.all()
    product_item = get_object_or_404(Product, id=pk)

    basket = get_basket(request.user)
    same_products = get_same_product(product_item)

    context = {
        'title': title,
        'links_menu': links_menu,
        'product': product_item,
        'basket': basket,
        'same_products': same_products,
    }

    return render(request, 'mainapp/product.html', context)
