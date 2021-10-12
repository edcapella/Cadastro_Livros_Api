from django.db import models

from uuid import uuid4

# Create your models here.


'''função para fazer o upload das imagens. a instancia do objeto vai receber "instance" + o id_livro para não haver
 problemas de ter dois nomes iguals, mais o nome do arquivo que vai receber o filename'''
def upload_image_livros(instance, filename):
    return f'{instance.id_livro}-{filename}'

class Livros(models.Model):
    id_livro = models.UUIDField(primary_key=True, default=uuid4, editable=False)    # chave primaria com uuid
    titulo = models.CharField(max_length=255)
    autor = models.CharField(max_length=255)
    lancamento = models.IntegerField()
    estado_livro = models.CharField(max_length=50)
    paginas = models.IntegerField()
    editora = models.CharField(max_length=255)
    criado_em = models.DateField(auto_now_add=True)     # auto adicionar a data que for criado dentro do campo.
    image = models.ImageField(upload_to=upload_image_livros, blank=True, null=True) #blank vai receber true se nao quiser colocar imagens