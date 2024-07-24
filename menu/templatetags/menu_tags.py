from django import template
from ..models import Menu

register = template.Library()


@register.inclusion_tag('menu/draw_menu.html', takes_context=True)
def draw_menu(context, menu_name):
    request = context['request']
    try:
        menu = Menu.objects.get(name=menu_name)
    except Menu.DoesNotExist:
        menu = None
    menu_items = menu.items.filter(parent__isnull=True) if menu else []
    active_item = get_active_item(menu, request.path) if menu else None
    print(f'Menu: {menu}, Active Item: {active_item}')
    return {'menu': menu, 'menu_items': menu_items, 'active_item': active_item}


def get_active_item(menu, path):
    for item in menu.items.all():
        item_url = item.get_url()
        print(f'Checking item: {item.title}, URL: {item_url}, Request Path: {path}')
        if path == item_url:
            return item
    return None
