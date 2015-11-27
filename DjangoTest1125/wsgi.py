"""
WSGI config for DjangoTest1125 project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/1.8/howto/deployment/wsgi/
"""

import os
 
from django.core.wsgi import get_wsgi_application
 
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "DjangoTest1125.settings")
 
application = get_wsgi_application()


# https://devcenter.heroku.com/articles/django-assets
# import os
# import sys
# 
# path = '/home/lstrue/django-blog'  # use your own username here
# if path not in sys.path:
#     sys.path.append(path)
# 
# os.environ['DJANGO_SETTINGS_MODULE'] = 'DjangoTest1125.settings'
# 
# from django.core.wsgi import get_wsgi_application
# from whitenoise.django import DjangoWhiteNoise
# application = DjangoWhiteNoise(get_wsgi_application())