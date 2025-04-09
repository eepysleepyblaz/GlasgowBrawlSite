from django.urls import path
from brawl import views

app_name = 'brawl'

urlpatterns = [
    path('', views.home, name='home'),
    path('home/', views.home, name='home'),
    path('validate_decklist/', views.ValidateDecklistView.as_view(), name='validate_decklist'),
]