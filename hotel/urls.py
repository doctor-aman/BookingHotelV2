from rest_framework.routers import SimpleRouter
from django.urls import path, include

from hotel.views import HotelView

router = SimpleRouter()
router.register('Hotel', HotelView)

urlpatterns = [
    path('', include(router.urls))
]