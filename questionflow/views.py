from django.shortcuts import render, redirect, get_object_or_404
from . models import *
from django.contrib.auth.decorators import login_required
from . forms import QuestionForm, AnswerForm, AnswerUpdate
from django.contrib import messages

# Create your views here.
@login_required
def question_list(request, tag=None):
    if tag:
        questions = Question.objects.filter(tags__slug=tag)
    else:
        questions = Question.objects.all()

    context = {'questions':questions}
    return render(request, 'questions/question_flow.html', context)

@login_required
def recent_questions(request):
    questions = Question.objects.all().order_by('-created_at')
    context = {'questions':questions}
    return render(request, 'questions/recent_question.html', context)

@login_required
def question_create(request):
    form = QuestionForm()
    if request.method == 'POST':
        form = QuestionForm(request.POST)
        if form.is_valid():
            title = form.cleaned_data['title']
            if Question.objects.filter(title=title).exists():
                messages.error(request, 'Question title already exists')
            else:
                var = form.save(commit=False)
                var.user = request.user
                var.save()
                messages.success(request, 'Your Question has been created successfully')
                return redirect('questions')
        else:
            messages.error(request, 'Form is not valid')
    else:
        form = QuestionForm()
    return render(request, 'questions/question_create.html', {'form':form})

@login_required
def question_detail(request, pk):
    question = get_object_or_404(Question, pk=pk)
    if request.method == 'POST':
        form = AnswerForm(request.POST)
        if form.is_valid():
            answer = form.save(commit=False)
            answer.user = request.user
            answer.question = question
            answer.save()
            messages.success(request, 'Your answer has been submitted successfully.')
            return redirect('questionflow:question-detail', pk=question.pk)
    else:
        form = AnswerForm()
    
    context = {
        'question': question, 
        'form': form,
        'answers': question.answer_set.all()
    }
    return render(request, 'questions/question_detail.html', context)


@login_required
def upvote_question(request, pk):
    question = get_object_or_404(Question, pk=pk)
    if question.user != request.user:
        question.upvote.add(request.user)
        
    return redirect('question-detail', question.id)


