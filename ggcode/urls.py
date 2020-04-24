from django.conf.urls import url, include
from django.contrib import admin
from ggcode import views


urlpatterns = [
    url(r'^$', views.GeoCodeView, name='geocode'),
]
