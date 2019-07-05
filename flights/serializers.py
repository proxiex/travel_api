"""Flights serializers."""

from rest_framework import serializers
from . import models


class FlightSerializer(serializers.ModelSerializer):
    """flight serializer."""

    class Meta:
        """Meta class."""

        model = models.Flight
        fields = (
            'id', 'from_location', 'to_location', 'departure_time',
            'arrival_time', 'airline', 'no_of_seats', 'price',)

    def validate(self, data):
        """Validate to and from locations are not the same."""
        if data['to_location'] == data['from_location']:
            raise serializers.ValidationError(
                'from and to location cannot be the same')
        return data


class BookingSerializer(serializers.ModelSerializer):
    """Booking serializer."""

    class Meta:
        """Meta class."""

        model = models.Booking
        read_only_fields = ('created_at', 'updated_at')
        fields = (
            'id', 'flight', 'user', 'booked',
            'created_at', 'updated_at')


class SearchSerializer(serializers.ModelSerializer):
    """Search Flight serializer."""

    class Meta:
        """Meta class."""

        model = models.Flight
        fields = ('from_location', 'to_location', 'departure_time')

    def validate(self, data):
        """Validate to and from locations are not the same."""
        if data['to_location'] == data['from_location']:
            raise serializers.ValidationError(
                'from and to location cannot be the same')
        return data


class ReportSerializer(serializers.ModelSerializer):
    """Report serilizer."""

    # flight = serializers.PrimaryKeyRelatedField(many=True, read_only=True)
    # user = serializers.PrimaryKeyRelatedField(many=True, read_only=True)

    username = serializers.SerializerMethodField()
    email = serializers.SerializerMethodField()
    from_location = serializers.SerializerMethodField()
    to_location = serializers.SerializerMethodField()
    flight_number = serializers.SerializerMethodField()
    departure_time = serializers.SerializerMethodField()
    arrival_time = serializers.SerializerMethodField()
    price = serializers.SerializerMethodField()

    class Meta:
        """Meta class."""

        model = models.Booking
        fields = (
            'username', 'email', 'from_location',
            'to_location', 'flight_number', 'departure_time',
            'arrival_time', 'price')

    def get_username(self, obj):
        """Get method."""
        return obj.user.username

    def get_email(self, obj):
        """Get method."""
        return obj.user.email

    def get_from_location(self, obj):
        """Get method."""
        return obj.flight.from_location

    def get_to_location(self, obj):
        """Get method."""
        return obj.flight.to_location

    def get_flight_number(self, obj):
        """Get method."""
        return obj.flight.airline.flight_number

    def get_departure_time(self, obj):
        """Get method."""
        return obj.flight.departure_time

    def get_arrival_time(self, obj):
        """Get method."""
        return obj.flight.arrival_time

    def get_price(self, obj):
        """Get method."""
        return obj.flight.price
