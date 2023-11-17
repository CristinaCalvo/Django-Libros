from django.urls import path
from .views import ListaLibros, LibroNuevo, DetallesClass, EditaLibro

urlpatterns = [
    path('', ListaLibros.as_view(), name='libros_list'),
	path('nuevo_libro/', LibroNuevo.as_view(), name='nuevo_libro'),
    path('detalles/<int:pk>/', DetallesClass.as_view(), name='detalles'),
    path('edita/<int:pk>/', EditaLibro.as_view(), name='edita'),
]