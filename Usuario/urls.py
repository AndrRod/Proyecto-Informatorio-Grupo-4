
from django.urls import path
from Usuario import views


# from django.contrib.auth.views import logout_then_login



urlpatterns = [
    path('Juego/', views.JuegoVistaGeneral, name= 'Juego'),
    path('Jugar/', views.Juego, name= 'Jugar'),
    path('resultados_multiplechoice/', views.tablero, name='resultados_multiplechoice'),
    # path('reiniciar_intento/', views.reinicar_intento, name ='reinicar_intento'),
    path('resultados/<int:pregunta_respondida_pk>/', views.resultado_pregunta, name='resultados'),
    path('tabla_posiciones', views.tabla_posiciones, name= 'tabla_posiciones'),
    
    # quiero que redireccione el resultado de la pregunta respondida a resultado.html
]