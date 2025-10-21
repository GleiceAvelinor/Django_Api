# minha_api/views.py

from rest_framework import generics
# Importa os seus modelos de banco de dados
from .models import Empresa, Pessoa, Usuario
# Importa os seus Serializers
from .serializers import EmpresaSerializer, PessoaSerializer, UsuarioSerializer

# 1. Views para o modelo Empresa (Company)

class EmpresaListCreate(generics.ListCreateAPIView):
    """
    Endpoint: /empresas/
    Métodos:
    - GET: Lista todas as empresas.
    - POST: Cria uma nova empresa.
    """
    queryset = Empresa.objects.all()
    serializer_class = EmpresaSerializer

class EmpresaRetrieveUpdateDestroy(generics.RetrieveUpdateDestroyAPIView):
    """
    Endpoint: /empresas/<pk>/
    Métodos:
    - GET: Recupera os detalhes de uma empresa específica.
    - PUT/PATCH: Atualiza uma empresa específica.
    - DELETE: Deleta uma empresa específica.
    """
    queryset = Empresa.objects.all()
    serializer_class = EmpresaSerializer


# 2. Views para o modelo Pessoa (Person)

class PessoaListCreate(generics.ListCreateAPIView):
    """
    Endpoint: /pessoas/
    Métodos:
    - GET: Lista todas as pessoas.
    - POST: Cria uma nova pessoa.
    """
    queryset = Pessoa.objects.all()
    serializer_class = PessoaSerializer

class PessoaRetrieveUpdateDestroy(generics.RetrieveUpdateDestroyAPIView):
    """
    Endpoint: /pessoas/<pk>/
    Métodos:
    - GET: Recupera os detalhes de uma pessoa específica.
    - PUT/PATCH: Atualiza uma pessoa específica.
    - DELETE: Deleta uma pessoa específica.
    """
    queryset = Pessoa.objects.all()
    serializer_class = PessoaSerializer



# 3. Views para o modelo Usuario (User)

class UsuarioListCreate(generics.ListCreateAPIView):
    """
    Endpoint: /usuarios/
    Métodos:
    - GET: Lista todos os usuários.
    - POST: Cria um novo usuário.
    """
    queryset = Usuario.objects.all()
    serializer_class = UsuarioSerializer

class UsuarioRetrieveUpdateDestroy(generics.RetrieveUpdateDestroyAPIView):
    """
    Endpoint: /usuarios/<pk>/
    Métodos:
    - GET: Recupera os detalhes de um usuário específico.
    - PUT/PATCH: Atualiza um usuário específico.
    - DELETE: Deleta um usuário específico.
    """
    queryset = Usuario.objects.all()
    serializer_class = UsuarioSerializer