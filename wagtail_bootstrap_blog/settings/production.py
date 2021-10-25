from __future__ import absolute_import, unicode_literals
from .base import *
import dj_database_url

DEBUG = int(os.environ.get("DEBUG", default=1))
SECRET_KEY = os.environ.get("SECRET_KEY")
ALLOWED_HOSTS = os.environ.get("DJANGO_ALLOWED_HOSTS").split(" ")

DATABASES['default'] =  dj_database_url.config()
    
# Honor the 'X-Forwarded-Proto' header for request.is_secure()
SECURE_PROXY_SSL_HEADER = ('HTTP_X_FORWARDED_PROTO', 'https')

# DO NOT use on production, test key is available in the URL below
# https://developers.google.com/recaptcha/docs/faq
RECAPTCHA_PUBLIC_KEY: '6Lc1cPMbAAAAAAd2S996JYEtBG2xXFwL3msYHxAt'
RECAPTCHA_PRIVATE_KEY: '6Lc1cPMbAAAAAO_94mWAv7keFlhRTWf8OQ1adWNo'
NOCAPTCHA = True
SILENCED_SYSTEM_CHECKS = ["captcha.recaptcha_test_key_error"]

STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'
COMPRESS_OFFLINE = True
COMPRESS_CSS_FILTERS = [
    'compressor.filters.css_default.CssAbsoluteFilter',
    'compressor.filters.cssmin.CSSMinFilter',
]
COMPRESS_CSS_HASHING_METHOD = 'content'


try:
    from .local import *
except ImportError:
    pass
