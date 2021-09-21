from django.db import models

from mainapp.models import Product
from stepshop import settings


class Basket(models.Model):
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name='basket',
    )

    product = models.ForeignKey(
        Product,
        on_delete=models.CASCADE,
    )

    quantity = models.PositiveIntegerField(
        verbose_name='количество',
        default=0,
    )

    add_datetime = models.DateTimeField(
        verbose_name='время',
        auto_now_add=True,
    )

    @property
    def product_cost(self):
        return self.product.price * self.quantity

    @property
    def total_quantity(self):
        __items = Basket.objects.filter(user=self.user)
        __total_quantity = sum(list(map(lambda x: x.quantity, __items)))
        return __total_quantity

    @property
    def total_cost(self):
        __items = Basket.objects.filter(user=self.user)
        __total_cost = sum(list(map(lambda x: x.product_cost, __items)))
        return __total_cost

    def __str__(self):
        return f'{self.product} ({self.quantity}) - {self.user}' or f'Id корзины - {self.pk}'

    class Meta:
        verbose_name = 'корзина'
        verbose_name_plural = 'корзины'
