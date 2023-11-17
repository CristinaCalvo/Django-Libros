from django.shortcuts import render, redirect
from .models import Libro
from .forms import LibroForm
from django.views import View
from django.shortcuts import get_object_or_404
from django.views.generic import ListView, DetailView


# Create your views here.


#class ListaLibros(View):
 #   template_name = 'libros/libros_list.html'

  #  def get(self, request):
   #     libros = Libro.objects.all()
    #    return render(request, self.template_name, {'libros': libros})

class ListaLibros(ListView):
    model = Libro
    template_name = 'libros/libros_list.html'


class LibroNuevo(View):
    libros = Libro.objects.all()

    def post(self, request):
        form = LibroForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('nuevo_libro')
        return render(request, 'libros/nuevo_libro.html', {'libros': self.libros, 'form' : form})
    

    def get(self, request):
        form=LibroForm()
        return render(request, 'libros/nuevo_libro.html', {'form' : form})
    
class DetallesClass(DetailView):
    model = Libro
    template_name = 'libros/detalles.html'


#class DetallesClass(View):

 #   def get(self, request, pk): 
  #   libros = get_object_or_404(Libro, pk=pk) 
   #  return render(request, 'libros/detalles.html', {'libros': libros})
    

class EditaLibro(View):

    def post(self, request, pk):
        libros = get_object_or_404(Libro, pk=pk)
        form = LibroForm(request.POST,instance=libros)

        if form.is_valid():
            form.save()
            return redirect('libros_list')
        return render(request, 'libros/edita.html', {'libros': libros, 'form': form})
    
    def get(self, request, pk):
        libros = get_object_or_404(Libro, pk=pk)
        form = LibroForm(instance=libros)
        libros = get_object_or_404(Libro, pk=pk)
        return render(request, 'libros/edita.html', {'libros': libros, 'form': form})