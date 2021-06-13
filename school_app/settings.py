"""
Django settings for school_app project.

Generated by 'django-admin startproject' using Django 3.0.5.

For more information on this file, see
https://docs.djangoproject.com/en/3.0/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/3.0/ref/settings/
"""

import os
import django_heroku


# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/3.0/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '__$1ud47e&nyso5h5o3fwnqu4+hfqcply9h$k*h2s34)hn5@nc'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True


ALLOWED_HOSTS = ['*']


# Application definition

INSTALLED_APPS = [
    'bootstrapform',
    'django_bootstrap_breadcrumbs',
    'users.apps.UsersConfig',
    'crispy_forms',
    'django.contrib.auth',
    'django.contrib.admin',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.humanize',
    'widget_tweaks',
    'ckeditor',
    'ckeditor_uploader',
    'corecode',
    'students',
    'staffs',
    'finance',
    'result',


]
CKEDITOR_UPLOAD_PATH = "content/ckeditor/"
MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'corecode.middleware.SiteWideConfigs',
    'whitenoise.middleware.WhiteNoiseMiddleware',
]


STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'

ROOT_URLCONF = 'school_app.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [
            os.path.join(BASE_DIR, 'templates')
        ],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
                'corecode.context_processors.site_defaults',
            ],
        },
    },
]

WSGI_APPLICATION = 'school_app.wsgi.application'


DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3')
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

CKEDITOR_CONFIGS = {
    'awesome_ckeditor': {
        'toolbar': 'customes',
        'extraPlugins' : ','.join(['codesnippet', 'youtube']),
        'height': 291,
        'width': '100%',
    }

}

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/3.0/howto/static-files/

DATA_UPLOAD_MAX_NUMBER_FIELDS = 10240
CRISPY_TEMPLATE_PACK = 'uni_form'


# Extra places for collectstatic to find static files.

STATIC_URL = '/static/'
STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')

STATICFILES_DIRS = (
    os.path.join(BASE_DIR, 'static'),
)

MEDIA_ROOT = os.path.join(BASE_DIR, 'media')
MEDIA_URL = '/media/'

LOGOUT_REDIRECT_URL = 'home'

CRISPY_TEMPLATE_PACK = 'bootstrap4'

LOGIN_REDIRECT_URL = '/dashboard'
LOGIN_URL = 'login'

EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST = 'smtp.gmail.com'
EMAIL_PORT = 587
EMAIL_USE_TLS = True
EMAIL_HOST_USER = os.environ.get('shiva850681@gmail.com')
EMAIL_HOST_PASSWORD = os.environ.get('Shiva8506')

