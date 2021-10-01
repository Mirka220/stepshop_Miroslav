from django.http import HttpResponseRedirect
from django.shortcuts import render, get_object_or_404
from django.urls import reverse
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

from mainapp.models import Product, ProductCategory
from basketapp.models import Basket


def get_basket(user_):
    if user_.is_authenticated:
        return Basket.objects.filter(user=user_)
    else:
        return []


def get_same_product(current_product):
    return Product.objects.filter(category=current_product.category, is_active=True).exclude(id=current_product.id)


def products(request, pk=None, page=1):
    title = 'продукты | каталог'

    links_menu = ProductCategory.objects.filter(is_active=True)  # all()

    products_all = Product.objects.filter(category__is_active=True, is_active=True)  # all()
    category = {'name': 'продукты'}

    if pk is not None:
        products_all = Product.objects.filter(category__id=pk, is_active=True)
        category = get_object_or_404(ProductCategory, id=pk)
        if not category.is_active:
            return HttpResponseRedirect(reverse('products:index'))

    basket = get_basket(request.user)

    paginator = Paginator(products_all, 3)

    try:
        products_paginator = paginator.page(page)
    except PageNotAnInteger:
        products_paginator = paginator.page(1)
    except EmptyPage:
        products_paginator = paginator.page(paginator.num_pages)

    context = {
        'title': title,
        'links_menu': links_menu,
        'products': products_paginator,  # products_all,
        'category': category,
        'pk': pk,
        'basket': basket,
    }

    return render(request, 'mainapp/products.html', context)


def product(request, pk):
    title = 'продукт'

    links_menu = ProductCategory.objects.all()
    product_item = get_object_or_404(Product, id=pk)

    category = product_item.category

    if not category.is_active or not product_item.is_active:
        return HttpResponseRedirect(reverse('products:index'))

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
