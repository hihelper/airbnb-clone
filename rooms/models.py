from django.db import models
from django_countries.fields import CountryField
from core import models as core_models


# Create your models here.


class AbstractItem(core_models.TimeStampedModel):

    """Abstract Item"""

    name = models.CharField(max_length=80)

    class Meta:
        abstract = True

    def __str__(self):
        return self.name


class RoomType(AbstractItem):
    class Meta:
        verbose_name = "Room Type"
        ordering = ["name"]


class Amenity(AbstractItem):
    class Meta:
        verbose_name_plural = "Amenities"


class Facility(AbstractItem):
    class Meta:
        verbose_name_plural = "Facilities"


class HouseRule(AbstractItem):
    class Meta:
        verbose_name = "House Rule"


class photo(core_models.TimeStampedModel):

    caption = models.CharField(max_length=80)
    file = models.ImageField()
    # 바로아래줄 코드를 보면 아직 선언되지 않은 클래스 Room을 사용하고 있다. 파이썬은 상하수직 방향으로 작동하므로 아직 선언되지 않은 Room은 아직 정의되지 않은 변수명이 된다.
    # 이를 해결하기 위해서는 단순히 현재 클래스를 Room클래스 아래에 위치시키는 방법이 있다. 또 다른 방법은
    # string으로 해결하는 방법이다.
    # 모델 이름을 문자열로(string으로) 작성하면 Django가 INSTALLED_APPS에서 모델을 찾습니다.
    room = models.ForeignKey("Room", related_name="photos", on_delete=models.CASCADE)

    def __str__(self):
        return self.caption


class Room(core_models.TimeStampedModel):

    name = models.CharField(max_length=150)
    description = models.TextField()
    price = models.IntegerField()

    country = CountryField()
    city = models.CharField(max_length=80)
    address = models.CharField(max_length=150)
    guests = models.IntegerField()
    beds = models.IntegerField()
    bedrooms = models.IntegerField()
    baths = models.IntegerField()

    check_in = models.TimeField()
    check_out = models.TimeField()
    instant_book = models.BooleanField(default=False)
    # host 는 ForeignKey로 생성한 뒤 on_delete=models.CASCADE를 해주었다는 점을 반드시 이해해야 합니다.
    host = models.ForeignKey(
        "users.User", related_name="rooms", on_delete=models.CASCADE
    )
    roomType = models.ForeignKey(
        "RoomType",
        related_name="rooms",
        blank=True,
        on_delete=models.SET_NULL,
        null=True,
    )
    amenities = models.ManyToManyField("Amenity", related_name="rooms", blank=True)
    facilities = models.ManyToManyField("Facility", related_name="rooms", blank=True)
    house_rules = models.ManyToManyField("HouseRule", related_name="rooms", blank=True)

    def __str__(self):
        return self.name

    def total_rating(self):
        all_reviews = self.reviews.all()
        all_ratings = 0
        for review in all_reviews:
            all_ratings += review.rating_average()
        return all_ratings / len(all_reviews)
