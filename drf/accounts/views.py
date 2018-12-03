from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import permissions
from rest_framework_jwt.settings import api_settings

from django.contrib.auth import authenticate
from django.contrib.auth.models import User
from django.db.models import Q

jwt_payload_handler = api_settings.JWT_PAYLOAD_HANDLER
jwt_encode_handler = api_settings.JWT_ENCODE_HANDLER
jwt_response_payload_handler = api_settings.JWT_RESPONSE_PAYLOAD_HANDLER

# User = get_user_model()


class ExampleView(APIView):
    permission_classes = [permissions.IsAuthenticated]

    def get(self, request, format=None):
        content = {
            'status': 'request was permitted'
        }
        return Response(content)


class LoginView(APIView):
    authentication_classes = []
    permission_classes = [permissions.AllowAny]

    def post(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            return Response({'detail': 'You are already authenticated'},
                            status=400)
        data = request.data
        username = data.get('username')
        password = data.get('password')
        user = authenticate(username=username, password=password)

        try:
            user_obj = User.objects.get(Q(username__iexact=username) |
                                        Q(email__iexact=username))
        except User.DoesNotExist as ex:
            return Response({'detail': 'User does not exists'}, status=404)

        if user_obj.check_password(password):
            user = user_obj
            payload = jwt_payload_handler(user)
            token = jwt_encode_handler(payload)
            response = jwt_response_payload_handler(
                token, user, request=request)
            return Response(response)
        return Response({'detail': "Invalid credentials"}, status=401)
