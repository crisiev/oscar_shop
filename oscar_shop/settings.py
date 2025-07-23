import os
from pathlib import Path
from oscar.defaults import *
import dj_database_url  # Para configurar la DB desde URL en producción

BASE_DIR = Path(__file__).resolve().parent.parent

# Clave secreta fija para desarrollo y pruebas. Cambia esto en producción, mi amor.
SECRET_KEY = os.getenv('SECRET_KEY', '1234')

# DEBUG activado por defecto para que puedas ver errores mientras pruebas
DEBUG = os.getenv('DEBUG', 'True') == 'True'

# Hosts permitidos para evitar problemas de seguridad, aquí tu dominio de Render y localhost
ALLOWED_HOSTS = os.getenv('ALLOWED_HOSTS', 'oscar-shop-3.onrender.com,localhost,127.0.0.1').split(',')

# Aplicaciones instaladas, Oscar con todo su esplendor + dependencias externas
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.sites',
    'django.contrib.flatpages',

    # Oscar apps
    'oscar.config.Shop',
    'oscar.apps.analytics',
    'oscar.apps.checkout',
    'oscar.apps.address',
    'oscar.apps.shipping',
    'oscar.apps.catalogue',
    'oscar.apps.catalogue.reviews',
    'oscar.apps.communication',
    'oscar.apps.partner',
    'oscar.apps.basket',
    'oscar.apps.payment',
    'oscar.apps.offer',
    'oscar.apps.order',
    'oscar.apps.customer',
    'oscar.apps.search',
    'oscar.apps.voucher',
    'oscar.apps.wishlists',
    'oscar.apps.dashboard',
    'oscar.apps.dashboard.reports',
    'oscar.apps.dashboard.users',
    'oscar.apps.dashboard.orders',
    'oscar.apps.dashboard.catalogue',
    'oscar.apps.dashboard.offers',
    'oscar.apps.dashboard.partners',
    'oscar.apps.dashboard.pages',
    'oscar.apps.dashboard.ranges',
    'oscar.apps.dashboard.reviews',
    'oscar.apps.dashboard.vouchers',
    'oscar.apps.dashboard.communications',
    'oscar.apps.dashboard.shipping',

    # Externas
    'widget_tweaks',
    'haystack',
    'treebeard',
    'sorl.thumbnail',
    'django_tables2',
]

SITE_ID = 1

# Middleware, con WhiteNoise para servir estáticos en producción sin líos
MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'whitenoise.middleware.WhiteNoiseMiddleware',  # Para manejar estáticos en producción
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'oscar.apps.basket.middleware.BasketMiddleware',
    'django.contrib.flatpages.middleware.FlatpageFallbackMiddleware',
]

ROOT_URLCONF = 'oscar_shop.urls'

# Templates con los context processors que Oscar necesita
TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [BASE_DIR / 'templates'],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',  # Muy importante para Oscar
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',

                # Context processors específicos de Oscar
                'oscar.apps.search.context_processors.search_form',
                'oscar.apps.checkout.context_processors.checkout',
                'oscar.apps.communication.notifications.context_processors.notifications',
                'oscar.core.context_processors.metadata',
            ],
        },
    },
]

WSGI_APPLICATION = 'oscar_shop.wsgi.application'

# Configuración de base de datos:
# Si tienes DATABASE_URL (Render la provee), úsala para configurar postgres
DATABASE_URL = os.getenv('DATABASE_URL')
if DATABASE_URL:
    DATABASES = {
        'default': dj_database_url.parse(DATABASE_URL)
    }
else:
    # Si no, usa SQLite para desarrollo local tranquilo
    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.sqlite3',
            'NAME': BASE_DIR / 'db.sqlite3',
        }
    }

# Backends de autenticación (Email + default)
AUTHENTICATION_BACKENDS = (
    'oscar.apps.customer.auth_backends.EmailBackend',
    'django.contrib.auth.backends.ModelBackend',
)

# Internacionalización básica
LANGUAGE_CODE = 'en-us'
TIME_ZONE = 'UTC'
USE_I18N = True
USE_TZ = True

# Configuración de archivos estáticos
STATIC_URL = '/static/'
STATIC_ROOT = BASE_DIR / 'staticfiles'

# Usa WhiteNoise para servir archivos estáticos en producción
STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'

# Archivos media (subidos)
MEDIA_URL = '/media/'
MEDIA_ROOT = BASE_DIR / 'media'

# Datos Oscar muy básicos y personalizables después
OSCAR_SHOP_NAME = 'Mi Tienda Oscar'
OSCAR_SHOP_TAGLINE = 'E‑commerce con elegancia'

# Buscador simple para pruebas
HAYSTACK_CONNECTIONS = {
    'default': {'ENGINE': 'haystack.backends.simple_backend.SimpleEngine'}
}

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

# Moneda default para Oscar
OSCAR_DEFAULT_CURRENCY = 'USD'

