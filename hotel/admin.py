from django.contrib import admin

from hotel.models import Hotel, BookingModels, Comment

admin.site.register(Hotel)
admin.site.register(BookingModels)
admin.site.register(Comment)