from django.urls import path

from . import views

urlpatterns = [
  path('', views.room, name='room'),
  path('send/', views.send, name='send'),
  path('get_messages/', views.get_messages, name='get_messages'),
]