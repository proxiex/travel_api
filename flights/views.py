import datetime
from rest_framework import viewsets
from rest_framework import generics, status
from django.shortcuts import get_object_or_404
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.response import Response
from . import models, serializers, permissions
from rest_framework_jwt.settings import api_settings
from django.db.models import Q

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
    """
    Flight booking viewset.
    """
    permission_classes = (IsAuthenticated,)
    queryset = models.Booking.objects.all()
    serializer_class = serializers.BookingSerializer

    def post(self, request):
        flight_pk = request.data.get("flight", "")
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

    def get(self, request):
        if request.user.is_superuser:
            booked_flights = models.Booking.objects.all()
        else:
            booked_flights = models.Booking.objects.filter(user=request.user)

        serializer = serializers.BookingSerializer(booked_flights, many=True)
        send_email()

        return Response(
            data={
                "booked_flight": serializer.data
            })


class SearchFlight(generics.ListCreateAPIView):
    """
    Search flight view set.
    """
    serializer_class = serializers.SearchSerializer
    queryset = models.Flight.objects.all()
    permission_classes = (AllowAny,)
    http_method_names = [u'post', u'put', u'patch', u'delete', u'head', u'options', u'trace']

    def post(self, request):
        from_location = request.data.get('from_location')
        to_location = request.data.get('to_location')
        departure_time = request.data.get('departure_time')

        if not from_location or not to_location or not departure_time:
            return Response(
                data={
                    "error": "All data fields are required! - from_location, departure_time, to_location "
                },
                status=status.HTTP_400_BAD_REQUEST
            )

        #  validate time format
        try:
            departure_time = datetime.datetime.strptime(departure_time, "%Y-%m-%d")
            start_date = departure_time + datetime.timedelta(days=-2)
            end_date = departure_time + datetime.timedelta(days=3)
        except ValueError:
            return Response(
                data={
                    "error": "Date-Time format is invalid: Format Y-m-d"
                },
                status=status.HTTP_400_BAD_REQUEST
            )

        results = models.Flight.objects.filter(
            Q(from_location__icontains=from_location) & Q(to_location__icontains=to_location) & Q(departure_time__range=[start_date, end_date])
        )

        return Response(
            data=serializers.FlightSerializer(results, many=True).data,
            status=status.HTTP_200_OK
        )
