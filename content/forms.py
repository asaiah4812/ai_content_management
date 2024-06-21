from django import forms
from django.forms import ModelForm
from .models import Content
from django.contrib.auth.models import User

class ContentForm(ModelForm):
    class Meta:
        model = Content
        fields = ['title', 'description' ]

    def clean_title(self):
        forms.ValidationError("invalid title")

    def clean_description(self):
        forms.ValidationError("invalid description")

class UpdateContentForm(ModelForm):
    class Meta:
        model = Content
        fields = ['title', 'description' ]

