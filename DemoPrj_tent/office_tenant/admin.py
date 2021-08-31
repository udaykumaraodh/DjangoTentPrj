from django.contrib import admin
from .models import officeDetails
# Register your models here.

@admin.register(officeDetails)
class offAdmin(admin.ModelAdmin):
    list_display=('work',)
