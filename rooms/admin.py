from django.contrib import admin

from . import models


@admin.register(models.RoomType, models.Facility, models.Amenity, models.HouseRule)
class ItemAdmin(admin.ModelAdmin):
    pass


@admin.register(models.Room)
class RoomAdmin(admin.ModelAdmin):

    list_display = (
        "name",
        "price",
        "country",
        "city",
        "guests",
        "beds",
        "bedrooms",
        "baths",
        "check_in",
        "check_out",
        "instant_book",
    )

    list_filter = ("city", "country")

    search_fields = ("city",)


@admin.register(models.photo)
class RoomAdmin(admin.ModelAdmin):

    pass


# Register your models here.
