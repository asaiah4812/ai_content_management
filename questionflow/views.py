from django.shortcuts import render, redirect, get_object_or_404
from . models import *
from django.contrib.auth.decorators import login_required
from . forms import QuestionForm
from django.contrib import messages

# Create your views here.

def question_list(request, tag=None):
    if tag:
        questions = Question.objects.filter(tags__slug=tag)
    else:
        questions = Question.objects.all()

    context = {'questions':questions}
    return render(request, 'questions/question_flow.html', context)


def question_create(request):
    if request.method == 'POST':
        form = QuestionForm(request.POST)
        if form.is_valid():
            var = form.save(commit=False)
            var.user = request.user
            var.save()
            messages.success(request, 'Your Question Has been Created SuccessFully')
    return render(request, 'questions/question_create.html', {'form':form})


def question_detail(request, pk):
    question = get_object_or_404(Question, pk=pk)
    context = {'question':question}
    return render(request, 'questions/question_detail.html', context)
