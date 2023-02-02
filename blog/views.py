import datetime
from blog.models import Articulos
from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def saludo(request):
      persona = Persona("Iván", "Escalante")
      temas_del_curso = ["Formularios", "Modelos", "Vistas", "Despliegue"]
      fecha_actual = datetime.datetime.now()
      return render(request, "saludo.html", {"nombre_persona":persona.nombre, "apellido_persona":persona.apellido, "fecha_actual":fecha_actual,  "temas" : temas_del_curso})

def despedida(request):
      return HttpResponse("Esta es la página de despedida")

def dameFecha(request):
      fecha_actual = datetime.datetime.now()

      documento = """
      <html>
      <body>
      <h2>
      La fecha y hora actual es: {}
      </h2>
      </body>
      </html>
      """.format(fecha_actual)

      return HttpResponse(documento)

def calculaEdadActual(request, edad, agno):
      periodo = agno - datetime.datetime.now().year 
      nueva_edad = edad + periodo
      documento = """
        <html>
        <body>
        <h2>
        En el año {} tendrás: {}
        </h2>
        </body>
        </html>
        """.format(agno, nueva_edad)

      return HttpResponse(documento)

class Persona(object):
      def __init__(self, nombre, apellido):
        self.nombre = nombre
        self.apellido = apellido

def saludo(request):
  #  return render(request, "saludo.html", {"nombre_persona": "Iván", "apellido_persona": "Escalante", "fecha_actual": datetime.datetime.now()})
      persona = Persona("Iván", "Escalante")
      temas_del_curso = ["Formularios", "Modelos", "Vistas", "Despliegue"]
      fecha_actual = datetime.datetime.now()
      return render(request, "saludo.html",
        {"nombre_persona":persona.nombre,
        "apellido_persona":persona.apellido,
        "fecha_actual":fecha_actual,
        "temas" : temas_del_curso})

def curso_django(request):
    fecha_actual = datetime.datetime.now()
    return render(request, "curso_django.html", {"fecha_actual":fecha_actual})

def curso_python(request):
    fecha_actual = datetime.datetime.now()
    return render(request, "curso_python.html", {"fecha_actual":fecha_actual})

def articulo(request, nombre, seccion, precio):
      articulo = Articulos.crear_articulo(nombre, seccion, precio)
      return render(request, "filtrado.html", {"articulo":articulo})

def todos_los_articulos(request):
      articulos = Articulos.todos_los_articulos()
      return render(request, "mostrar_articulos.html", {"articulos":articulos})

def borrar_articulo(request,id):
      Articulos.borrar_articulo(id)
      documento = """
        <html>
        <body>
        <h2>
        Has borrado el objeto con id {}
        </h2>
        </body>
        </html>
        """.format(id)
      return HttpResponse(documento)

def update_articulo(request,id,nombre,seccion,precio):
      articulo = Articulos.update_articulo(id,nombre,seccion,precio)
      return render(request,'update_articulos.html',{"articulo":articulo})