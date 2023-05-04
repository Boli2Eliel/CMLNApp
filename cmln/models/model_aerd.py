from django.core.validators import RegexValidator
from django_countries.fields import CountryField
from django.db import models
from enum import Enum
from cmln.models.model_membre import *
from cmln.models.model_aerd import *


SEXE =(
    ('Féminin', 'Féminin'),
    ('Masculin', 'Masculin'),
    
)
class SexeChoice(Enum):
    F = "Féminin"
    M = "Masculin"

OUI_NON =(
    ('Oui', 'Oui'),
    ('Non', 'Non'),
)
class OuiNonChoice(Enum):
    OUI = "OUI"
    NON = "NON"

SITUATION =(
    ('-', '-'),
    ('Stagiaire', 'Stagiaire'),
    ('Aerd confirmé', 'Aerd confirmé'),
    ('En formation N+', 'En formation N+'),
)
class SituationChoice(Enum):
    STAGIAIRE = "STAGIAIRE"
    AERD = "Aerd confirmé"
    FORMATION_N = "En formation N+"

NIVEAU_FORMATION =(
    ('N2', 'N2'),
    ('N3', 'N3'),
    ('N4', 'N4'),
)
class NiveauFormationChoice(Enum):
    N2 = "N2"
    N3 = "N3"
    N4 = "N4"

POSITION =(
    ('Leader Principal', 'Leader Principal'),
    ('Pasteur titulaire', 'Pasteur titulaire'),
    ('Pasteur Stagiaire', 'Pasteur Stagiaire'),
    ('Assistant Pasteur', 'Assistant Pasteur'),
    ('Ancien(ne)', 'Ancien(ne)'),
    ('Diacre/ Diaconnesse', 'Diacre/ Diaconnesse'),
    ('Ouvrier', 'Ouvrier'),
)
class PositionChoice(Enum):
    LEADER = "Leader Principal"
    PASTEUR= "Pasteur titulaire"
    PASTEUR_ADJOINT= "Pasteur Stagiaire"
    AP= "Assistant Pasteur"
    ANCIEN = "Ancien(ne)"
    DIACRE = "Diacre/ Diaconnesse"

MINISTERE =(
    ('Puissance', 'Puissance'),
    ('Louange', 'Louange'),
    ('CMLN étoile', 'CMLN étoile'),
    ('CMLN Junior', 'CMLN Junior'),
    ('Amnagement', 'Amnagement'),
    ('Femmes de feu', 'Femmes de feu'),
    ("Hommes d'action", "Hommes d'action"),
    ("Secretariat général", "Secretariat général"),
)
class MinistereChoice(Enum):
    PUISSANCE = "Puissance"
    LOUANGE = "Louange"
    JCE = "CMLN Etoile"
    CMLN_JUNIOR = "CMLN Junior"
    AMENAGEMENT = "Aménagement"
    HA = "Hommes d'actions"
    FDF = "Femmes de Feu"


COMMUNAUTE = (
    ('Communauté CMLN/ Ensemble des églises CMLN','Communauté CMLN/ Ensemble des églises CMLN'),
    ('-', '-'),
)




class Aerd(models.Model):
    created_at= models.DateTimeField(auto_now_add=True, blank=True, null=True)
    updated_at = models.DateTimeField(auto_now=True, blank=True, null=True)
    membre = models.OneToOneField(Membre, on_delete=models.CASCADE, null=True, verbose_name="Ouvrier", unique=True)
    position =  models.CharField( max_length=100, blank=True, null=True, verbose_name="Position actuelle", choices=POSITION)
    situation = models.CharField(max_length=100, blank=True, null=True, verbose_name="Situation actuelle", choices=SITUATION)
    niveau_formation = models.CharField( max_length=100, blank=True, null=True, verbose_name="Niveau actuelle(si AERD confirmé ou en formation N+)", choices=NIVEAU_FORMATION)
    responsabilite = models.CharField( max_length=100, blank=True, null=True, verbose_name="Role")
    extension = models.ForeignKey(Extension, on_delete=models.CASCADE, null=True, blank=True, verbose_name="Extension")
    inactif = models.BooleanField(default=False, verbose_name="Desactivé (Ne cocher que si vous ne souhaitez plus gérer ce AERD dans l'application)")
    commentaire = models.TextField(max_length=500, null=True, blank=True)

    def __str__(self):
        return f"{self.membre.nom} {self.membre.prenom}"

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


class Ministre(models.Model):
    aerd = models.ForeignKey(Aerd, on_delete=models.CASCADE, blank=True, null=True, verbose_name="Nom", )
    date_entree = models.DateTimeField(blank=True, null=True, verbose_name="Prise de fonction", )
    date_sortie = models.DateTimeField(auto_now_add=True, blank=True, null=True, verbose_name="Fin de fonction", )
    inactif = models.BooleanField(default=False, verbose_name="Desactivé")
    commentaire = models.TextField(max_length=500, null=True, blank=True, verbose_name="Commentaires")

    def __str__(self):
        return f"{self.aerd.membre.nom} {self.aerd.membre.prenom}"

class Ministere(models.Model):
    designation = models.CharField(max_length=100, blank=True, null=True, verbose_name="Nom",)
    ministre = models.ForeignKey(Ministre, on_delete=models.CASCADE, null=True, blank=True, verbose_name="Ministre")
    description = models.CharField(max_length=300, blank=True, null=True, verbose_name="Bref description",)
    def __str__(self):
        return self.designation


class Coordonateur(models.Model):
    aerd = models.ForeignKey(Aerd, on_delete=models.CASCADE, blank=True, null=True, verbose_name="Nom", )
    date_entree = models.DateTimeField(blank=True, null=True, verbose_name="Prise de fonction", )
    date_sortie = models.DateTimeField(blank=True, null=True, verbose_name="Fin de fonction", )
    inactif = models.BooleanField(default=False, verbose_name="Desactivé")
    commentaire = models.TextField(max_length=500, null=True, blank=True, verbose_name="Commentaires")

    def __str__(self):
        return f"{self.aerd.membre.nom} {self.aerd.membre.prenom}"

class Departement(models.Model):
    designation = models.CharField( max_length=100, blank=True, null=True, verbose_name="Nom")
    coordonateur = models.ForeignKey(Coordonateur, on_delete=models.CASCADE, null=True, blank=True, verbose_name="Coordonateur",)
    ministere = models.ForeignKey(Ministere, on_delete=models.CASCADE, null=True, blank=True, verbose_name="Ministère" )
    attributions = models.CharField(max_length=300, blank=True, null=True, verbose_name="Attributions", )
    def __str__(self):
        return self.designation

class Charge(models.Model):
    aerd = models.ForeignKey(Aerd, on_delete=models.CASCADE, blank=True, null=True, verbose_name="Nom", )
    date_entree = models.DateTimeField(blank=True, null=True, verbose_name="Prise de fonction", )
    date_sortie = models.DateTimeField(blank=True, null=True, verbose_name="Fin de fonction", )
    inactif = models.BooleanField(default=False, verbose_name="Desactivé")
    commentaire = models.TextField(max_length=500, null=True, blank=True)

    def __str__(self):
        return f"{self.aerd.membre.nom} {self.aerd.membre.prenom}"

class Ouvrier(models.Model):
    aerd = models.ForeignKey(Aerd, on_delete=models.CASCADE, blank=True, null=True, verbose_name="Nom", )
    date_entree = models.DateTimeField(blank=True, null=True, verbose_name="Date d'entrée", )
    date_sortie = models.DateTimeField(blank=True, null=True, verbose_name="Fin de fonction", )
    inactif = models.BooleanField(default=False, verbose_name="Desactivé")
    commentaire = models.TextField(max_length=500, null=True, blank=True, verbose_name="Commentaires")

    def __str__(self):
        return f"{self.aerd.membre.nom} {self.aerd.membre.prenom}"

class Leader(models.Model):
    aerd = models.ForeignKey(Aerd,on_delete=models.CASCADE, blank=True, null=True, verbose_name="Nom", )
    principal = models.BooleanField(default=False, verbose_name="Leader Principal")
    communaute = models.CharField(max_length=120,verbose_name="Communauté" , null=True, blank=True, choices=COMMUNAUTE)
    extension = models.ForeignKey(Extension, on_delete=models.CASCADE, null=True, blank=True, verbose_name="Extension")
    date_entree = models.DateTimeField(blank=True, null=True, verbose_name="Prise de fonction", )
    date_sortie = models.DateTimeField(blank=True, null=True, verbose_name="Fin de fonction", )
    inactif = models.BooleanField(default=False, verbose_name="Desactivé")
    commentaire = models.TextField(max_length=500, null=True, blank=True, verbose_name="Commentaires")
    def __str__(self):
        return f"{self.aerd.membre.nom} {self.aerd.membre.prenom}"

class Pasteur(models.Model):
    aerd = models.ForeignKey(Aerd,on_delete=models.CASCADE, blank=True, null=True, verbose_name="Nom", )
    extension = models.ForeignKey(Extension, on_delete=models.CASCADE, null=True, blank=True)
    date_entree = models.DateTimeField(blank=True, null=True, verbose_name="Prise de fonction", )
    date_sortie = models.DateTimeField(blank=True, null=True, verbose_name="Fin de fonction", )
    inactif = models.BooleanField(default=False, verbose_name="Desactivé")
    commentaire = models.TextField(max_length=500, null=True, blank=True, verbose_name="Commentaires")
    def __str__(self):
        return f"{self.aerd.membre.nom} {self.aerd.membre.prenom}"

class AssistantPasteur(models.Model):
    aerd = models.ForeignKey(Aerd,on_delete=models.CASCADE, blank=True, null=True, verbose_name="Nom", )
    extension = models.ForeignKey(Extension, on_delete=models.CASCADE, null=True, blank=True, verbose_name="Extension")
    stagiaire = models.BooleanField(default=False, verbose_name="Adjoint")
    pasteur = models.ForeignKey(Pasteur, on_delete=models.CASCADE, null=True, blank=True)
    date_entree = models.DateTimeField(blank=True, null=True, verbose_name="Prise de fonction", )
    date_sortie = models.DateTimeField(blank=True, null=True, verbose_name="Fin de fonction", )
    inactif = models.BooleanField(default=False, verbose_name="Desactivé")
    commentaire = models.TextField(max_length=500, null=True, blank=True, verbose_name="Commentaires")
    def __str__(self):
        return f"{self.aerd.membre.nom} {self.aerd.membre.prenom}"

class Ancien(models.Model):
    aerd = models.ForeignKey(Aerd,on_delete=models.CASCADE, blank=True, null=True, verbose_name="Nom", )
    extension = models.ForeignKey(Extension, on_delete=models.CASCADE, null=True, blank=True, verbose_name="Extension")
    date_entree = models.DateTimeField(blank=True, null=True, verbose_name="Prise de fonction", )
    date_sortie = models.DateTimeField(blank=True, null=True, verbose_name="Fin de fonction", )
    inactif = models.BooleanField(default=False, verbose_name="Desactivé")
    commentaire = models.TextField(max_length=500, null=True, blank=True, verbose_name="Commentaires")
    def __str__(self):
        return f"{self.aerd.membre.nom} {self.aerd.membre.prenom}"

class Diacre(models.Model):
    aerd = models.ForeignKey(Aerd,on_delete=models.CASCADE, blank=True, null=True, verbose_name="Nom", )
    extension = models.ForeignKey(Extension, on_delete=models.CASCADE, null=True, blank=True, verbose_name="Extension")
    date_entree = models.DateTimeField(blank=True, null=True, verbose_name="Prise de fonction", )
    date_sortie = models.DateTimeField(blank=True, null=True, verbose_name="Fin de fonction", )
    inactif = models.BooleanField(default=False, verbose_name="Desactivé")
    commentaire = models.TextField(max_length=500, null=True, blank=True, verbose_name="Commentaires")
    def __str__(self):
        return f"{self.aerd.membre.nom} {self.aerd.membre.prenom}"

class AerdDepartement(models.Model):
    aerd = models.ForeignKey(Aerd, on_delete=models.CASCADE, null=True, blank=True, verbose_name="Ouvrier", )
    departement = models.ForeignKey(Departement, on_delete=models.CASCADE, null=True, blank=True, verbose_name="Departement", )