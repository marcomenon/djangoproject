import os
import mimetypes
from pathlib import Path
from dotenv import load_dotenv
from django.db.backends.postgresql.psycopg_any import IsolationLevel

# Aggiunge il MIME type per i file JavaScript
mimetypes.add_type("application/javascript", ".js", True)

# Directory base del progetto
BASE_DIR = Path(__file__).resolve().parent.parent

# Percorso del file .env per le variabili di ambiente
ENV_PATH = BASE_DIR / ".env"
load_dotenv(ENV_PATH)

# Funzione per convertire stringhe in booleani
def str_to_bool(value):
    return value.lower() in {"true", "1", "yes"}

# Variabili di base
PROJECT_NAME = os.getenv("PROJECT_NAME", "djangoweb")
SECRET_KEY = os.getenv("SECRET_KEY", "default-secret-key")
DEBUG = str_to_bool(os.getenv("DEBUG", "true"))

# Configurazione degli host consentiti
ALLOWED_HOSTS_DOMAIN = os.getenv("ALLOWED_HOSTS_DOMAIN", "example.com").split(",")
ALLOWED_HOSTS_IP = os.getenv("ALLOWED_HOSTS_IP", "127.0.0.1").split(",")
ALLOWED_MAINTENANCE_HOSTS = os.getenv("ALLOWED_MAINTENANCE_HOSTS", "localhost").split(",")
ALLOWED_MAINTENANCE_IPS = os.getenv("ALLOWED_MAINTENANCE_IPS", "127.0.0.1").split(",")

# Imposta la modalità di manutenzione
MAINTENANCE_MODE = str_to_bool(os.getenv("MAINTENANCE_MODE", "false"))

# Unisce gli host autorizzati senza duplicati
ALLOWED_HOSTS = list(set(ALLOWED_HOSTS_IP + ALLOWED_MAINTENANCE_IPS + ALLOWED_HOSTS_DOMAIN + ALLOWED_MAINTENANCE_HOSTS))

# Definizione delle applicazioni installate
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    # App di terze parti
    'django_extensions',
    'django.contrib.sites',
    'allauth',
    'allauth.account',
    'django_htmx',
    'widget_tweaks',
    'debug_toolbar',
    'django_tables2',
    # App personalizzate
    'accounts',
]

# Middleware del progetto
MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'core.middlewares.maintenance.MaintenanceMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'debug_toolbar.middleware.DebugToolbarMiddleware',
    'django_htmx.middleware.HtmxMiddleware',
    'allauth.account.middleware.AccountMiddleware',
]

ROOT_URLCONF = 'core.urls'

# Configurazione dei template
TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [BASE_DIR / "templates", BASE_DIR / "templates/common"],
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

WSGI_APPLICATION = 'core.wsgi.application'

# Configurazione del database
DATABASES = {
    'default': {
        "ENGINE": os.getenv("DB_ENGINE", "django.db.backends.postgresql"),
        "NAME": os.getenv("DB_NAME", "postgres_djangoproject"),
        "USER": os.getenv("DB_USER", "user_djangoproject"),
        "PASSWORD": os.getenv("DB_PASS", "password_djangoproject"),
        "HOST": os.getenv("DB_HOST", "localhost"),
        "PORT": int(os.getenv("DB_PORT", "5432")),
        "OPTIONS": {
            "client_encoding": "UTF8",
        },
    }
}

# Validatori delle password
AUTH_PASSWORD_VALIDATORS = [
    {'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator'},
    {'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator'},
    {'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator'},
    {'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator'},
]

# Configurazione lingua e fuso orario
LANGUAGE_CODE = os.getenv("LANGUAGE_CODE", "it-IT")
TIME_ZONE = os.getenv("TIME_ZONE", "Europe/Rome")
USE_I18N = True
USE_TZ = True

# Configurazione dei file statici e media
STATIC_URL = '/static/'
STATIC_ROOT = Path(os.getenv("STATIC_ROOT", str(BASE_DIR / "staticfiles")))
STATICFILES_DIRS = [BASE_DIR / "static"]
MEDIA_URL = '/media/'
MEDIA_ROOT = Path(os.getenv("MEDIA_ROOT", str(BASE_DIR / "media")))

# Configurazione della cache con Redis
CACHES = {
    "default": {
        "BACKEND": "django_redis.cache.RedisCache",
        "LOCATION": "redis://127.0.0.1:6379/1",
        "OPTIONS": {
            "CLIENT_CLASS": "django_redis.client.DefaultClient",
        }
    }
}

# Configurazione delle sessioni
SESSION_ENGINE = "django.contrib.sessions.backends.cache"
SESSION_CACHE_ALIAS = "default"

# Configurazione Email
EMAIL_BACKEND = os.getenv("EMAIL_BACKEND", "django.core.mail.backends.smtp.EmailBackend")
EMAIL_HOST = os.getenv("EMAIL_HOST", "smtp.gmail.com")
EMAIL_PORT = int(os.getenv("EMAIL_PORT", 587))
EMAIL_HOST_USER = os.getenv("EMAIL_HOST_USER", "your_email@gmail.com")
EMAIL_HOST_PASSWORD = os.getenv("EMAIL_HOST_PASSWORD", "your_password")
EMAIL_USE_TLS = str_to_bool(os.getenv("EMAIL_USE_TLS", "true"))
EMAIL_TIMEOUT = int(os.getenv("EMAIL_TIMEOUT", 10))
DEFAULT_FROM_EMAIL = os.getenv("DEFAULT_FROM_EMAIL", EMAIL_HOST_USER)

# Configurazione django-allauth
AUTHENTICATION_BACKENDS = (
    'django.contrib.auth.backends.ModelBackend',
    'allauth.account.auth_backends.AuthenticationBackend',
)
SITE_ID = 1
INTERNAL_IPS = ['127.0.0.1']

# Configurazioni per django-allauth
_login_methods = os.getenv("ACCOUNT_LOGIN_METHODS", "username")
ACCOUNT_LOGIN_METHODS = frozenset(m.strip() for m in _login_methods.split(","))
ACCOUNT_EMAIL_VERIFICATION = os.getenv("ACCOUNT_EMAIL_VERIFICATION", "none")
ACCOUNT_EMAIL_REQUIRED = str_to_bool(os.getenv("ACCOUNT_EMAIL_REQUIRED", "false"))
ACCOUNT_USERNAME_REQUIRED = str_to_bool(os.getenv("ACCOUNT_USERNAME_REQUIRED", "true"))

# Modello personalizzato per l'utente
AUTH_USER_MODEL = "accounts.CustomUser"
