from django import template
from Goods.models import Categories, BroadCategories

register = template.Library()


@register.filter
def order_subcaategories_by_slug(things, slug):
    return things.filter(slug__contains=f"{slug.split('-')[-1]}")
