from django.db import models

# Create your models here.
class Pessoa(models.Model):
    id_pessoa = models.AutoField(primary_key=True)
    nome = models.TextField(max_length=255)
    temp = models.IntegerField()
    peso = models.IntegerField()
    pressao = models.TextField(max_length=10)