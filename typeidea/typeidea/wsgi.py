"""
WSGI config for typeidea project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/3.0/howto/deployment/wsgi/
"""

import os

from django.core.wsgi import get_wsgi_application

# os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'typeidea.settings')

profile = os.environ.get('TYPEIDEA_PROFILE', 'develop') #新增，调用settings文件夹中的配置文件
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "typeidea.settings.%s" % profile) #新增，调用settings文件夹中的配置文件

application = get_wsgi_application()
