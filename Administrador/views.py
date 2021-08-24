



from django.shortcuts import get_object_or_404, render
from django.urls.base import reverse
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
from AniversarioChaco.admin import ElegirRespuesta, ElegirRespuestaAdmin, PreguntaAdmin
from django.forms.models import inlineformset_factory


ElegirResFormset = inlineformset_factory(
    Pregunta, ElegirRespuesta, fields=('pregunta', 'correcta', "texto")
)

"""
class CrearPreg(CreateView):
    template_name = "cargar_preguntas.html"
    model = Pregunta
    from_class = PreguntaAdmin
    # en teoria trabaja por defecto con el nombre que esté en el template
    # context_object_name = "agregarPreg"
    # inlines = (ElegirRespuestaAdmin,)
    fields = '__all__'
    # # redirecciona
    success_url = reverse_lazy('pregunta_creada')
    

class pregunta_creada(CreateView):
    model = ElegirRespuesta
    from_class = ElegirRespuestaAdmin
    # context_object_name = 'respuestas'
    template_name = "pregunta_creada.html"
    fields = '__all__'
    success_url = reverse_lazy('agregar')
"""

class CrearPreg(CreateView):
    template_name = "cargar_preguntas.html"
    model = Pregunta
    fields = '__all__'
    def get_context_data(self, **kwargs):
        data = super().get_context_data(**kwargs)
        if self.request.POST:
            data["pregunta"] = ElegirResFormset(self.request.POST)
        else:
            data['pregunta'] = ElegirResFormset()
        return data
    
    def form_valid(self, form):
        contexto = self.get_context_data()
        pregunta = contexto["pregunta"]
        self.objtect = form.save()
        if pregunta.is_valid():
            pregunta.instance = self.objtect
            pregunta.save()

        return super().form_valid(form)
    
    def get_success_url(self):
        return reverse("agregar")



class Modif_pregunta_creada(UpdateView):
    template_name = "modif_pregunta_creada.html"
    model = Pregunta
    fields = '__all__'
    def get_context_data(self, **kwargs):
        data = super().get_context_data(**kwargs)
        if self.request.POST:
            data["pregunta"] = ElegirResFormset(self.request.POST, instance=self.object)
        else:   
            data['pregunta'] = ElegirResFormset(instance=self.object)
        return data

    # def get_object(self):
    #     id = self.kwargs.get('id')
    #     return get_object_or_404(Pregunta, id= id)
    
    def form_valid(self, form):
        contexto = self.get_context_data()
        pregunta = contexto["pregunta"]
        self.objtect = form.save()
        if pregunta.is_valid():
            pregunta.instance = self.objtect
            pregunta.save()

        return super().form_valid(form)
    def get_success_url(self):
        return reverse("actualizar")



""" 
class Modif_pregunta_creada(UpdateView):
    model = ElegirRespuesta
    from_class = ElegirRespuestaAdmin
    # context_object_name = 'respuestas'
    template_name = "modif_pregunta_creada.html"
    fields = '__all__'

    def get_success_url(self):
        return reverse('agregar')

"""    
def resulPreguntas(request):
    return render(request, 'resultados_preguntas.html')