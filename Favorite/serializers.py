from rest_framework import serializers

from Favorite.models import Favorites


class FavoriteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Favorites
        fields = '__all__'