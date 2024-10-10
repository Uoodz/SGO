import uuid
from django.db import models
from stdimage.models import StdImageField
from django.utils.translation import gettext_lazy as _

def get_file_path(_instance, filename):
    ext = filename.split('.')[-1]
    filename = f'{uuid.uuid4()}.{ext}'
    return filename

# Create your models here.
class Pessoa(models.Model):
    nome = models.CharField(('Nome'), max_length=100)
    #foto = StdImageField(('Foto'), null=True, blank=True, upload_to=get_file_path, variations={'thumb': {'width': 480, 'height': 480, 'crop': True}})
    facebook = models.CharField(('Facebook'), blank=True, max_length=200)
    linkedin = models.CharField(('LinkedIn'), blank=True, max_length=200)
    twitter = models.CharField(('Twitter'), blank=True, max_length=200)
    instagram = models.CharField(('Instagram'), blank=True, max_length=200)

    class Meta:
        abstract = True
        verbose_name = ('Pessoa')
        verbose_name_plural = ('Pessoas')
        ordering = ['id']

    def __str__(self):
        return self.nome

class AssistenteSocial(models.Model):
    nome = models.CharField(max_length=100, blank= False)
    #foto = StdImageField('Foto', null=True, blank=True, upload_to=get_file_path, variations={'thumb': {'width': 480, 'height': 480, 'crop': True}})
    contato = models.IntegerField()
    email = models.EmailField()
    dataNascimento = models.DateField()
    cpf = models.CharField(max_length=11, null= False, blank= False, unique= True)
    estadoCivil = models.CharField(max_length=50, blank= True)
    escolaridade = models.CharField(max_length=50)
    endereco = models.CharField(max_length=255)

    class Meta:
        verbose_name = ('Assistente Social')
        verbose_name_plural = ('Assistentes Sociais')

class ONG(models.Model):
    nome = models.CharField(max_length=100, blank= False)
    foto = StdImageField('Foto', null=True, blank=True, upload_to=get_file_path, variations={'thumb': {'width': 480, 'height': 480, 'crop': True}})
    endereco = models.CharField(max_length=255)
    contato = models.IntegerField()
    email = models.EmailField()
    cnpj = models.CharField(max_length=14, null= False, blank= False, unique= True)

    class Meta:
        verbose_name = ('ONG')
        verbose_name_plural = ('ONGs')

class Diretor(models.Model):
    nome = models.CharField(max_length=100, blank= False)
    #foto = StdImageField('Foto', null=True, blank=True, upload_to=get_file_path, variations={'thumb': {'width': 480, 'height': 480, 'crop': True}})
    contato = models.IntegerField()
    email = models.EmailField()
    dataNascimento = models.DateField()
    cpf = models.CharField(max_length=11, null= False, blank= False)
    estadoCivil = models.CharField(max_length=50, blank= True)
    escolaridade = models.CharField(max_length=50, blank= True)
    endereco = models.CharField(max_length=255)
    ong = models.OneToOneField(ONG, on_delete=models.CASCADE, null= False, blank= False)

    class Meta:
        verbose_name = ('Diretor')
        verbose_name_plural = ('Diretores')

class Assistido(models.Model):
    nome = models.CharField(max_length=100, blank= False)
    #foto = StdImageField('Foto', null=True, blank=True, upload_to=get_file_path, variations={'thumb': {'width': 480, 'height': 480, 'crop': True}})
    dataNascimento = models.DateField()
    email = models.EmailField()
    contato = models.IntegerField()
    profissao = models.CharField(max_length=100, blank= True)
    dependentes = models.CharField(max_length=255)
    salario = models.IntegerField()
    casaPropria = models.BooleanField()
    estadoCivil = models.CharField(max_length=50, blank= True)
    cpf = models.CharField(max_length=11, null= False, blank= False)
    escolaridade = models.CharField(max_length=50, blank= True)
    endereco = models.CharField(max_length=255)

    class Meta:
        verbose_name = ('Assistido')
        verbose_name_plural = ('Assistidos')

class Dependente(models.Model):
    nome = models.CharField(max_length=100, null= False, blank= False)
    #foto = StdImageField('Foto', null=True, blank=True, upload_to=get_file_path, variations={'thumb': {'width': 480, 'height': 480, 'crop': True}})
    dataNascimento = models.DateField()
    profissao = models.CharField(max_length=100, blank= True)
    assistido = models.ForeignKey(Assistido, on_delete=models.CASCADE, null= False, blank= False)

    class Meta:
        verbose_name = ('Dependente')
        verbose_name_plural = ('Dependentes')

class Atendimento(models.Model):
    data = models.DateField()
    assistente_social = models.ForeignKey(AssistenteSocial, on_delete=models.CASCADE, null= False, blank= False)
    assistido = models.ForeignKey(Assistido, on_delete=models.CASCADE, null= False, blank= False)

    class Meta:
        verbose_name = ('Atendimento')
        verbose_name_plural = ('Atendimentos')

class Voluntario(models.Model):
    nome = models.CharField(max_length=100, blank= False)
    #foto = StdImageField('Foto', null=True, blank=True, upload_to=get_file_path, variations={'thumb': {'width': 480, 'height': 480, 'crop': True}})
    contato = models.IntegerField()
    dataNascimento = models.DateField()
    profissao = models.CharField(max_length=100, blank= True)
    cpf = models.CharField(max_length=11, null= False, blank= False)
    estadoCivil = models.CharField(max_length=50, blank= True)
    escolaridade = models.CharField(max_length=50, blank= True)
    endereco = models.CharField(max_length=255)

    class Meta:
        verbose_name = ('Voluntário')
        verbose_name_plural = ('Voluntários')

class Visita(models.Model):
    data = models.DateField()
    assistido = models.ForeignKey(Assistido, on_delete=models.CASCADE, null= False, blank= False)
    voluntario = models.ForeignKey(Voluntario, on_delete=models.CASCADE, null= False, blank= False)

    class Meta:
        verbose_name = ('Visita')
        verbose_name_plural = ('Visitas')

class Pergunta(models.Model):
    pergunta = models.CharField(max_length=255, null= False, blank= False)

    class Meta:
        verbose_name = ('Pergunta')
        verbose_name_plural = ('Perguntas')

class Questionario(models.Model):
    titulo = models.CharField(max_length=255, null= False, blank= False)
    perguntas = models.ManyToManyField(Pergunta, blank= False)

    class Meta:
        verbose_name = ('Questionário')
        verbose_name_plural = ('Questionários')

class RespostaQuestionario(models.Model):
    informacoes = models.TextField()
    questionario = models.ForeignKey(Questionario, on_delete=models.CASCADE, null= False, blank= False)
    visita = models.ForeignKey(Visita, on_delete=models.CASCADE, null= False, blank= False)

    class Meta:
        verbose_name = ('Resposta')
        verbose_name_plural = ('Respostas')

