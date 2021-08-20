from Usuario.views import Juego
from django.urls import path
from Usuario import views


# from django.contrib.auth.views import logout_then_login



urlpatterns = [
    path('Juego/', views.Juego, name= 'Juego'),
    path('resultados_multiplechoice/', views.resultados, name='resultados_multiplechoice'),
    
]