from rest_framework import serializers
from .models import *

class AreasSerializer(serializers.ModelSerializer):
    class Meta:
        many = True
        model = Areas
        fields = '__all__'

class UsuariosSerializer(serializers.ModelSerializer):
    class Meta:
        many = True
        model = Usuarios
        fields = '__all__'
        
    
class MotivosSerializer(serializers.ModelSerializer):
    class Meta:
        many = True
        model = Motivos
        fields = '__all__'
        

class OcorrenciasSerializer(serializers.ModelSerializer):
    motivoFK = MotivosSerializer(read_only=True)
    UsuarioFK = UsuariosSerializer(read_only=True)
    class Meta:
        many = True
        model = Ocorrencias
        fields = '__all__'
        
