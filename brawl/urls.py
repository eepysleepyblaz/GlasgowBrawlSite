from django.urls import path
from brawl import views

app_name = 'brawl'

urlpatterns = [
    path('', views.home, name='home'),
]