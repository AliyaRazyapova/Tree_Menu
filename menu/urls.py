from django.urls import path
from .views import index_view, menu_view

urlpatterns = [
    path('', index_view, name='index'),
    path('<str:menu_name>/', menu_view, name='menu_view'),
]
