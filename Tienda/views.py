from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.messages.views import SuccessMessageMixin
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import Producto
from .forms import ProductoForm

class ProductoListView(ListView):
    model = Producto
    template_name = 'Tienda/lista_productos.html'
    context_object_name = 'productos'

    def get_queryset(self):
        return Producto.objects.select_related('categoria').all()

class ProductoDetailView(DetailView):
    model = Producto
    template_name = 'Tienda/detalle_producto.html'
    context_object_name = 'producto'

    def get_queryset(self):
        return Producto.objects.select_related('categoria')

class ProductoCreateView(LoginRequiredMixin, SuccessMessageMixin, CreateView):
    model = Producto
    form_class = ProductoForm
    template_name = 'Tienda/producto_form.html'
    success_url = reverse_lazy('lista_productos')
    success_message = "¡Producto creado exitosamente!"

class ProductoUpdateView(LoginRequiredMixin, SuccessMessageMixin, UpdateView):
    model = Producto
    form_class = ProductoForm
    template_name = 'Tienda/producto_form.html'
    success_url = reverse_lazy('lista_productos')
    success_message = "¡Producto actualizado correctamente!"

class ProductoDeleteView(LoginRequiredMixin, DeleteView):
    model = Producto
    template_name = 'Tienda/producto_confirm_delete.html'
    success_url = reverse_lazy('lista_productos')
    context_object_name = 'producto'
    
    def delete(self, request, *from_args, **kwargs):
        from django.contrib import messages
        messages.success(self.request, "¡Producto eliminado del sistema!")
        return super().delete(request, *from_args, **kwargs)