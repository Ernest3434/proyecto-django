from django.shortcuts import render, HttpResponse

# Create your views here.

def principal(request):
    contenido = "<h1>Hola DJANGO</h1>"
    return HttpResponse(contenido)

def contacto(request):
    return render(request, "inicio/contacto.html")

def nombre(request):
    contenido = "<h1>Ernesto Antonio Avellaneda Avila</h1>"
    return HttpResponse(contenido)

def formulario(request):
    return render(request, "inicio/formulario.html")

def principal(request):
    return render(request, "inicio/principal.html")

def ejemplo(request):
    return render(request, "inicio/ejemplo.html")

def seguridad(request, nombre=None):
    nombre = request.GET.get('nombre')
    return render(request,"inicio/seguridad.html",
    {'nombre':nombre})
