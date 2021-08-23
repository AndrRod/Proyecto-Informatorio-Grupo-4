



from os import name
from django.contrib import admin
from django.urls import path
from Administrador import views


from django.contrib.auth import views as authViews

urlpatterns = [
     path('agregar/', views.CrearPreg.as_view(), name="agregar"),
     path('respuestas/', views.pregunta_creada.as_view(), name="respuestas"),
    
    
]
    # path('tabla/', views.tabla, name="tabla"),
    # path('agregarp/', views.agregar.as_view(), name="agregarp"),

