import os
from website.settings import BASE_DIR

SECRET_KEY = 'd+mw&mscg5i&tx+#@bf+6m%e+d5z!u#!n%z-^o9u7y1felv2o&'

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'netology_homework_db3',
        'USER': 'dor',
        'PASSWORD': 'dor',
        'HOST': '127.0.0.1',
        'PORT': '5432',
    }
}