"""Test API."""

from rest_framework.test import APITestCase, APIClient
from rest_framework import status
import json


class UserAuthTest(APITestCase):
    """User Auth API."""

    client = APIClient()

    def test_register_user_fail(self):
        """Test user registration error."""
        response = self.client.post(
            '/api/v1/register/',
            data=json.dumps({"username": "", "password": ""}),
            content_type="application/json"
        )
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_register_user_invalid_email(self):
        """Test user registration with invalid email address."""
        response = self.client.post(
            '/api/v1/register/',
            data=json.dumps({"username": "email", "password": "password!34"}),
            content_type="application/json"
        )
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertIn("error", response.data)

    def test_register_user(self):
        """Test user registration."""
        response = self.client.post(
            '/api/v1/register/',
            data=json.dumps({
                "username": "username",
                "email": "email@email.com",
                "password": "password!34"}),
            content_type="application/json"
        )
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_login_user_fail(self):
        """Test user login error."""
        response = self.client.post(
            '/api/v1/login/',
            data=json.dumps({"username": "", "password": ""}),
            content_type="application/json"
        )
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_login_user(self):
        """Test user login."""
        self.client.post(
            '/api/v1/register/',
            data=json.dumps({
                "username": "username",
                "email": "email@email.com",
                "password": "password!34"}),
            content_type="application/json"
        )

        response = self.client.post(
            '/api/v1/login/',
            data=json.dumps({"username": "username", "password": "password!34"}),
            content_type="application/json"
        )
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertIn("token", response.data)
