import os
import dj_database_url
import environ

env = environ.Env()

ROOT_DIR = environ.Path(__file__) - 3
APPS_DIR = ROOT_DIR.path('nekidaem-blog')

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

SECRET_KEY = env.str('DJANGO_SECRET_KEY', default='secret-key')

DEBUG = env.bool('DJANGO_DEBUG', default=True)

ALLOWED_HOSTS = env.list(
    'DJANGO_ALLOWED_HOSTS', default=['0.0.0.0'])

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'base',
    'blog',
    'django_rq'
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'config.urls'

WSGI_APPLICATION = 'config.wsgi.application'

# Database connection
# https://github.com/kennethreitz/dj-database-url
# -----------------------------------------------------------------------------
DATABASES = {
    'default': dj_database_url.config(
        'DJANGO_DEFAULT_DATABASE_URL',
        'postgres://postgres:postgres@db:5432/postgres')}

# Password validation
# https://docs.djangoproject.com/en/2.2/ref/settings/#auth-password-validators
# -----------------------------------------------------------------------------
AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

# django-rq
# https://github.com/rq/django-rq
# -----------------------------------------------------------------------------
RQ_QUEUES = {
    'default': {
        'HOST': env.str('REDIS_HOST', 'redis'),
        'PORT': env.int('REDIS_PORT', 6379),
        'DB': env.int('REDIS_DB', 0),
        'DEFAULT_TIMEOUT': 360,
    }
}

# Internationalization
# https://docs.djangoproject.com/en/2.2/topics/i18n/
# -----------------------------------------------------------------------------
LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True

STATIC_ROOT = os.path.join(ROOT_DIR, 'staticfiles')
STATIC_URL = '/static/'

STATICFILES_DIRS = [
    os.path.join(ROOT_DIR, "static/")
]

# Email configuration
# https://docs.djangoproject.com/en/dev/ref/settings/#email-backend
# -----------------------------------------------------------------------------
EMAIL_BACKEND = env('DJANGO_EMAIL_BACKEND',
                    default='django.core.mail.backends.smtp.EmailBackend')
EMAIL_USE_SSL = env('EMAIL_USE_SSL', default=True)
EMAIL_HOST = env('EMAIL_HOST', default='smtp.gmail.com')
EMAIL_HOST_USER = env('EMAIL_HOST_USER', default='nekidaemblog@gmail.com')
EMAIL_HOST_PASSWORD = env('EMAIL_HOST_PASSWORD')
EMAIL_PORT = env('EMAIL_PORT', default=465)
