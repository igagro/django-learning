from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import permissions, generics
from rest_framework_jwt.settings import api_settings

from django.contrib.auth import authenticate, get_user_model, login, logout
from django.db.models import Q
from django.shortcuts import get_object_or_404

from .models import *
from .permissions import AnnonPermisionOnly

from .serializers import (UserRegisterSerializer,
                          ProfileSerializer,
                          UserLoginSerializer)


jwt_payload_handler = api_settings.JWT_PAYLOAD_HANDLER
jwt_encode_handler = api_settings.JWT_ENCODE_HANDLER
jwt_response_payload_handler = api_settings.JWT_RESPONSE_PAYLOAD_HANDLER

User = get_user_model()


class LoginView(APIView):
    permission_classes = [AnnonPermisionOnly]
    serializer_class = UserLoginSerializer

    def post(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            return Response({'detail': 'You are already authenticated'},
                            status=400)
        data = request.data
        username = data.get('username')
        password = data.get('password')
        user = authenticate(username=username, password=password)

        user_obj = get_object_or_404(
            User, Q(username__iexact=username) | Q(email__iexact=username)
        )

        if user_obj.check_password(password):
            user = user_obj
            payload = jwt_payload_handler(user)
            token = jwt_encode_handler(payload)
            response = jwt_response_payload_handler(
                token, user, request=request)
            login(request, user)
            return Response(response)
        return Response({'detail': "Invalid credentials"}, status=401)


class RegisterAPIView(generics.CreateAPIView):
    serializer_class = ProfileSerializer
    permission_classes = [AnnonPermisionOnly]


class LogoutView(APIView):
    permission_classes = [permissions.IsAuthenticated]

    def get(self, request):
        try:
            logout(request)
            return Response({'detail': "You're logged out"})
        except:
            return Response({'detail': "Can't log out. Try again"})
