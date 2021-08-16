# se crea un url de la aplicacion
# from django.contrib import admin
# hay que enlazar el urls del proyecto y de la aplicacions
# from ProyectoWeb.AniversarioChaco.views import registro
from django.urls import path
from AniversarioChaco import views


# from django.contrib.auth.views import logout_then_login



urlpatterns = [
    path('home', views.home, name= 'home'),
    path('contacto/', views.Contacto, name= 'contacto'),
    # los sgtes refieren a los html que pueden servir al proyecto
    path('resultados_multiplechoice/', views.resultados_t, name='resultados_multiplechoice'),
    path('registro/', views.registro, name='registro'),
    
]