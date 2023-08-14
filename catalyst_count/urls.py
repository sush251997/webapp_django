from django.contrib import admin
from django.urls import path
from app import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name="home"),
    path('loginUser', views.loginUser, name="loginUser"),
    path('userIndex', views.userIndex, name="userIndex"),
    path('buildQuery', views.buildQuery, name="buildQuery"),
    path('addUser', views.addUser, name="addUser"),
    path('logout', views.logout, name="logout")

]
