from django.urls import path

from .views import products, product

app_name = 'products'

urlpatterns = [
    path('', products, name='index'),
    path('page/<int:page>/', products, name='page'),
    path('category/<int:pk>/', products, name='category'),
    path('category/<int:pk>/page/<int:page>/', products, name='category_page'),
    path('product/<int:pk>/', product, name='product'),
]
