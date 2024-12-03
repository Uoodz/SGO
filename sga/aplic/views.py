from django.contrib import messages
from django.shortcuts import render, redirect
from django.views.generic import TemplateView
from .forms import SolicitarAjudaForm
from .models import SolicitacaoAjuda


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