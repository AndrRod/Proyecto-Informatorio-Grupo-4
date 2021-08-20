# se crea un url de la aplicacion
# from django.contrib import admin
# hay que enlazar el urls del proyecto y de la aplicacions
# from ProyectoWeb.AniversarioChaco.views import registro

from django.urls import path
from AniversarioChaco import views
from django.contrib.auth import views as authViews






urlpatterns = [
    path('home/', views.home, name= 'home'),
    path('contacto/', views.Contacto, name= 'contacto'),    
    path('registro/', views.registro, name='registro'),


    # login basado en clases
    path('login/', authViews.LoginView.as_view(template_name='registration/login.html'), name="login"),
    # practicando logout
    path('logout/', authViews.LogoutView.as_view(), name = 'logout')
    
]

    # login basado en funciones
    # path('login/', views.loginView, name='login'),