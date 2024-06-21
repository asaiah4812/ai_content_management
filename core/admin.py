from django.contrib import admin
from .models import *

# Register your models here.

@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    list_display = ['addressLine1', 'addressLine2', 'city',  'country', 'postalCode']
    list_filter = ['country', 'city']
    
admin.site.register(Task)
