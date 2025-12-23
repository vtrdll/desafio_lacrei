from django.db import models


class Profissional(models.Model):
    nome = models.CharField(max_length=200, blank=False, null=False)
    profissao = models.CharField(max_length=50, blank=False, null=False)
    endereco = models.CharField(max_length=200, blank=False, null=False)
    contato = models.EmailField(max_length=50, blank=False, null=False)

    def __str__(self):
        return f"Nome {self.nome} - Profissão {self.profissao}"


class Consulta(models.Model):
    profissional = models.ForeignKey(Profissional, on_delete=models.CASCADE)
    data = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Profissional{self.profissional} data da consulta {self.data}"
