from django.shortcuts import render, get_object_or_404
from .models import Menu


def index_view(request):
    menus = Menu.objects.all()
    try:
        default_menu = Menu.objects.get(name='main_menu')
        menu_items = default_menu.items.filter(parent__isnull=True)
    except Menu.DoesNotExist:
        default_menu = None
        menu_items = []
        print("Menu 'main_menu' does not exist")

    context = {
        'menus': menus,
        'menu': default_menu,
        'menu_items': menu_items
    }
    return render(request, 'menu/index.html', context)


def menu_view(request, menu_name):
    menu = get_object_or_404(Menu, name=menu_name)
    menu_items = menu.items.filter(parent__isnull=True)
    context = {
        'menu': menu,
        'menu_items': menu_items
    }
    return render(request, 'menu/draw_menu.html', context)
