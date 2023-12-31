# Generated by Django 4.2.1 on 2023-05-25 07:18

import django.core.validators
from django.db import migrations, models
import django_countries.fields


class Migration(migrations.Migration):

    dependencies = [
        ('cmlnGestion', '0015_activite_nouveaux_venus'),
    ]

    operations = [
        migrations.AddField(
            model_name='extension',
            name='adresse',
            field=models.CharField(blank=True, max_length=200, null=True, verbose_name='Adresse'),
        ),
        migrations.AddField(
            model_name='extension',
            name='telephone_1',
            field=models.CharField(blank=True, max_length=100, null=True, validators=[django.core.validators.RegexValidator(message='Veuillez entrer un numéro de téléphone valide', regex='[0-9]{9}')], verbose_name='Standard'),
        ),
        migrations.AlterField(
            model_name='extension',
            name='pays',
            field=django_countries.fields.CountryField(blank=True, max_length=2, null=True, verbose_name='Pays'),
        ),
        migrations.AlterField(
            model_name='extension',
            name='ville',
            field=models.CharField(blank=True, max_length=150, null=True, verbose_name='Ville'),
        ),
    ]
