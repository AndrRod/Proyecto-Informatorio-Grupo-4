
from django.urls import path
from Usuario import views

from django.contrib.auth import views as authViews
# from django.contrib.auth.views import logout_then_login



urlpatterns = [
    path('Juego/', views.JuegoVistaGeneral, name= 'Juego'),
    path('Jugar/', views.Juego, name= 'Jugar'),
    path('resultados_multiplechoice/', views.tablero, name='resultados_multiplechoice'),
    
    path('resultados/<int:pregunta_respondida_pk>/', views.resultado_pregunta, name='resultados'),
    path('tabla_posiciones', views.tabla_posiciones, name= 'tabla_posiciones'),
    


    
]


# estas url.py esaban destinadas a crear un juego con categorias que no esta implementado (Juego_categoria.html y Jugar_categoria.html)
    # path('Juego_categoria_VistaGeneral', views.Juego_categoria_VistaGeneral, name='Juego_categoria_VistaGeneral'),
    # path('Jugar_categoria', views.Juego_categoria, name='Jugar_categoria')