from django.urls import path
from . import views


urlpatterns = [
    path('', views.login_user, name='login'),
    path('home', views.baseView, name='home'),
    path('logout', views.logout_user,name='logout'),
]