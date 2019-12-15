from django.shortcuts import render
from hello_world.models import hello_world
# Create your views here.
def hello_world(request):
    return render(request,'hello_world.html',{})

def project_index(request):

    projects = hello_world.objects.all()

    context = {

        'projects': projects

    }

    return render(request, 'project_index.html', context)

def project_detail(request, pk):

    project = hello_world.objects.get(pk=pk)

    context = {

        'project': project

    }

    return render(request, 'project_detail.html', context)