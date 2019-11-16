# Generated by Django 2.2.6 on 2019-10-29 21:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Wortschatz', '0005_auto_20191026_1427'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='land',
            options={'ordering': ['name', 'slug', 'created', 'modified'], 'verbose_name': 'País', 'verbose_name_plural': 'Países'},
        ),
        migrations.AlterModelOptions(
            name='sprache',
            options={'ordering': ['name', 'slug', 'created', 'modified'], 'verbose_name': 'Idioma', 'verbose_name_plural': 'Idiomas'},
        ),
        migrations.RemoveField(
            model_name='sprache',
            name='abkurtzung',
        ),
        migrations.AddField(
            model_name='sprache',
            name='created',
            field=models.DateTimeField(auto_now_add=True, null=True, verbose_name='Criado em'),
        ),
        migrations.AddField(
            model_name='sprache',
            name='modified',
            field=models.DateTimeField(auto_now=True, null=True, verbose_name='Modificado em'),
        ),
        migrations.AddField(
            model_name='sprache',
            name='slug',
            field=models.SlugField(default=models.CharField(max_length=100, unique=True, verbose_name='Nome'), max_length=7, unique=True, verbose_name='Abreviatura'),
        ),
    ]
