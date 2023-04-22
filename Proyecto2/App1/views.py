from django.shortcuts import render
from App1.models import Curso
from django.http import HttpResponse

# Create your views here.
def curso(self):
    curso= Curso(nombre="Desarrollo Web", camada = 19673)
    curso.save()
    texto = f"----> Asignatura: {curso.nombre}, Camada: {curso.camada}"

    return HttpResponse(texto)