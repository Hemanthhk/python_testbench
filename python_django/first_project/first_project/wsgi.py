"""
WSGI config for first_project project.
The Web Server Gateway Interface (WSGI) is a standard interface between web servers and Python web applications or frameworks.
WSGI acts as a middleman that allows your Python code (like Flask, Django, etc.) 
to communicate with web servers (like Gunicorn, uWSGI, Apache with mod_wsgi, or Nginx via a WSGI server).



It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/4.2/howto/deployment/wsgi/
"""

import os

from django.core.wsgi import get_wsgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'first_project.settings')

application = get_wsgi_application()
