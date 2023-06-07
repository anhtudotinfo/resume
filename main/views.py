from django.shortcuts import render
from .models import Comment

# Create your views here.
def home(request):
    return render(request, 'main/home.html', {})

def resume(request):
    return render(request, 'main/resume.html', {})

def projects(request):
    return render(request, 'main/projects.html', {})

def inspirations(request):
    return render(request, 'main/inspirations.html', {})

def contact(request):
    return render(request, 'main/contact.html', {'comments': Comment.objects.all()})
