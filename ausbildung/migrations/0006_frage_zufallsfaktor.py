# Generated by Django 2.2.6 on 2019-11-27 16:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ausbildung', '0005_auto_20191124_1729'),
    ]

    operations = [
        migrations.AddField(
            model_name='frage',
            name='Zufallsfaktor',
            field=models.IntegerField(default=5, verbose_name='Fator de aleatoriedade'),
        ),
    ]
