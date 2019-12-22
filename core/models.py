from django.db import models

# Create your models here.
class TimeStampedModel(models.Model):

    """ Time Stampd Model """

    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True

    # abstract 모델은 데이터베이스에 반영이 되지 않는 모델이다. 확장하기 위해 작성함.

