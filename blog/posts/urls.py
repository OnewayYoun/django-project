from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('register', views.register, name='register'),
    path('login', views.login, name='login'),
    path('logout', views.logout, name='logout'),
    path('blog', views.blog, name='blog'),
    path('post/<str:pk>', views.post, name='post'),
    path('blog/write', views.write, name='write'),
]