from .base import *

SECRET_KEY = env.str('DJANGO_SECRET_KEY')

DEBUG = True

ALLOWED_HOSTS = env.list('DJANGO_ALLOWED_HOSTS')
