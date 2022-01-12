from django.contrib.auth import get_user_model
from django.core.validators import MinValueValidator, MaxValueValidator
from django.db import models

# статусы бронирования отеля
class Status(models.Model):
    STATUS = (
        ('COMPLETED', "zavershen"),
        ('DROPPED', "udalen"),
    )
    status = models.CharField(max_length=10, choices=STATUS, unique=True)

    def __str__(self):
        return self.status


class Hotel(models.Model):
    name = models.CharField(max_length=50, unique=True)
    location = models.TextField(blank=True, null=True)
    visitorCount = models.IntegerField(blank=True, null=True, default=0)
    cost = models.FloatField(blank=True, null=True)
    rating = models.SmallIntegerField(
        validators=[
            MinValueValidator(1),
            MaxValueValidator(5)
        ])

    def __str__(self):
        return self.name
#
#
#
# class Booking(models.Model):
#     hotel_id = models.ForeignKey("Hotel", on_delete=models.CASCADE)
#     user = models.ForeignKey(get_user_model(),
#                              on_delete=models.CASCADE,
#                              related_name='booking')
#     time = models.DateField(auto_now_add=True)
#     amount = models.FloatField(blank=True, null=True)
#     status = models.ForeignKey("Status", on_delete=models.CASCADE)
#     checkInDate = models.DateField(auto_now_add=True, blank=True, null=True)
#     checkOutDate = models.DateField(auto_now_add=True, blank=True, null=True)
#
#     def __str__(self):
#         return str(self.hotel_id)
#
#     class Meta:
#         verbose_name = "Booking"
#         verbose_name_plural = "Bookings"
#
#
# class HotelFeature(models.Model):
#     h_id = models.ForeignKey("Hotel", on_delete=models.CASCADE)
#     f_id = models.ForeignKey("Feature", on_delete=models.CASCADE)
#
#     def __str__(self):
#         return str(self.f_id)
#
#     class Meta:
#         verbose_name = "HotelFeature"
#         verbose_name_plural = "HotelFeatures"
#
# class Search(models.Model):
#     user = models.ForeignKey(get_user_model(), on_delete=models.CASCADE, related_name='search')
#     location = models.CharField(max_length=50)
#     checkInDate = models.DateField(blank=True, null=True)
#     checkOutDate = models.DateField(blank=True, null=True)
#     amount = models.FloatField(blank=True, null=True)
#
#     def __str__(self):
#         return str(self.user)
#
