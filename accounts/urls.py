from django.urls import path


from django.contrib.auth import login

from . import views

urlpatterns = [path("login", login, {"return": "accounts/login.html"}, name="login")]
