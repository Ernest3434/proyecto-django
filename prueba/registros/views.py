from urllib import request

from django.shortcuts import render
from .models import Alumnos
from .models import ComentarioContacto
from .forms import ComentarioContactoForm
from django.shortcuts import get_object_or_404
import datetime
from .models import Archivos
from .forms import FormArchivos
from django.contrib import messages
from django.shortcuts import render, redirect


# Create your views here.



def registros(request):
    alumnos=Alumnos.objects.all()

    return render(request, 'registros/principal.html', {'8A':alumnos})


def registrar(request):
    if request.method == 'POST':
        usuario = request.POST.get('usuario')
        mensaje = request.POST.get('mensaje')

        if usuario and mensaje:
            ComentarioContacto.objects.create(
                usuario=usuario,
                mensaje=mensaje
            )
            return redirect('Comentarios')

    return redirect('Contacto')

    return render(request, 'registros/contacto.html')


def contacto(request):
    return render(request, 'registros/contacto.html')


def consultarComentario(request):
    comentarios = ComentarioContacto.objects.all().order_by('-id')
    return render(request, 'registros/consultarComentario.html',
                  {'comentarios': comentarios})


def eliminarComentarioContacto(request, id,
    confirmacion ='registros/confirmarEliminacion.html'):
    comentario = get_object_or_404(ComentarioContacto, id=id)
    if request.method == 'POST':
        comentario.delete()
        comentarios = ComentarioContacto.objects.all()
        return render(request, 'registros/consultarComentario.html', {'comentarios': comentarios})
    return render(request, confirmacion, {'comentario': comentario})

def consultarComentarioIndividual(request,id):
    comentario=ComentarioContacto.objects.get(id=id)
    return render(request,"registros/formEditarComentario.html",
                  {'comentario': comentario})


def editarComentarioContacto(request,id):
       comentario = get_object_or_404(ComentarioContacto, id=id)
       form = ComentarioContactoForm(request.POST, instance=comentario)
       if form.is_valid(): #Si los datos recibidos son correctos
            form.save() #inserta
            comentarios = ComentarioContacto.objects.all() #consulta
            return render(request, 'registros/consultarComentario.html',
                           {'comentarios': comentarios})
    #Si algo sale mal se reenvian al formulario los datos ingresados
       return render(request,'registros/formEditarComentario.html',
              {'comentario': comentario})

#Funcion FILTER
#filter nos retornara los registros que coinciden con los parametros de busqueda dados

def consultas1(request):
     #con una sola condicion
     alumnos=Alumnos.objects.filter(carrera="TI")
     return render(request,"registros/consultas.html", {"8A":alumnos})


def consultas2(request):
     #con una sola condicion
     alumnos=Alumnos.objects.filter(carrera="TI").filter(turno="Matutino")
     return render(request,"registros/consultas.html", {'8A':alumnos})

def consultas3(request):
     #con una sola condicion
     alumnos=Alumnos.objects.all().only("matricula","nombre","carrera","turno","imagen")
     return render(request,"registros/consultas.html", {'8A':alumnos})

def consultas4(request):
     #con una sola condicion
     alumnos=Alumnos.objects.filter(turno__contains="Vesp")
     return render(request,"registros/consultas.html", {"8A":alumnos})

def consultas5(request):
     #con una sola condicion
     alumnos=Alumnos.objects.filter(nombre__in=["Juan" , "Ana"])
     return render(request,"registros/consultas.html", {"8A":alumnos})

def consultas6(request):
     fechaInicio = datetime.date(2026, 2 , 3)
     fechaFin = datetime.date(2026, 3, 12)
     alumnos=Alumnos.objects.filter(created__range=(fechaInicio,fechaFin))
     return render(request,"registros/consultas.html", {"8A":alumnos})


def consultas7(request):
     #con una sola condicion
     alumnos=Alumnos.objects.filter(comentario__coment__contains='No inscrito')
     return render(request,"registros/consultas.html", {"8A":alumnos})

def archivos(request):
    if request.method == 'POST':
        form = FormArchivos(request.POST, request.FILES)
        if form.is_valid():
            titulo = request.POST['titulo']
            descripcion = request.POST['descripcion']
            archivo = request.FILES['archivo']
            insert = Archivos(titulo=titulo, descripcion=descripcion, archivo=archivo)
            insert.save()
            return render(request, "registros/archivos.html")
        else:
            messages.error(request, "Error al procesar el formulario")
    else:
        return render(request, "registros/archivos.html", {'archivo': Archivos})


def consultasSQL(request):
    alumnos = Alumnos.objects.raw(
         'SELECT id,matricula, nombre, carrera, turno, imagen FROM registros_alumnos WHERE carrera="TI" ORDER BY turno DESC')

    return render(request, "registros/consultas.html", {'8A': alumnos})