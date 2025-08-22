from .base import *
import os
from dotenv import load_dotenv

# .envファイルを読み込む
load_dotenv()

DEBUG = True

SECRET_KEY = os.environ.get('SECRET_KEY')

ALLOWED_HOSTS = ['localhost', '127.0.0.1']

EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'
