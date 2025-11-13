from django.shortcuts import render
from django.http import HttpResponse
from django.http import JsonResponse
from django.template import loader
from .models import Tarefa

# Create your views here.
def index(request):
    return HttpResponse("Hello, world. You´re at tasks index!")

def tarefas(request):
    return HttpResponse('Essas são minhas tarefas')

def tarefa(request, id):
    lista_de_tarefas = list(Tarefa.objects.all().values())
    template = loader.get_template("tarefas/index.html")
    context = {"lista_de_tarefas": lista_de_tarefas}
    return HttpResponse(template.render(context, request))