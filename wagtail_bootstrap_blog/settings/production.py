from .base import *
import dj_database_url

DEBUG = int(os.environ.get("DEBUG", default=1))
SECRET_KEY = os.environ.get("SECRET_KEY")
ALLOWED_HOSTS = os.environ.get("DJANGO_ALLOWED_HOSTS").split(" ")

# DO NOT use on production, test key is available in the URL below
# https://developers.google.com/recaptcha/docs/faq
RECAPTCHA_PUBLIC_KEY: '6Lc1cPMbAAAAAAd2S996JYEtBG2xXFwL3msYHxAt'
RECAPTCHA_PRIVATE_KEY: '6Lc1cPMbAAAAAO_94mWAv7keFlhRTWf8OQ1adWNo'
NOCAPTCHA = True
SILENCED_SYSTEM_CHECKS = ["captcha.recaptcha_test_key_error"]

STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'

if "DATABASE_URL" in env:
    DATABASES['default'] = dj_database_url.config(conn_max_age=600, ssl_require=True)


try:
    from .local import *
except ImportError:
    pass
