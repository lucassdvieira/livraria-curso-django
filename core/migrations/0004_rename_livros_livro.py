# Generated by Django 4.0.5 on 2022-06-19 00:03

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0003_alter_autor_options_livros'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Livros',
            new_name='Livro',
        ),
    ]
