from django.urls import path
from .views import *



urlpatterns=[
    path("crear_psicologo/", crear_psicologo),
    path("listar_psicologos/", listar_psicologos),
    path("psicologos/", psicologo, name="psicologo"),
    path("contato/", contacto, name="contacto"),
    path("especialidad/", especialidad, name="especialidad"),
    path("busquedaespecialidad/", busquedaespecialidad, name="busquedaespecialidad"),
    path("buscar/", buscar, name="buscar") ,
]