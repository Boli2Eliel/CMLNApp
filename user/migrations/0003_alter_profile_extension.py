# Generated by Django 4.2.1 on 2023-05-24 17:31

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('cmlnGestion', '0015_activite_nouveaux_venus'),
        ('user', '0002_profile_extension'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='extension',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='cmlnGestion.extension', verbose_name='Extension'),
        ),
    ]
