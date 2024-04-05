from django.db import models
import os
from django.db.models.signals import post_save
from django.dispatch import receiver


# Create your models here.

def file_path(instance, filename):
        
        return f'requests/{instance.cpf}/{filename}'

class Solicitacao(models.Model):
    name = models.CharField(verbose_name='Nome',
                            max_length=180, blank=False, null=False)
    cpf = models.CharField(
        verbose_name="CPF", max_length=11, blank=False, null=False)
    coren_number = models.CharField(
        verbose_name="Número de Inscrição", max_length=11, blank=False, null=False)
    email = models.EmailField(max_length=180, blank=False, null=False)
    cel = models.CharField(verbose_name="Celular",
                           max_length=11, blank=False, null=False)
    workplace = models.CharField(
        verbose_name="Local de Trabalho", max_length=180, blank=False, null=False)
    city = models.CharField(verbose_name="Município",
                            max_length=50, blank=False, null=False)

    file = models.FileField(
        verbose_name="Escolha o arquivo", upload_to=(file_path))
    data = models.DateTimeField(auto_now_add=True, blank=False, null=False)



