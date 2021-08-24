



from os import name
from django.contrib import admin
from django.urls import path
from Administrador import views
from django.contrib.admin.views.decorators import staff_member_required

from django.contrib.auth import views as authViews

urlpatterns = [
     path('agregar/', staff_member_required(views.CrearPreg.as_view()), name="agregar"),
     path('resultados/', staff_member_required(views.resulPreguntas), name="resultPreg"),
     path('actualizar/', staff_member_required(views.Modif_pregunta_creada.as_view()), name="actualizar"),
    
    
]

    # path('tabla/', views.tabla, name="tabla"),
    # path('agregarp/', views.agregar.as_view(), name="agregarp"),

