from rest_framework import serializers
from .models import Empresa, Pessoa,Usuario

class EmpresaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Empresa
        fields = '__all__'


class PessoaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Pessoa
        fields = '__all__'
        
class UsuarioSerializer(serializers.ModelSerializer):
    class Meta:
        model = Usuario
        fields = '__all__'
        
        
        