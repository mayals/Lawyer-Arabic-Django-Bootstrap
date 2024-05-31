"""
Django settings for site_proj project.

Generated by 'django-admin startproject' using Django 3.1.4.

For more information on this file, see
https://docs.djangoproject.com/en/3.1/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/3.1/ref/settings/
"""

import django_heroku


from pathlib import Path
import os


# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/3.1/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'F8B87Faffb05C6Aaead64Ee31Be710C4Cbda6D086D9A0441'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = []


# Application definition
INSTALLED_APPS = [
    #--SuitConfig must be before admin--#
    'blog_app.apps.SuitConfig',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    #--local--#
    'pages_app.apps.PagesAppConfig',
    'blog_app.apps.BlogAppConfig',
    'account_app.apps.AccountAppConfig',
    #-- crispy_forms --#
    'crispy_forms',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'whitenoise.middleware.WhiteNoiseMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'site_proj.urls'

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
            ],
        },
    },
]

WSGI_APPLICATION = 'site_proj.wsgi.application'


# Database
# https://docs.djangoproject.com/en/3.1/ref/settings/#databases

DATABASES = {
    'default': {
        # 'ENGINE': 'django.db.backends.postgresql',
        # 'NAME': 'lawyer_db',
        # 'USER': 'postgres',
        # 'PASSWORD': 'burgerking_2010',
        # 'HOST': 'localhost',
        # 'PORT': '5432',


        
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',

         
    }
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
STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')

STATICFILES_DIRS = [os.path.join(BASE_DIR,'static')]
STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'


# -- MEDIA ---#
MEDIA_URL = '/media/'
# MEDIA_ROOT = os.path.join(BASE_DIR, 'media')-- this also work ok but it is old version need import os library
MEDIA_ROOT = BASE_DIR / 'media'






############################### Sending emails with Django  ###################################
############################   by using GMAIL(( smtp.gmail.com ))###############################################
#-------------------------- from book django by example2 ----page 121--#--also work ok :)
#---------------------------------(Muhammed essa) use in in new project 2020 book ------------------------------------


# send emails via Gmail servers using a Google account:
# -----------------------------------------------------
# EMAIL_HOST = 'smtp.gmail.com'
# EMAIL_HOST_USER = 'your_account@gmail.com'
# EMAIL_HOST_PASSWORD = 'your_password'
# EMAIL_PORT = 587
# EMAIL_USE_TLS = True



#EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend' ---dend to console not to true email
EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST = 'smtp.gmail.com'
EMAIL_HOST_USER = ''
EMAIL_HOST_PASSWORD = ''
EMAIL_PORT = 587
EMAIL_USE_TLS = True
#--------------------

#--  crispy_forms --#
CRISPY_TEMPLATE_PACK = 'bootstrap4'




# ---- heroku -----#
django_heroku.settings(locals())






############################### password_reset ###################################
############################  by useing sendgrid (smtp.sendgrid.net) ###############################################
#---------------------------- from book django for beginners --------------------also work ok :)
#---------------------------------------------------------------------
#EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
#DEFAULT_FROM_EMAIL = 'your_custom_email_account'
#EMAIL_HOST = 'smtp.sendgrid.net'
#EMAIL_HOST_USER = 'apikey'
#EMAIL_HOST_PASSWORD = 'sendgrid_password' ## this API key i do in sendgrid website for name:Newspaper
#EMAIL_PORT = 587
#EMAIL_USE_TLS = True
#---------------------------------



### --- from book django for beginners -- page 230 ---####
#we need sendgrid to send to true email 

# EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend' --- # notchange
# email account of my sendgrid account
# DEFAULT_FROM_EMAIL = 'mayalsanea2016@gmail.com'
# EMAIL_HOST = 'smtp.sendgrid.net'  # not change for any sendgrid
# EMAIL_HOST_USER = 'apikey'       # not change from sendgrid website page
## this API key i do in sendgrid website for name:Newspaper
# EMAIL_HOST_PASSWORD = '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'
# EMAIL_PORT = 587   # not change from sendgrid website page
# EMAIL_USE_TLS = True    # not change from sendgrid website page
