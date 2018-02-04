from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [

    # url(r'^$',views.home),
    # url(r'^$',views.Stations,name='Stations'),
    path('', views.home, name='home'),
    path('Stations/', views.stations, name='Stations'),
    path('Emission/', views.emission, name='Emission'),
    path('Monitor/', views.monitor, name='Monitor'),
    path('About/', views.about, name='About')
]
