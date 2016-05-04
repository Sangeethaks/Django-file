from django.conf.urls import patterns, url,include
from . import views

urlpatterns = patterns('myapp.views',
    url(r'^$','list', name='list'),


)
