from django.contrib import admin
from .models import EmpDetails



# Register your models here.

@admin.register(EmpDetails)
class EmpAdmin(admin.ModelAdmin):
    list_display=['empno','ename','salary']