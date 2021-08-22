import django
from django.db.models import fields
from django.http.response import FileResponse
from django.shortcuts import redirect, render, HttpResponse
from django import forms

# 09/08/2021 
# importa: formulario de django, modelo de usuario predeterminado y formulario de creacion de usuario
# solo lleva 3 parametros, pero se pueden agregan más elmentos
# agregando import User
from django.contrib.auth.forms import UserCreationForm

from django.contrib import messages



#14/08/2021 para crear formulario manualmente
from django.contrib.auth import authenticate, login, logout, get_user_model


# 15/08/2021 para agregar a un usuario a un grupo

from django.contrib.auth.models import Group 

# para restringir el ingreso
from django.contrib.auth.decorators import login_required
# @login_required(redirect_field_name='login') # para resgringir el ingreso

#Probando una vista basada en clases
# TemplateView hereda de View
# por lo que internamente hace return render(request, template_name)

from django.views.generic import View, TemplateView
from django.views.generic.list import ListView

# class home(TemplateView):
#      template_name = "home.html"

# vista basa de clase
def home(request):
    return render(request, "home.html")


def Contacto(request):
    return render(request, "Contacto.html")

# class Contacto(TemplateView):
#      template_name = "Contacto.html"

    
    
# importamos el formulario de registro que creamos en form.py
from .form import RegistroFromulario, UsuarioLoginFormulario


# login basado en funciones

def registro(request):
    mensaje = ''
    if request.method == 'POST':
        #  este es el registro creado en modulo form.py en el cual se agrega correo y otros parametros
        form = RegistroFromulario(request.POST)

        # este es el registro que viene por defencto en django
        
        if form.is_valid():
            form.save()
            username = form.cleaned_data['username']
            mensaje = messages.success(request, f'Usuario {username} fue creado con exito')
            return redirect("login")
        
        
    else:
        form = RegistroFromulario()   

    contexto = {'formu': form, 'mensaje': mensaje}                    
            
    return render(request, "registration/login_registro.html", contexto)






































# este es el registro que viene por defencto en django
# form = UserCreationForm(request.POST)

# crear usuario y guardarlo en un grupo determinado
# user = form.save()
# group = Group.objects.get(name="Grupo Jugadores")
# user.groups.add(group)











# login basa en funciones: 

# def loginView(request):
#     titulo = 'login'
    
#     if request.method == 'POST':
#         form = UsuarioLoginFormulario(request.POST or None)

#         if form.is_valid():
#             username = form.cleaned_data.get('username')
#             password = form.cleaned_data.get('password')
#             usuario = authenticate(username= username, password = password)
#             login(request, usuario)
#             return redirect('/home/')
    

#     else: form = UsuarioLoginFormulario()

#     contexto = {"form" : form, 'titulo': titulo}
#     return render(request, "registration/login.html", contexto)



# login basa en class: 

# def loginView(request):
#     titulo = 'login'
    
#     if request.method == 'POST':
#         form = UsuarioLoginFormulario(request.POST or None)

#         if form.is_valid():
#             username = form.cleaned_data.get('username')
#             password = form.cleaned_data.get('password')
#             usuario = authenticate(username= username, password = password)
#             login(request, usuario)
#             return redirect('/home/')
    

#     else: form = UsuarioLoginFormulario()

#     contexto = {"form" : form, 'titulo': titulo}
#     return render(request, "registration/login.html", contexto)





# ____________________________________________________________________________________________________________

# Probando CODIGO:

# prbando agregando codigo para hacer el ingreso usuario
# from django.contrib.auth.models import User


# la forma más directa de crear un usuario
# Create user and save to the database
# user = User.objects.create_user('myusername', 'myemail@crazymail.com', 'mypassword')

# # Update fields and then save again
# user.first_name = 'John'
# user.last_name = 'Citizen'
# user.save()


# def registro(request):
#     data = { 'form': UserCreationForm} 
#     if request.method == 'POST':
#         formulario = UserCreationForm( data= request.POST)
#         if formulario.is_valid():
#             formulario.save()
#             user = authenticate(username = formulario.cleaned_data["username"], password= formulario.cleaned_data["password1"])
#             login(request, user)
#             messages.success(request, f'Usuario {user.get_username} creado')
#             return redirect(to='home')
#         data["form"] = formulario
#     return render(request, "registration/registro.html")



# usercreationform
# para registro de usuario


# estudiar ListView
# getqueryset (filtrar informacion)
# get_context_data()

# request esta como atributo de listview

# estudiar CreateView
# addView para actualizar cosas



# -_____------------------------------------------------------
# Listview también hereda de view

""" 
class lista(ListView):
    template_name = 
    queryset = hace por defecto Model.object.all()
    contex_object_name = por defecto es object_list  y con esto podemos darle un nombre distinto

"""