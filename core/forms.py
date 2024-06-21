from django import forms
from .models import *
from django_countries.fields import CountryField

class ProfileForm(forms.ModelForm):
    country = CountryField(blank_label='(Select country)', max_length=100).formfield(
        widget=forms.Select(attrs={
            'class': 'bg-gray-50 border border-gray-300 text-gray-900 text-sm rounded-lg focus:ring-blue-500 focus:border-blue-500 block w-full p-2.5 dark:bg-gray-700 dark:border-gray-600 dark:placeholder-gray-400 dark:text-white dark:focus:ring-blue-500 dark:focus:border-blue-500'
        })
    )
    class Meta:
        model = Profile
        fields = [
            'addressLine1',
            'addressLine2',
            'city',
            'country',
            'postalCode',
            ]


class TaskForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = ['title', 'description', 'category']