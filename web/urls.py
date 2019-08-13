from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('devices', views.table, name='devices'),
    path('config', views.config, name='config'),
]
