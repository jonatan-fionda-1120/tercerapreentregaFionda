from django.shortcuts import render
from .models import Psicologos,Contacto,Especialidades
from django.http import HttpResponse
from .forms import *

# Create your views here.


def crear_psicologo(request):
    
    
    nombre_psicologo="Juan Maria"
    apellido_psicologo="Ocampos"
    email_psicologo="jocampos@psicos.com"
    especialidad_psicologo="psicoanalista"
    print("creando psicologo")
    psicologo=Psicologos(nombre=nombre_psicologo,apellido=apellido_psicologo,email=email_psicologo,especialidad=especialidad_psicologo)
    psicologo.save()
    respuesta=f"psicologo creado: {psicologo.nombre} - {psicologo.apellido} - {psicologo.email} - {psicologo.especialidad}"
    return HttpResponse(respuesta)


def listar_psicologos(request):
    psicologos=Psicologos.objects.all()
    respuesta=""
    for psicologo in psicologos:
        respuesta+=f"{psicologo.nombre} - {psicologo.apellido} - {psicologo.email} -{psicologo.especialidad}<br>"
    return HttpResponse(respuesta)


def inicio(request):
    
    return render(request,"apppsicos/inicio.html")


def contacto(request):
    return render(request,"apppsicos/contacto.html")

def psicologo(request):
        
   if request.method=="POST":
      form=psicologoform(request.POST)
      
      if form.is_valid():
         info=form.cleaned_data
         nombre=info["nombre"]
         apellido=info["apellido"]
         email=info["email"]
         especialidad=info["especialidad"]
         psicologo=Psicologos(nombre=nombre,apellido=apellido,email=email,especialidad=especialidad)
         psicologo.save()
         formlulario_psicologo=psicologoform()
         return render(request,"apppsicos/psicologo.html", {"mensaje": "agregado","formulario":formlulario_psicologo})
        
    
      else: 
        return render(request,"apppsicos/psicologo.html", {"mensaje": "datos invalidos"})
          
   else:
        formlulario_psicologo=psicologoform()
        return render(request,"apppsicos/psicologo.html", {"formulario":formlulario_psicologo})
   

def psicologo(request):
        
   if request.method=="POST":
      form=psicologoform(request.POST)
      
      if form.is_valid():
         info=form.cleaned_data
         nombre=info["nombre"]
         apellido=info["apellido"]
         email=info["email"]
         especialidad=info["especialidad"]
         psicologo=Psicologos(nombre=nombre,apellido=apellido,email=email,especialidad=especialidad)
         psicologo.save()
         formlulario_psicologo=psicologoform()
         return render(request,"apppsicos/psicologo.html", {"mensaje": "agregado","formulario":formlulario_psicologo})
        
    
      else: 
        return render(request,"apppsicos/psicologo.html", {"mensaje": "datos invalidos"})
          
   else:
        formlulario_psicologo=psicologoform()
        return render(request,"apppsicos/psicologo.html", {"formulario":formlulario_psicologo})

def contacto(request):
    
    if request.method=="POST":
       form=contactoform(request.POST)
       if form.is_valid():
         info=form.cleaned_data
         nombre=info["nombre"]
         apellido=info["apellido"]
         email=info["email"]
         mensaje=info["mensaje"]
         contacto=Contacto(nombre=nombre,apellido=apellido,email=email,mensaje=mensaje)
         contacto.save()
         formlulario_contacto=contactoform()
         return render(request,"apppsicos/contacto.html", {"mensaje": "agregado","formulario":formlulario_contacto})
       return render(request,"apppsicos/contacto.html", {"mensaje": "datos invalidos"})
          
    else:
        formlulario_contacto=contactoform()
        return render(request,"apppsicos/contacto.html", {"formulario":formlulario_contacto})
        


def especialidad(request):
   if request.method=="POST":
       form=especialidadesform(request.POST)
       if form.is_valid():
         info=form.cleaned_data
         tipo=info["tipo"]
         especialidad=Especialidades(tipo=tipo)
         especialidad.save()
         formlulario_Especialidad=especialidadesform()
         return render(request,"apppsicos/especialidad.html", {"mensaje": "agregado","formulario":formlulario_Especialidad})
       return render(request,"apppsicos/especialidad.html", {"mensaje": "datos invalidos"})
          
   else:
         formlulario_Especialidad=especialidadesform()
         return render(request,"apppsicos/especialidad.html", {"formulario":formlulario_Especialidad})
   
def busquedaespecialidad(request):
    return render(request, "apppsicos/busquedaespecialidad.html")

def buscar(request):
    especialidad=request.GET["especialidad"]
    
    if especialidad:
        especialidades_filtradas=Especialidades.objects.filter(tipo__icontains=especialidad)
        return render(request, "apppsicos/resultadosbusqueda.html", {"especialidades_filtradas":especialidades_filtradas})
    else:
        return render(request, "apppsicos/busquedaespecialidad.html", {"mensaje":"No Ingresaste Nada!"})
   

      
      
   
   









