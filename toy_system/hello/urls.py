from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.index, name='home'),
    url(r'^(?P<person_id>[0-9]+)/$', views.detail, name='detail'),
    url(r'^(?P<person_id>[0-9]+)/edit/$', views.edit, name='edit'),
]
