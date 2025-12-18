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


def home(request):
    text = f"""
    <h1>"Изучаем django"</h1>
    <strong>Автор</strong>: <i>{USER['last_name']}.{USER['first_name'][0]}.{USER['middle_name'][0]}</i>
    """
    return HttpResponse(text)


def about(request):
    # pprint.pprint(dir(request))
    text = f"""
        <p>Имя: {USER['first_name']}</p>
        <p>Отчество: {USER['middle_name']}</p>
        <p>Фамилия: {USER['last_name']}</p>
        <p>телефон: {USER['phone']}</p>
        <p>email: {USER['email']}</p>
    """
    return HttpResponse(text)


def items(request):
    text = ['<ol>', '</ol>']
    for i in ITEMS:
        text.insert(-1, f'<li><a href="item/{i['id']}">{i['name']}, {i['quantity']}</a></li>')
    text = ''.join(text)
    return HttpResponse(text)


def item(request, id: int):
    text = f'<p>Товар с id={id} не найден</p>'
    for i in ITEMS:
        if id == i['id']:
            text = f'<p>{i['name']}, {i['quantity']}</p><a href="/items">Назад к списку товаров</a>'
            return HttpResponse(text)
    return HttpResponse(text)
