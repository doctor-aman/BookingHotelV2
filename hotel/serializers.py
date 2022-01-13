from rest_framework import serializers


from hotel.models import Hotel, BookingModels, Comment
from rating.serializers import RatingSerializer


class HotelSerializer(serializers.ModelSerializer):

    class Meta:
        model = Hotel
        fields = ('id', 'name', 'location', 'visitorCount', 'cost', 'stars')

    def to_representation(self, instance):
        representation = super().to_representation(instance)
        rating_data = RatingSerializer(instance.ratings.all(), many=True).data
        total = 0
        for ord in rating_data:
            total+=ord.get('star')
            representation['rating'] = total/len(rating_data)
        return representation

class BookingSerializer(serializers.ModelSerializer):
    class Meta:
        model = BookingModels
        fields = '__all__'

class CommentSerializer(serializers.ModelSerializer):

    class Meta:
        model = Comment
        fields = '__all__'
