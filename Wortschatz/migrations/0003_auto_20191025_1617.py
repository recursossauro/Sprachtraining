# Generated by Django 2.2.6 on 2019-10-25 19:17

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Wortschatz', '0002_auto_20191025_1613'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='land',
            options={'ordering': ['name', 'abkurtzung'], 'verbose_name': 'País', 'verbose_name_plural': 'Países'},
        ),
    ]