from django.contrib import admin
from .models import *

class detAreas(admin.ModelAdmin):
    list_display = ('id','nome')
    list_display_links = ('id',)
    search_fields = ('nome',)
    list_per_page = 10

class detUsuarios(admin.ModelAdmin):
    list_display = ('id','nome', 'edv', 'area', 'senha', 'admin')
    list_display_links = ('id',)
    search_fields = ('nome',)
    list_per_page = 10

class detMotivos(admin.ModelAdmin):
    list_display = ('id','nome')
    list_display_links = ('id',)
    search_fields = ('nome',)
    list_per_page = 10

class detOcorrencias(admin.ModelAdmin):
    list_display = ('id','motivoFK', 'UsuarioFK', 'dtInicio', 'dtFinal', 'hrInicio', 'hrFinal', 'descricao', 'arquivo')
    list_display_links = ('id',)
    search_fields = ('motivoFK',)
    list_per_page = 10

admin.site.register(Areas, detAreas)
admin.site.register(Usuarios, detUsuarios)
admin.site.register(Motivos, detMotivos)
admin.site.register(Ocorrencias, detOcorrencias)
