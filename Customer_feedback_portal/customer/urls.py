from django.urls import path

from . import views

urlpatterns = [
    path('',views.login),
    path('home', views.home,name='home'),
    path('signup', views.signup, name='signup'),
    path('login',views.login,name='login'),
    path('feedback',views.feedback,name='feedback'),
    path('logout',views.logout,name='logout')
]