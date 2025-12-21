from django.shortcuts import render
from django.http import HttpResponse
import pprint

USER = {
    "first_name": "Vladimir",
    "middle_name": "Andreevich",
    "last_name": "Romanov",
    "phone": "888-000-99988",
    "email": "888@yandex.ru",
}

ITEMS = [
    {"id": 1, "name": "Кроссовки abibas", "quantity": 5},
    {"id": 2, "name": "Куртка кожаная", "quantity": 2},
    {"id": 5, "name": "Coca-cola 1 литр", "quantity": 12},
    {"id": 7, "name": "Картофель фри", "quantity": 0},
    {"id": 8, "name": "Кепка", "quantity": 124},
]

menu = [
    {'name': 'Home', 'path': '/'},
    {'name': 'About', 'path': '/about'},
    {'name': 'Items', 'path': '/items'},
]

def home(request):
    context = {
        "first_name": "Vladimir",
        "middle_name": "Andreevich",
        "last_name": "Romanov",
        "phone": "888-000-99988",
        "email": "888@yandex.ru",
        "page_name": 'Главная страница',
        "menu": menu
    }
    return render(request, 'index.html', context=context)


def about(request):
    context = {'USER': USER, 'menu': menu}
    return render(request, 'about.html', context)


def items(request):
    context = {'items': ITEMS, 'menu': menu}
    return render(request, 'items.html', context)


def item(request, id: int):
    context = {'name': 'Товар не найден', 'quantity': 0, 'menu': menu}
    for i in ITEMS:
        if id == i['id']:
            context = {'name': i['name'], 'quantity': i['quantity'], 'menu': menu}
    return render(request, 'item.html', context)
