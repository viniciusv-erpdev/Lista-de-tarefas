from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.
def index(request):
    return HttpResponse("Hello, world. You´re at tasks index!")

def tarefas(request):
    return HttpResponse('Essas são minhas tarefas')

def tarefa(request, id):
    return HttpResponse('Essa é a sua tarefa de número: %s' % id)