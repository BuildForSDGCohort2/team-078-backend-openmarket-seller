import os
from pathlib import Path

from dotenv import load_dotenv, find_dotenv
import django_heroku
import dj_database_url

load_dotenv(find_dotenv())

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve(strict=True).parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/3.1/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = str(os.getenv('SECRET_KEY'))

# # SECURITY WARNING: don't run with debug turned on in production!
DEBUG = bool(os.getenv('DEBUG_STATUS'))

ALLOWED_HOSTS = ['*']


# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    # 'whitenoise.runserver_nostatic',
    'django.contrib.staticfiles',
    'django.contrib.sites',
    'allauth',
    'allauth.account',
    'allauth.socialaccount',
    'dj_rest_auth.registration',
    'allauth.socialaccount.providers.google',
    'allauth.socialaccount.providers.facebook',
    'rest_framework',
    'rest_framework.authtoken',
    'dj_rest_auth',
    # apps
    'api',
    'accounts',
    'store',
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
]

ROOT_URLCONF = 'openMarket.urls'

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
                # allauth
                'django.template.context_processors.request',
            ],
        },
    },
]

WSGI_APPLICATION = 'openMarket.wsgi.application'


# Database
# https://docs.djangoproject.com/en/3.1/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
    # 'default': {
    #     'ENGINE': str(os.getenv('DATABASE_ENGINE')), #django.db.backends.postgresql_psycopg2 ,django.db.backends.mysql
    #     'NAME': str(os.getenv('DATABASE_NAME')),
    #     'USER': str(os.getenv('DATABASE_USER')),  # root
    #     'PASSWORD': str(os.getenv('DATABASE_PASSWORD')),
    #     'HOST': str(os.getenv('DATABASE_HOST')),#localhost
    #     'PORT': str(os.getenv('DATABASE_PORT')),
    # }

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

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/3.1/howto/static-files/

STATIC_URL = '/static/'

STATIC_ROOT = os.path.join(BASE_DIR,'static')

STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'

AUTH_USER_MODEL = 'accounts.User'

REST_FRAMEWORK = {
  'DEFAULT_AUTHENTICATION_CLASSES': (
      'rest_framework.authentication.TokenAuthentication',
    #   'rest_framework.authentication.SessionAuthentication'
    )
}

AUTHENTICATION_BACKENDS = [
    'django.contrib.auth.backends.ModelBackend',
    # allauth
    'allauth.account.auth_backends.AuthenticationBackend',
]
EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'

SOCIALACCOUNT_PROVIDERS = {
    'google': {
        'APP': {
            'client_id': '123',
            'secret': '456',
            'key': ''
        }
    }
}

SITE_ID = 1
ACCOUNT_USER_MODEL_USERNAME_FIELD = None
ACCOUNT_USERNAME_REQUIRED = False
ACCOUNT_AUTHENTICATION_METHOD = 'email'
ACCOUNT_EMAIL_REQUIRED=True
# ACCOUNT_EMAIL_VERIFICATION = 'mandatory'

REST_AUTH_REGISTER_SERIALIZERS = {
    'REGISTER_SERIALIZER': 'api.serializers.RegisterSerializer',
}

REST_AUTH_SERIALIZERS = {
    'LOGIN_SERIALIZER': 'api.serializers.LoginSerializer',
}
if bool(os.getenv('HEROKU')):
    DATABASES['default'] = dj_database_url.config(conn_max_age=500)
    # db_from_env = dj_database_url.config(conn_max_age=500)
    # DATABASES['default'].update(db_from_env)
    
    
django_heroku.settings(locals())