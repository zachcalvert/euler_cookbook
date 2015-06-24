"""
Django settings for euler_cookbook project.

For more information on this file, see
https://docs.djangoproject.com/en/1.7/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.7/ref/settings/
"""

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
import os
BASE_DIR = os.path.dirname(os.path.dirname(__file__))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.7/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'n=!uuzh5#7%c_c4#*6p_qk%3we&r@mh)5av3d9+bqm2j$_8#i^'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = False

TEMPLATE_DEBUG = False

ALLOWED_HOSTS = ['.eulerscookbook.org','127.0.0.1', 'localhost']


# Application definition

INSTALLED_APPS = (
    'grappelli',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',

    'accounts',
    'django_extensions',
    'problems',
    'rest_framework',
)

MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.auth.middleware.SessionAuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
)

ROOT_URLCONF = 'euler_cookbook.urls'

WSGI_APPLICATION = 'euler_cookbook.wsgi.application'


REST_FRAMEWORK = {
    # Use Django's standard `django.contrib.auth` permissions,
    # or allow read-only access for unauthenticated users.
    'DEFAULT_PERMISSION_CLASSES': [
        'rest_framework.permissions.DjangoModelPermissionsOrAnonReadOnly'
    ]
}


# Database
# https://docs.djangoproject.com/en/1.7/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'eulerdb',
        'USER': 'root',
        'PASSWORD': '',
        'HOST': '127.0.0.1',
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

STATIC_ROOT = os.path.join(BASE_DIR, 'www', 'static')
STATICFILES_DIRS = (os.path.join(BASE_DIR, 'www', 'media'),)
STATIC_URL = '/static/'
STATICFILES_STORAGE = 'django.contrib.staticfiles.storage.StaticFilesStorage'

COMPRESS_ENABLED = False  # safe default, expect override in settings_local.py
COMPRESS_ROOT = STATIC_ROOT
COMPRESS_URL = STATIC_URL
COMPRESS_STORAGE = STATICFILES_STORAGE

STATICFILES_FINDERS = (
    'django.contrib.staticfiles.finders.AppDirectoriesFinder',
    'compressor.finders.CompressorFinder',
    'django.contrib.staticfiles.finders.FileSystemFinder',
)

COMPRESS_CSS_FILTERS = [
    # Disable default filter to prevent compressed assets
    # from diverging across app servers.
    #'compressor.filters.css_default.CssAbsoluteFilter',
    'compressor.filters.cssmin.CSSMinFilter',
]
