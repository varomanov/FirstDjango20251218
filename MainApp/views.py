from django.shortcuts import render
from django.http import HttpResponse
from .models import Item
from django.db.models import Sum
from django.core.exceptions import ObjectDoesNotExist

USER = {
    "first_name": "Vladimir",
    "middle_name": "Andreevich",
    "last_name": "Romanov",
    "phone": "888-000-99988",
    "email": "888@yandex.ru",
}

menu = [
    {'name': 'Главная', 'path': '/'},
    {'name': 'Обо мне', 'path': '/about'},
    {'name': 'Товары', 'path': '/items'},
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
    products = Item.objects.all()
    context = {'items': products, 'menu': menu,
               'total_count': products.aggregate(total=Sum('count'))['total']}
    return render(request, 'items.html', context)


def item(request, id: int):
    context = {'name': 'Товар не найден', 'quantity': 0, 'menu': menu}
    try:
        products = Item.objects.get(id=id)
        if products:
            return render(request, 'item.html', {'name': products.name, 'quantity': products.count, 'menu': menu, 'description': products.description})
    except Item.DoesNotExist:
        return render(request, 'item.html', context)
    