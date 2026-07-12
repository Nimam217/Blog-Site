"""
Django settings for mysite project.


For more information on this file, see
https://docs.djangoproject.com/en/5.2/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/5.2/ref/settings/
"""

from pathlib import Path
import os
# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/5.2/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = os.environ.get("SECRET_KEY")

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = os.environ.get('DEBUG', '0') == '1'

ALLOWED_HOSTS = ["*"]


# Application definition

INSTALLED_APPS = [
    'multi_captcha_admin',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'core.apps.CoreConfig',
    'blog.apps.BlogConfig',
    'accounts.apps.AccountsConfig',
    'contact.apps.ContactConfig',
    'django.contrib.humanize',
    'django.contrib.sites',
    'django.contrib.sitemaps',
    'robots',
    'debug_toolbar',
    'taggit',
    'django_summernote',
    'captcha'
    
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'debug_toolbar.middleware.DebugToolbarMiddleware'
]

ROOT_URLCONF = 'mysite.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [BASE_DIR / 'templates'],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
                'django.template.context_processors.media',
            ],
        },
    },
]

WSGI_APPLICATION = 'mysite.wsgi.application'


# Database
# https://docs.djangoproject.com/en/5.2/ref/settings/#databases

# Source - https://stackoverflow.com/a/5421511
# Posted by Alireza Savand, modified by community. See post 'Timeline' for change history
# Retrieved 2026-07-02, License - CC BY-SA 3.0

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': os.environ.get("POSTGRES_DB"),
        'USER': os.environ.get("POSTGRES_USER"),
        'PASSWORD': os.environ.get("POSTGRES_PASSWORD"),
        'HOST': 'db',
        'PORT': '5432',
    }
}



# Password validation
# https://docs.djangoproject.com/en/5.2/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/5.2/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/5.2/howto/static-files/

STATIC_URL= '/static/'
STATIC_ROOT=BASE_DIR / 'staticfiles'
STATICFILES_DIRS=[
    BASE_DIR / 'static'
]
MEDIA_URL= "/media/"
MEDIA_ROOT= BASE_DIR / "media"

# Default primary key field type
# https://docs.djangoproject.com/en/5.2/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

# messages

from django.contrib.messages import constants as messages

# sites framework

SITE_ID = 3

#robots

ROBOTS_USE_HOST = False
ROBOTS_USE_SITEMAP = False

#debug_toolbar

INTERNAL_IPS = [
    '127.0.0.1',
]

#summernote
SUMMERNOTE_THEME = 'bs5'  # Show summernote with Bootstrap5
X_FRAME_OPTIONS = "SAMEORIGIN"
SUMMERNOTE = "bs5"


SUMMERNOTE_CONFIG = {
    'iframe': True,

    'summernote': {
        'airMode': False,
        'width': '300%',
        'height': '480',

        # زبان خودکار مرورگر
        'lang': None,

        'toolbar': [
            ['style', ['style']],
            ['font', ['bold', 'underline', 'clear']],
            ['fontname', ['fontname']],
            ['color', ['color']],
            ['para', ['ul', 'ol', 'paragraph']],
            ['table', ['table']],
            ['insert', ['link', 'picture', 'video']],
            ['view', ['fullscreen', 'codeview', 'help']],
        ],

        'print': {
            'stylesheetUrl': '/static/css/printable.css',
        },

        'codemirror': {
            'mode': 'htmlmixed',
            'lineNumbers': True,
            'theme': 'monokai',
        },
    },

    # پیوست‌ها
    'attachment_require_authentication': True,
    'disable_attachment': False,
    'attachment_absolute_uri': True,

    # در صورت نیاز
    # 'attachment_upload_to': my_custom_upload_to_func,
    # 'attachment_storage_class': 'my.custom.storage.class.name',
    # 'attachment_model': 'my.custom.attachment.model',

    # فایل‌های اضافی
    'css': (
        '//cdnjs.cloudflare.com/ajax/libs/codemirror/5.29.0/theme/monokai.min.css',
    ),

    'js': (
        '/static/js/summernote-ext-print.js',
    ),

    # برای inplace widget
    'css_for_inplace': (),
    'js_for_inplace': (),

    # مقداردهی تنبل
    'lazy': True,
}

# admin captcha
MULTI_CAPTCHA_ADMIN = {
    'engine': 'simple-captcha',
}