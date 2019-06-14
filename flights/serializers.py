from rest_framework import serializers
from . import models


class FlightSerializer(serializers.ModelSerializer):
    """
    flight serializer.
    """
    class Meta:
        model = models.Flight
        fields = (
            'id', 'from_location', 'to_location', 'departure_time',
            'arrival_time', 'airline', 'no_of_seats', 'price',)

    def validate(self, data):
        """
        validate to and from locations are not the same.
        """
        if data['to_location'] == data['from_location']:
            raise serializers.ValidationError(
                'from and to location cannot be the same')
        return data
