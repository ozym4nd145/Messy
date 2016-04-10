from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.LoginRequest, name='login'),
    url(r'^home/$', views.Home),
    url(r'^account.html/',views.Account),
    url(r'^logout/$',views.Logout),
    url(r'^reviews/$',views.Review),
]
