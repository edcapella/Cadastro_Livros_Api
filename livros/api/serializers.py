from rest_framework import serializers

from livros import models


class LivrosSerializers(serializers.ModelSerializer):
    class Meta:
        model = models.Livros   # class meta vai recer os modelos de livros
        fields = '__all__'  # importa todos as fields de models
