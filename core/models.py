import uuid
from email.policy import default
from django.db import models
from stdimage.models import StdImageField
from PIL import Image
Resampling = getattr(Image, 'Resampling', Image.LANCZOS)


def get_file_path(_instamce, filename):
    ext = filename.split('.')[-1]
    filename = f'{uuid.uuid4()}.{ext}'
    return filename

class Base(models.Model):
    criados = models.DateField('Criação', auto_now_add=True)
    modificado = models.DateField('Atualização', auto_now=True)
    ativo = models.BooleanField('Ativo: ', default=True)

    class Meta:
        abstract = True


class Feature(Base):                    #TESTADO
    ICONE_CHOICES = (
        ('lni-rocket', 'Foguete'),
        ('lni-laptop-phone', 'Notebook'),
        ('lni-cog', 'Engranagem'),
        ('lni-leaf', 'Folha'),
        ('lni-layers', 'Design'),
    )
    feature = models.CharField('Nome', max_length=50)
    descricao = models.CharField('Descrição', max_length=200)
    icone = models.CharField('Icone', max_length=16, choices=ICONE_CHOICES)

    class Meta:
        verbose_name = 'Feature'
        verbose_name_plural = 'Features'

    def __str__(self):
        return self.feature

class Servico(Base):                    #TESTADO
    ICONE_CHOICES = (
        ('lni-cog', 'Engrenagem'),
        ('lni-stats-up', 'Gráfico'),
        ('lni-users', 'Usuários'),
        ('lni-layers', 'Desing'),
        ('lni-mobile', 'Mobile'),
        ('lni-rocket', 'Foguete'),
    )
    servico = models.CharField('Serviço', max_length=100)
    descricao = models.TextField('Descrição', max_length=200)
    icone = models.CharField('Icone', max_length=12, choices=ICONE_CHOICES)

    class Meta:
        verbose_name = 'Serviço'
        verbose_name_plural = 'Serviços'

    def __str__(self):
        return self.servico


class Cargo(Base):                  #TESTADO
    cargo = models.CharField('Cargo', max_length=100)

    class Meta:
        verbose_name = 'Cargo'
        verbose_name_plural = 'Cargos'

    def __str__(self):
        return self.cargo


class PrecoServico(Base):           #TESTADO
    ICONE_CHOICES = (
        ('lni-package', 'Caixa'),
        ('lni-drop', 'Drop'),
        ('lni-star', 'Estrela')
    )
    icone = models.CharField('Icone', max_length=12, choices=ICONE_CHOICES)
    valor = models.DecimalField('Preço', max_digits=10, decimal_places=2) #*
    titulo = models.CharField('Titulo', max_length=50)
    usuarios = models.IntegerField('Usuários', max_length=10)
    gbStorage = models.CharField('Armazenamento', max_length=100)
    tipeEmailSuport = models.CharField('Estatus de Email Suporte', max_length=25)
    lifetimeUpdates = models.BooleanField('LifetimesUpdates', default=True)

    class Meta:
        verbose_name = 'PreçoServiço'
        verbose_name_plural = 'PreçoServiços'

    def __str__(self):
        return self.titulo


class Funcionario(Base):              #TESTADO
    nome = models.CharField('Nome', max_length=100)
    cargo = models.ForeignKey('core.Cargo', verbose_name='Cergo', on_delete=models.CASCADE)
    bio = models.TextField('Bio', max_length=200)
    imagem = StdImageField('Imagem', upload_to=get_file_path, variations={'thumb': {'width':480, 'height':480, 'crop': True}})
    facebook = models.CharField('Facebook', max_length=100, default='#')
    x = models.CharField('X', max_length=100, default='#')
    instagram = models.CharField('Instagram', max_length=100, default='#')

    class Meta:
        verbose_name = 'Funcionario'
        verbose_name_plural = 'Equipe'

    def __str__(self):
        return self.nome
