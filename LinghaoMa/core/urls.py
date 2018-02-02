from django.contrib import admin
from django.urls import path
from . import views

app_name = 'core'
urlpatterns = [
    path('', views.emission, name="emission"),
    path('station/', views.station),
    path('monitor/', views.monitor, name='monitor'),
    path('about/', views.about, name='about')
]