from rest_framework import viewsets
from rest_framework import generics, status
from django.shortcuts import get_object_or_404
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from . import models, serializers, permissions
from rest_framework_jwt.settings import api_settings

jwt_payload_handler = api_settings.JWT_PAYLOAD_HANDLER
jwt_encode_handler = api_settings.JWT_ENCODE_HANDLER


class FlightViewSet(viewsets.ModelViewSet):
    """
    Flight model viewSet
    """
    serializer_class = serializers.FlightSerializer
    queryset = models.Flight.objects.all()
    permission_classes = [permissions.IsSuperUserOrReadOnly, ]


class FlightBooking(generics.ListCreateAPIView):
    permission_classes = (IsAuthenticated,)
    queryset = models.Booking.objects.all()
    serializer_class = serializers.BookingSerializer

    def post(self, request, flight_pk=None):
        flight = get_object_or_404(models.Flight, pk=flight_pk)
        try:
            booked = models.Booking.objects.get(user=request.user, flight=flight)
        except models.Booking.DoesNotExist:
            booked = None

        if booked:
            return Response(
                data={
                    "message": "You have already booked this fight!"
                },
                status=status.HTTP_409_CONFLICT
            )
        booking = models.Booking.objects.create(
            flight=flight,
            user=request.user
        )

        return Response(
            data=serializers.BookingSerializer(booking).data,
            status=status.HTTP_201_CREATED
        )
