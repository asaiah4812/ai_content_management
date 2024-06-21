from django.shortcuts import render, get_object_or_404
from django.contrib.auth.models import User
from .forms import ProfileForm, TaskForm
from django.contrib.auth.decorators import login_required
from .models import *
from django.views.decorators.http import require_POST, require_http_methods
from django.http import HttpResponse
from .filters import TaskFilter
from django.contrib.auth.models import User

# Create your views here.

def home(request):
    return render(request, 'core/landing.html')

@login_required
def dashboard(request):
    users = User.objects.exclude(id=request.user.id)
    return render(request, 'core/dashboard.html', {'users': users})


# profile view actions page
@login_required
def profile_edit_view(request):
    if not request.user.is_authenticated:
        return redirect('login')
    form = ProfileForm(instance=request.user.profile)
    if request.method == 'POST':
        form = ProfileForm(request.POST, request.FILES, instance=request.user.profile)
        if form.is_valid():
            form.save()
            return redirect('profile', request.user.username)
    else:
        form = ProfileForm(instance=request.user.profile)
    context = {
        'form': form
    }
    return render(request, 'core/profile_edit.html')
@login_required
def profile(request, username=None):
    if username:
        profile = get_object_or_404(User, username=username).profile
    else:
        profile = request.user.profile

    context ={
        'profile':profile
    }
    return render(request, 'core/profile.html', context)


#todo list view actions page

@login_required
def todo_list(request):
    task_filter = TaskFilter(request.GET, queryset=Task.objects.filter(user=request.user).order_by('-created_at'))


    form = TaskForm()
    context = {
        'filter':task_filter,
        'form':form,
    }
    if request.htmx:
        return render(request, 'core/partials/tasks.html', context)
    return render(request, 'core/todo_list.html', context)


@login_required
@require_POST
def submit_task(request):
    form = TaskForm(request.POST)
    if form.is_valid():
        task = form.save(commit=False)
        task.user = request.user
        task.save()
        #return an Html partial
        context = {'task':task}
        return render(request,'core/todo_list.html#taskitem-partial', context)
    
@login_required
@require_POST
def complete_task(request, pk):
    task = get_object_or_404(Task, pk=pk, user=request.user)
    task.is_completed = True
    task.save()
    context = {'task':task}
    return render(request,'core/todo_list.html#taskcomplete-partial', context)


@login_required
@require_http_methods(['DELETE'])
def delete_task(request, pk):
    task = get_object_or_404(Task, pk=pk, user=request.user)
    task.delete()
    response = HttpResponse(status=204)
    response['HX-Trigger'] = 'delete-task'
    return response

# def follow_user(request, user_id):
#     user_to_follow = get_object_or_404(User, id=user_id)
#     is_following = request.user.following.filter(id=user_id).exists()
#     if not is_following:
#         Follow.objects.create(follower=request.user, following=user_to_follow)
#     return redirect('profile', is_following=is_following)  # Pass the following status


# def unfollow_user(request, user_id):
#     user_to_unfollow = get_object_or_404(User, id=user_id)
#     request.user.following.filter(id=user_id).delete()
#     return redirect('profile')


 