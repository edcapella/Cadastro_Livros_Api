from rest_framework import viewsets
from livros import  models

# importando o serializer da pasta api
from livros.api import serializers


class LivrosViewSets(viewsets.ModelViewSet):
    serializer_class = serializers.LivrosSerializers
    queryset = models.Livros.objects.all()