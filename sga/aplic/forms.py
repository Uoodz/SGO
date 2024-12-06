from django import forms
from .models import SolicitacaoAjuda, VisitaSite

class SolicitarAjudaForm(forms.ModelForm):
    class Meta:
        model = SolicitacaoAjuda
        fields = ['nome', 'contato', 'tipo_ajuda', 'descricao']
        widgets = {
            'nome': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Digite seu nome'}),
            'contato': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Digite seu telefone ou email'}),
            'tipo_ajuda': forms.Select(attrs={'class': 'form-select'}),
            'descricao': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Descreva sua necessidade'}),
        }

class VisitaForm(forms.ModelForm):
    class Meta:
        model = VisitaSite
        fields = ['ip_address', 'user_agent']