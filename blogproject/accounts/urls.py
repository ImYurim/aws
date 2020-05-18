from django.contrib import admin
from django.urls import path, include
import accounts.views

urlpatterns = [

    path('signup/', accounts.views.signup, name="signup"),
    path('login/', accounts.views.login, name="login"),

]
