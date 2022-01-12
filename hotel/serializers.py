from rest_framework import serializers

from hotel.models import Hotel, BookingModels


class HotelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Hotel
        fields = '__all__'

class BookingSerializer(serializers.ModelSerializer):
    class Meta:
        model = BookingModels
        fields = '__all__'

