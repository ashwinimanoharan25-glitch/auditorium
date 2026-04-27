from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('history/',views.history,name='history'),
    path('booking/', views.booking_page, name='booking'),
]
