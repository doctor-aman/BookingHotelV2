from rest_framework import serializers


from hotel.models import Hotel, BookingModels, Comment


class HotelSerializer(serializers.ModelSerializer):

    class Meta:
        model = Hotel
        fields = ('id', 'name', 'location', 'visitorCount', 'cost', 'stars')

class BookingSerializer(serializers.ModelSerializer):
    class Meta:
        model = BookingModels
        fields = '__all__'

class CommentSerializer(serializers.ModelSerializer):

    class Meta:
        model = Comment
        fields = '__all__'
