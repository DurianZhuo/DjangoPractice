from django.conf.urls import url
from . import views
urlpatterns = [
    url(r'^$', views.register),
    url(r'^showall/$', views.showall),
    url(r'^getstu/$', views.getstu),
]