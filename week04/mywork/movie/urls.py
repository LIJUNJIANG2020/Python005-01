from django.urls import path, include, re_path
from . import views

app_name = 'movie'

urlpatterns = [
    path('', views.list, name='list'),
    re_path('comm/(?P<pk>[0-9]+)?/$', views.commnet, name='comm'),
]