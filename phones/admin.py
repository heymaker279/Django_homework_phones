from django.contrib import admin

from .models import *

@admin.register(Phone)
class PhoneAdmin(admin.ModelAdmin):
    list_display = ("id", "name", "price", "slug", "release_date", "image")
    # prepopulated_fields = {"slug": ('name',)}
