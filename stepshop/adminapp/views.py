from django.contrib.auth.decorators import user_passes_test
from django.http import HttpResponseRedirect
from django.shortcuts import render, get_object_or_404
from django.urls import reverse

from authapp.forms import ShopUserRegisterForm, ShopUserEditForm
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
    title = 'админка | создать пользователя'

    if request.method == 'POST':
        user_form = ShopUserRegisterForm(request.POST, request.FILES)

        if user_form.is_valid():
            user_form.save()
            return HttpResponseRedirect(reverse('admin_staff:user'))

    else:
        user_form = ShopUserRegisterForm()

    context = {
        'title': title,
        'user_form': user_form,
    }

    return render(request, 'adminapp/users/user_create.html', context)


def user_update(request, pk):
    title = 'админка | редактировать пользователя'

    edit_user = get_object_or_404(ShopUser, id=pk)

    if request.method == 'POST':
        edit_form = ShopUserEditForm(request.POST, request.FILES, instance=edit_user)

        if edit_form.is_valid():
            edit_form.save()
            return HttpResponseRedirect(reverse('admin_staff:user'))

    else:
        edit_form = ShopUserEditForm(instance=edit_user)

    context = {
        'title': title,
        'edit_form': edit_form,
        'edit_user': edit_user,
    }

    return render(request, 'adminapp/users/user_update.html', context)


def user_delete(request, pk):
    title = 'админка | удаление пользователя'

    user = get_object_or_404(ShopUser, id=pk)

    if request.method == 'POST':
        user.is_active = False
        user.save()
        return HttpResponseRedirect(reverse('admin_staff:users'))

    context = {
        'title': title,
        'user_to_delete': user,
    }

    return render(request, 'adminapp/users/user_delete.html', context)


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
