from django.core.validators import RegexValidator
from django_countries.fields import CountryField
from django.db import models
from enum import Enum
from cmln.models.model_membre import Extension


class SexeChoice(Enum):
    F = "Féminin"
    M = "Masculin"

class OuiNonChoice(Enum):
    OUI = "OUI"
    NON = "NON"

class SituationChoice(Enum):
    MEMBRE = "Membre"
    INTEGRATION = "En cours d'intégration - N1"
    STAGIAIRE = "STAGIAIRE"
    AERD = "Aerd confirmé"
    FORMATION = "En formation N+"

class MinistereChoice(Enum):
    PUISSANCE = "Puissance"
    LOUANGE = "Louange"
    JEUNESSE = "CMLN Etoile"
    ENFANTS = "CMLN Junior"
    AMENAGEMENT = "Aménagement"

class Departement(models.Model):
    nom = models.CharField( max_length=100, blank=True, null=True)
    ministere = models.CharField( max_length=100, blank=True, null=True, verbose_name="Ministère", choices=[(tag.name, tag.value) for tag in MinistereChoice])

class Aerd(models.Model):
    created_at= models.DateTimeField(auto_now_add=True, blank=True, null=True)
    updated_at = models.DateTimeField(auto_now=True, blank=True, null=True)
    prenom = models.CharField( max_length=100, blank=True, null=True)
    nom = models.CharField( max_length=100, blank=True, null=True)
    sexe = models.CharField(max_length=20, blank=True, null=True, verbose_name="Sexe",
                            choices=[(tag.name, tag.value) for tag in SexeChoice])
    situation =  models.CharField( max_length=100, blank=True, null=True, verbose_name="Situation actuelle", choices=[(tag.name, tag.value) for tag in SituationChoice])
    date_naissance = models.DateField(verbose_name="Date de naissance", null=True, blank=True)
    date_bapteme = models.DateField(verbose_name="Date de bapteme(par immersion)", null=True, blank=True)
    date_arrivee = models.DateField(auto_now_add=True, verbose_name="Date d'arrivée à CMLN", blank=True, null=True)
    departement = models.ForeignKey(Departement, on_delete=models.PROTECT, null=True, blank=True)

    email = models.CharField(max_length=150, blank=True, null=True)
    adresse = models.CharField(max_length=100, blank=True, null=True)
    telephone_regex = RegexValidator(
        regex="[0-9]{9}", message="Veuillez entrer un numéro de téléphone valide"
    )
    telephone = models.CharField(validators=[telephone_regex], max_length=100, blank=True, null=True)
    ville = models.CharField(max_length=100, blank=True, null=True)
    extension = models.ForeignKey(Extension, on_delete=models.CASCADE, null=True, blank=True)
    inactif = models.BooleanField(default=False, verbose_name="Desactivé (Ne cocher que si vous ne souhaitez plus gérer ce AERD dans l'application)")
    commentaire = models.TextField(max_length=500)
    def __str__(self):
        return f"{self.prenom} {self.nom}"

    def get_adresse_complete_str(self):
        return f"{self.adresse} , {self.ville}"

    def get_extension_str(self):
        return f"{self.extension.description}"

    def is_from_stagiaire(self):
        return self.situation == SituationChoice.STAGIAIRE.name

    def is_from_aerd(self):
        return self.situation == SituationChoice.AERD.name

    def is_from_formation(self):
        return self.situation == SituationChoice.FORMATION.name