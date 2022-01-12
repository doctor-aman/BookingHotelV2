from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.decorators import action
from rest_framework.filters import SearchFilter, OrderingFilter
from rest_framework.viewsets import ModelViewSet

from hotel.models import Hotel, BookingModels, Comment
from hotel.serializers import HotelSerializer, BookingSerializer, CommentSerializer


class HotelView(ModelViewSet):
    queryset = Hotel.objects.all()
    serializer_class = HotelSerializer
    filter_backends = [SearchFilter, OrderingFilter, DjangoFilterBackend]
    search_fields = ['name']  # поиск по названию
    ordering_fields = ['name', 'cost', 'location']


class BookingView(ModelViewSet):
    queryset = BookingModels.objects.all()
    serializer_class = BookingSerializer
    filter_backends = [SearchFilter, OrderingFilter, DjangoFilterBackend]
    search_fields = ['customer_name', 'status', 'checkOutDate']
    ordering_fields = ['customer_name']


class CommentView(ModelViewSet):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
    filter_backends = [SearchFilter, OrderingFilter, DjangoFilterBackend]
    search_fields = ['author']
    ordering_fields = ['created_at']


