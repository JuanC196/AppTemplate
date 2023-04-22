from django.shortcuts import render
from App1.models import Curso
from django.http import HttpResponse

# Create your views here.
def curso(self):
    curso= Curso(nombre="Desarrollo Web", camada = 19673)
    curso.save()
    texto = f"----> Asignatura: {curso.nombre}, Camada: {curso.camada}"

    return HttpResponse(texto)

def inicio(request):
    return render(request, "AppCoder/inicio.html")

def cursos(request):
    return render(request, "AppCoder/cursos.html")

def profesores(request):
    return render(request, "AppCoder/profesores.html")

def estudiantes(request):
    return render(request, "AppCoder/estudiantes.html")

def entregables(request):
    return render(request, "AppCoder/entregables.html")

