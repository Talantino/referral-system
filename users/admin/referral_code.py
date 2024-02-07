from django.contrib import admin

from users.models import ReferralCode


@admin.register(ReferralCode)
class ReferralCodeAdmin(admin.ModelAdmin):
    list_display = ('id', 'user', "expiry_date")
    search_fields = ("user__username", "code")
    search_help_text = "Поиск по пользователю/коду"
