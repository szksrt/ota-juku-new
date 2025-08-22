from .base import *
import os

from dotenv import load_dotenv
load_dotenv()


DEBUG = False

SECRET_KEY = os.environ['SECRET_KEY']  # 必須

ALLOWED_HOSTS = ['ota-juku-new.onrender.com']

EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'

# Staticファイル最適化
STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'
