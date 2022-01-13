from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet

from rating.models import Rating
from rating.serializers import RatingSerializer


class RatingView(ModelViewSet):
    queryset = Rating.objects.all()
    serializer_class = RatingSerializer

