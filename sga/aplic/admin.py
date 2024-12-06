from django.contrib import admin

from .models import AssistenteSocial, ONG, Diretor, Assistido, Dependente, Atendimento, Voluntario, Visita, Pergunta, \
    Questionario, RespostaQuestionario, SolicitacaoAjuda, VisitaSite


# Register your models here.
@admin.register(AssistenteSocial)
class AssistenteSocialAdmin(admin.ModelAdmin):
    list_display = ('nome', 'contato', 'email', 'cpf')

@admin.register(ONG)
class ONGAdmin(admin.ModelAdmin):
    list_display = ('nome', 'endereco', 'contato', 'email', 'cnpj')

@admin.register(Diretor)
class DiretorAdmin(admin.ModelAdmin):
    list_display = ('nome', 'email', 'cpf', 'estadoCivil', 'ong')

@admin.register(Assistido)
class AssistidoAdmin(admin.ModelAdmin):
    list_display = ('nome', 'dataNascimento', 'email', 'contato', 'profissao', 'salario', 'estadoCivil', 'cpf')

@admin.register(Dependente)
class DependenteAdmin(admin.ModelAdmin):
    list_display = ('nome', 'dataNascimento', 'profissao', 'assistido')

@admin.register(Atendimento)
class AtendimentoAdmin(admin.ModelAdmin):
    list_display = ('data', 'assistente_social', 'assistido')

@admin.register(Voluntario)
class VoluntarioAdmin(admin.ModelAdmin):
    list_display = ('nome', 'contato', 'profissao', 'cpf', 'estadoCivil')

@admin.register(Visita)
class VisitaAdmin(admin.ModelAdmin):
    list_display = ('data', 'assistido', 'voluntario')

@admin.register(Pergunta)
class PerguntaAdmin(admin.ModelAdmin):
    list_display = ('pergunta',)

@admin.register(Questionario)
class QuestionarioAdmin(admin.ModelAdmin):
    list_display = ('titulo',)

@admin.register(RespostaQuestionario)
class RespostaQuestionarioAdmin(admin.ModelAdmin):
    list_display = ('informacoes', 'questionario', 'visita')

@admin.register(SolicitacaoAjuda)
class SolicitacaoAjudaAdmin(admin.ModelAdmin):
    list_display = ('nome', 'contato', 'tipo_ajuda', 'data_descricao_formatada')

@admin.register(VisitaSite)
class VisitaSiteAdmin(admin.ModelAdmin):
    list_display = ('ip_address', 'user_agent', 'data_hora')
    list_filter = ('data_hora',)