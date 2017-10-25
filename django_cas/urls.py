__author__ = 'sannies'

from django.conf.urls import url

from django_cas.views import login, logout, proxy_callback


urlpatterns = [
    url(r'^login$', login, name="cas_login"),
    url(r'^logout$', logout, name="cas_logout"),
    url(r'^proxycallback$', proxy_callback, name="cas_proxy_callback"),
]
