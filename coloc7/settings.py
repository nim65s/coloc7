"""
Django settings for coloc7 project.

For more information on this file, see
https://docs.djangoproject.com/en/1.7/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.7/ref/settings/
"""

from os.path import dirname, join

from pathlib import Path

PROJECT = "coloc7"
PROJECT_VERBOSE = "Portail web de la Coloc7"
MAIL_USER = "majo"
SELF_MAIL = False
ALLOWED_HOSTS = ["coloc7.eu"]
ALLOWED_HOSTS.append("www.%s" % ALLOWED_HOSTS[0])

BASE_DIR = dirname(dirname(__file__))
CONF_DIR = Path("/etc/nim/" + PROJECT)

if not CONF_DIR.is_dir():
    CONF_DIR.mkdir(parents=True)

SECRET_KEY = (CONF_DIR / "secret_key.txt").open().read().strip()

DEBUG, INTEGRATION, PROD = False, False, False

if (CONF_DIR / "integration").is_file():
    INTEGRATION = True
elif (CONF_DIR / "prod").is_file():
    PROD = True
else:
    DEBUG = True

EMAIL_SUBJECT_PREFIX = ("[%s Dev] " if DEBUG or INTEGRATION else "[%s] ") % PROJECT_VERBOSE

EMAIL_USE_SSL = True
EMAIL_HOST = "smtp.%s" % (ALLOWED_HOSTS[0] if SELF_MAIL else "totheweb.fr")
EMAIL_PORT = 465
EMAIL_HOST_USER = "%s@%s" % (MAIL_USER, ALLOWED_HOSTS[0] if SELF_MAIL else "totheweb.fr")
SERVER_EMAIL = "%s+%s@%s" % (MAIL_USER, PROJECT, ALLOWED_HOSTS[0] if SELF_MAIL else "totheweb.fr")
DEFAULT_FROM_EMAIL = "%s <%s@%s>" % (PROJECT_VERBOSE, MAIL_USER, ALLOWED_HOSTS[0] if SELF_MAIL else "totheweb.fr")
EMAIL_HOST_PASSWORD = (CONF_DIR / "email_password").open().read().strip()

ADMINS = (
        ("Guilhem Saurel", "guilhem+admin-%s@saurel.me" % PROJECT),
        # TODO: on vous ajoute ici dès que tout tourne…
        )
MANAGERS = ADMINS
TEMPLATE_DEBUG = DEBUG

INSTALLED_APPS = [
    PROJECT,
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.sites',
    'django.contrib.sitemaps',
    'django.contrib.staticfiles',
    'pybb',
    'bootstrap3',
    'sorl.thumbnail',
    'comptes',
]

MIDDLEWARE_CLASSES = [
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.auth.middleware.SessionAuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

TEMPLATE_CONTEXT_PROCESSORS = [
    'django.contrib.auth.context_processors.auth',
    'django.core.context_processors.debug',
    'django.core.context_processors.i18n',
    'django.core.context_processors.request',
    'django.core.context_processors.media',
    'django.core.context_processors.static',
    'django.core.context_processors.tz',
    'django.contrib.messages.context_processors.messages',
]

ROOT_URLCONF = '%s.urls' % PROJECT

WSGI_APPLICATION = '%s.wsgi.application' % PROJECT

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': PROJECT,
        'USER': PROJECT,
        'PASSWORD': (CONF_DIR / 'db_password.txt').open().read().strip(),
        'HOST': 'localhost',
    }
}

LANGUAGE_CODE = 'fr-FR'
TIME_ZONE = 'Europe/Paris'
USE_I18N = True
USE_L10N = True
USE_TZ = True

SITE_ID = 1

MEDIA_ROOT = join(BASE_DIR, 'media')
MEDIA_URL = '/media/'
STATIC_URL = '/static/'
STATIC_ROOT = join(BASE_DIR, 'static_dest') if DEBUG else '/var/www/%s/static_dest' % PROJECT

CACHES = {
        "default": {
            "BACKEND": "django.core.cache.backends.memcached.MemcachedCache",
            "LOCATION": "127.0.0.1:11211",
            }
        }

LOGGING = {
    "version": 1,
    "disable_existing_loggers": False,
    "handlers": {
        "null": {
            "level": "DEBUG",
            "class": "logging.NullHandler",
        },
    },
    "loggers": {
        "django.security.DisallowedHost": {
            "handlers": ["null"],
            "propagate": False,
        },
    },
}

if (Path(BASE_DIR) / PROJECT / 'context_processors.py').is_file():
    TEMPLATE_CONTEXT_PROCESSORS.append('%s.context_processors.%s' % (PROJECT, PROJECT))

if not DEBUG:
    INSTALLED_APPS.append('raven.contrib.django.raven_compat')
    RAVEN_CONFIG = {"dsn": (CONF_DIR / "raven").open().read().strip()}

if 'pybb' in INSTALLED_APPS:
    PYBB_MARKUP = 'markdown'
    TEMPLATE_CONTEXT_PROCESSORS.append('pybb.context_processors.processor')
    MIDDLEWARE_CLASSES.append('pybb.middleware.PybbMiddleware')
    PYBB_DEFAULT_TITLE = "Forum de la Coloc7"

LOGIN_REDIRECT_URL = '/'
