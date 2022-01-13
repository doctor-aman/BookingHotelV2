from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.decorators import action
from rest_framework.filters import SearchFilter, OrderingFilter
from rest_framework.mixins import CreateModelMixin, UpdateModelMixin, DestroyModelMixin
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet, GenericViewSet
from django.shortcuts import get_object_or_404

from Favorite.models import Favorites
from hotel.models import Hotel, BookingModels, Comment
from hotel.permission import IsAuthor
from hotel.serializers import HotelSerializer, BookingSerializer, CommentSerializer


class HotelView(ModelViewSet):
    queryset = Hotel.objects.all()
    serializer_class = HotelSerializer
    filter_backends = [SearchFilter, OrderingFilter, DjangoFilterBackend]
    search_fields = ['name']  # поиск по названию
    ordering_fields = ['name', 'cost', 'location']

    def get_context_data(self, **kwargs):
        data = super().get_context_data(**kwargs)

        likes_connected = get_object_or_404(Hotel, id=self.kwargs['pk'])
        liked = False
        if likes_connected.likes.filter(id=self.request.user.id).exists():
            liked = True
        data['number_of_likes'] = likes_connected.number_of_likes()
        data['is_liked'] = liked
        return data

    def get_permissions(self):
        # создавать может пост авторизованный пользователь
        if self.action in ['create', 'add_to_favorites', 'remove_from_favorites']:
            return [IsAuthenticated()]
        # изменять и удалять модет только автор поста
        elif self.action in ['update', 'partial_update', 'destroy']:
            return [IsAuthor()]
        # просмотр поста доступен всем
        return []

    @action(['POST'], detail=True)
    def add_to_favorites(self, request, pk=None):
        hotel = self.get_object()
        data = Favorites.objects.all()
        for favorite in data:
            if favorite.hotel.id == hotel.id:
                if favorite.user.email == request.user.email:
                    return Response('Уже добавлено в избранное')
        Favorites.objects.create(hotel=hotel, user=request.user)
        return Response('Добавлено в избранное')

    @action(['DELETE'], detail=True)
    def remove_from_favorites(self, request, pk=None):
        hotel = self.get_object()
        data = Favorites.objects.all()
        for favorite in data:
            if favorite.hotel.id == hotel.id:
                if favorite.user.email == request.user.email:
                    favorite.delete()
                    return Response('Удален из избранных')
        return Response('Невозможно удалить, так как нет в избранных')




class BookingView(ModelViewSet):
    queryset = BookingModels.objects.all()
    serializer_class = BookingSerializer
    filter_backends = [SearchFilter, OrderingFilter, DjangoFilterBackend]
    search_fields = ['customer_name', 'status', 'checkOutDate']
    ordering_fields = ['customer_name']

    def get_permissions(self):
        # создавать может пост авторизованный пользователь
        if self.action in ['create', 'add_to_favorites', 'remove_from_favorites']:
            return [IsAuthenticated()]
        # изменять и удалять модет только автор поста
        elif self.action in ['update', 'partial_update', 'destroy']:
            return [IsAuthor()]
        # просмотр поста доступен всем
        return []


class CommentView(CreateModelMixin,
                     UpdateModelMixin,
                     DestroyModelMixin,
                     GenericViewSet):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer

    def get_permissions(self):
        # создавать может пост авторизованный пользователь
        if self.action == 'create':
            return [IsAuthenticated()]
        # изменять и удалять может только автор поста
        elif self.action in ['update', 'partial_update', 'destroy']:
            return [IsAuthor()]

