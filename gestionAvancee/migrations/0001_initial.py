# Generated by Django 4.2.4 on 2023-10-24 13:38

import django.core.validators
from django.db import migrations, models
import django_countries.fields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Extension',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True, null=True, verbose_name="Date d'ajout")),
                ('updated_at', models.DateTimeField(auto_now=True, null=True, verbose_name='Date de mise à jour')),
                ('nom', models.CharField(max_length=100)),
                ('description', models.CharField(max_length=200)),
                ('telephone_1', models.CharField(blank=True, max_length=100, null=True, validators=[django.core.validators.RegexValidator(message='Veuillez entrer un numéro de téléphone valide', regex='[0-9]{9}')], verbose_name='Standard')),
                ('adresse', models.CharField(blank=True, max_length=200, null=True, verbose_name='Adresse')),
                ('ville', models.CharField(blank=True, max_length=150, null=True, verbose_name='Ville')),
                ('pays', django_countries.fields.CountryField(blank=True, max_length=2, null=True, verbose_name='Pays')),
            ],
        ),
    ]
