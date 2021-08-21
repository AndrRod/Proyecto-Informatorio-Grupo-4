from django.contrib import admin
from django.urls import path
from Administrador import views


urlpatterns = [
    path('agregar/', views.agregar, name="agregar"),
    
]
    # path('tabla/', views.tabla, name="tabla"),