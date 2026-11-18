from django.urls import path
from .views import (
    ProductoListView, 
    ProductoDetailView, 
    ProductoCreateView, 
    ProductoUpdateView,
    ProductoDeleteView
)

urlpatterns = [
    path('productos/', ProductoListView.as_view(), name='lista_productos'),
    path('producto/<int:pk>/', ProductoDetailView.as_view(), name='detalle_producto'),
    path('producto/nuevo/', ProductoCreateView.as_view(), name='crear_producto'),
    path('producto/editar/<int:pk>/', ProductoUpdateView.as_view(), name='editar_producto'),
    path('producto/eliminar/<int:pk>/', ProductoDeleteView.as_view(), name='eliminar_producto'),
]