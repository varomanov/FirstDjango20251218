# FirstDjango

## Инструкция по созданию проекта
1. Создать виртуальное окружение
```
python3 -m venv .env
```
2. Активировать виртуальное окружение
```
source .env/bin/activate
```
3. Установить нужные библиотеки в виртуальное окружение
```
pip install -r requirements.txt
```
4. Запустить сервер
```
python manage.py runserver
```

## Дополнительно

1. Полезное расширение для шаблонов: `django`
```
ext install batisteo.vscode-django
```
2. Добавить в `settings.json`
```
"emmet.includeLanguages": {
    "django-html": "html"
},
"files.associations": {
    "*. html": "django-html"
}
```