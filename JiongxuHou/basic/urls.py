from django.urls import path
from . import views

app_name = 'basic'
urlpatterns = [
    path('',views.stations, name='stations'),
    path('Stations/',views.stations, name='stations'),
    path('Emission/', views.emission, name='emission'),
    path('Monitor/', views.monitor, name='monitor'),
    path('About/', views.about, name='about'),
]