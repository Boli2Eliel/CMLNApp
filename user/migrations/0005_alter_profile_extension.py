# Generated by Django 4.2.4 on 2023-10-24 13:38

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('gestionAvancee', '0001_initial'),
        ('user', '0004_remove_profile_staff'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='extension',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='gestionAvancee.extension', verbose_name='Extension'),
        ),
    ]
