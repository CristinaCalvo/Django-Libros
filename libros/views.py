from django.shortcuts import render, redirect
from .models import Libro
from .forms import LibroForm
from django.views import View
from django.shortcuts import get_object_or_404

# Create your views here.

class ListaLibros(View):
    template_name = 'libros/libros_list.html'

    def get(self, request):
        libros = Libro.objects.all()
        return render(request, self.template_name, {'libros': libros})

    def post(self, request):
        form = LibroForm(request.POST)
        form.save()
        libros = Libro.objects.all() #actualizar
        return render(request, self.template_name, {'libros': libros})
        

class LibroNuevo(View):
    libros = Libro.objects.all()

    def post(self, request):
        form = LibroForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('nuevo_libro')
        return render(request, 'libros/nuevo_libro.html', {'libros': self.libros, 'form' : form})
    

    def get(self, request):
        libros = Libro.objects.all()
        form=LibroForm()
        return render(request, 'libros/nuevo_libro.html', {'form' : form})
    
              #a  

class DetallesClass(View):

    def get(self, request, pk): 
     libros = get_object_or_404(Libro, pk=pk) 
     return render(request, 'libros/detalles.html', {'libros': libros})