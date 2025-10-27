from rest_framework import viewsets
from django_filters.rest_framework import DjangoFilterBackend
from .models import Empresa, Pessoa, Usuario
from .serializers import EmpresaSerializer, PessoaSerializer, UsuarioSerializer
from .filters import EmpresaFilter, PessoaFilter, UsuarioFilter 

class EmpresaViewSet(viewsets.ModelViewSet):
    
    queryset = Empresa.objects.all()
    serializer_class = EmpresaSerializer
       
    filter_backends = [DjangoFilterBackend]
    filterset_class = EmpresaFilter
    
class PessoaViewSet(viewsets.ModelViewSet):
    
    queryset = Pessoa.objects.all()
    serializer_class = PessoaSerializer
    
 
    filter_backends = [DjangoFilterBackend]
    filterset_class = PessoaFilter

class UsuarioViewSet(viewsets.ModelViewSet):
    
    queryset = Usuario.objects.all()
    serializer_class = UsuarioSerializer
   
    filter_backends = [DjangoFilterBackend]
    filterset_class = UsuarioFilter