from django.contrib import admin

from . import models


@admin.register(models.RoomType, models.Facility, models.Amenity, models.HouseRule)
class ItemAdmin(admin.ModelAdmin):
    list_display = ("name", "used_by")

    def used_by(self, obj):
        return obj.rooms.count()


@admin.register(models.Room)
class RoomAdmin(admin.ModelAdmin):

    fieldsets = (
        (
            "Room information",
            {"fields": ("name", "description", "price"), "classes": ["collapse"]},
        ),
        (
            "Detail information",
            {
                "fields": (
                    "country",
                    "city",
                    "address",
                    "guests",
                    "beds",
                    "bedrooms",
                    "baths",
                ),
                "classes": ["collapse"],
            },
        ),
        (
            "Use information",
            {
                "fields": (
                    "check_in",
                    "check_out",
                    "instant_book",
                    "host",
                    "roomType",
                    "amenities",
                    "facilities",
                    "house_rules",
                ),
                "classes": ["collapse"],
            },
        ),
    )

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
        "count_amenities",
        "count_photos",
        "total_rating",
    )

    list_filter = (
        "instant_book",
        "host__superhost",
        "host__gender",
        "roomType",
        "amenities",
        "facilities",
        "house_rules",
        "city",
        "country",
    )

    search_fields = ("city",)

    filter_horizontal = ("amenities", "facilities", "house_rules")

    ordering = ("price", "guests", "beds", "bedrooms", "baths")

    def count_amenities(self, obj):
        return obj.amenities.count()

    # count_amenities.short_description = "cnt amenities"

    def count_photos(self, obj):
        return obj.photos.count()


@admin.register(models.photo)
class RoomAdmin(admin.ModelAdmin):

    pass


# Register your models here.
