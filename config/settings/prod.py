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

