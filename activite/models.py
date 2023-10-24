from django_countries.fields import CountryField
from django.db import models
from enum import Enum

from cmlnGestion.models.model_aerd import ACTIVITE
from cmlnGestion.models.model_membre import Extension


class ActiviteChoice(Enum):
    LEADER_PRINCIPAL = "Leader Principal"
    PASTEUR = "Pasteur titulaire"
    PASTEUR_ADJOINT = "Pasteur Stagiaire"
    ASSISTANT_PASTEUR = "Assistant Pasteur"
    ANCIEN = "Ancien(ne)"
    DIACRE = "Diacre/ Diaconnesse"
    OUVRIER = "Ouvrier"


class Activite(models.Model):
    extension = models.ForeignKey(Extension, on_delete=models.CASCADE, null=True, blank=True, verbose_name="Extension")
    type = models.CharField(choices=ACTIVITE, default="Culte de célébration", max_length=120,
                            verbose_name="Type d'activité")
    date = models.DateField(verbose_name="Date")
    heure_debut = models.TimeField(verbose_name="Heure de début")
    heure_fin = models.TimeField(verbose_name="heure de fin")
    theme = models.CharField(max_length=120, null=True, blank=True, verbose_name="Thème")
    moderateur = models.CharField(max_length=120, null=True, blank=True, verbose_name="Moderateur / Conducteur")
    intervenant = models.CharField(max_length=120, null=True, blank=True, verbose_name="Orateur / Intervenant")
    ref_biblique = models.CharField(max_length=120, null=True, blank=True, verbose_name="Références bibliques")
    resume = models.TextField(verbose_name="Resumé")
    nbre_hommes = models.IntegerField()
    nbre_femmes = models.IntegerField()
    nbre_enfants = models.IntegerField()
    nouveaux_venus = models.IntegerField(null=True, blank=True)
    offrande = models.FloatField(verbose_name="Offrandes")
    dime = models.FloatField(verbose_name="Dîmes")
    premices = models.FloatField(verbose_name="Premices")
    action_grace = models.FloatField(verbose_name="Action de grâce")
    achat_parcelle = models.FloatField(verbose_name="Achat parcelle")
    construction = models.FloatField(verbose_name="Construction")
    autres = models.FloatField(verbose_name="Autres")

    class Meta:
        unique_together = [['extension', 'type', 'date']]

    def __str__(self):
        return f"{self.extension},{self.type}, {self.date}"

    def save(self, *args, **kwargs):
        print(self.date.isocalendar())
        super().save(*args, **kwargs)

    def total_participants(self):
        return (self.nbre_hommes) + (self.nbre_femmes) + (self.nbre_enfants)

    def total_offrandes(self):
        return (self.offrande) + (self.dime) + (self.premices) + (self.action_grace) + (self.achat_parcelle) + (
            self.construction) + (self.autres)
