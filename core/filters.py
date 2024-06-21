import django_filters
from .models import Task
from django import forms

class TaskFilter(django_filters.FilterSet):
    category_type = django_filters.ChoiceFilter(
        field_name='category', 
        choices=Task.TASK_CATEGORY, 
        lookup_expr='iexact', 
        empty_label="Any")
    class Meta:
        model = Task
        fields = ['category_type']