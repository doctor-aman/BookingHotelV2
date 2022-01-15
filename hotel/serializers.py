from rest_framework import serializers


from hotel.models import Hotel, BookingModels, Comment, HotelImage
from rating.serializers import RatingSerializer


class HotelSerializer(serializers.ModelSerializer):
    image = serializers.SerializerMethodField()

    class Meta:
        model = Hotel
        fields = ('id', 'name', 'location', 'visitorCount', 'cost', 'stars', 'image')

    def to_representation(self, instance):
        representation = super().to_representation(instance)
        rating_data = RatingSerializer(instance.ratings.all(), many=True).data
        total = 0
        for ord in rating_data:
            total+=ord.get('star')
            representation['rating'] = total/len(rating_data)
        return representation

    def get_image(self, request):
        first_image = request.pics.first()
        if first_image and first_image.image:
                return first_image.image.url  # если image есть вернет URL
        return ''  # если image то вернет пустую строку


class HotelImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = HotelImage
        fields = '__all__'

class HotelsSerializer(serializers.ModelSerializer):
    images = serializers.ListField(child=serializers.ImageField(allow_empty_file=False), write_only=True,
                                   required=False)

    class Meta:
        model = Hotel
        exclude = ['user']

    def create(self, validated_data):
        user = self.context.get('request').user
        validated_data['user'] = user
        images = validated_data.pop('images', [])
        post = super().create(validated_data)
        for image in images:
            HotelImage.objects.create(post=post, image=image)
        return post

    def update(self, instance, validated_data):
        images = validated_data.pop('images', [])  # по default пустой список
        if images:
            for image in images:
                HotelImage.objects.create(post=instance, image=image)
        return super().update(instance, validated_data)

    def to_representation(self, instance):
        representation = super().to_representation(instance)
        representation['images'] = HotelImageSerializer(instance.pics.all(), many=True).data

class BookingSerializer(serializers.ModelSerializer):
    class Meta:
        model = BookingModels
        fields = '__all__'

class CommentSerializer(serializers.ModelSerializer):

    class Meta:
        model = Comment
        fields = '__all__'
