from django import template
from menu.models import MenuBy

register = template.Library()


@register.simple_tag(name='get_list_categories')
def get_categories():
    return MenuBy.objects.all()


@register.inclusion_tag('menu_template.html')
def show_categories(arg1='Hello', arg2='world'):
    # categories = Category.objects.all()
    categories = MenuBy.objects.all()
    # categories = get_categories()
    return {"categories": categories, "arg1": arg1, "arg2": arg2}
