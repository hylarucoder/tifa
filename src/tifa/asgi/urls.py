import datetime

from django.http import HttpResponse
from django.urls import path


def index(request):
    now = datetime.datetime.now()
    html = "<html><body>It is now %s.</body></html>" % now
    return HttpResponse(html)


api_urls = [
    path("", index),
]

urlpatterns = api_urls
