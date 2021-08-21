from django.shortcuts import render
from AniversarioChaco.models import Usuario, Pregunta, PreguntasRespondidas
# Create your views here.

# heredar la clase ListView y atributos 
from django.views.generic import ListView

class agregar(ListView):
    template_name = "cargar_preguntas.html"
    model = Pregunta
    context_object_name = "agregar_pregunta"

