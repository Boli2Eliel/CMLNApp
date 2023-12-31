# Generated by Django 4.2.4 on 2023-10-24 13:38

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0005_alter_profile_extension'),
        ('authentication', '0003_alter_account_extension'),
        ('activite', '0002_alter_activite_extension'),
        ('gestionAvancee', '0001_initial'),
        ('cmlnGestion', '0031_delete_activite'),
    ]

    operations = [
        migrations.AlterField(
            model_name='aerd',
            name='extension',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='gestionAvancee.extension', verbose_name='Extension'),
        ),
        migrations.AlterField(
            model_name='ancien',
            name='extension',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='gestionAvancee.extension', verbose_name='Extension'),
        ),
        migrations.AlterField(
            model_name='assistantpasteur',
            name='extension',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='gestionAvancee.extension', verbose_name='Extension'),
        ),
        migrations.AlterField(
            model_name='diacre',
            name='extension',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='gestionAvancee.extension', verbose_name='Extension'),
        ),
        migrations.AlterField(
            model_name='leader',
            name='extension',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='gestionAvancee.extension', verbose_name='Extension'),
        ),
        migrations.AlterField(
            model_name='membre',
            name='extension',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='gestionAvancee.extension'),
        ),
        migrations.AlterField(
            model_name='pasteur',
            name='extension',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='gestionAvancee.extension'),
        ),
        migrations.DeleteModel(
            name='Extension',
        ),
    ]
