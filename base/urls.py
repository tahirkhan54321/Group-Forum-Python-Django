
# This file is responsible for mapping URL patterns to Python functions (views). 
# It's where you define the URL routes for your application.

from django.urls import path
from . import views

urlpatterns = [
    path('login/', views.loginPage, name='login'),
    path('logout/', views.logoutUser, name='logout'),
    path('', views.home, name="home"),
    path('room/<str:pk>/', views.room, name="room"), #pk stands for primary key
    path('create-room/', views.createRoom, name="create-room"),
    path('update-room/<str:pk>/', views.updateRoom, name="update-room"),
    path('delete-room/<str:pk>/', views.deleteRoom, name="delete-room"),
]