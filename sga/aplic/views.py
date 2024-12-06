from django.contrib import messages
from django.shortcuts import render, redirect
from django.views.generic import TemplateView
from .forms import SolicitarAjudaForm
from .models import SolicitacaoAjuda, VisitaSite
#t

# Create your views here.
def solicitar_ajuda(request):
    if request.method == 'POST':
        nome = request.POST.get('nome')
        contato = request.POST.get('contato')
        tipo_ajuda = request.POST.get('tipo_ajuda')
        descricao = request.POST.get('descricao')
        SolicitacaoAjuda.objects.create(
            nome=nome,
            contato=contato,
            tipo_ajuda=tipo_ajuda,
            descricao=descricao
        )
        messages.success(request, 'Solicitação enviada com sucesso!')
        return redirect('solicitar_ajuda')
    return render(request, 'ajuda.html')

def registrar_visita(request):
    ip_address = get_client_ip(request)
    user_agent = request.META.get('HTTP_USER_AGENT', '')

    VisitaSite.objects.create(ip_address=ip_address, user_agent=user_agent)
    print(f"Visita registrada: IP={ip_address}, User Agent={user_agent}")

def get_client_ip(request):
    x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
    if x_forwarded_for:
        ip = x_forwarded_for.split(',')[0]
    else:
        ip = request.META.get('REMOTE_ADDR')
    print(f"IP do visitante: {ip}")
    return ip

def minha_view(request):
    registrar_visita(request)
    return render(request, 'minha_pagina.html')

def lista_visitas(request):
    visitas = VisitaSite.objects.all().order_by('-data_hora')
    print(visitas)
    return render(request, 'visitas.html', {'visitas': visitas})

class IndexView(TemplateView):
    template_name = 'index.html'

    def get_context_data(self, **kwargs):
        context = super(IndexView, self).get_context_data(**kwargs)
        return context

class TesteView(TemplateView):
    template_name = 'teste.html'

    def get_context_data(self, **kwargs):
        context = super(TesteView, self).get_context_data(**kwargs)
        return context

class SobreView(TemplateView):
    template_name = 'sobre.html'

    def get_context_data(self, **kwargs):
        context = super(SobreView, self).get_context_data(**kwargs)
        return context

class AjudaView(TemplateView):
    template_name = 'ajuda.html'

    def get_context_data(self, **kwargs):
        context = super(AjudaView, self).get_context_data(**kwargs)
        return context