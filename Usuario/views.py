from ProyectoWeb.AniversarioChaco.models import Usuarios
from django.core.exceptions import ObjectDoesNotExist
from django.http.response import Http404
from django.utils import tree
from AniversarioChaco.models import Usuarios, Pregunta, PreguntasRespondidas
from django.shortcuts import redirect, render, get_object_or_404


from AniversarioChaco.views import *

# Create your views here.


# traemos de models de Aniversario a Usuario
# de esta manera se crea el campo de usuario    
# va a crear o traer al usuario

def tablero(request):
	total_usuarios = Usuarios.objects.order_by('-puntajeTotal')[:10]
	contador = total_usuarios.count()

	context = {

		'usuario': total_usuarios,
		'contar_user':contador
	}

	return render(request, 'resultados_multiplechoice.html', context)

def Juego(request):
    UsuarioJugador, created = Usuarios.objects.get_or_create(usuario=request.user)
    # vamos a necesitar condicionales dentro de un formulario sino va a entrar en el else
    # si estamos enviando datos
    # hay que encontrar el identificador de la pregunta
    # encontrar el id de esa pregunta
    # y si es correcto que se tome
    if request.method == "POST":
        pregunta_pk = request.POST.get('pregunta_pk')
        # vamos a la clase PreguntasRespondidas para acceder a related_name='intentos'
        # con select_related vamos a tomar de pregunta para obtener el id de la pregunta
        pregunta_respondida = UsuarioJugador.intentos.select_related("pregunta").get(pregunta__pk= pregunta_pk)
        respuesta_pk = request.POST.get('respuesta_pk')
        try:
            # así obtenemos la pregunta que seleccionamos, el identificador y si hay error nos manda al except  
            opcion_seleccionada = pregunta_respondida.pregunta.opciones.get(pk=respuesta_pk)
        except ObjectDoesNotExist:
            raise Http404
        
        UsuarioJugador.validar_intentos(pregunta_respondida, opcion_seleccionada)
        return redirect("/Usuario/resultados", pregunta_respondida.pk)

        
        
        # validar nuestro intento

    else:
        # registro de nuevas preguntas

        
# enlazamos pregunta respondida con el usuario LOgeado (Usuario) devuelve una tupla
        respondidas = PreguntasRespondidas.objects.filter(usuarioPreg= UsuarioJugador).values_list('pregunta__pk', flat=True) 
# podemos ver todas las preguntas creadas (all() selecciona a todos y exclude() excluye) excluye las que fueron respondidas
        pregunta = Pregunta.objects.exclude(pk__in=respondidas)

        pregunta = UsuarioJugador.obtener_Nuev_preguntas()
        if pregunta is not None:
            UsuarioJugador.crear_intento(pregunta)


        context = {
            'pregunta': pregunta

        }
    return render(request, "Jugar.html", context)



# def resultados(request):
#     return render(request, "resultados_multiplechoice.html")


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