# Generated by Django 3.2.8 on 2021-10-12 17:27

from django.db import migrations, models
import livros.models


class Migration(migrations.Migration):

    dependencies = [
        ('livros', '0002_alter_livros_id_livro'),
    ]

    operations = [
        migrations.AddField(
            model_name='livros',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to=livros.models.upload_image_livros),
        ),
    ]
