"""User decorators."""

import re
from rest_framework.response import Response
from rest_framework.views import status


def validate_password(password):
    """Validate Password.

    :params: password
    :returns: Boolean
    """
    if re.search(r"^(?=.*[A-Za-z])(?=.*\d)(?=.*[@$!%*#?&])[A-Za-z\d@$!%*#?&]{6,}$", password) is not None:
        return True
    return False


def validate_email(email):
    """Validate Email.

    :params: email
    :returns: Boolean
    """
    if re.search(r"(^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$)", email) is not None:
        return True
    return False


def validate_user_registration(fn):
    """Validate user registration data decorator.

    :returns: fn
    """
    def decorator(*args, **kwargs):

        username = args[0].request.data.get("username", "")
        email = args[0].request.data.get("email", "")
        password = args[0].request.data.get("password", "")

        if not username and not email and not password:
            return Response(
                data={
                    "message": "All data fields are required. Email, Username and Password",
                },
                status=status.HTTP_400_BAD_REQUEST
            )

        if not validate_email(email):
            return Response(
                data={
                    "message": "Please enter a valid email"
                },
                status=status.HTTP_400_BAD_REQUEST
            )
        if not validate_password(password):
            return Response(
                data={
                    "message": "Password must be at least six characters, must be alphanumeric character and must contain at least one special character"
                },
                status=status.HTTP_400_BAD_REQUEST
            )
        return fn(*args, **kwargs)
    return decorator


def validate_user_login(fn):
    """Validate user login data decorator.

    :returns: fn
    """
    def decorator(*args, **kwargs):

        username = args[0].request.data.get("username", "")
        password = args[0].request.data.get("password", "")
        if not username:
            return Response(
                data={
                    "message": "Username is required"
                },
                status=status.HTTP_400_BAD_REQUEST
            )
        if not password:
            return Response(
                data={
                    "message": "Password is required"
                },
                status=status.HTTP_400_BAD_REQUEST
            )
        return fn(*args, **kwargs)
    return decorator
