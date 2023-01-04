from django.shortcuts import render, HttpResponse, redirect
from django.contrib import messages


# Create your views here.

def index(request):
    return render(request, "index.html")

def integrantes(request):
    integrantes = ["Prado Zuta, Miguel Angel", "Rakauskas Purca, Sebastián Alberto", "Quispe Cancho, Diego"]
    diccionario = {"Titulo": "Integrantes del Proyecto",
                    "integrantes": integrantes}
 
    return render(request, "integrantes.html", diccionario)

def cursos(request):
    return render(request, 'cursos.html')

def crearCurso(request):
    return render(request, 'crearCursos.html')

def docente(request):
    return render(request, 'docente.html')

def crearDocente(request):
    return render(request, 'crearDocente.html')

def integrantes(request):
    return render(request, 'integrantes.html')

def saludo(request):
    diccionario = {"Titulo": "Saludo",
                    "saludo": "Bienvenidos al proyecto Final del Curso de LP3 III"}
    return render(request, "saludo.html", diccionario)