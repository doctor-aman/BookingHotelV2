
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.decorators import action
from rest_framework.filters import SearchFilter, OrderingFilter
from rest_framework.viewsets import ModelViewSet

from hotel.models import Hotel
from hotel.serializers import HotelSerializer


class HotelView(ModelViewSet):
    queryset = Hotel.objects.all()
    serializer_class = HotelSerializer
    filter_backends = [SearchFilter, OrderingFilter, DjangoFilterBackend]
    search_fields = ['name']  # поиск по названию
    ordering_fields = ['name', 'cost', 'location']

    # @action(['GET'], detail=True)
    # def comments(self, request, pk):
    #     product = self.get_object()
    #     comments = product.comments.all()  # queryset сделали
    #     serializer = CommentSerializer(comments, many=True)
    #     return Response(serializer.data)
