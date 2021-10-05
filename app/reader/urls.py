from django.http.response import HttpResponse
from django.conf.urls import url
from reader import views

from . import views

urlpatterns = [
    url(r'^$', views.MainPage.as_view())
]
