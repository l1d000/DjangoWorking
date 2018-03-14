from django.shortcuts import render
from django.http import HttpResponse  
import json
from  pytools.tool_shell import shell_command
from models import BuildProject

# Create your views here.
def index(request):
    context          = {}
    context['title'] = 'Hello World!'
    project_names = BuildProject.objects.all()
    context['project_names'] = project_names
    for i in project_names:
        print(i.project_Name)
    return render(request, 'index.html', context)

def animation(request):
    context          = {}
    return render(request, 'animation.html', context)

def default(request):
    context          = {}
    return render(request, 'default.html', context)

def test(request):
    context          = {}
    shell_command("cd /home/lidongzhou/HTC/work/test;find -name *.txt")
    return render(request, 'default.html', context)
