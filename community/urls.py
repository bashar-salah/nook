from django.urls import path
from . import views

urlpatterns = [
    path('', views.community, name='community'),
    path('room/<str:room_name>/', views.chatroom, name='room'),
    path('room/<str:room_name>/getMessages/<str:room_name1>/', views.getMessages, name='getMessages'),
    path('room/<str:room_name>/sendMessage/', views.sendMessage, name='sendMessage'),
    path('room/<str:room_name>/clear/', views.clearchat, name='clearchat'),
]
