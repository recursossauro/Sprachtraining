# Generated by Django 2.2.6 on 2019-11-24 20:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ausbildung', '0002_auto_20191121_1205'),
    ]

    operations = [
        migrations.AddField(
            model_name='antwort',
            name='Fragetext',
            field=models.CharField(default='None', max_length=1000, verbose_name='Texto da Resposta'),
        ),
    ]
