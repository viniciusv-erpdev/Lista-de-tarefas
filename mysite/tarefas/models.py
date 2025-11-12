from django.db import models

class Tarefa(models.Model):

    STATUS_TAREFA = [
        ('R', 'Realizado'),
        ('N', 'Não Realizado'),
    ]

    titulo = models.CharField(max_length=200)
    descricao = models.CharField(max_length=200)
    data_tarefa = models.DateTimeField()
    status_tarefa = models.CharField(max_length=1, choices=STATUS_TAREFA, default='N')
    
    def __str__(self):
        return self.tarefa_text