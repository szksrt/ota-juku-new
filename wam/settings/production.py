from .base import *
import os
import dj_database_url

DEBUG = False

SECRET_KEY = os.environ['SECRET_KEY']

DATABASE_URL = os.environ['DATABASE_URL']

ALLOWED_HOSTS = []
RENDER_EXTERNAL_HOSTNAME = os.environ.get('RENDER_EXTERNAL_HOSTNAME')

if RENDER_EXTERNAL_HOSTNAME:
    ALLOWED_HOSTS.append(RENDER_EXTERNAL_HOSTNAME)

DATABASES = {
    'default': dj_database_url.config(default=DATABASE_URL, conn_max_age=600, ssl_require=True)
}

EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'

# Staticファイル最適化
STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'
