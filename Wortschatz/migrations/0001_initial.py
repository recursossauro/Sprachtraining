# Generated by Django 2.2.6 on 2019-10-21 00:54

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Land',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, unique=True, verbose_name='Nome')),
                ('abkurtzung', models.CharField(max_length=4, unique=True, verbose_name='Abreviatura')),
            ],
        ),
        migrations.CreateModel(
            name='Land_Sprache',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Amtssprache', models.BooleanField(default=True, verbose_name='Língua Oficial')),
                ('land', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Wortschatz.Land')),
            ],
        ),
        migrations.CreateModel(
            name='Sprache',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, unique=True, verbose_name='Nome')),
                ('abkurtzung', models.CharField(max_length=7, unique=True, verbose_name='Abreviatura')),
                ('lands', models.ManyToManyField(through='Wortschatz.Land_Sprache', to='Wortschatz.Land', verbose_name='Países')),
            ],
        ),
        migrations.AddField(
            model_name='land_sprache',
            name='sprache',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Wortschatz.Sprache'),
        ),
    ]
