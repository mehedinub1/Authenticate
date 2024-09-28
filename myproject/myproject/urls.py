
from django.contrib import admin
from django.urls import path
from myproject.views import*
urlpatterns = [
    path('admin/', admin.site.urls),
    path('master/',master,name="master"),
    path('',registerpage,name="registerpage"),
    path('loginpage/',loginpage,name="loginpage"),
    path('logoutpage/',logoutpage,name="logoutpage"),
]
