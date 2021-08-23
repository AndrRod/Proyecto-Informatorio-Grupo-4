


from django.shortcuts import render
from django.views.generic.base import TemplateView
from AniversarioChaco.models import Usuario, Pregunta, PreguntasRespondidas, ElegirRespuesta
# Create your views here.
from AniversarioChaco.form import *
# heredando de mixins se puede restringir la pagina
# from django.contrib.auth.mixins import LoginRequiredMixin

# heredar la clase ListView y atributos 
from django.views.generic import ListView, CreateView, UpdateView
from AniversarioChaco import form
# probando si puedo usar el modelo de admin de AniversarioChaco


"""
class agregar(ListView):
    template_name = "cargar_preguntas.html"
    model = Pregunta
    # en su defecto te pasa por contexto object_list para dar un nombre distinto se usa context_objet_name
    context_object_name = "agre"



    # hacer filtrado
    def get_queryset(self):
        return Pregunta.objects.filter


    # asi se redefine el context data
   
    def get_context_data(self, **kwargs):
        # guardar en context todo lo que viene de la clase padre
        # context es un diccionario
        context = super().get_context_data(**kwargs)
        context['color']= "amarillo"
        return context
    def get_queryset(self):
        usuario = self.request.user
        return usuario
    """
from django.urls import reverse_lazy
from AniversarioChaco.admin import ElegirRespuesta

class CrearPreg(CreateView):
    template_name = "cargar_preguntas.html"
    model = Pregunta
    from_class = AdminPreguntaForm    
    # en teoria trabaja por defecto con el nombre que esté en el template
    # context_object_name = "agregarPreg"
    fields = '__all__'
    # # redirecciona
    success_url = reverse_lazy('pregunta_creada')
    

class pregunta_creada(CreateView):
    model = ElegirRespuesta
    from_class = AdminRespuestaForm   
    # context_object_name = 'respuestas'
    template_name = "pregunta_creada.html"
    fields = '__all__'
    success_url = reverse_lazy('agregar')