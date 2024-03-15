import logging
import os

from django.core.asgi import get_asgi_application
from fastapi import FastAPI

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "tifa.settings")

django_application = get_asgi_application()

logger = logging.getLogger()
app = FastAPI()
from tifa.app import current_app

current_app.mount("/dj/api", django_application)

application = current_app
