from django.urls import path
from brawl import views

app_name = 'brawl'

urlpatterns = [
    path('', views.home, name='home'),
    path('home/', views.home, name='home'),
    path('event/<str:event_date>', views.show_event, name='show_event'),
    path('validate_decklist/', views.ValidateDecklistView.as_view(), name='validate_decklist'),
    path('events/', views.events, name='events'),
]