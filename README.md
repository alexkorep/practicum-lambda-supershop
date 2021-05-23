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

## Zappa commands

# Deploy

```
zappa deploy prod
```

# Collect static to S3

```
./manage.py collectstatic --settings=config.settings.prod
```

# Apply migrations

```
zappa manage dev migrate
```

# Create superuser

```
zappa invoke --raw dev "from django.contrib.auth.models import User; User.objects.create_superuser('admin', 'admin@yourdomain.com', 'Y0urpassword')"
```

# Load test

```
npx loadtest -c 10 https://example.com/dev/admin/
```
