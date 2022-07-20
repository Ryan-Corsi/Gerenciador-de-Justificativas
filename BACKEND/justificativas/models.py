from django.db import models

class Areas(models.Model):
    
    nome =  models.CharField(max_length=55)

    def __str__(self):
        return self.nome

class Usuarios(models.Model):
    nome = models.CharField(max_length=55)
    edv = models.IntegerField()
    area = models.ForeignKey(Areas, related_name="areas", on_delete=models.CASCADE) 
    senha = models.CharField(max_length=20)
    admin = models.BooleanField()
    primeiroAcesso = models.BooleanField(default=True) 
    
    def __str__(self):
        return self.nome

class Motivos(models.Model):
    nome = models.CharField(max_length=55)
    
    def __str__(self):
        return self.nome
    
class Ocorrencias(models.Model):
    motivoFK = models.ForeignKey(Motivos, related_name="motivo", on_delete=models.CASCADE)
    UsuarioFK = models.ForeignKey(Usuarios, related_name="usuario", on_delete=models.CASCADE)
    dtInicio = models.DateField()
    dtFinal = models.DateField()
    hrInicio = models.TimeField(blank=True)
    hrFinal = models.TimeField(blank=True)
    descricao = models.TextField(blank=True)
    arquivo = models.FileField(blank=True)
    
    def __str__(self):
        return self.descricao
    
