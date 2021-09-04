from django.db import models
from django.db.models.base import Model
from django.db.models.deletion import CASCADE
from django.conf import settings
from django.contrib.auth.models import User
import random

from django.urls.base import reverse



# Create your models here.

# Create your models here.


# intentando incorporar categoria primero y despues duración de examen si se puede

DIFICULTAD = (('Facil', 'Facil'), ('Medio', 'Medio'), ('Dificil', 'Dificil'))



# class Caract_Categoria(models.Model):
#     dificultad_o_categoria = models.CharField(max_length=90, verbose_name= "dificultad", choices= DIFICULTAD, null= True)
# #     # puede ser tiempo que dure el examen
# #     # tiempo = models.IntegerField()
#     class Meta:
#         verbose_name = "dificultad"
     
#     def __str__(self):
#         return self.dificultad_o_categoria



# el usuario que va a participar
# para que nos tome el usuario lo importamos
# por defecto el puntaje es cero

# Creando el texto de nuestras preguntas
class Pregunta(models.Model):
    RESPUESTAS_PERMITIDAS = 1
    texto = models.TextField(verbose_name= 'Texto de la pregunta')
    # creamos atributo puntaje maximo que va a estar por defecto en 2
    # y con verbose_name ponemos como queremos que se vea en el panel de administracion
    
    max_puntaje = models.DecimalField(verbose_name= "Maximo Puntaje", default= 1, decimal_places=2, max_digits=6)
    dificultad_o_categoria = models.CharField(max_length=90, verbose_name= "dificultad", choices= DIFICULTAD, default = "Facil", null= True)
       

    # categoria = models.ForeignKey(Caract_Categoria, on_delete=models.CASCADE)
    class Meta:
        verbose_name ="pregunta"

    # def get_absolute_url(self):
    #     return reverse('detalle_pregunta', kwargs={'pk': self.pk})

    def __str__(self):
        return f'(Dif: {self.dificultad_o_categoria}) {self.texto}'



# elecciones a las preguntas
# hay que conectar la pregunta con la respuesta
# le damos respuestas a esa pregunta
class ElegirRespuesta(models.Model):
    #limitar las opciones
    MAXIMO_RESPUESTAS = 4

    # on_delete es para que desde la base de datos cuando se elimine una respuesta se elimina las dependencias
    pregunta = models.ForeignKey(Pregunta, related_name='opciones', on_delete=models.CASCADE)
    # para saber la pregunta verdadera lo hacemos con un booleano
    correcta = models.BooleanField(verbose_name= 'correcta', default=False, null=False)
    # texto posible respuestas
    texto = models.TextField(verbose_name= 'Texto de la respuesta')

    # para observar el texto de la respuesta
    def __str__(self):
        return self.texto
    

    # def get_absolute_url(self):
    #     return reverse('detalle_pregunta', kwargs={'pk': self.pk})

# import datetime
# from datetime import datetime
from django.utils import timezone

class Usuario(models.Model):
    usuario = models.OneToOneField(User, on_delete=CASCADE)
    puntajeTotal = models.DecimalField(verbose_name='Pungaje Total', default=0, max_digits= 10, decimal_places=2, null=True)
    # datetime.now fecha y dia de hoy
    fecha_creacion = models.DateField(default= timezone.now(), verbose_name="fecha de login")
    # fecha y hora tiene atributos especiales DatetimeField, el auto now (que la primera vez que se cree este registro será la unica vez que se modifique salvo que se coloque auto_now_add)
    fecha_modificacion = models.DateTimeField(auto_now= True, verbose_name="fecha de ultima partida")
    # fecha_actualizacion = models.DateTimeField(auto_now_add= True)
    CANTIDAD_PARTIDAS_JUGADAS = models.IntegerField(default=0, verbose_name = 'historial cantidad de partidas Jugadas')
    CANTIDAD_PREGUNTAS_RESPONDIDAS_CORRECTAMENTE  = models.IntegerField(default=0, verbose_name = 'historial cantidad de preguntas respondidas correctamente')

    

# intentar despues contador de ingreso y fecha ultimo ingreso
    # contador_de_ingresos = 
    # fecha_ultimo_ingreso = 
    

    # creamos funcionalidades de la aplicacion:
    # creamos los intentos y lo guardamos
    def crear_intento(self, pregunta):
        intentos = PreguntasRespondidas(pregunta= pregunta, usuarioPreg= self)
        intentos.save()
    
    def obtener_Nuev_preguntas(self):
        # hacemos la relación con PreguntasRespondidas
        # vamos a filtrar el usuario y con velue_lista accedemos a todas las preguntas que hemos tomado
        respondidas = PreguntasRespondidas.objects.filter(usuarioPreg= self).values_list('pregunta__pk', flat= True)
    
        preguntas_restantes = Pregunta.objects.exclude(pk__in=respondidas)
        # si no existe preguntas restantes
        if not preguntas_restantes.exists():
            return None
        # que returna preguntas aleatorias
        return random.choice(preguntas_restantes)

    def validar_intentos(self, pregunta_respondida, respuesta_seleccionada):
        if pregunta_respondida.pregunta_id != respuesta_seleccionada.pregunta_id:
            return
        pregunta_respondida.respuesta_seleccionada = respuesta_seleccionada
        if respuesta_seleccionada.correcta is True:
            pregunta_respondida.correcta = True
            pregunta_respondida.puntajeObtenido = respuesta_seleccionada.pregunta.max_puntaje
            pregunta_respondida.respuesta = respuesta_seleccionada
            self.CANTIDAD_PREGUNTAS_RESPONDIDAS_CORRECTAMENTE +=1
        # guardamos nuestra respuesta a la pregunta respondida  
        # si preguntas respondidas que hemos seleccionado coincide con la correcta que creamos, si es la correcta la validamos con un puntaje
         
        else:
            pregunta_respondida.respuesta = respuesta_seleccionada

        pregunta_respondida.save()
        self.actualizar_puntaje()
    

    def actualizar_puntaje(self):
        puntaje_actualizado = self.intentos.filter(correcta=True).aggregate(models.Sum('puntajeObtenido'))['puntajeObtenido__sum']

        self.puntajeTotal = puntaje_actualizado
        self.save()


# Una vez que se contesta la pregunta esa pregunta sera guardada
# y si es correcta el campo booleano se volvera True
#  y el puntaje sumara  
# crear clase que va a guardar los intentos de preguntas
class PreguntasRespondidas(models.Model):
    usuarioPreg = models.ForeignKey(Usuario, on_delete=models.CASCADE, related_name='intentos', null=False)
    # elminada una pregunta respondida que se elimine también la pregunta de la base de datos
    pregunta = models.ForeignKey(Pregunta, on_delete=models.CASCADE)
    # intentos hechos
    respuesta = models.ForeignKey(ElegirRespuesta, on_delete=models.CASCADE, null=True)
    # default false, es que por defecto no viene seleccionada
    correcta = models.BooleanField(verbose_name='Es esta la respuesta correcta?', default=False, null=False)
    # puntaje que por defecta será cero
    puntajeObtenido = models.DecimalField(verbose_name='Puntaje Obtenido', default=0, max_digits=6, decimal_places=2)




    # Categoria = models.CharField(max_length=90, verbose_name= "dificultad", null= True, choices= DIFICULTAD)

    # intentando incorporar categoria
    # cate = models.ForeignKey(Caract_Categoria, on_delete=models.CASCADE)



