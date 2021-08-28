from django.core.checks import messages
from django.http.response import HttpResponseRedirect
from django.views.generic.detail import DetailView
from django.views.generic.edit import FormView
from AniversarioChaco.admin import PreguntasRespondidasAdmin
from django.shortcuts import get_object_or_404, render
from django.urls.base import reverse
from django.views.generic.base import TemplateView
from AniversarioChaco.models import Usuario, Pregunta, PreguntasRespondidas, ElegirRespuesta
# Create your views here.
from Administrador.form import AdminRespuestaForm, AdminPreguntaForm
# heredando de mixins se puede restringir la pagina
# from django.contrib.auth.mixins import LoginRequiredMixin

# heredar la clase ListView y atributos 
from django.views.generic import ListView, CreateView, UpdateView, DetailView, DeleteView
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
# from AniversarioChaco.admin import ElegirRespuesta, ElegirRespuestaAdmin, PreguntaAdmin
from django.forms.models import inlineformset_factory


ElegirResFormset = inlineformset_factory(
    Pregunta, ElegirRespuesta, fields=('correcta', "texto")
)

RespuestasPreguntaFormSet = inlineformset_factory(
    Pregunta, ElegirRespuesta, fields=('pregunta', 'correcta', "texto")
)


class CrearPreg(CreateView):
    template_name = "cargar_preguntas.html"
    model = Pregunta
    from_class = RespuestasPreguntaFormSet
    # en teoria trabaja por defecto con el nombre que esté en el template
    # context_object_name = "agregarPreg"
    # inlines = (ElegirRespuestaAdmin,)
    fields = '__all__'
    # # redirecciona
    success_url = reverse_lazy('agregar')

"""
    
class pregunta_creada(CreateView):
    model = ElegirRespuesta
    from_class = RespuestasPreguntaFormSet
    # context_object_name = 'respuestas'
    template_name = "pregunta_creada.html"
    fields = '__all__'
    success_url = reverse_lazy('agregar')


class CrearPreg(CreateView):
    template_name = "cargar_preguntas.html"
    model = Pregunta
    fields = ['texto']
    
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
"""
""" 
class Modif_pregunta_creada(UpdateView):
    template_name = "modif_pregunta_creada.html"
    model = Pregunta
    from_class = ElegirResFormset
    # en teoria trabaja por defecto con el nombre que esté en el template
    context_object_name = "pregunta"
    
    fields = '__all__'
    # # redirecciona
    success_url = reverse_lazy('ListaPreg')
"""



class Modif_pregunta_creada(UpdateView):
    template_name = "modif_pregunta_creada.html"
    model = Pregunta
    form_class = ElegirResFormset
    # o se coloca form_class o fields
    # fields = '__all__'
    
    # success_url = reverse_lazy ('editado')

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
        pregunta = contexto['pregunta']
        # self.object = form.save()
        if pregunta.is_valid():
            # pregunta.instance = self.object
            pregunta.save()

        # return super().form_valid(form)
        return HttpResponseRedirect(self.get_success_url())



    # def get_success_url(self):
    #     return reverse('lista_preguntas')


    def get_success_url(self):
    #    pk = self.kwargs["pk"]
    #    , kwargs={"pk": pk}
        return reverse("listaPreg")



class ListaPreg(ListView):
    model = Pregunta
    template_name = "lista_preguntas.html"




class respuestasDetailView(DetailView):
    model = Pregunta
    template_name = "respuestas_detalle.html"
    form_class = AdminPreguntaForm
    
class borrar_preg(DeleteView):
    model = Pregunta
    template_name= 'eliminar_pregunta.html'
    success_url = '/Adm/lista_preguntas'
    
""" 
from django.views.generic.detail import SingleObjectMixin

class Modif_pregunta_creada(SingleObjectMixin, FormView):    
    model = Pregunta
    template_name = "modif_pregunta_creada.html"
    def get(self, request, *args, **kwargs):
        self.object = self.get_object(queryset=Pregunta.objects.all())
        return super().get(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        self.object = self.get_object(queryset=Pregunta.objects.all())
        return super().get(request, *args, **kwargs)

    def get_form(self, form_class: None):
        return RespuestasPreguntaFormSet(**self.get_form_kwargs(), instance= self.object)
    
    def form_valid(self, form):
        form.save()
        
        messages.add_message(

            self.request,
            messages.SUCCESS,
            "Los cambios fueron salvados"

        )
        return HttpResponseRedirect(self.get_success_url())
    def get_success_url(self):
        return reverse('modificar')


"""

def resulPreguntas(request):
    return render(request, 'resultados_preguntas.html')


def Editado(request):
    return render(request, 'pregunta_cambiada.html')    


from Usuario.views import tablero

def tablero(request):    
    total_usuarios = Usuario.objects.order_by('-puntajeTotal')[:10]
    contador = total_usuarios.count()
    context = {
		'usuario': total_usuarios,
		'contar_user':contador
	}
    return render(request, 'resultados_historico.html', context)