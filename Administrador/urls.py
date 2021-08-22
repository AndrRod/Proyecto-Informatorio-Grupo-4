


from django.contrib import admin
from django.urls import path
from Administrador import views
from AniversarioChaco import form
from django.contrib.auth import views as authViews

urlpatterns = [
     path('agregar/', views.AdminPregForm.as_view(), name="agregar"),
     path('pregunta_creada/', views.pregunta_creada.as_view(), name="pregunta_creada"),
    
    
]
    # path('tabla/', views.tabla, name="tabla"),
    # path('agregarp/', views.agregar.as_view(), name="agregarp"),

