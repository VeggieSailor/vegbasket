import os

from django.utils.translation import ugettext_lazy as _
PROJECT_DIR = os.path.dirname(__file__)

BASE_DIR = os.path.dirname(os.path.dirname(__file__))
LOCALE_DIR = os.path.join(BASE_DIR, 'locale')
#TEMPLATE_DIRS = (
    ## Put strings here, like "/home/html/django_templates" or "C:/www/django/templates".
    ## Always use forward slashes, even on Windows.
    ## Don't forget to use absolute paths, not relative paths.
    #os.path.join(PROJECT_DIR, "templates"),

#)

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.7/howto/deployment/checklist/

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

#TEMPLATE_DEBUG = True

ALLOWED_HOSTS = []

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                # Insert your TEMPLATE_CONTEXT_PROCESSORS here or use this
                # list if you haven't customized them:
                'django.contrib.auth.context_processors.auth',
                'django.template.context_processors.debug',
                'django.template.context_processors.i18n',
                'django.template.context_processors.media',
                'django.template.context_processors.static',
                'django.template.context_processors.tz',
                'django.contrib.messages.context_processors.messages',
            ],     
            },
    },
]


# Application definition

INSTALLED_APPS = (
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.sites',
    'django.contrib.flatpages',
    'meta',
    'haystack',
    'foundation',
    'vegbasketapp.home',
    'vegbasketapp.transformer',
    'vegbasketapp.personal',
    'vegbasketapp.content',
    'vegbasketapp.frontend',
    'vegbasketapp.diary',
    'vegbasketapp.vegapi',
    'vegbasketapp.recipe',
    'social.apps.django_app.default',
    'django_sb_admin',
    'django-dia',
    
    
)
AUTHENTICATION_BACKENDS = (
    'social.backends.facebook.FacebookOAuth2',
    'social.backends.open_id.OpenIdAuth',
    'social.backends.google.GoogleOAuth2',
    'social.backends.persona.PersonaAuth',    
    'social.backends.vk.VKOAuth2',
    'django.contrib.auth.backends.ModelBackend',
)
MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.locale.LocaleMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.auth.middleware.SessionAuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'vegbasketapp.personal.middlewares.VSSocialAuthExceptionMiddleware'
)

ROOT_URLCONF = 'vegbasketapp.urls'

WSGI_APPLICATION = 'vegbasketapp.wsgi.application'


# Database
# https://docs.djangoproject.com/en/1.7/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2', # Add 'postgresql_psycopg2', 'mysql', 'sqlite3' or 'oracle'.
        'NAME': 'vegbasket',                      # Or path to database file if using sqlite3.
        # The following settings are not used with sqlite3:
        'USER': 'veggiesailor',
        'PASSWORD': 'veggiesailor',
        'HOST': '127.0.0.1',                      # Empty for localhost through domain sockets or '127.0.0.1' for localhost through TCP.
        'PORT': '',                      # Set to empty string for default.
    }
}


# Internationalization
# https://docs.djangoproject.com/en/1.7/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.7/howto/static-files/

STATIC_URL = '/static/'

# Additional locations of static files
STATICFILES_DIRS = (
        os.path.join(PROJECT_DIR, "static/"),
)

from vegbasketapp.settings_secret import *
# DEBUG=False
ALLOWED_HOSTS=['localhost:8000']

# Days
DEFALT_EXPIRE_TIME = 3

SOCIAL_AUTH_NEW_USER_REDIRECT_URL = '/accounts/setup/'
AUTH_PROFILE_MODULE = 'vegbasketapp.personal.models.UserProfile'

SOCIAL_AUTH_PIPELINE = (
    'social.pipeline.social_auth.social_details',
    'social.pipeline.social_auth.social_uid',
    'social.pipeline.social_auth.auth_allowed',
    'social.pipeline.social_auth.social_user',
    'social.pipeline.user.get_username',
    'social.pipeline.user.create_user',
    'vegbasketapp.personal.pipeline.save_profile',  # <--- set the import-path to the function
    'social.pipeline.social_auth.associate_user',
    'social.pipeline.social_auth.load_extra_data',
    'social.pipeline.user.user_details'
)

LOGIN_REDIRECT_URL = '/p/'
MEDIA_ROOT = 'media/'
MEDIA_URL = '/media/'

HAYSTACK_CONNECTIONS = {
    'default': {
        'ENGINE': 'haystack.backends.elasticsearch_backend.ElasticsearchSearchEngine',
        'URL': 'http://127.0.0.1:9200/',
        'INDEX_NAME': 'haystack',
    },
}


META_SITE_DOMAIN = 'veggiesailor.com'
META_SITE_TYPE = 'restaurant.restaurant'
META_SITE_NAME = 'Veggie Sailor'
META_IMAGE_URL = 'https://veggiesailor.com/static/frontend/img/logo.png'
META_DEFAULT_KEYWORDS = ['Veggie Sailor', 'Vegeterian', 'Vegan', 'Veggie', 'Bar', 'Hotel', 'Restaurant']
META_USE_OG_PROPERTIES = True
META_USE_TWITTER_PROPERTIES = True

if DEBUG:
    INSTALLED_APPS = list(INSTALLED_APPS)
    INSTALLED_APPS.insert(3,'debug_toolbar')
    INSTALLED_APPS = tuple(INSTALLED_APPS)
    
    MIDDLEWARE_CLASSES = list(MIDDLEWARE_CLASSES)
    MIDDLEWARE_CLASSES.insert(3, 'debug_toolbar.middleware.DebugToolbarMiddleware')
    MIDDLEWARE_CLASSES = tuple(MIDDLEWARE_CLASSES)
    DEBUG_TOOLBAR_PATCH_SETTINGS = True
    

LANGUAGES = [
    ('ru', _('Russian')),
    ('en', _('English')),
    ('es', _('Spanish'))
]

#from vegbasketapp.dummy_trans import output
LOCALE_PATHS = (LOCALE_DIR,)
SITE_ID = 1
