from django.shortcuts import render
from .models import *
from .serializer import *
from rest_framework.views import APIView
from rest_framework.response import Response
from django.http import HttpResponseRedirect
from rest_framework.permissions import IsAuthenticated

class AreasAPIView(APIView):
    
    def get(self, request, pk=""):
        areas = Areas.objects.all()
        serializer = AreasSerializer(areas, many=True)
        return Response(serializer.data)
    
    def post(self, request):
        serializer = AreasSerializer(data=request.data, many=True)
        serializer.is_valid(raise_exception=True)
        serializer.save()        
        return Response({"msg": "Area inserida com sucesso..."})

    def put(self, request, pk=''):
        usuarios = Areas.objects.get(id=pk)
        serializer = AreasSerializer(areas, data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)

    def delete(self, request, pk=''):        
        areas = Areas.objects.get(id=pk)       
        areas.delete()
        return Response({"msg": "Area deletada..."})

class UsuariosAPIView(APIView):
    def get(self, request, pk=""):
        usuarios = Usuarios.objects.all()
        serializer = UsuariosSerializer(usuarios, many=True)
        return Response(serializer.data)
    
    def post(self, request):
        serializer = UsuariosSerializer(data=request.data, many=True)
        serializer.is_valid(raise_exception=True)
        serializer.save()        
        return Response({"msg": "Usuário inserido com sucesso..."})

    def put(self, request, pk=''):
        usuarios = Usuarios.objects.get(id=pk)
        serializer = UsuariosSerializer(usuarios, data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)

    def delete(self, request, pk=''):        
        usuarios = Usuarios.objects.get(id=pk)       
        usuarios.delete()
        return Response({"msg": "Usuário deletado..."})

class MotivosAPIView(APIView):
    def get(self, request, pk=""):
        usuarios = Motivos.objects.all()
        serializer = MotivosSerializer(usuarios, many=True)
        return Response(serializer.data)
    
    def post(self, request):
        serializer = MotivosSerializer(data=request.data, many=True)
        serializer.is_valid(raise_exception=True)
        serializer.save()        
        return Response({"msg": "Motivo inserido com sucesso..."})

    def put(self, request, pk=''):
        usuarios = Motivos.objects.get(id=pk)
        serializer = MotivosSerializer(usuarios, data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)

    def delete(self, request, pk=''):        
        usuarios = Motivos.objects.get(id=pk)       
        usuarios.delete()
        return Response({"msg": "Motivo deletado..."})
    
class OcorrenciasAPIView(APIView):
    def get(self, request, pk=""):
        usuarios = Ocorrencias.objects.all()
        serializer = OcorrenciasSerializer(usuarios, many=True)
        return Response(serializer.data)
    
    def post(self, request):
        serializer = OcorrenciasSerializer(data=request.data, many=True)
        serializer.is_valid(raise_exception=True)
        serializer.save()        
        return Response({"msg": "Ocorrencia inserida com sucesso..."})

    def put(self, request, pk=''):
        usuarios = Ocorrencias.objects.get(id=pk)
        serializer = OcorrenciasSerializer(usuarios, data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)

    def delete(self, request, pk=''):        
        usuarios = Ocorrencias.objects.get(id=pk)       
        usuarios.delete()
        return Response({"msg": "Motivo deletado..."})