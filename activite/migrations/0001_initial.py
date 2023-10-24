# Generated by Django 4.2.4 on 2023-10-09 11:46

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('cmlnGestion', '0031_delete_activite'),
    ]

    operations = [
        migrations.CreateModel(
            name='Activite',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('type', models.CharField(choices=[('Culte de célébration', 'Culte de célébration'), ('Enseignement', 'Enseignement'), ('Yada', 'Yada'), ('Conférence', 'Conférence'), ('Séminaire', 'Séminaire'), ('Veillée de prière', 'Veillée de prière'), ('Autres', 'Autres')], default='Culte de célébration', max_length=120, verbose_name="Type d'activité")),
                ('date', models.DateField(verbose_name='Date')),
                ('heure_debut', models.TimeField(verbose_name='Heure de début')),
                ('heure_fin', models.TimeField(verbose_name='heure de fin')),
                ('theme', models.CharField(blank=True, max_length=120, null=True, verbose_name='Thème')),
                ('moderateur', models.CharField(blank=True, max_length=120, null=True, verbose_name='Moderateur / Conducteur')),
                ('intervenant', models.CharField(blank=True, max_length=120, null=True, verbose_name='Orateur / Intervenant')),
                ('ref_biblique', models.CharField(blank=True, max_length=120, null=True, verbose_name='Références bibliques')),
                ('resume', models.TextField(verbose_name='Resumé')),
                ('nbre_hommes', models.IntegerField()),
                ('nbre_femmes', models.IntegerField()),
                ('nbre_enfants', models.IntegerField()),
                ('nouveaux_venus', models.IntegerField(blank=True, null=True)),
                ('offrande', models.FloatField(verbose_name='Offrandes')),
                ('dime', models.FloatField(verbose_name='Dîmes')),
                ('premices', models.FloatField(verbose_name='Premices')),
                ('action_grace', models.FloatField(verbose_name='Action de grâce')),
                ('achat_parcelle', models.FloatField(verbose_name='Achat parcelle')),
                ('construction', models.FloatField(verbose_name='Construction')),
                ('autres', models.FloatField(verbose_name='Autres')),
                ('extension', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='cmlnGestion.extension', verbose_name='Extension')),
            ],
            options={
                'unique_together': {('extension', 'type', 'date')},
            },
        ),
    ]
