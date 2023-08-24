# Generated by Django 4.2.1 on 2023-05-26 13:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cmlnGestion', '0016_extension_adresse_extension_telephone_1_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='aerd',
            name='position',
            field=models.CharField(choices=[('Leader Principal', 'Leader Principal'), ('Pasteur titulaire', 'Pasteur titulaire'), ('Pasteur Stagiaire', 'Pasteur Stagiaire'), ('Assistant Pasteur', 'Assistant Pasteur'), ('Ancien(ne)', 'Ancien(ne)'), ('Diacre/ Diaconnesse', 'Diacre/ Diaconnesse'), ('Ouvrier', 'Ouvrier')], default='Ouvrier', max_length=100, verbose_name='Position actuelle'),
        ),
        migrations.AlterField(
            model_name='aerd',
            name='situation',
            field=models.CharField(choices=[('-', '-'), ('Stagiaire', 'Stagiaire'), ('Aerd confirmé', 'Aerd confirmé'), ('En formation N+', 'En formation N+')], default='-', max_length=100, verbose_name='Situation actuelle'),
        ),
    ]