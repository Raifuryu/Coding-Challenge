from django.contrib import admin
from django.urls import path
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from .views import RegistrationApiView

urlpatterns = [
    path('signup', RegistrationApiView.as_view(), name="Registration"),
    #path('token', TokenObtainPairView.as_view(), name="login"),
    #path('token-refresh', TokenRefreshView.as_view(), name="Refresh Token")
]
