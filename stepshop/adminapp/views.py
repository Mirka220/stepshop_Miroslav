from django.contrib.auth.decorators import user_passes_test
from django.http import HttpResponseRedirect
from django.shortcuts import render, get_object_or_404
from django.urls import reverse, reverse_lazy
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic.list import ListView

from adminapp.forms import ProductCategoryCreateForm, ProductCategoryEditForm, ProductEditForm
from authapp.forms import ShopUserRegisterForm, ShopUserEditForm
from authapp.models import ShopUser
from mainapp.models import ProductCategory, Product


class UserListView(ListView):
    model = ShopUser
    template_name = 'adminapp/users.html'
    context_object_name = 'objects'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data()
        context['title'] = 'админка | пользователи'
        return context

    def get_queryset(self):
        return ShopUser.objects.all().order_by('-is_active', '-is_superuser', '-is_staff', 'username')


# @user_passes_test(lambda u: u.is_superuser)
# def users(request):
#     title = 'админка | пользователи'
#
#     user_list = ShopUser.objects.all().order_by('-is_active', '-is_superuser', '-is_staff', 'username')
#
#     context = {
#         'title': title,
#         'objects': user_list,
#     }
#
#     return render(request, 'adminapp/users.html', context)


class UserCreateView(CreateView):
    model = ShopUser
    form_class = ShopUserRegisterForm
    template_name = 'adminapp/users/user_create.html'
    success_url = reverse_lazy('admin_staff:users')

    def get_context_data(self, **kwargs):
        context = super().get_context_data()
        context['title'] = 'админка | создать пользователя'
        return context


# def user_create(request):
#     title = 'админка | создать пользователя'
#
#     if request.method == 'POST':
#         user_form = ShopUserRegisterForm(request.POST, request.FILES)
#
#         if user_form.is_valid():
#             user_form.save()
#             return HttpResponseRedirect(reverse('admin_staff:users'))
#
#     else:
#         user_form = ShopUserRegisterForm()
#
#     context = {
#         'title': title,
#         'user_form': user_form,
#     }
#
#     return render(request, 'adminapp/users/user_create.html', context)


class UserUpdateView(UpdateView):
    model = ShopUser
    form_class = ShopUserEditForm
    template_name = 'adminapp/users/user_update.html'
    success_url = reverse_lazy('admin_staff:users')
    context_object_name = 'user'

    def get_context_data(self, **kwargs):
        context = super().get_context_data()
        context['title'] = 'админка | редактировать пользователя'
        return context


# def user_update(request, pk):
#     title = 'админка | редактировать пользователя'
#
#     edit_user = get_object_or_404(ShopUser, id=pk)
#
#     if request.method == 'POST':
#         edit_form = ShopUserEditForm(request.POST, request.FILES, instance=edit_user)
#
#         if edit_form.is_valid():
#             edit_form.save()
#             return HttpResponseRedirect(reverse('admin_staff:users'))
#
#     else:
#         edit_form = ShopUserEditForm(instance=edit_user)
#
#     context = {
#         'title': title,
#         'edit_form': edit_form,
#         'edit_user': edit_user,
#     }
#
#     return render(request, 'adminapp/users/user_update.html', context)


class UserDeleteView(DeleteView):
    model = ShopUser
    template_name = 'adminapp/users/user_delete.html'
    success_url = reverse_lazy('admin_staff:users')
    context_object_name = 'user_to_delete'

    def delete(self, request, *args, **kwargs):
        self.object = self.get_object()
        self.object.is_active = False
        self.object.save()
        return HttpResponseRedirect(self.get_success_url())

    def get_context_data(self, **kwargs):
        context = super().get_context_data()
        context['title'] = 'админка | удаление пользователя'
        return context


# def user_delete(request, pk):
#     title = 'админка | удаление пользователя'
#
#     user = get_object_or_404(ShopUser, id=pk)
#
#     if request.method == 'POST':
#         user.is_active = False
#         user.save()
#         return HttpResponseRedirect(reverse('admin_staff:users'))
#
#     context = {
#         'title': title,
#         'user_to_delete': user,
#     }
#
#     return render(request, 'adminapp/users/user_delete.html', context)


class CategoryListView(ListView):
    model = ProductCategory
    template_name = 'adminapp/categories.html'
    context_object_name = 'objects'
    paginate_by = 4

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data()
        context['title'] = 'админка | категории'
        return context


# @user_passes_test(lambda u: u.is_staff)
# def categories(request):
#     title = 'админка | категории'
#
#     categories_list = ProductCategory.objects.all()
#
#     context = {
#         'title': title,
#         'objects': categories_list,
#     }
#
#     return render(request, 'adminapp/categories.html', context)


class CategoryCreateView(CreateView):
    model = ProductCategory
    form_class = ProductCategoryCreateForm
    template_name = 'adminapp/categories/category_create.html'
    success_url = reverse_lazy('admin_staff:categories')

    def get_context_data(self, **kwargs):
        context = super().get_context_data()
        context['title'] = 'админка | создать категорию'
        return context


# def category_create(request):
#     title = 'админка | создать категорию'
#
#     if request.method == 'POST':
#         category_form = ProductCategoryCreateForm(request.POST, request.FILES)
#
#         if category_form.is_valid():
#             category_form.save()
#             return HttpResponseRedirect(reverse('admin_staff:categories'))
#
#     else:
#         category_form = ProductCategoryCreateForm()
#
#     context = {
#         'title': title,
#         'category_form': category_form,
#     }
#
#     return render(request, 'adminapp/categories/category_create.html', context)


class CategoryUpdateView(UpdateView):
    model = ProductCategory
    form_class = ProductCategoryEditForm
    template_name = 'adminapp/categories/category_update.html'
    success_url = reverse_lazy('admin_staff:categories')

    def get_context_data(self, **kwargs):
        context = super().get_context_data()
        context['title'] = 'админка | редактировать категорию'
        return context


# def category_update(request, pk):
#     title = 'админка | редактировать категорию'
#
#     edit_category = get_object_or_404(ProductCategory, id=pk)
#
#     if request.method == 'POST':
#         edit_form = ProductCategoryEditForm(request.POST, request.FILES, instance=edit_category)
#
#         if edit_form.is_valid():
#             edit_form.save()
#             return HttpResponseRedirect(reverse('admin_staff:categories'))
#
#     else:
#         edit_form = ProductCategoryEditForm(instance=edit_category)
#
#     context = {
#         'title': title,
#         'edit_form': edit_form,
#         'edit_category': edit_category,
#     }
#
#     return render(request, 'adminapp/categories/category_update.html', context)


class CategoryDeleteView(DeleteView):
    model = ProductCategory
    template_name = 'adminapp/categories/category_delete.html'
    success_url = reverse_lazy('admin_staff:categories')
    context_object_name = 'category_to_delete'

    def delete(self, request, *args, **kwargs):
        self.object = self.get_object()
        self.object.is_active = False
        self.object.save()
        return HttpResponseRedirect(self.get_success_url())

    def get_context_data(self, **kwargs):
        context = super().get_context_data()
        context['title'] = 'админка | удаление категории'
        return context


# def category_delete(request, pk):
#     title = 'админка | удаление категории'
#
#     category = get_object_or_404(ProductCategory, id=pk)
#
#     if request.method == 'POST':
#         category.is_active = False
#         category.save()
#         return HttpResponseRedirect(reverse('admin_staff:categories'))
#
#     context = {
#         'title': title,
#         'category_to_delete': category,
#     }
#
#     return render(request, 'adminapp/categories/category_delete.html', context)


class ProductsListView(ListView):
    model = Product
    template_name = 'adminapp/products.html'
    context_object_name = 'objects'
    paginate_by = 4

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        category = get_object_or_404(ProductCategory, pk=self.kwargs.get('pk'))
        context['title'] = 'админка | продукты'
        context['category'] = category
        return context

    def get_queryset(self):
        return Product.objects.filter(category__pk=self.kwargs.get('pk')).order_by('name')


# @user_passes_test(lambda u: u.is_staff)
# def products(request, pk):
#     title = 'админка | продукты'
#
#     category = get_object_or_404(ProductCategory, id=pk)
#     products_list = Product.objects.filter(category__pk=pk).order_by('name')
#
#     context = {
#         'title': title,
#         'category': category,
#         'objects': products_list,
#     }
#
#     return render(request, 'adminapp/products.html', context)


class ProductDetailView(DetailView):
    model = Product
    template_name = 'adminapp/product/product_read.html'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data()
        context['title'] = 'админка | продукты подробнее'
        return context


# def product_read(request, pk):
#     title = 'админка | продукты подробнее'
#
#     product = get_object_or_404(Product, id=pk)
#
#     context = {
#         'title': title,
#         'product': product,
#     }
#
#     return render(request, 'adminapp/product/product_read.html', context)


class ProductCreateView(CreateView):
    model = ProductCategory
    form_class = ProductEditForm
    template_name = 'adminapp/product/product_create.html'
    # success_url = reverse_lazy('admin_staff:categories')

    def get_success_url(self):
        return reverse('admin_staff:products', args=[self.get_object().category.pk])

    def get_context_data(self, **kwargs):
        context = super().get_context_data()
        category = get_object_or_404(ProductCategory, pk=self.kwargs.get('pk'))
        context['title'] = 'админка | создать продукт'
        context['category'] = category
        return context


# def product_create(request, pk):
#     title = 'админка | создать продукт'
#
#     category = get_object_or_404(ProductCategory, id=pk)
#
#     if request.method == 'POST':
#         product_form = ProductEditForm(request.POST, request.FILES)
#
#         if product_form.is_valid():
#             product_form.save()
#             return HttpResponseRedirect(reverse('admin_staff:products', args=[pk]))
#     else:
#         product_form = ProductEditForm(initial={'category': category})
#
#     context = {
#         'title': title,
#         'create_form': product_form,
#         'category': category,
#     }
#
#     return render(request, 'adminapp/product/product_create.html', context)


class ProductUpdateView(UpdateView):
    model = Product
    form_class = ProductEditForm
    template_name = 'adminapp/product/product_update.html'
    # success_url = reverse_lazy('admin_staff:categories')
    context_object_name = 'product'

    def get_success_url(self):
        return reverse('admin_staff:products', args=[self.get_object().category.pk])

    def get_context_data(self, **kwargs):
        context = super().get_context_data()
        product = get_object_or_404(Product, pk=self.kwargs.get('pk'))
        context['title'] = 'админка | редактировать продукт'
        context['product'] = product
        return context


# def product_update(request, pk):
#     title = 'админка | редактировать продукт'
#
#     edit_product = get_object_or_404(Product, id=pk)
#
#     if request.method == 'POST':
#         edit_form = ProductEditForm(request.POST, request.FILES, instance=edit_product)
#
#         if edit_form.is_valid():
#             edit_form.save()
#             return HttpResponseRedirect(reverse('admin_staff:products', args=[edit_product.category.pk]))
#     else:
#         edit_form = ProductEditForm(instance=edit_product)
#
#     context = {
#         'title': title,
#         'update_form': edit_form,
#         'product': edit_product,
#     }
#
#     return render(request, 'adminapp/product/product_update.html', context)


class ProductDeleteView(DeleteView):
    model = Product
    template_name = 'adminapp/product/product_delete.html'
    context_object_name = 'product_to_delete'

    def delete(self, request, *args, **kwargs):
        self.object = self.get_object()
        self.object.is_active = False
        self.object.save()
        self.success_url = reverse_lazy('admin_staff:products', args=[self.get_object().category.pk])
        return HttpResponseRedirect(self.get_success_url())

    def get_context_data(self, **kwargs):
        context = super().get_context_data()
        context['title'] = 'админка | удалить продукт'
        return context


# def product_delete(request, pk):
#     title = 'админка | удалить продукт'
#
#     product = get_object_or_404(Product, id=pk)
#
#     if request.method == 'POST':
#         product.is_active = False
#         product.save()
#         return HttpResponseRedirect(reverse('admin_staff:products', args=[product.category.pk]))
#
#     context = {
#         'title': title,
#         'product_to_delete': product,
#     }
#
#     return render(request, 'adminapp/product/product_delete.html', context)
