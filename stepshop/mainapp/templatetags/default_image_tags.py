from django import template
from stepshop import settings

register = template.Library()


@register.filter(name='default_product_image')
def default_product_image(image_url):
    if not image_url:
        image_url = 'product_images/default.png'
    return f'{settings.MEDIA_URL}{image_url}'


@register.filter(name='default_avatar_image')
def default_avatar_image(image_url):
    if not image_url:
        image_url = 'users_avatars/default-avatar.png'
    return f'{settings.MEDIA_URL}{image_url}'
