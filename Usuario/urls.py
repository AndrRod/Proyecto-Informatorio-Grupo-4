
from django.urls import path
from Usuario import views


# from django.contrib.auth.views import logout_then_login



urlpatterns = [
    path('Juego/', views.Juego, name= 'Juego'),
    path('resultados_multiplechoice/', views.tablero, name='resultados_multiplechoice'),
    # quiero que redireccione el resultado de la pregunta respondida a resultado.html
    path('resultados/<int:pregunta_respondida_pk>/', views.resultado_pregunta, name='resultados'),
    
]