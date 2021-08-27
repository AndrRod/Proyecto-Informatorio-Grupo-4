import django
from AniversarioChaco import form
from django import forms

from AniversarioChaco.models import Usuario, Pregunta, PreguntasRespondidas, ElegirRespuesta


# class PreguntaModelForm(ModelForm):
#     class Meta:
#         model = Pregunta
#         fields = '__all__'


# class RespuestasModelForm(ModelForm):
#     class Meta:
#         model = ElegirRespuesta
#         fields = ['correcta', "texto"]


# class PreguntaRespuestaModelForm(MultiForm):
#     form_classes = {
#         'pregunta': PreguntaModelForm,
#         'respuesta': RespuestasModelForm,
#     }




# Probando clase formulario para crear




class AdminPreguntaForm(forms.ModelForm):
    class Meta:
    #  model hace referencia al modelo que va a pertenecer
        model = Pregunta
    #  fields hace referencia a todos los campos que tiene el modelo que van a ser rellenados cuando creemos una nueva pregunta en este caso
        fields = '__all__'


class AdminRespuestaForm(forms.ModelForm):
    class Meta:
    #  model hace referencia al modelo que va a pertenecer
        model = ElegirRespuesta
    #  fields hace referencia a todos los campos que tiene el modelo que van a ser rellenados cuando creemos una nueva pregunta en este caso
        fields = '__all__'

