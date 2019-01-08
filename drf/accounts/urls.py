from django.contrib import admin
from django.urls import include, path
from rest_framework_jwt.views import obtain_jwt_token, refresh_jwt_token
from .views import LoginView, RegisterAPIView, LogoutView

app_name = 'accounts'
urlpatterns = [
    path('login/', LoginView.as_view(), name='login'),
    path('register/', RegisterAPIView.as_view(), name='register'),
    path('login-jwt/', obtain_jwt_token),
    path('login/refresh-jwt/', refresh_jwt_token),
    path('logout/', LogoutView.as_view())
]
