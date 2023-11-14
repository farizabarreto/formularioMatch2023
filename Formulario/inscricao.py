from django import forms
from .models import Inscrite


class formInscricao(forms.ModelForm):

    #Define nomes legíveis para os campos do ModelForm
    nome = forms.CharField(max_length=60, label="Nome completo")
    idade = forms.IntegerField(label="Idade")
    endereco = forms.CharField(max_length=80, label="Endereço")
    numero = forms.CharField(max_length=5, label="Número")
    complemento = forms.CharField(max_length=30, label="Complemento")
    bairro = forms.CharField(max_length=40, label="Bairro")
    cidade = forms.CharField(max_length=30, label="Cidade")
    uf = forms.CharField(max_length=2, label="UF")
    ciencia = forms.BooleanField(label="Tem ciência que o evento ocorre dia 22 de novembro às 19h?")

    class Meta:
        model = Inscrite
        fields = '__all__'
