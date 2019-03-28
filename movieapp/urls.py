from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.showmovie),
    url(r'^page/$', views.djangopage),
]