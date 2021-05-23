import os
from .base import *

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': os.getenv('DB_NAME', 'movies_database'),
        'USER': os.getenv('DB_USER', 'video'),
        'PASSWORD': os.getenv('DB_PASSWORD', '27s60781yAA8E'),
        'HOST': os.getenv('DB_HOST', 'localhost'),
        'PORT': 5432,
    }
}

DEBUG = False

LOGGING = {
    'version': 1,
    'disable_existing_loggers': True,
    'filters': {
        'require_debug_true': {
            '()': 'django.utils.log.RequireDebugTrue',
        }
    },
    'formatters': {
        'default': {
            'format': '%(asctime)s %(levelname)s: %(message)s [in %(pathname)s:%(lineno)d]',
        },
    },
    'handlers': {
        'debug-console': {
            'class': 'logging.StreamHandler',
            'formatter': 'default',
            'filters': ['require_debug_true'],
        },
    },
} 

# TODO Update with production hosts
ALLOWED_HOSTS = ['q8niji9mmf.execute-api.eu-central-1.amazonaws.com']

########################################################################
# Static files
YOUR_S3_BUCKET = "practicum-zappa-static"

STATICFILES_STORAGE = "django_s3_storage.storage.StaticS3Storage"
AWS_S3_BUCKET_NAME_STATIC = YOUR_S3_BUCKET

# These next two lines will serve the static files directly 
# from the s3 bucket
AWS_S3_CUSTOM_DOMAIN = '%s.s3.amazonaws.com' % YOUR_S3_BUCKET
STATIC_URL = "https://%s/" % AWS_S3_CUSTOM_DOMAIN

# custom domain for your static files
#AWS_S3_PUBLIC_URL_STATIC = "https://static.example.com/"