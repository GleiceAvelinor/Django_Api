import django_filters
from .models import Empresa, Pessoa,Usuario

class EmpresaFilter(django_filters.FilterSet):
    nome = django_filters.CharFilter(
        field_name='nome',
        lookup_expr='icontains',
        label='Filtrar por nome (busca parcial, não sensível a maiúsculas)',
    )
    id = django_filters.NumberFilter(
        field_name='id',
        lookup_expr='exact',
        label='Filtrar por ID (busca exata)',
    )
    # Exemplo de filtro com busca exata em um campo booleano
    status = django_filters.BooleanFilter(
        field_name='status',
        label='Filtrar por status ativo',
    )

    class Meta:
        model = Empresa
        fields = ['nome', 'id', 'status']
        
class PessoaFilter(django_filters.FilterSet):
    nome = django_filters.CharFilter(
        field_name='nome',
        lookup_expr='icontains',
        label='Filtrar por nome (busca parcial, não sensível a maiúsculas)',
    )
    id = django_filters.NumberFilter(
        field_name='id',
        lookup_expr='exact',
        label='Filtrar por ID (busca exata)',
    )
    
    status= django_filters.BooleanFilter(
        field_name='status',
        label='Filtrar por status ativo',
    )

    class Meta:
        model = Pessoa
        fields = ['nome', 'id', 'status']

class UsuarioFilter(django_filters.FilterSet):
    nome = django_filters.CharFilter(
        field_name='nome',
        lookup_expr='icontains',
        label='Filtrar por nome (busca parcial, não sensível a maiúsculas)',
    )
    id = django_filters.NumberFilter(
        field_name='id',
        lookup_expr='exact',
        label='Filtrar por ID (busca exata)',
    )
    
    status= django_filters.BooleanFilter(
        field_name='status',
        label='Filtrar por status ativo',
    )

    class Meta:
        model = Usuario
        fields = ['nome', 'id', 'status']

