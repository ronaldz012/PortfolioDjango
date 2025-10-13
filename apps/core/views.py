# apps/core/views.py
from django.shortcuts import render
from django.http import HttpResponse
# Importamos el modelo Project para poder acceder a los datos
from .models import Project 

# Ya no necesitas 'from . import views' dentro de este archivo

# --- Funciones de vista actualizadas ---

def test(request):
   """
   Obtiene todos los proyectos y los pasa a la plantilla index.html.
   """
   # 1. Obtiene todos los objetos Project
   all_projects = Project.objects.all() 
   
   # 2. Prepara el contexto (el diccionario de datos para la plantilla)
   context = {
       'projects': all_projects 
   }
   
   # 3. Renderiza la plantilla, pasando los datos
   return render(request, 'core/index.html', context)

# Si usas esta vista como tu página de inicio, puedes renombrarla a 'home' o 'index'

def home(request):
   # Esta es la página de inicio, si decides que solo debe mostrar un mensaje estático
   return HttpResponse("This is home page") 

def about(request):
   return HttpResponse("This is about page")

def contact(request):
   return HttpResponse("This is contact page")

def projects(request):
   # Si decides usar esta función para la página de listado en lugar de project_list,
   # simplemente copia el contenido de project_list aquí.
   return HttpResponse("This is projects page")