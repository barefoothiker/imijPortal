"""
Django settings for chronux project.

For more information on this file, see
https://docs.djangoproject.com/en/1.7/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.7/ref/settings/
"""

import os

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
#import pyexcel.ext.xlsx  # This is required for tmp file handlers.

#import pyexcel.ext  # This is required for tmp file handlers.

BASE_DIR = os.path.dirname(os.path.dirname(__file__))

PROJECT_BASE_FOLDER = BASE_DIR
TFS_PROJECTS = ["FRONTIERS","MMRFClonality","MSSM","PCD","TEST"]
CURRENT_PROJECT = ""
BASE_DATA_FOLDER = "/data1/daphni/"
DATA_FOLDER = BASE_DATA_FOLDER+"web/data/"
IMAGE_FOLDER = BASE_DATA_FOLDER+"web/img/"

ROOT_URLCONF = 'daphniFrontendPatientDB.urls'

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.7/howto/deployment/checklist/

## Make this unique, and don't share it with anybody.
SECRET_KEY = 'idmm)d5h)kwxcopo%0rirfk@^88xcki4dx#slgp5_v#0)lt7gd'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

#TEMPLATE_DEBUG = True

ALLOWED_HOSTS = ['*']

# Application definition
INSTALLED_APPS = (
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'daphniFrontendPatientDB',
    'corsheaders',
    'registration'
)
CORS_ORIGIN_ALLOW_ALL = True
CORS_ALLOW_CREDENTIALS = False
MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
#     'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.auth.middleware.SessionAuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'corsheaders.middleware.CorsMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
)
# allow access to angular
CORS_ORIGIN_ALLOW_ALL = True

# # table prefix name
# DB_PREFIX = 'daphniFrontend'
# # Local time zone for this installation. Choices can be found here:
# DATABASES = {
#     'default': {
#         'ENGINE': 'django.db.backends.mysql', # Add 'postgresql_psycopg2', 'postgresql', 'mysql', 'sqlite3' or 'oracle'.
#         'NAME': 'daphniwebdb',                      # Or path to database file if using sqlite3.
#         'USER': 'benoitai',                      # Not used with sqlite3.
#         'PASSWORD': 'riker',                  # Not used with sqlite3.
#         'HOST': 'crusher.mssm.edu',                      # Set to empty string for localhost. Not used with sqlite3.
#         #'HOST': 'ec2-54-224-162-101.compute-1.amazonaws.com',
#         #'USER': 'root',                      # Not used with sqlite3.
#         #'PASSWORD': 'admin',                  # Not used with sqlite3.
#         #'HOST': 'localhost',                      # Set to empty string for localhost. Not used with sqlite3.
#         'PORT': '3306',                      # Set to empty string for default. Not used with sqlite3.
#         'OPTIONS': {
#             'init_command': 'SET default_storage_engine=INNODB',
#             }
#     }
# }
# table prefix name
DB_PREFIX = 'daphniFrontendPatientDB'
# Local time zone for this installation. Choices can be found here:



DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql', # Add 'postgresql_psycopg2', 'postgresql', 'mysql', 'sqlite3' or 'oracle'.
        'NAME': 'daphnipatients',                      # Or path to database file if using sqlite3.
        'USER': 'benoitai',                      # Not used with sqlite3.
        'PASSWORD': 'riker',                  # Not used with sqlite3.
        'HOST': 'crusher.mssm.edu',                      # Set to empty string for localhost. Not used with sqlite3.
        #'HOST': 'ec2-54-224-162-101.compute-1.amazonaws.com',
        #'USER': 'root',                      # Not used with sqlite3.
        #'PASSWORD': 'admin',                  # Not used with sqlite3.
        #'HOST': 'localhost',                      # Set to empty string for localhost. Not used with sqlite3.
        'PORT': '3306',                      # Set to empty string for default. Not used with sqlite3.
        'OPTIONS': {
            'init_command': 'SET default_storage_engine=INNODB',
            }
    }
}
# Internationalization
# https://docs.djangoproject.com/en/1.7/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True

STATICFILES_DIRS = [
     os.path.join(BASE_DIR, './static'),
]

STATIC_URL = '/static/'

# TEMPLATE_DIRS = (
#     BASE_DIR + '/templates/',
# )

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.contrib.auth.context_processors.auth',
            ],
            },
    },
]

FILE_UPLOAD_HANDLERS = ("django.core.files.uploadhandler.MemoryFileUploadHandler",
                        "django.core.files.uploadhandler.TemporaryFileUploadHandler",)


LOGIN_REDIRECT_URL = "/webdaphni/"
