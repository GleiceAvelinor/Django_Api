from django.db import models # type: ignore

class Empresa(models.Model):
    nome = models.CharField(max_length=100)
    CNPJ = models.CharField(max_length=200)
    endereco = models.CharField(max_length=255)
    num = models.CharField(max_length=10)
    cep = models.CharField(max_length=20)
    bairro = models.CharField(max_length=100)
    cidade = models.CharField(max_length=100)
    UF = models.CharField(max_length=2)
    status = models.BooleanField(default=True)
    
    class Meta:
        verbose_name = "Empresa"
        verbose_name_plural = "Empresas"

    def __str__(self):
        return self.nome
    
class Pessoa (models.Model):
    nome = models.CharField(max_length=100)
    CPF =  models.CharField(max_length=200, null=True,blank=True)
    telefone = models.CharField(max_length=200,default='sem telefone')
    endereco = models.CharField(max_length=255)
    num = models.CharField(max_length=10)
    cep = models.CharField(max_length=20)
    bairro = models.CharField(max_length=100)
    cidade = models.CharField(max_length=100)
    UF = models.CharField(max_length=2)
    status = models.BooleanField(default=True)
    idEmpresa = models.ForeignKey(Empresa, on_delete=models.CASCADE)
    
    
    class Meta:
        verbose_name = "Pessoa"
        verbose_name_plural = "Pessoas"

    def __str__(self):
        return self.nome
    
class Usuario(models.Model):
    nome = models.CharField(max_length=100)
    email = models.EmailField(max_length=100)
    senha = models.CharField(max_length=100)
    status = models.BooleanField(default=True)
    idEmpresa = models.ForeignKey(Pessoa, on_delete=models.CASCADE,)
    
    class Meta:
        verbose_name = "Usuario"
        verbose_name_plural = "Usuarios"

    def __str__(self):
        return self.nome
    
    