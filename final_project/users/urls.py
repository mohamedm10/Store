from django.urls import path
from . import views

app_name = 'users'

urlpatterns = [
    path('login', views.signin, name='login'),
    path('logout', views.signout, name='logout'),
    path('register', views.register, name='register'),

    path('all-users', views.users, name='users'),
]