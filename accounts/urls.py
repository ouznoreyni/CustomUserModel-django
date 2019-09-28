from django.urls import path
from . import views

app_name='accounts'
urlpatterns = [
    path('', views.index, name='home'),
    path('dashboard', views.dashboard, name='dashboard'),
    path('register', views.registerView, name='register'),
    path('login', views.loginView, name='login'),
    path('logout', views.logoutView, name='logout'),
]