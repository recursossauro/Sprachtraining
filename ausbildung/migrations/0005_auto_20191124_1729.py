# Generated by Django 2.2.6 on 2019-11-24 20:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ausbildung', '0004_auto_20191124_1729'),
    ]

    operations = [
        migrations.AlterField(
            model_name='antwort',
            name='Fragetext',
            field=models.CharField(max_length=1000, verbose_name='Texto da Resposta'),
        ),
    ]
