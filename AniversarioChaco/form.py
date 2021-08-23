from django import forms
from django.forms.forms import Form

from .models import Pregunta, ElegirRespuesta, PreguntasRespondidas



# esta class hay que llevarla al admin
class ElegirInlineFormSet(forms.BaseInlineFormSet):
    def clean(self):
        super(ElegirInlineFormSet, self).clean()

        respuesta_correcta = 0


        for formulario in self.forms:
            if not formulario.is_valid():
                return
            
            if formulario.cleaned_data and formulario.cleaned_data.get('correcta') is True:
                respuesta_correcta += 1
            
        try:
            # esto es para determinar el máximo de respuestas permitidas
            assert respuesta_correcta == Pregunta.RESPUESTAS_PERMITIDAS
        except AssertionError:
            raise forms.ValidationError("Solo una respuesta es permitida")
# si en el formulario obtenemos 'correcta' es true (es decir si es correcta la respuesta) va a sumar al acumulador





# probando alternativa a formulario de inicio
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate, get_user_model



# modelo User
User = get_user_model()

class RegistroFromulario(UserCreationForm):
    email = forms.EmailField(required=True)
    first_name = forms.CharField(required=True)
    last_name = forms.CharField(required=True)

    class Meta:
        model = User
        # indicar que formularios queremos agregar y en que orden ser renderizado
        fields = [
            'first_name',
            'last_name',
            'username',
            'password1',
            'password2',
            'email'
        ]
    # def __str__(self):
    #     return f'Usuario {self.fields['username']} creado'

# forms.Form = Es un formulario sin base
# modelFoms = hereda de un formulario base

# from AniversarioChaco.admin import PreguntaAdmin


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

 







# practicando formulario ingreso /NO ESTA EJECUTANDOSE
# crear formulario de login basado en formulario
class UsuarioLoginFormulario(forms.Form):
    username = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput)

    def limpiar(self, *arg, **kwargs):
        username = self.cleaned_data.get('username')
        password = self.cleaned_data.get('password')

        if username and password:
            user = authenticate(username= username, password= password)
            if not user:
                raise forms.ValidationError("Este usuario No existe")
            if not user.check_password(password):
                raise forms.ValidationError("Contraseña Incorrecta")
            if not user.is_active:
                raise forms.ValidationError("Este usuario no esta activo")

        return super(UsuarioLoginFormulario, self).clean(*arg, **kwargs)