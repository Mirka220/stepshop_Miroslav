from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpResponseRedirect, JsonResponse
from django.shortcuts import render, get_object_or_404
from django.template.loader import render_to_string
from django.urls import reverse, reverse_lazy
from django.views.generic.list import ListView

from basketapp.models import Basket
from mainapp.models import Product


# class BasketListView(LoginRequiredMixin, ListView):
#     model = Basket
#     template_name = 'basketapp/basket.html'
#     context_object_name = 'basket'
#     login_url = '/admin/'
#     login_url = reverse_lazy('products:index')
#     raise_exception = True
#
#     def get_context_data(self, *, object_list=None, **kwargs):
#         context = super().get_context_data()
#         context['title'] = 'корзина'
#         return context
#
#     def get_queryset(self):
#         return Basket.objects.filter(user=self.request.user)


@login_required
def basket(request):
    if request.user.is_authenticated:
        basket_item = Basket.objects.filter(user=request.user)

        for item in basket_item:
            item.product_total_price = item.product.price * item.quantity

        context = {
            'basket': basket_item,
            # 'product_total_price': product_total_price,
        }

        return render(request, 'basketapp/basket.html', context)
    return HttpResponseRedirect(request.META.get('HTTP_REFERER'))


@login_required
def basket_add(request, pk):
    if 'login' in request.META.get('HTTP_REFERER'):
        return HttpResponseRedirect(reverse('products:product', args=[pk]))

    product = get_object_or_404(Product, id=pk)

    basket = Basket.objects.filter(user=request.user, product=product).first()

    if not basket:
        basket = Basket(user=request.user, product=product)

    basket.quantity += 1
    basket.save()

    return HttpResponseRedirect(request.META.get('HTTP_REFERER'))


@login_required
def basket_edit(request, pk, quantity):
    if request.is_ajax():
        quantity = int(quantity)
        basket_item = Basket.objects.get(id=int(pk))

        if quantity > 0:
            basket_item.quantity = quantity
            basket_item.save()
        else:
            basket_item.delete()

        basket = Basket.objects.filter(user=request.user).order_by('product__category')

        context = {
            'basket': basket,
        }

        product_total_price = basket_item.product.price * basket_item.quantity

        # result = render_to_string('basketapp/includes/inc_basket_list.html', context)
        result = render_to_string('basketapp/includes/inc_basket_summary.html', context)

        return JsonResponse({'result': result, 'product_total_price': product_total_price})



@login_required
def basket_remove(request, pk):
    basket_record = get_object_or_404(Basket, id=pk)
    basket_record.delete()

    return HttpResponseRedirect(request.META.get('HTTP_REFERER'))
