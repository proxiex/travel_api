"""Test API."""

from rest_framework.test import APITestCase, APIClient
from rest_framework import status
import json


class FlightAPITest(APITestCase):
    """Flight API test."""

    client = APIClient()

    def test_creating_flight_fail(self):
        """Test create flight without auth error."""
        response = self.client.post(
            '/api/v1/flights/',
            data=json.dumps({}),
            content_type="application/json"
        )
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)
