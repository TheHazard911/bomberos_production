"""
Django settings for Web_App project.

Generated by 'django-admin startproject' using Django 5.1.1.

For more information on this file, see
https://docs.djangoproject.com/en/5.1/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/5.1/ref/settings/
"""

import os
from pathlib import Path
import dj_database_url

# Build paths inside the project like this: BASE_DIR / 'subdir'.

# esto lo estoy probando
# BASE_DIR = Path(__file__).resolve().parent.parent /esta es la original
# esto es para el render
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/5.1/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-usf!gyb)c_93(yhk-ab2gm%&_(hlk1ough81m110qhhrn4$cvy'

# SECURITY WARNING: don't run with debug turned on in production!
# Debug true significa desarrollo modo de pruebas
DEBUG = True

#------------- modo produccion-----------------
# Debug false significa produccion quiere decir listo para usarse
# DEBUG = False

# ALLOWED_HOSTS = []

ALLOWED_HOSTS = ['localhost', '127.0.0.1', 'bomberos-production.onrender.com']





# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    "web"
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'whitenoise.middleware.WhiteNoiseMiddleware',
    'web.middleware.LogoutIfAuthenticatedMiddleware',  # Tu middleware existente
    'web.middleware.NoCacheMiddleware',  # Ajusta esto según tu estructura
    'web.middleware.LoadingScreenMiddleware',
]

LOGIN_URL = 'home'  # Cambia esto al nombre de tu URL de inicio de sesión
LOGIN_REDIRECT_URL = '/dashboard/'  # Cambia esto a la vista a la que quieres redirigir después del inicio de sesión

SESSION_COOKIE_AGE = 18000  # Tiempo en segundos (15 minutos)
SESSION_EXPIRE_AT_BROWSER_CLOSE = True  # Cierra sesión al cerrar el navegador

STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'

ROOT_URLCONF = 'Web_App.urls'

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

WSGI_APPLICATION = 'Web_App.wsgi.application'


# Database
# https://docs.djangoproject.com/en/5.1/ref/settings/#databases

# DATABASES = {
#     'default': {
#         'ENGINE': 'django.db.backends.sqlite3',
#         # 'NAME': BASE_DIR / 'db.sqlite3', comentada para el render esta es original
#         # nueva linea para el render 
#         'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
#     }
# }

# DATABASES = {
#     'default': {
#         'ENGINE': 'django.db.backends.postgresql_psycopg2',
#         'NAME': 'bomberos_db',
#         'USER': 'postgres',
#         'PASSWORD': 'anthonym7',
#         'PORT': '5432',
#         'HOST': 'localhost'
#     }
# }

# Base de Datos del Render (Eber)
# DATABASES = {
#     'default': dj_database_url.config(default="postgresql://data_rad4_user:Akjqm5bt9mEcBcxEhx9JsikkQ5RwMnDu@dpg-cskgpc3tq21c73dohb3g-a.oregon-postgres.render.com/data_rad4")
# }

# Base de Datos del Render (Sala Situacional)
DATABASES = {
    'default': dj_database_url.config(default="postgresql://bomberos_db_user:5wuTseoCTH2EvZaKsR7Ct529uc8sdpVg@dpg-csp2esm8ii6s73a525sg-a.oregon-postgres.render.com/bomberos_db")
}

# Password validation
# https://docs.djangoproject.com/en/5.1/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/5.1/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'America/Caracas'

USE_I18N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/5.1/howto/static-files/

STATIC_URL = 'static/'
STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')

# Default primary key field type
# https://docs.djangoproject.com/en/5.1/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'
