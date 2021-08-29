import os
from datetime import timedelta

from envparse import env

# *****************************
# Environment specific settings
# *****************************

DEBUG = True

SECRET_KEY = 'DO_NOT_use_Unsecure_Secrets_in_production_environments'
COOKIE_SECURE = 'Secure'
COOKIE_DURATION = timedelta(days=365)

FLASK_PUBLIC_PORT = env.int('FLASK_PUBLIC_PORT')

ROOT_FILEPATH = os.path.realpath(os.path.dirname(__file__))

BABEL_TRANSLATION_DIRECTORIES = os.path.join(os.path.abspath(
    os.path.dirname(__file__)), 'translations/')

BABEL_DEFAULT_LOCALE = 'ru'


'''
# FUTURE FEATURE 

MAIL_SERVER = 'smtp.gmail.com'
MAIL_PORT = 587
MAIL_USE_SSL = False
MAIL_USE_TLS = True
MAIL_USERNAME = 'yourname@gmail.com'
MAIL_PASSWORD = 'password'
MAIL_DEFAULT_SENDER = '"Your Name" <yourname@gmail.com>'

ADMINS = [
    '"Admin One" <admin1@gmail.com>',
]
'''
