from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from . import models


# Register your models here.
@admin.register(models.User)
class CustomUserAdmin(UserAdmin):

    """ custom user display """

    fieldsets = UserAdmin.fieldsets + (
        (
            "banana 이 부분은 우리가 직접 추가한 어드민 내용입니다 나머지 부분은 장고에서 제공하는 UserAdmin.fieldsets 입니다.",
            {
                "fields": (
                    "avatar",
                    "gender",
                    "job",
                    "bio",
                    "birthdate",
                    "language",
                    "currency",
                    "superhost",
                )
            },
        ),
    )

    list_filter = UserAdmin.list_filter + ("superhost",)

    list_display = (
        "username",
        "first_name",
        "last_name",
        "email",
        "is_active",
        "language",
        "currency",
        "superhost",
        "is_staff",
        "is_superuser",
    )
