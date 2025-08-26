from django.urls import path, include
from passwords import views

app_name = 'passwords'

urlpatterns = [
    path('', views.index, name='index'),
    path('register', views.registration, name='register'),
    path('logout', views.user_logout, name='user_logout'),
    path('login', views.user_login, name='user_login'),
]