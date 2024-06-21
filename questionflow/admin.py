from django.contrib import admin
from . models import *

# Register your models here.

@admin.register(Question)
class QuestionAdmin(admin.ModelAdmin):
    list_display = ['title', 'created_at', 'updated_at']
    
@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    list_display = ('name', 'slug')  # Add this line
    prepopulated_fields = {'slug': ('name',)}


admin.site.register(Answer)
