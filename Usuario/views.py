
from django.core.exceptions import ObjectDoesNotExist
from django.http.response import Http404

from AniversarioChaco.models import Usuario, Pregunta, PreguntasRespondidas, ElegirRespuesta
from django.shortcuts import redirect, render, get_object_or_404
from django.contrib.auth.models import User

from AniversarioChaco.views import *


from django.contrib.auth.decorators import login_required

# Create your views here.


# traemos de models de Aniversario a Usuario
# de esta manera se crea el campo de usuario    
# va a crear o traer al usuario

CANT_PREG_POR_JUEGO = 10

@login_required(login_url= '/')
def tablero(request):
    context = {}
    
    UsuarioJugador, created = Usuario.objects.get_or_create(usuario=request.user)
    respondidas = PreguntasRespondidas.objects.filter(usuarioPreg= UsuarioJugador)
    pregunta = UsuarioJugador.obtener_Nuev_preguntas()
    context = {}
    
    
    """intentando que sean 10 preguntas al azar"""
    respondidas = PreguntasRespondidas.objects.filter(usuarioPreg= UsuarioJugador)
    
    contador_preguntas = respondidas.count()    
    # if contador_preguntas < 3:

    # if pregunta is None:
        # se puede poner 2 parametros de orden y agarra en primer termino uno y despues el otro
    total_usuarios = Usuario.objects.order_by('-puntajeTotal', '-CANTIDAD_PREGUNTAS_RESPONDIDAS_CORRECTAMENTE', '-CANTIDAD_PARTIDAS_JUGADAS')[:10]

    contador = total_usuarios.count()
    contador +=1
    pregunta_totales = Pregunta.objects.all().count()


    context = {

        'usuario': total_usuarios,
        'contar_user':contador,
        'contador_preg' : contador_preguntas,
        'CANT_PREG_POR_JUEGO' : CANT_PREG_POR_JUEGO,
        'pregunta' : pregunta,
        'pregunta_totales': pregunta_totales
}


    # if request.method == "POST":        
    #     PregResp = PreguntasRespondidas.objects.all()
    #     PregResp.delete()        
    #     return redirect('Juego')

    return render(request, 'resultados_multiplechoice.html', context)
    


# 
  
@login_required(login_url= '/')
def Juego(request):
    UsuarioJugador, created = Usuario.objects.get_or_create(usuario=request.user)
    
    
    pregunta_totales = Pregunta.objects.all().count()
    

    context = {"CANT_PREG_POR_JUEGO": CANT_PREG_POR_JUEGO, 'pregunta_totales': pregunta_totales} 
    
    # vamos a necesitar condicionales dentro de un formulario sino va a entrar en el else
    # si estamos enviando datos
    # hay que encontrar el identificador de la pregunta
    # encontrar el id de esa pregunta
    # y si es correcto que se tome
    if request.method == "POST":
               
        
        pregunta_pk = request.POST.get('pregunta_pk')
        # vamos a la clase PreguntasRespondidas para acceder a related_name='intentos'
        # con select_related vamos a tomar de pregunta para obtener el id de la pregunta
        pregunta_respondida = UsuarioJugador.intentos.select_related('pregunta').get(pregunta__pk= pregunta_pk)
        respuesta_pk = request.POST.get('respuesta_pk')
        try:
            # as?? obtenemos la pregunta que seleccionamos, el identificador y si hay error nos manda al except  
            opcion_seleccionada = pregunta_respondida.pregunta.opciones.get(pk=respuesta_pk)
        except ObjectDoesNotExist:
            return redirect('Jugar')
        
        UsuarioJugador.validar_intentos(pregunta_respondida, opcion_seleccionada)
        return redirect('resultados', pregunta_respondida.pk)
        
        # validar nuestro intento

    else:
        # registro de nuevas preguntas

        
# enlazamos pregunta respondida con el usuario LOgeado (Usuario) devuelve una tupla
        respondidas = PreguntasRespondidas.objects.filter(usuarioPreg= UsuarioJugador).values_list('pregunta__pk', flat=True) 
# podemos ver todas las preguntas creadas (all() selecciona a todos y exclude() excluye) excluye las que fueron respondidas
        pregunta = Pregunta.objects.exclude(pk__in=respondidas)
        
        
        """probando generar 10 preguntas"""
        contador_preguntas = respondidas.count()
        contador_preguntas +=1

        pregunta = UsuarioJugador.obtener_Nuev_preguntas()

        pregunta_totales = Pregunta.objects.all().count()

        if contador_preguntas < (CANT_PREG_POR_JUEGO+1):
            if pregunta is not None:
                # if pregunta is not None:
                UsuarioJugador.crear_intento(pregunta)


                context = {
                    'pregunta': pregunta,
                    'contador': contador_preguntas,
                    'CANT_PREG_POR_JUEGO': CANT_PREG_POR_JUEGO,
                    'pregunta_totales': pregunta_totales
                    

                }
            elif pregunta_totales == 0:
                pass            
            else:
                UsuarioJugador.CANTIDAD_PARTIDAS_JUGADAS +=1
                UsuarioJugador.save()
                        
        else:
            UsuarioJugador, created = Usuario.objects.get_or_create(usuario=request.user)
            UsuarioJugador.CANTIDAD_PARTIDAS_JUGADAS +=1
            UsuarioJugador.save()
            return redirect('resultados_multiplechoice')
            
            
    return render(request, "Jugar.html",  context)


@login_required(login_url= '/')
def resultado_pregunta(request, pregunta_respondida_pk):
    # si no obtiene el objeto nos devuelve error
	respondida = get_object_or_404(PreguntasRespondidas, pk=pregunta_respondida_pk)

	context = {
		'respondida':respondida
	}
	return render(request, 'resultados.html', context)

# esto iba en el else de la clase juego
# Aca tomamos las respuestas respondidas y enlazarlas mediante el id, entramos a presguntasRespondidasUser,  y exxcluimos las preguntas (pk) respnodidas

# enlazamos pregunta respondida con el usuario LOgeado (Usuario) devuelve una tupla
        # respondidas = PreguntasRespondidas.objects.filter(usuario= UsuarioJugador).values_list('pregunta__pk', flat=True) 
# podemos ver todas las preguntas creadas (all() selecciona a todos y exclude() excluye) excluye las que fueron respondidas
        # pregunta = Pregunta.objects.exclude(pk__in=respondidas)

@login_required(login_url= '/')
def JuegoVistaGeneral(request):     
    UsuarioJugador, created = Usuario.objects.get_or_create(usuario=request.user)
    respondidas = PreguntasRespondidas.objects.filter(usuarioPreg= UsuarioJugador)
    pregunta = Pregunta.objects.exclude(pk__in=respondidas)
    pregunta = UsuarioJugador.obtener_Nuev_preguntas()
        
    """intentando que sean 10 preguntas al azar"""
    respondidas = PreguntasRespondidas.objects.filter(usuarioPreg= UsuarioJugador)
    
    contador_preguntas = respondidas.count()    

    
    pregunta_totales = Pregunta.objects.all().count()
    
    context = {
        'pregunta': pregunta,
        'contador_preg': contador_preguntas,
        'CANT_PREG_POR_JUEGO': CANT_PREG_POR_JUEGO,
        'pregunta_totales': pregunta_totales
        }
    
    if request.method == "POST":
        PregResp = PreguntasRespondidas.objects.all()
        PregResp.delete()        
        UsuarioJugador.puntajeTotal = 0
        UsuarioJugador.save()
        return redirect('Jugar')
    return render(request, 'Juego.html', context)




@login_required(login_url= '/')    
def tabla_posiciones(request):
    UsuarioJugador, created = Usuario.objects.get_or_create(usuario=request.user)
    respondidas = PreguntasRespondidas.objects.filter(usuarioPreg= UsuarioJugador)
    pregunta = UsuarioJugador.obtener_Nuev_preguntas()
    #  if pregunta None (significa porque no hay preguntas agregadas)
    context = {}
    

    """probando generar 10 preguntas"""
    respondidas = PreguntasRespondidas.objects.filter(usuarioPreg= UsuarioJugador).values_list('pregunta__pk', flat=True) 
    
    contador_preguntas = respondidas.count()


    
    # if contador_preguntas == (CANT_PREG_POR_JUEGO-1):
    # if pregunta is None:
    total_usuarios = Usuario.objects.order_by('-puntajeTotal', '-CANTIDAD_PREGUNTAS_RESPONDIDAS_CORRECTAMENTE', '-CANTIDAD_PARTIDAS_JUGADAS')[:10]
    contador = total_usuarios.count()
    
    context = {

        'usuario': total_usuarios,
        'contar_user':contador,
        "contador_preguntas": contador_preguntas,
        "CANT_PREG_POR_JUEGO": CANT_PREG_POR_JUEGO,
        
    }
    return render(request, 'tabla_posiciones.html', context)
    








# intentando juego con categorias parte del juego no se esta ejecutando, por falta de tiempo me queda como meta mejorar despues del curso
"""
@login_required(login_url= '/')
def Juego_categoria_VistaGeneral(request):     
    
    if request.method == "POST":
               
        
        categoria = request.POST.get('categoria')
        
        try:
            
            Preguntas_categoria_elegida = Pregunta.objects.filter(dificultad_o_categoria= categoria)
           
        except ObjectDoesNotExist:
            return redirect('Juego_categoria')
        
        
        return redirect('Jugar_categoria', {'preguntas_cat' : Preguntas_categoria_elegida})
    
        

    dificultad = Pregunta.objects.filter(dificultad_o_categoria= 'Facil')
    context = {

        "dificultad" : dificultad

    }    
    return render(request, "Juego_categoria.html",  context)



@login_required(login_url= '/')
def Juego_categoria(request):
    UsuarioJugador, created = Usuario.objects.get_or_create(usuario=request.user)
    
    
    if request.method == "POST":
        pass

"""