from django.shortcuts import render, get_object_or_404
from .models import *
from .forms import *

# Create your views here.


def contents(request):
    contents =  Content.objects.all()

    return render(request, 'content/contents.html', {'contents':contents})

def content_detail(request, pk):
    pics = Files.objects.filter(content=pk)
    content = get_object_or_404(Content, pk=pk)
    if request.method == 'POST':
        files = request.FILES.getlist('files')
        for file in files:
            new_file = Files(
                files = file,
                content = content.pk
            )
            new_file.save()
            
        
            return render(request, 'content/content_detail.html', {'content':content, 'pics':pics})
    context = {
        'content':content,
        'new_url': str(new_file.file.url),
        }
   
    return render(request, 'content/content_detail.html', context)

def create_content(request):
     if request.method == 'POST':
        form = ContentForm(request.POST or None)
        if form.is_valid():
            var = form.save(commit=False)
            var.owner = request.user
            var.save()
            return render(request, 'content/content_detail.html', {'content':var, 'edit':True})
     form = ContentForm()
     return render(request, 'content/content_create.html', {'form':form})

def content_edit(request, pk):
    content = get_object_or_404(Content, pk=pk)
    if request.method == 'POST':
        form = ContentForm(request.POST, instance=content)
        if form.is_valid():
            var = form.save()
            return render(request, 'content/content_detail.html', {'content':var, 'edit':True})
    form = ContentForm(instance=content)
    return render(request, 'content/content_edit.html', {'content':content, 'form':form})

 

    