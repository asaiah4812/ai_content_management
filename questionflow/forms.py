from django.forms import ModelForm
from django import forms
from .models import Question, Answer
from django_summernote.widgets import SummernoteWidget, SummernoteInplaceWidget
# from django import forms

class QuestionForm(ModelForm):
    # tags = forms.ModelMultipleChoiceField(queryset=Ailment.objects.all(), required=False, widget=forms.CheckboxSelectMultiple)
    class Meta:
        model = Question
        fields = ['title', 'content']
        

class AnswerForm(ModelForm):
    class Meta:
        model = Answer
        fields = ['content']
        widgets = {
            'content': forms.Textarea(attrs={
                'class': 'w-full px-3 py-2 text-gray-700 border rounded-lg focus:outline-none focus:border-blue-500',
                'rows': 5,
                'placeholder': 'Write your answer here...'
            })
        }

class AnswerUpdate(ModelForm):
    class Meta:
        model = Answer
        fields = ['user', 'question', 'content']