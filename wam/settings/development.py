from .base import *

DEBUG = True

SECRET_KEY = 'dev-secret-key'

ALLOWED_HOSTS = ['localhost', '127.0.0.1']

EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'
