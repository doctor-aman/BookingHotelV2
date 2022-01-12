from rest_framework import serializers

from hotel.models import Hotel, BookingModels, Comment


class HotelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Hotel
        fields = '__all__'

class BookingSerializer(serializers.ModelSerializer):
    class Meta:
        model = BookingModels
        fields = '__all__'

class CommentSerializer(serializers.ModelSerializer):
    hotel = serializers.PrimaryKeyRelatedField(queryset=Hotel.objects.all(),
                                                  write_only=True)
    class Meta:
        model = Comment
        exclude = ['user']

    def create(self, validated_data):
        user = self.context.get('request').user
        validated_data['user'] = user
        return super().create(validated_data)