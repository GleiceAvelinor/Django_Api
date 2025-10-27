from django.urls import path, include
from rest_framework.routers import DefaultRouter

from .views import EmpresaViewSet, PessoaViewSet, UsuarioViewSet 

router = DefaultRouter()

router.register(r'empresas', EmpresaViewSet)
router.register(r'pessoas', PessoaViewSet)
router.register(r'usuarios', UsuarioViewSet)

urlpatterns = [
    path('', include(router.urls)),
    
]

