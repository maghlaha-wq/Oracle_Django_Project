from django.urls import path
from . import views

urlpatterns = [
    path('reserver/', views.reserver, name='reserver'),
    path('reservations/', views.lister_reservations, name='lister_reservations'),
    path('notifications/', views.lister_notifications, name='lister_notifications'),
]