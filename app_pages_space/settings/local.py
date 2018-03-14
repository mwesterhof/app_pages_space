from app_pages_space.settings.base import *  # noqa


DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'app_pages_space',
    }
}

INSTALLED_APPS += [
    'django_extensions'
]

AUTH_PASSWORD_VALIDATORS = []
