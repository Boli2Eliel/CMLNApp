from django.core.validators import RegexValidator
from django_countries.fields import CountryField
from django.db import models
from enum import Enum
from cmln.models.model_membre import Extension, Membre


class SexeChoice(Enum):
    F = "Féminin"
    M = "Masculin"

class OuiNonChoice(Enum):
    OUI = "OUI"
    NON = "NON"

class SituationChoice(Enum):
    STAGIAIRE = "STAGIAIRE"
    AERD = "Aerd confirmé"
    FORMATION = "En formation N+"

class NiveauFormationChoice(Enum):
    N2 = "N2"
    N3 = "N3"
    N4 = "N4"
class PositionChoice(Enum):
    LEADER = "Leader Principal"
    PASTEUR= "Pasteur titulaire"
    PASTEUR_ADJOINT= "Pasteur Stagiaire"
    AP= "Assistant Pasteur"
    ANCIEN = "Ancien"
    DIACRE = "Diacre"

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
    membre = models.ForeignKey(Membre, on_delete=models.PROTECT, null=True, verbose_name="Ouvrier")
    position =  models.CharField( max_length=100, blank=True, null=True, verbose_name="Position actuelle", choices=[(tag.name, tag.value) for tag in PositionChoice])
    situation = models.CharField(max_length=100, blank=True, null=True, verbose_name="Situation actuelle",
                                 choices=[(tag.name, tag.value) for tag in SituationChoice])
    niveau_formation = models.CharField( max_length=100, blank=True, null=True, verbose_name="Niveau actuelle(si AERD confirmé ou en formation N+)", choices=[(tag.name, tag.value) for tag in NiveauFormationChoice])
    date_bapteme = models.DateField(verbose_name="Date de bapteme(par immersion)", null=True, blank=True)
    departement = models.ForeignKey(Departement, on_delete=models.PROTECT, null=True, blank=True)
    ville = models.CharField(max_length=100, blank=True, null=True)
    extension = models.ForeignKey(Extension, on_delete=models.CASCADE, null=True, blank=True)
    inactif = models.BooleanField(default=False, verbose_name="Desactivé (Ne cocher que si vous ne souhaitez plus gérer ce AERD dans l'application)")
    commentaire = models.TextField(max_length=500, null=True, blank=True)
    def __str__(self):
        return f"{self.membre.nom} , {self.membre.prenom}"

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