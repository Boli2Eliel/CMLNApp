# Generated by Django 4.2 on 2023-05-11 16:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cmlnGestion', '0011_alter_aerd_niveau_formation_alter_aerd_position_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='aerd',
            name='position',
            field=models.CharField(blank=True, choices=[('LEADER_PRINCIPAL', 'Leader Principal'), ('PASTEUR', 'Pasteur titulaire'), ('PASTEUR_ADJOINT', 'Pasteur Stagiaire'), ('ASSISTANT_PASTEUR', 'Assistant Pasteur'), ('ANCIEN', 'Ancien(ne)'), ('DIACRE', 'Diacre/ Diaconnesse'), ('OUVRIER', 'Ouvrier')], max_length=100, null=True, verbose_name='Position actuelle'),
        ),
    ]
