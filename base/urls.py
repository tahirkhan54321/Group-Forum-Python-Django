from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name="home"),
    path('room/<str:pk>/', views.room, name="room"), #pk stands for primary key
    path('create-room/', views.createRoom, name="create-room"),
]