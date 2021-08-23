from django.contrib import admin
from django.db.models import fields

# Register your models here.
from .models import Pregunta, ElegirRespuesta, PreguntasRespondidas, Usuario
from .form import ElegirInlineFormSet
from django import forms




# Register your models here.

# para herederar los campos de ElegirRespue esta y observarlo en Pregunta para verlo en administrador

# tabularInline se usa para instanciar nuestros metodos elegirRespuestas
class ElegirRespuestaAdmin(admin.TabularInline):
    model = ElegirRespuesta
    #para que no se puedan borrar las respuestas (true o false)
    can_delete = False
    # esto determina la cantidad de respuestas posibles para elegir
    max_num = ElegirRespuesta.MAXIMO_RESPUESTAS
    min_num = ElegirRespuesta.MAXIMO_RESPUESTAS
    formset = ElegirInlineFormSet

class PreguntaAdmin(admin.ModelAdmin):
    model = Pregunta
    inlines = (ElegirRespuestaAdmin,)
    # desde el campo pregunta traer el texto
    list_display = ['texto',]
    # campos de busqueda
    # agregar el related_name de ElegirRespuesta en pregunta
    # preguntas__texto por si alguien quire encontrar una posible respuesta
    search_fields = ['texto', 'pregunta__texto']
    
    





# como se vera en panalla las preguntas respondidas
class PreguntasRespondidasAdmin(admin.ModelAdmin):
    list_display = ['pregunta', 'respuesta', 'correcta', 'puntajeObtenido']

    class Meta:
        model = PreguntasRespondidas

admin.site.register(PreguntasRespondidas, PreguntasRespondidasAdmin)
admin.site.register(Pregunta, PreguntaAdmin)
admin.site.register(ElegirRespuesta)
admin.site.register(Usuario)
