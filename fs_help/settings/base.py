import os

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

SECRET_KEY = 'eg&k$aj-m-!_ex*mya%%gn(*i)+z!n-d^(1wuc=1#yx#j35j8#'
DEBUG = True
ALLOWED_HOSTS = []


INSTALLED_APPS = (
    'fs_help.core',
    'fs_help.core.profiles',
    'fs_help.lfs_help',
    'fs_help.help_admin',
    'fs_help.users',

    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
)

MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.auth.middleware.SessionAuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'django.middleware.security.SecurityMiddleware',
    'fs_help.core.LocalUserMiddleware'
)

ROOT_URLCONF = 'fs_help.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [
            os.path.join(BASE_DIR, 'templates'),
        ],
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

WSGI_APPLICATION = 'fs_help.wsgi.application'

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}

TIME_ZONE = 'Europe/Oslo'

LANGUAGE_CODE = 'en'
LANGUAGES = (
    ('en', 'Engelsk'),
    ('no', 'Norsk'),
    ('dk', 'Dansk'),
    ('se', 'Svensk'),
)

USE_I18N = True
USE_L10N = True
USE_TZ = True

STATIC_URL = '/static/'
STATICFILES_DIRS = os.path.join(BASE_DIR, 'files/static'),
LOCALE_PATHS = os.path.join(BASE_DIR, 'locale'),
