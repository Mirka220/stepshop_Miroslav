from django.contrib.auth.decorators import user_passes_test
from django.shortcuts import render, get_object_or_404

from authapp.models import ShopUser
from mainapp.models import ProductCategory, Product


@user_passes_test(lambda u: u.is_staff)
def users(request):
    title = 'админка | пользователи'

    user_list = ShopUser.objects.all().order_by('-is_active', '-is_superuser', '-is_staff', 'username')

    context = {
        'title': title,
        'objects': user_list,
    }

    return render(request, 'adminapp/users.html', context)


def user_create(request):
    pass


def user_update(request):
    pass


def user_delete(request):
    pass


@user_passes_test(lambda u: u.is_staff)
def categories(request):
    title = 'админка | категории'

    categories_list = ProductCategory.objects.all()

    context = {
        'title': title,
        'objects': categories_list,
    }

    return render(request, 'adminapp/categories.html', context)


def category_create(request):
    pass


def category_update(request):
    pass


def category_delete(request):
    pass


@user_passes_test(lambda u: u.is_superuser)
def products(request, pk):
    title = 'админка | продукты'

    category = get_object_or_404(ProductCategory, id=pk)
    products_list = Product.objects.filter(category__pk=pk).order_by('name')

    context = {
        'title': title,
        'category': category,
        'objects': products_list,
    }

    return render(request, 'adminapp/products.html', context)


def product_read(request):
    pass


def product_create(request):
    pass


def product_update(request):
    pass


def product_delete(request):
    pass
