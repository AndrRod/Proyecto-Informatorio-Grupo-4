
from django import forms
from django.shortcuts import redirect, render, HttpResponse


# 09/08/2021
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages



#14/08/2021 para crear formulario manualmente
from django.contrib.auth import authenticate, login


# 15/08/2021 para agregar a un usuario a un grupo

from django.contrib.auth.models import Group 




# Create your views here.
def home(request):
    return render(request, "home.html")




def Contacto(request):
    return render(request, "Contacto.html")

# html que pueden servir para el proyecto

def resultados_t(request):
    return render(request, "resultados_multiplechoice.html")





    # 09/08/2021

def registro(request):
    mensaje = ''
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        
        if form.is_valid():
            user = form.save()
            group = Group.objects.get(name="Grupo Jugadores")
            user.groups.add(group)
            username = form.cleaned_data['username']
            mensaje = messages.success(request, f'Usuario {username} creado')
            return redirect("registro")
        
        else:   mensaje = 'Usuario no fue creado correctamente'
    else:
        form = UserCreationForm()

    contexto = {'formulario': form, 'mensaje': mensaje}                    
            
    return render(request, "registration/login_registro.html", contexto)






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