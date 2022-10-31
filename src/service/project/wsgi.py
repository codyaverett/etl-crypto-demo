"""
WSGI config for project project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/4.1/howto/deployment/wsgi/
"""
import os
from dotenv import load_dotenv
from django.core.wsgi import get_wsgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'project.settings')

# Load dotenv file from the project src directory
dotenv_file = os.path.join(os.path.join(os.path.dirname(__file__), ".env"))
load_dotenv(dotenv_file, override=True)

application = get_wsgi_application()
