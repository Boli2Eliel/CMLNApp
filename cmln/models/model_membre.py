from enum import Enum

from django.core.validators import RegexValidator
from django_countries.fields import CountryField
from django.db import models

class SexeChoice(Enum):
    F = "Féminin"
    M = "Masculin"

class OuiNonChoice(Enum):
    OUI = "OUI"
    NON = "NON"

class SituationChoice(Enum):
    NOUVEAU = "Nouvel arrivant"
    INTEGRATION = "En cours d'intégration - N1"

class Extension(models.Model):
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Date d'ajout", blank=True, null=True)
    updated_at = models.DateTimeField(auto_now=True, verbose_name="Date de mise à jour", blank=True, null=True)
    nom = models.CharField(max_length=100)
    description = models.CharField(max_length=200)
    ville = models.CharField(max_length=150)
    pays = CountryField(blank_label='(select country)')

    def __str__(self):
        return f"{self.nom}/{self.description}"

    def get_nom_description_str(self):
        return f"{self.nom} - {self.description}, {self.ville}"

class Membre(models.Model):
    created_at= models.DateTimeField(auto_now_add=True, blank=True, null=True)
    updated_at = models.DateTimeField(auto_now=True, blank=True, null=True)
    prenom = models.CharField( max_length=100, blank=True, null=True)
    nom = models.CharField( max_length=100, blank=True, null=True)
    sexe = models.CharField(max_length=20, blank=True, null=True, verbose_name="Sexe",
                            choices=[(tag.name, tag.value) for tag in SexeChoice])
    date_naissance = models.DateField(null=True, blank=True)
    date_arrivee = models.DateField(auto_now_add=True, verbose_name="Date d'arrivée à CMLN", blank=True, null=True)
    baptise = models.CharField(max_length=20, blank=True, null=True, verbose_name="Baptisé",
                            choices=[(tag.name, tag.value) for tag in OuiNonChoice])
    situation = models.CharField(max_length=100, blank=True, null=True, verbose_name="Situation actuelle",
                                 choices=[(tag.name, tag.value) for tag in SituationChoice])
    email = models.CharField(max_length=150, blank=True, null=True)
    adresse = models.CharField(max_length=100, blank=True, null=True)
    ville = models.CharField(max_length=100, blank=True, null=True)
    extension = models.ForeignKey(Extension, on_delete=models.CASCADE, null=True, blank=True)
    telephone_regex = RegexValidator(
        regex="[0-9]{9}", message="Veuillez entrer un numéro de téléphone valide"
    )
    telephone = models.CharField(validators=[telephone_regex], max_length=100, blank=True, null=True)
    date_inscription = models.DateField(auto_now_add=True, verbose_name="Date d'inscription", blank=True, null=True)
    commentaire = models.CharField(max_length=500, blank=True)

    def __str__(self):
        return f"{self.prenom} {self.nom}"

    def get_adresse_complete_str(self):
        return f"{self.adresse} , {self.ville}"

    def get_extension_str(self):
        return f"{self.extension.description}"

    def is_from_nouveau(self):
        return self.situation == SituationChoice.NOUVEAU.name

    def is_from_integration(self):
        return self.situation == SituationChoice.INTEGRATION.name
