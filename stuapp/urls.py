from django.conf.urls import url



from . import views

urlpatterns = [
    url(r'^register/$', views.register),
    url(r'^showinfo/$', views.showinfo),
    url(r'^login/$', views.login),
    url(r'^pic/$', views.pic),
    url(r'^showpic/$', views.showpic),
    url(r'^setcookie/$', views.setcookie),
    url(r'^getcookie/$', views.getcookie),


]




