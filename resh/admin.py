from django.contrib import admin

from .models import CustomLocation


# Register your models here.
class CustomLocationAdmin(admin.ModelAdmin):
    list_display = ('name', )


admin.site.register(CustomLocation, CustomLocationAdmin)
