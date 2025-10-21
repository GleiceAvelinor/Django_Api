# minha_api/urls.py

from django.urls import path
from .views import (
    EmpresaListCreate,
    EmpresaRetrieveUpdateDestroy,
    PessoaListCreate,
    PessoaRetrieveUpdateDestroy,
    UsuarioListCreate,
    UsuarioRetrieveUpdateDestroy
)

urlpatterns = [
   
    path('empresas/', EmpresaListCreate.as_view(), name='empresa-list-create'),
    
    path('empresas/<int:pk>/', EmpresaRetrieveUpdateDestroy.as_view(), name='empresa-detail'),
    
    path('pessoas/', PessoaListCreate.as_view(), name='pessoa-list-create'),
    
    path('pessoas/<int:pk>/', PessoaRetrieveUpdateDestroy.as_view(), name='pessoa-detail'),

    path('usuarios/', UsuarioListCreate.as_view(), name='usuario-list-create'),
    
    path('usuarios/<int:pk>/', UsuarioRetrieveUpdateDestroy.as_view(), name='usuario-detail'),
]