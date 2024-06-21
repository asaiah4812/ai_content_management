from django.forms import ModelForm
from .models import Question
# from django import forms

class QuestionForm(ModelForm):
    # tags = forms.ModelMultipleChoiceField(queryset=Ailment.objects.all(), required=False, widget=forms.CheckboxSelectMultiple)
    class Meta:
        model = Question
        fields = ['title', 'content']