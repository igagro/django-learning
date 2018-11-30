from django.contrib import admin
from django.urls import include, path
from rest_framework_jwt.views import obtain_jwt_token, refresh_jwt_token
from accounts import views
from .views import LoginView

urlpatterns = [
    path('login/', LoginView.as_view()),
    path('login-jwt/', obtain_jwt_token),
    path('login/refresh-jwt/', refresh_jwt_token)
]
