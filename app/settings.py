import environ
from pathlib import Path

# BASE DIR
BASE_DIR = Path(__file__).resolve().parent.parent

try:
    from dotenv import load_dotenv
    load_dotenv(BASE_DIR / ".env")
except:
    print("Cannot load dotenv variables. Is python-dotenv package installed?")

# ENV SET
env = environ.Env()

# SECRET KEY
SECRET_KEY = env.str('DJANGO_SECRET_KEY')

# DEBUG
DEBUG = env.bool('DEBUG', default=True)

# ALLOWED HOSTS
ALLOWED_HOSTS = env.list('ALLOWED_HOSTS', default=['*'])

# INSTALLED APPS
INSTALLED_APPS = [
    'jazzmin',
    "tailwind",
    "theme",
    
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',

    'configuration',
    'accounts',
    'travel_claim',
    'bank_account',
]

# MIDDLEWARE
MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

# ROOT URLCONF
ROOT_URLCONF = 'app.urls'

# TEMPLATES
TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [BASE_DIR, 'theme/templates'],
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

# WSGI APPLICATION
WSGI_APPLICATION = 'app.wsgi.application'

# AUTH USER MODEL
AUTH_USER_MODEL = 'accounts.User'

# AUTHENTICATION BACKENDS
AUTHENTICATION_BACKENDS = [
    'accounts.backends.UsernameOrEmailBackend',
]

# DATABASES
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}

# AUTH PASSWORD VALIDATORS
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

# INTERNATIONALIZATION & TIME SETTINGS
LANGUAGE_CODE = 'en-us'
TIME_ZONE = 'UTC'
USE_I18N = True
USE_TZ = True

# MEDIA JS CSS CONFIGRATION
STATIC_URL = "/static/"
STATIC_ROOT = BASE_DIR / "staticfiles"
STATICFILES_DIRS = [BASE_DIR / "static"]
MEDIA_URL = "/media/"
MEDIA_ROOT = BASE_DIR / "media"

# DEFAULT AUTO FIELD
DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

# DOMAIN_NAME
DOMAIN_NAME = env.str('DOMAIN_NAME')

# TAILWIND APP NAME
TAILWIND_APP_NAME = "theme"

# SMTP EMAIL CONFIGRATION
EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST = 'smtp.gmail.com'
EMAIL_PORT = 587
EMAIL_USE_TLS = True

EMAIL_HOST_USER = 'rm77rasel@gmail.com'
EMAIL_HOST_PASSWORD = 'ncqf rrex rzrg jttr'

# SESSION CONFIGURATION
# 7 DAYS IN SECONDS: 7 * 24 * 60 * 60 = 604800
SESSION_COOKIE_AGE = 604800  
SESSION_EXPIRE_AT_BROWSER_CLOSE = False

# SMTP EMAIL CONFIGRATION
EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST = 'smtp.gmail.com'
EMAIL_PORT = 587
EMAIL_USE_TLS = True
EMAIL_HOST_USER = 'programmerwebrm@gmail.com'
EMAIL_HOST_PASSWORD = 'hspl dlxy rhax kmac'
DEFAULT_FROM_EMAIL = 'South Asian Football Federation <programmerwebrm@gmail.com>'

CSRF_TRUSTED_ORIGINS = [
    "https://dev.saff.mashaallahenterprise.com"
]

