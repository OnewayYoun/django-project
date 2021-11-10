from django.urls import path
from . import views

urlpatterns = [
    path('', views.chat, name='chat'),
    path('<str:room>/', views.room, name='room'),
    path('checkview', views.checkview, name='checkview'),
    path('send', views.send, name='send'),
    path('get_messages/<str:room>/', views.get_messages, name='get_messages'),

]
