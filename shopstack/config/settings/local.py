from .base import *

DEBUG = True

# IP that requests come from. For debug toolbar.
# Added print request.META.get('REMOTE_ADDR', None) in views to see IP.
INTERNAL_IPS = ('127.0.0.1', '10.0.2.2',)

INSTALLED_APPS += (
    'debug_toolbar',
)
