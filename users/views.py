from .models import CustomUser
from django.contrib.auth import authenticate, login
from rest_framework_jwt.settings import api_settings
from rest_framework import permissions, generics, status
from rest_framework.response import Response

from .serializers import TokenSerializer, UserSerializer
from users.helpers.decorators import validate_user_registration, validate_user_login

jwt_payload_handler = api_settings.JWT_PAYLOAD_HANDLER
jwt_encode_handler = api_settings.JWT_ENCODE_HANDLER


class LoginView(generics.CreateAPIView):
    """
    Login view:

    POST auth/login/
    """

    permission_classes = (permissions.AllowAny,)
    queryset = CustomUser.objects.all()
    serializer_class = UserSerializer

    @validate_user_login
    def post(self, request, *args, **kwargs):
        username = request.data.get("username", "")
        password = request.data.get("password", "")

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            serializer_class = TokenSerializer(
                data={
                    "token": jwt_encode_handler(
                        jwt_payload_handler(user))
                })
            serializer_class.is_valid()
            return Response(serializer_class.data)
        error_msg = {"error": "Invalid login credentials!"}
        return Response(error_msg, status=status.HTTP_401_UNAUTHORIZED)


class RegisterView(generics.CreateAPIView):
    """
    Registration View:

    POST /register/
    """
    permission_classes = (permissions.AllowAny,)
    serializer_class = UserSerializer

    @validate_user_registration
    def post(self, request, *args, **kwargs):
        username = request.data.get("username", "")
        password = request.data.get("password", "")
        email = request.data.get("email", "")

        if not username and not password and not email:
            return Response(
                data={
                    "message": "username, password and email is required to register a user"
                },
                status=status.HTTP_400_BAD_REQUEST
            )
        new_user = CustomUser.objects.create_user(
            username=username, password=password, email=email
        )
        return Response(
            data=UserSerializer(new_user).data,
            status=status.HTTP_201_CREATED
        )
