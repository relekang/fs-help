# -*- coding: utf-8 -*-
# Django settings for filtersystem project.

import os.path

BASE_PATH = os.path.dirname(__file__)

DEBUG = True
TEMPLATE_DEBUG = DEBUG

SERVER_EMAIL = 'data@lekang.com'

ADMINS = ()
MANAGERS = ADMINS

LFS_LOGIN_URL = ''
LFS_URL = ''
LFS_TOKEN = ''

if DEBUG:
    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.sqlite3',
            'NAME': 'project.db',
        }
    }

TIME_ZONE = 'Europe/Oslo'

LANGUAGE_CODE = 'no'
LANGUAGES = (
    ('en', 'Engelsk'),
    ('no', 'Norsk'),
    ('dk', 'Dansk'),
    ('se', 'Svensk'),
)

SITE_ID = 1

USE_I18N = True

MEDIA_ROOT = os.path.join(BASE_PATH, 'files/media')
MEDIA_URL = '/media/'
STATIC_URL = '/static/'

STATICFILES_DIRS = (
    os.path.join(BASE_PATH, 'files/static'),
)

# Make this unique, and don't share it with anybody.
SECRET_KEY = 'm%ly)xctv^5vckv3*p+(iwo)a+grz7x2i0f9@rw-3dxwdbcmj4'

# List of callables that know how to import templates from various sources.
TEMPLATE_LOADERS = (
    'django.template.loaders.filesystem.Loader',
    'django.template.loaders.app_directories.Loader',
)

MIDDLEWARE_CLASSES = (
    'django.middleware.common.CommonMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.middleware.doc.XViewMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'filtersystem.core.LocalUserMiddleware'
)

# STATICFILES_FINDERS = (
# 'django.contrib.staticfiles.finders.FileSystemFinder',
#   'django.contrib.staticfiles.finders.AppDirectoriesFinder',
#    'django.contrib.staticfiles.finders.DefaultStorageFinder',
# )

ROOT_URLCONF = 'filtersystem.urls'

TEMPLATE_DIRS = (
    os.path.join(BASE_PATH, 'templates'),
)
LOCALE_PATHS = (
    os.path.join(BASE_PATH, 'locale'),
)

INSTALLED_APPS = (
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.sites',
    'django.contrib.admin',
    #    'django.contrib.staticfiles',
    'django.contrib.messages',

    'filtersystem.core',
    'filtersystem.core.profiles',
    'filtersystem.lfs_help',
    'filtersystem.help_admin',
    'filtersystem.users',
)

# Override the server-derived value of SCRIPT_NAME
# See http://code.djangoproject.com/wiki/BackwardsIncompatibleChanges#lighttpdfastcgiandothers
FORCE_SCRIPT_NAME = ''
