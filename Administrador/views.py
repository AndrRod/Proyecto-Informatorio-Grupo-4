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


from django.contrib import messages

from Usuario.views import tablero, CANT_PREG_POR_JUEGO



from django.contrib.admin.views.decorators import staff_member_required
from django.urls import reverse_lazy
# from AniversarioChaco.admin import ElegirRespuesta, ElegirRespuestaAdmin, PreguntaAdmin
from django.forms.models import inlineformset_factory


ElegirResFormset = inlineformset_factory(
    Pregunta, ElegirRespuesta, fields=( 'correcta', "texto")
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
    # inlines = (ElegirRespuesta,)
    fields = '__all__'
    # # redirecciona
    success_url = reverse_lazy('agregar')

    def get_success_url(self):
        mensaje = messages.success(self.request, 'La pregunta fue creada con exito')
        return reverse("agregar")   



# from django.contrib.messages.views import SuccessMessageMixin




class Modif_pregunta_creada(UpdateView):
    template_name = "modif_pregunta_creada.html"
    model = Pregunta
    form_class = ElegirResFormset

    # o se coloca form_class o fields
    # fields = '__all__'

    # success_message = 'La pregunta fue modificada con exito'
    
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
        
        if pregunta.is_valid():
            # pregunta.instance = self.object
            mensaje = messages.success(self.request, 'La pregunta fue modificada  con exito')
            pregunta.save()

        # return super().form_valid(form)
        return HttpResponseRedirect(self.get_success_url())

    def get_success_url(self):
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



    

def resulPreguntas(request):
    return render(request, 'resultados_preguntas.html')


def Editado(request):
    return render(request, 'pregunta_cambiada.html')    




def tablero(request):    
    # context = {}
    
    # UsuarioJugador, created = Usuario.objects.get_or_create(usuario=request.user)
    # respondidas = PreguntasRespondidas.objects.filter(usuarioPreg= UsuarioJugador)
    # pregunta = UsuarioJugador.obtener_Nuev_preguntas()

    
        # total_usuarios = Usuario.objects.order_by('-puntajeTotal')[:10]
        # contador = total_usuarios.count()
        
        # context = {
        #     'usuario': total_usuarios,
        #     'contar_user':contador,
        #     "CANT_PREG_POR_JUEGO": CANT_PREG_POR_JUEGO
        # }


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
    total_usuarios = Usuario.objects.order_by('-puntajeTotal')[:10]
    contador = total_usuarios.count()
    
    context = {

        'usuario': total_usuarios,
        'contar_user':contador,
        "contador_preguntas": contador_preguntas,
        "CANT_PREG_POR_JUEGO": CANT_PREG_POR_JUEGO,
        
    }
    return render(request, 'resultados_historico.html', context)











# EL SIGUIENTE CODIGO ES UNA RECOPILACION DE LO QUE FUIMOS INTENTANDO (CREATVIEW, LISTVEW, UPDATEVIEW Y OTROS)
    
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
