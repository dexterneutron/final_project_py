from django.http.response import HttpResponse
from django.urls import path
from django.urls.conf import include

from . import views

urlpatterns = [
path('', views.feed, name = "feed"),

]
