# Proyecto-Informatorio-Grupo-4
Practicando alternativas para Modelo del Proyecto: Crear una página web que representa un juego de multiple choice en conmemoración del Aniversario de la Provincia del Chaco

Las siguientes instrucciones te permiten obtener una copia en tu maquina local para pruebas y desarrollo.
REQUISITOS:

*instalar en su entorno Virtual las dependencias del proyecto (ir a carpeta requirements para ver el archivo base.txt):
pip install -r base.txt

En settings.py de ProyectoWeb modificar con los datos que corresponden a su maquina local lo que esta en el apartado "DATABASES":

DATABASES = {
   
   'default': {
   
        'ENGINE': 'django.db.backends.# Aca agregamos nuestro Conector de DB',
        
        'NAME': 'MultipleChoice', # Aca nos aseguramos de crear una DB con el nombre 'MultipleChoice' en nuestro equipo para poder copiar la DB del Repositorio: python manage.py migrate
        
        'USER': '# Aca agregamos nuestro Usuario de DB',
        
        'PASSWORD': '# Aca agregamos nuestra Contraseña de DB',
        
        'HOST': '# Aca agregamos nuestro HOST de DB',
        
        'DATABASE_PORT': '# Aca agregamos nuestro Puerto de DB',
    }
}

- De esta forma ya podemos tener una copia del repositorio que sea funcional en nuestra maquina local.

 Especificaciones del Funcionamiento del Proyecto:
 
*El registro USUARIO solo puede jugar y ver su Resultado, y volver a intentarlo.

*El ADMINISTRADOR, es un SuperUSUARIO, que crea preguntas y respuestas y elige cuales son las correctas. Puede ver las planillas de Posiciones con los datos personales de los participantes (nombre, apellido, correo, puntaje, y si es o no Administrador)

*Para poder acceder a las funciones ambos deben Logearse.
