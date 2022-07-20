from django.contrib import admin
from django.urls import path

from .views import *

urlpatterns = [
    path("usuarios/", UsuariosAPIView.as_view(), name="usuarios"),
    path("usuarios/<int:pk>/", UsuariosAPIView.as_view(), name="usuariosParametros"),
    path("motivos/", MotivosAPIView.as_view(), name="motivos"),
    path("motivos/<int:pk>/", MotivosAPIView.as_view(), name="motivosParametros"),
    path("ocorrencias/", OcorrenciasAPIView.as_view(), name="ocorrencias"),
    path("ocorrencias/<int:pk>/", OcorrenciasAPIView.as_view(), name="ocorrenciasParametros"),
    path("areas/", AreasAPIView.as_view(), name="areas"),
    path("areas/<int:pk>/", AreasAPIView.as_view(), name="areasParametros"),
]