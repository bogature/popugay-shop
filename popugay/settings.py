"""
Django settings for popugay project.

Generated by 'django-admin startproject' using Django 3.0.3.

For more information on this file, see
https://docs.djangoproject.com/en/3.0/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/3.0/ref/settings/
"""

import os

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/3.0/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'z31ut91@f)h6mobyd*a_ad00zh)%$k+9mmjupay=aq@nxpg1gg'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ['*']

CORS_ORIGIN_WHITELIST = (
    "http://localhost:4200",
    "http://127.0.0.1:8000",
    "http://z979370u.beget.tech",
    "http://popu-235b5.web.app",
    "https://popu-235b5.web.app",
    # "zoo-tovary.pp.ua",
)

DEFAULT_PARSER_CLASSES = (
    'rest_framework.parsers.JSONParser',
    'rest_framework.parsers.MultiPartParser',
    'rest_framework.parsers.FileUploadParser',
),

REST_FRAMEWORK = {
    'DEFAULT_SCHEMA_CLASS': 'rest_framework.schemas.coreapi.AutoSchema'
}

CORS_ORIGIN_ALLOW_ALL = True

# REST_FRAMEWORK = {
#     'DEFAULT_PAGINATION_CLASS': 'rest_framework.pagination.LimitOffsetPagination',
# }

SWAGGER_SETTINGS = {
    'SHOW_REQUEST_HEADERS': True,
    'SUPPORTED_SUBMIT_METHODS': [
        'get',
        'post',
    ]
}


# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',

    'rest_framework',
    'rest_framework.authtoken',
    'djoser',
    'corsheaders',

    'apps.product',
    'apps.order',
    'apps.home',

]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',

    'corsheaders.middleware.CorsMiddleware',
    'django.middleware.common.CommonMiddleware',
]

ROOT_URLCONF = 'popugay.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'templates')]
        ,
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

WSGI_APPLICATION = 'popugay.wsgi.application'


# Database
# https://docs.djangoproject.com/en/3.0/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}


# Password validation
# https://docs.djangoproject.com/en/3.0/ref/settings/#auth-password-validators

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


# Internationalization
# https://docs.djangoproject.com/en/3.0/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/3.0/howto/static-files/

STATIC_URL = '/static/'
MEDIA_URL = '/media/'

CSS_URL = os.path.join(STATIC_URL, 'css/')
IMG_URL = os.path.join(STATIC_URL, 'img/')
LIB_URL = os.path.join(STATIC_URL, 'lib/')
JS_URL = os.path.join(STATIC_URL, 'js/')

SITE_NAME = ('Serg')

GRAPPELLI_ADMIN_TITLE = SITE_NAME

COMMENTS_APP = 'django_comments_xtd'

LOGIN_REDIRECT_URL = '/'

LOGIN_URL = 'django.contrib.auth.views.login'

COMMENTS_XTD_MAX_THREAD_LEVEL = 2

MANAGERS = (
    ('Joe Bloggs', 'joe.bloggs@example.com'),
)

COMMENTS_XTD_CONFIRM_EMAIL = False

ACCOUNT_ACTIVATION_DAYS = 2
EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST = 'smtp.gmail.com'
EMAIL_HOST_PASSWORD = 'montelepa123456'
EMAIL_HOST_USER = 'o.bogature@gmail.com'
EMAIL_PORT = 587
EMAIL_USE_TLS = True
DEFAULT_FROM_EMAIL = 'o.bogature@gmail.com'

try:
    from private_settings import *
except ImportError:
    print('File private_settings.py is required')