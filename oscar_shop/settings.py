import os
from pathlib import Path
from dotenv import load_dotenv
from oscar.defaults import *  # asegúrate de que esta línea esté al inicio del settings

load_dotenv()  # carga variables .env

BASE_DIR = Path(__file__).resolve().parent.parent

SECRET_KEY = os.getenv("SECRET_KEY", "1234")
#DEBUG = os.getenv("DEBUG", "False") == "True"
DEBUG = True
ALLOWED_HOSTS = os.getenv("ALLOWED_HOSTS", "localhost").split(",")

INSTALLED_APPS = [
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
    "django.contrib.sites",
    "django.contrib.flatpages",

    "oscar.config.Shop",
    "oscar.apps.analytics.apps.AnalyticsConfig",
    "oscar.apps.checkout.apps.CheckoutConfig",
    "oscar.apps.address.apps.AddressConfig",
    "oscar.apps.shipping.apps.ShippingConfig",
    "oscar.apps.catalogue.apps.CatalogueConfig",
    "oscar.apps.catalogue.reviews.apps.CatalogueReviewsConfig",
    "oscar.apps.communication.apps.CommunicationConfig",
    "oscar.apps.partner.apps.PartnerConfig",
    "oscar.apps.basket.apps.BasketConfig",
    "oscar.apps.payment.apps.PaymentConfig",
    "oscar.apps.offer.apps.OfferConfig",
    "oscar.apps.order.apps.OrderConfig",
    "oscar.apps.customer.apps.CustomerConfig",
    "oscar.apps.search.apps.SearchConfig",
    "oscar.apps.voucher.apps.VoucherConfig",
    "oscar.apps.wishlists.apps.WishlistsConfig",

    "oscar.apps.dashboard.apps.DashboardConfig",
    "oscar.apps.dashboard.reports.apps.ReportsDashboardConfig",
    "oscar.apps.dashboard.users.apps.UsersDashboardConfig",
    "oscar.apps.dashboard.orders.apps.OrdersDashboardConfig",
    "oscar.apps.dashboard.catalogue.apps.CatalogueDashboardConfig",
    "oscar.apps.dashboard.offers.apps.OffersDashboardConfig",
    "oscar.apps.dashboard.partners.apps.PartnersDashboardConfig",
    "oscar.apps.dashboard.pages.apps.PagesDashboardConfig",
    "oscar.apps.dashboard.ranges.apps.RangesDashboardConfig",
    "oscar.apps.dashboard.reviews.apps.ReviewsDashboardConfig",
    "oscar.apps.dashboard.vouchers.apps.VouchersDashboardConfig",
    "oscar.apps.dashboard.communications.apps.CommunicationsDashboardConfig",
    "oscar.apps.dashboard.shipping.apps.ShippingDashboardConfig",

    "widget_tweaks",
    "haystack",
    "treebeard",
    "django_tables2",
]

import os

# Configuración completa de variables OSCAR_*
OSCAR_SHOP_NAME = os.getenv("OSCAR_SHOP_NAME", "Oscar")
OSCAR_SHOP_TAGLINE = os.getenv("OSCAR_SHOP_TAGLINE", "")
OSCAR_HOMEPAGE = os.getenv("OSCAR_HOMEPAGE", None)
OSCAR_ACCOUNTS_REDIRECT_URL = os.getenv("OSCAR_ACCOUNTS_REDIRECT_URL", "customer:profile-view")
OSCAR_HIDDEN_FEATURES = []

OSCAR_DEFAULT_CURRENCY = os.getenv("OSCAR_DEFAULT_CURRENCY", "USD")
OSCAR_OFFERS_INCL_TAX = os.getenv("OSCAR_OFFERS_INCL_TAX", "False") == "True"
OSCAR_ALLOW_ANON_CHECKOUT = os.getenv("OSCAR_ALLOW_ANON_CHECKOUT", "True") == "True"
OSCAR_REQUIRED_ADDRESS_FIELDS = ("first_name", "last_name", "line1", "line4", "postcode", "country")

OSCAR_DASHBOARD_CATALOGUE_FORMS = {
    'category': 'oscar.apps.dashboard.catalogue.forms.CategoryForm',
}

# Slugs
OSCAR_SLUG_FUNCTION = 'django.utils.text.slugify'
OSCAR_SLUG_MAP = {}
OSCAR_SLUG_BLACKLIST = []
OSCAR_SLUG_ALLOW_UNICODE = False

# Imagenes y thumbnails
OSCAR_DELETE_IMAGE_FILES = False  # o True, según prefieras
OSCAR_MISSING_IMAGE_URL = None
OSCAR_THUMBNAILER = None
OSCAR_THUMBNAIL_DEBUG = False

# Ofertas
OSCAR_OFFER_ROUNDING_FUNCTION = None
OSCAR_OFFERS_IMPLEMENTED_TYPES = None

# Generales
OSCAR_STATIC_BASE_URL = None
OSCAR_URL_SCHEMA = 'http'
OSCAR_FROM_EMAIL = 'oscar@example.com'
OSCAR_GOOGLE_ANALYTICS_ID = ''
OSCAR_CSV_INCLUDE_BOM = False

OSCAR_PRODUCTS_PER_PAGE = int(os.getenv("OSCAR_PRODUCTS_PER_PAGE", 20))
OSCAR_OFFERS_PER_PAGE = int(os.getenv("OSCAR_OFFERS_PER_PAGE", 20))
OSCAR_REVIEWS_PER_PAGE = int(os.getenv("OSCAR_REVIEWS_PER_PAGE", 20))
OSCAR_ORDERS_PER_PAGE = int(os.getenv("OSCAR_ORDERS_PER_PAGE", 20))
OSCAR_ADDRESSES_PER_PAGE = int(os.getenv("OSCAR_ADDRESSES_PER_PAGE", 20))
OSCAR_DASHBOARD_ITEMS_PER_PAGE = int(os.getenv("OSCAR_DASHBOARD_ITEMS_PER_PAGE", 20))
OSCAR_SEARCH_FACETS = {
    'fields': {
        'product_class': {
            'name': 'Tipo de producto',
            'field': 'product_class',
        },
        'rating': {
            'name': 'Calificación',
            'field': 'rating',
        },
    },
    'queries': {
        'price_range': {
            'name': 'Precio',
            'field': 'price',
            'queries': [
                ('0 a 20', '[0 TO 20]'),
                ('20 a 40', '[20 TO 40]'),
                ('Más de 40', '[40 TO *]'),
            ]
        },
    },
}

OSCAR_PRODUCT_SEARCH_HANDLER = None
OSCAR_HIDDEN_FEATURES = []

OSCAR_RECENTLY_VIEWED_COOKIE_NAME = 'oscar_history'
OSCAR_RECENTLY_VIEWED_COOKIE_LIFETIME = 604800  # 7 días
OSCAR_RECENTLY_VIEWED_COOKIE_SECURE = False     # True si usas HTTPS
OSCAR_RECENTLY_VIEWED_COOKIE_HTTPONLY = True    # Oculta a JavaScript
OSCAR_RECENTLY_VIEWED_COOKIE_PATH = '/'         # Ruta del dominio
OSCAR_RECENTLY_VIEWED_COOKIE_DOMAIN = None      # Dominio explícito si es necesario
OSCAR_RECENTLY_VIEWED_PRODUCTS = 20  # o el número que desees mostrar
OSCAR_EMAILS_PER_PAGE = 20
OSCAR_NOTIFICATIONS_PER_PAGE = 20
OSCAR_STOCK_ALERTS_PER_PAGE = 20

OSCAR_COOKIES_DELETE_ON_LOGOUT = os.getenv("OSCAR_COOKIES_DELETE_ON_LOGOUT", "False") == "True"
OSCAR_GOOGLE_ANALYTICS_ID = os.getenv("OSCAR_GOOGLE_ANALYTICS_ID", "")

OSCAR_CSV_INCLUDE_BOM = os.getenv("OSCAR_CSV_INCLUDE_BOM", "False") == "True"
OSCAR_URL_SCHEMA = os.getenv("OSCAR_URL_SCHEMA", "http")

OSCAR_FROM_EMAIL = os.getenv("OSCAR_FROM_EMAIL", "oscar@example.com")
OSCAR_STATIC_BASE_URL = os.getenv("OSCAR_STATIC_BASE_URL", None)
OSCAR_SAVE_SENT_EMAILS_TO_DB = os.getenv("OSCAR_SAVE_SENT_EMAILS_TO_DB", "True") == "True"

OSCAR_DYNAMIC_CLASS_LOADER = os.getenv(
    "OSCAR_DYNAMIC_CLASS_LOADER",
    "oscar.core.loading.default_class_loader"
)

OSCAR_OFFER_ROUNDING_FUNCTION = os.getenv(
    "OSCAR_OFFER_ROUNDING_FUNCTION", None
)

OSCAR_OFFERS_IMPLEMENTED_TYPES = None
OSCAR_BASKET_COOKIE_LIFETIME = None
OSCAR_MAX_BASKET_QUANTITY_THRESHOLD = None
OSCAR_BASKET_COOKIE_OPEN = None
OSCAR_SLUG_FUNCTION = None
OSCAR_SLUG_MAP = {}
OSCAR_SLUG_ALLOW_UNICODE = False
OSCAR_THUMBNAILER = None
OSCAR_THUMBNAIL_DEBUG = None
OSCAR_MISSING_IMAGE_URL = None
OSCAR_DELETE_IMAGE_FILES = None
OSCAR_EAGER_ALERTS = True
OSCAR_SEND_REGISTRATION_EMAIL = True
OSCAR_STATIC_BASE_URL = None
OSCAR_SLUG_FUNCTION = 'django.utils.text.slugify'



MIDDLEWARE = [
    "django.middleware.security.SecurityMiddleware",
    "whitenoise.middleware.WhiteNoiseMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",  # Va antes de BasketMiddleware
    "django.contrib.messages.middleware.MessageMiddleware",
    'oscar.apps.basket.middleware.BasketMiddleware',           # Va después de AuthenticationMiddleware
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
]


ROOT_URLCONF = "oscar_shop.urls"

TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [BASE_DIR / "templates"],
        "APP_DIRS": True,
        "OPTIONS": {
            "context_processors": [
                "django.template.context_processors.debug",
                "django.template.context_processors.request",
                "django.contrib.auth.context_processors.auth",
                "django.contrib.messages.context_processors.messages",
                "oscar.core.context_processors.metadata",
            ],
        },
    },
]

WSGI_APPLICATION = "oscar_shop.wsgi.application"

DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.postgresql_psycopg2",
        "NAME": os.getenv("DB_NAME"),
        "USER": os.getenv("DB_USER"),
        "PASSWORD": os.getenv("DB_PASSWORD"),
        "HOST": os.getenv("DB_HOST"),
        "PORT": os.getenv("DB_PORT"),
    }
}

AUTHENTICATION_BACKENDS = (
    "oscar.apps.customer.auth_backends.EmailBackend",
    "django.contrib.auth.backends.ModelBackend",
)

LANGUAGE_CODE = "en-us"
TIME_ZONE = "UTC"
USE_I18N = True
USE_L10N = True
USE_TZ = True

STATIC_URL = "/static/"
STATIC_ROOT = BASE_DIR / "staticfiles"
STATICFILES_STORAGE = "whitenoise.storage.CompressedManifestStaticFilesStorage"

MEDIA_URL = "/media/"
MEDIA_ROOT = BASE_DIR / "media"

DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"

# Oscar settings
OSCAR_ALLOW_ANON_CHECKOUT = True
OSCAR_DEFAULT_CURRENCY = "USD"

# Haystack (si lo usas para búsqueda)
HAYSTACK_CONNECTIONS = {
    "default": {
        "ENGINE": "haystack.backends.simple_backend.SimpleEngine",
    },
}

# Django sites framework
SITE_ID = 1

# Tailwind si decides integrarlo
# TAILWIND_APP_NAME = "theme"

# CORS (si usas)
# CORS_ALLOWED_ORIGINS = [...]

# Logging, email y otros configs aquí según necesidad
EMAIL_BACKEND = "django.core.mail.backends.console.EmailBackend"

OSCAR_DASHBOARD_NAVIGATION = [
    {
        'label': 'Dashboard',
        'icon': 'fas fa-tachometer-alt',
        'url_name': 'dashboard:index',
    },
    {
        'label': 'Productos',
        'icon': 'fas fa-shopping-bag',
        'children': [
            {
                'label': 'Ver productos',
                'url_name': 'dashboard:catalogue-product-list',
            },
            {
                'label': 'Categorías',
                'url_name': 'dashboard:catalogue-category-list',
            },
        ]
    },
]
