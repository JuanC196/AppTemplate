from django.urls import path
from App1 import views
from App1.views import curso

urlpatterns = [
    path('curso/', curso),
    path('', views.inicio),
    path('cursos', views.cursos, name="Cursos"),
    path('profesores', views.profesores),
    path('estudiantes', views.estudiantes),
    path('entregables', views.entregables),
    
]