# Generated by Django 2.2.6 on 2019-10-25 19:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Wortschatz', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='land',
            name='created',
            field=models.DateTimeField(auto_now_add=True, null=True, verbose_name='Criado em'),
        ),
        migrations.AddField(
            model_name='land',
            name='modified',
            field=models.DateTimeField(auto_now=True, null=True, verbose_name='Modificado em'),
        ),
    ]
