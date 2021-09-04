# Proyecto-Informatorio-Grupo-4


Practicando alternativas para Modelo del Proyecto: Crear una página web que representa un juego de multiple choice en conmemoración del Aniversario de la Provincia del Chaco

## Las siguientes instrucciones te permiten obtener una copia en tu maquina local para pruebas y desarrollo.
####  🔧 REQUISITOS: 

*instalar en su entorno Virtual las dependencias del proyecto (ir a carpeta requirements para ver el archivo base.txt):
pip install -r base.txt

En `settings.py` de ProyectoWeb modificar con los datos que corresponden a su maquina local lo que esta en el apartado "DATABASES":


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

 Especificaciones del Funcionamiento del Proyecto:
 
## El JUEGO:
Se basa en un Multiple Choice, en el cual la pagina Principal nos presenta los datos de Contacto de los integrantes y una intro con datos historicos e imagenes. Para poder acceder al juego en si es necesario que el Usuario se registre. Una vez registrado puede logearse e ingresar a Jugar, y cuando finaliza el mismo puede compartir su resultado y ver una tabla de posiciones básica que consta de posición, nombre de usuario y puntaje.

### El administrador en el Juego:
Es un SuperUSUARIO, que crea y elimina preguntas y respuestas; Y tambien elige cual es la correcta. Puede ver una tabla de Posiciones de los participantes en detalle (fecha de registro, fecha de ultima partida, cantidad de partidas jugadas, historial de respuestas correctas)

### Como particularidad:
El JUEGO funciona enviando de manera aleatoria 10 preguntas, alcanzando como maximo los 10 Puntos. Solo es guardado y visible el puntaje de la ultima partida. En el caso de que el Administrador haya agregado menos de 10 preguntas, el juego da un aviso al Usuario para que lo tenga en cuenta y se ponga en contacto con el Administrador para informarle del fallo. En el caso de que dos o más Jugadores tengan el mismo puntaje final, su posición en la tabla estará dada en primer lugar por su historico de respuestas correctas y en segundo por la cantidad de partidas jugada. La tabla de posiciones es un top 10, es decir solo guarda 10 posiciones.


## 📄 Las reglas del juego son: 
1. El sistema te genera 10 preguntas aleatorias de distinta dificultad.
2. Cada pregunta vale 1 punto.
3. Las preguntas solo tienen una respuesta correcta.
4. Reiniciar o salir de la pantalla del juego se considera como una respuesta incorrecta y tendras que volver a retomar en el estado que se encontraba el cuestionario
5. No elegir ningúna pregunta se considera como una respuesta incorrecta.
6. Una vez que contestes todas las preguntas se te guardara un solo puntaje.
7. En el caso de que dos o más Jugadores tengan el mismo puntaje final, su posición en la tabla estará dada en primer lugar por su historico de respuestas correctas y en segundo por la cantidad de partidas jugadas
8. Puedes volver a Jugar una vez que finalice el cuestionario presionando sobre el boton
