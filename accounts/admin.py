from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import CustomUser


class CustomUserAdmin(UserAdmin):
    model = CustomUser

    list_display = (
        "username",
        "email",
        "phone_number",
        "user_type",
        "is_staff",
        "is_active",
    )

    readonly_fields = ("date_joined", "last_login")

    fieldsets = UserAdmin.fieldsets + (
        (
            "Additional Info",
            {
                "fields": (
                    "phone_number",
                    "address",
                    "user_type",
                )
            },
        ),
    )


admin.site.register(CustomUser, CustomUserAdmin)