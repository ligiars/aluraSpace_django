from django.urls import path
from galeria.views import index, imagem

# boa prática de programação
urlpatterns = [
    path('', index, name='index'),
    path('imagem/<int:foto_id>', imagem, name='imagem'),
]
