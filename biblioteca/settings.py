"""
Django settings for biblioteca project.

Generated by 'django-admin startproject' using Django 3.1.7.

For more information on this file, see
https://docs.djangoproject.com/en/3.1/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/3.1/ref/settings/
"""

from pathlib import Path
import os

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/3.1/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'd#sp@myuby_n1f-l1qw5sb-e1haxou)ld6pryyuxy!v0hxrw9b'

# SECURITY WARNING: don't run with debug turned on in production!
#DEBUG = True
#ALLOWED_HOSTS = []


#Descomentar estas 2 líneas para no usar el depurador (servidor en producción)
DEBUG = False           
ALLOWED_HOSTS = ['*']    



# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'cuentas',
    'peliculas',
    'rest_framework',
    'django_cleanup.apps.CleanupConfig',    #Para eliminar elementos imagenes antiguas
]

#Configuración de la api REST
REST_FRAMEWORK = {
    'DEFAULT_PAGINATION_CLASS': 'rest_framework.pagination.PageNumberPagination',
    'PAGE_SIZE': 10
}


MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'biblioteca.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
       # 'DIRS': [BASE_DIR / "biblioteca" / "templates"],
        'DIRS': ['./templates',],
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

WSGI_APPLICATION = 'biblioteca.wsgi.application'


# Database
# https://docs.djangoproject.com/en/3.1/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}


# Password validation
# https://docs.djangoproject.com/en/3.1/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/3.1/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'Europe/Madrid'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/3.1/howto/static-files/



STATIC_URL = '/static/'



STATICFILES_DIRS = [
    os.path.join(BASE_DIR,'/static/'),
]




AUTH_USER_MODEL = 'cuentas.Usuario'                     #Para indicar que queremos usar un usuario Custom

# Redirect to home URL after login (Default redirects to /accounts/profile/)
LOGIN_REDIRECT_URL = '/peliculas/'
LOGOUT_REDIRECT_URL = '/accounts/login/'

EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'

#Esto es para las imágenes

MEDIA_URL = '/media/'                           #URL pública a la base del directorio de almacenamiento

MEDIA_ROOT = os.path.join(BASE_DIR,'peliculas/static/media/')   #Ruta completa donde Django almacenará, archivos o imágenes cargadas
