from django.contrib import admin
from django.urls import path
from inicio import views
from registros import views as views_registros
from django.conf import settings


urlpatterns = [

    path('admin/', admin.site.urls),

    # PRINCIPAL (usuarios)
    path('', views_registros.registros, name="Principal"),
    # CONTACTO
    path('contacto/', views.contacto, name="Contacto"),

    # FORMULARIO
    path('formulario/', views.formulario, name="Formulario"),

    # NOMBRE
    path('nombre/', views.nombre, name="Nombre"),

    # EJEMPLO
    path('ejemplo/', views.ejemplo, name="Ejemplo"),

    # REGISTRAR USUARIOS
    path('registrar/', views_registros.registrar, name="Registrar"),

    # ELIMINAR
    path(
        'eliminarComentario/<int:id>/',
        views_registros.eliminarComentarioContacto,
        name='Eliminar' ),

    #COMENTARIOS
    path('comentarios/',views_registros.consultarComentario,name="Comentarios"),

    #EDITAR
    path(
        'editarComentario/<int:id>/',
        views_registros.editarComentarioContacto,
        name='Editar'
    ),
    # CONSULTAR COMENTARIO INDIVIDUAL (para editar)
    path(
    'consultarComentario/<int:id>/',
    views_registros.consultarComentarioIndividual,
    name='ConsultarComentario'),

    #Filtrar
    path('consultas1',views_registros.consultas1,
         name="Consultas1"),

    path('consultas2',views_registros.consultas2,
         name="Consultas2"),

    path('consultas3',views_registros.consultas3,
         name="Consultas3"),

    path('consultas4',views_registros.consultas4,
         name="Consultas4"),

    path('consultas5',views_registros.consultas5,
         name="Consultas5"),

    path('consultas6',views_registros.consultas6,
         name="Consultas6"),

    path('consultas7',views_registros.consultas7,
         name="Consultas7"),

   #Archivo
    path('subir', views_registros.archivos,name="Subir"),


    path('archivo', views_registros.archivos, name="Archivo"),

    path('consultasSQL', views_registros.consultasSQL, name="sql"),

    path('seguridad',views.seguridad,name="Seguridad"),
]


if settings.DEBUG:
    from django.conf.urls.static import static

    urlpatterns += static(
        settings.MEDIA_URL,
        document_root=settings.MEDIA_ROOT
    )