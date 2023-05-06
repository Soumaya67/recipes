from django.urls import path

from . import views, admin
from .views import *
from django.contrib.auth import views as auth_views
urlpatterns = [

     path('login/', auth_views.LoginView.as_view(),name='login'),
     path('signup/', views.SignupPage,name='signup'),
     path('home/', views.home, name='home'),
     path('faqs/', views.faqs, name='faqs'),
     path('aboutus/', views.aboutus, name='aboutus'),
     path('contact_us/', views.contactus, name='contactus'),
     path('ourteam/', views.ourteam, name='ourteam'),
     path('logout/', auth_views.LogoutView.as_view(), name='logout'),
     path('', dashboard, name='dashboard'),
     path('password_change/', auth_views.PasswordChangeView.as_view(), name='password_change'),
     path('password_change_done/', auth_views.PasswordChangeDoneView.as_view(),name='password_change_done'),


]