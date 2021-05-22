# Проект для иллюстрации запуска Django на AWS Lambda

## Инсталляция

```
virtualenv env
source env/bin/activate
pip install -r requirements/dev.txt
```

## Создание суперпользователя

```
./manage.py createsuperuser
```

## Запуск приложения

```
./manage.py runserver
```

Откройте с браузере http://127.0.0.1:8000/admin

## Генерация тестовых данных

```
./manage.py generate_test_data
```
