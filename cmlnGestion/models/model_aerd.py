from django.core.validators import RegexValidator
from django_countries.fields import CountryField
from django.db import models
from enum import Enum
from cmlnGestion.models.model_membre import *
from cmlnGestion.models.model_departement import Departement
from gestionAvancee.models import Extension


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
    OUI = "Oui"
    NON = "Non"

SITUATION =(
    ('-', '-'),
    ('Stagiaire', 'Stagiaire'),
    ('Aerd confirmé', 'Aerd confirmé'),
    ('En formation N+', 'En formation N+'),
)
class SituationChoice(Enum):
    NA = "-"
    STAGIAIRE = "Stagiaire"
    AERD = "Aerd confirmé"
    FORMATION_N = "En formation N+"


NIVEAU_FORMATION =(
    ('N2', 'N2'),
    ('N3', 'N3'),
    ('N4', 'N4'),
)
class NiveauFormationChoice(Enum):
    N_A = "-"
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
    LEADER_PRINCIPAL = "Leader Principal"
    PASTEUR= "Pasteur titulaire"
    PASTEUR_ADJOINT= "Pasteur Stagiaire"
    ASSISTANT_PASTEUR= "Assistant Pasteur"
    ANCIEN = "Ancien(ne)"
    DIACRE = "Diacre/ Diaconnesse"
    OUVRIER = "Ouvrier"

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

MINISTRES =(
    ('', ''),
    ('SOGNHY PAKA', 'SOGNHY PAKA'),
    ('Chistelle PAKA', 'Christelle'),

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

ACTIVITE =(
    ('Culte de célébration', 'Culte de célébration'),
    ('Enseignement', 'Enseignement'),
    ('Yada', 'Yada'),
    ('Conférence', 'Conférence'),
    ('Séminaire', 'Séminaire'),
    ('Veillée de prière', 'Veillée de prière'),
    ('Autres', 'Autres'),

)

class Aerd(models.Model):
    objects = None
    created_at= models.DateTimeField(auto_now_add=True, blank=True, null=True)
    updated_at = models.DateTimeField(auto_now=True, blank=True, null=True)
    membre = models.OneToOneField(Membre, on_delete=models.PROTECT, null=True, verbose_name="Ouvrier", unique=True)
    position =  models.CharField( max_length=100, verbose_name="Position actuelle", choices=POSITION, default="Ouvrier")
    situation = models.CharField(max_length=100, verbose_name="Situation actuelle", choices=SITUATION, default="-")
    niveau_formation = models.CharField( max_length=100, blank=True, null=True, verbose_name="Niveau actuelle(si AERD confirmé ou en formation N+)", choices=[(tag.name, tag.value) for tag in NiveauFormationChoice])
    ministere_1 = models.ForeignKey("Ministere", on_delete=models.CASCADE, related_name="aerds", null=True, blank=True, verbose_name="Ministère principal")
    ministere_2 = models.ForeignKey("Ministere", on_delete=models.CASCADE, null=True, blank=True, verbose_name="Ministère secondaire")
    #departement = models.ManyToManyField(Departement)
    responsabilite = models.CharField( max_length=100, blank=True, null=True, verbose_name="Role")
    extension = models.ForeignKey(Extension, on_delete=models.CASCADE, null=True, blank=True, verbose_name="Extension")
    inactif = models.BooleanField(default=False, verbose_name="Desactivé (Ne cocher que si vous ne souhaitez plus gérer ce AERD dans l'application)")
    commentaire = models.CharField(max_length=500, null=True, blank=True)

    def __str__(self):
        return f"{self.membre}"
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
    def is_from_leader(self):
        return self.position == PositionChoice.LEADER.name
    def is_from_pasteur(self):
        return self.position == PositionChoice.PASTEUR.name
    def is_from_pasteur_adjoint(self):
        return self.position == PositionChoice.PASTEUR_ADJOINT.name
    def is_from_assistant_pasteur(self):
        return self.position == PositionChoice.AP.name
    def is_from_ancien(self):
        return self.position == PositionChoice.ANCIEN.name
    def is_from_diacre(self):
        return self.position == PositionChoice.DIACRE.name
    def get_departement_list(self):
        pass

class Charge(models.Model):
    aerd = models.OneToOneField(Aerd, on_delete=models.CASCADE, blank=True, null=True, verbose_name="Nom", unique=True)
    date_entree = models.DateTimeField(blank=True, null=True, verbose_name="Prise de fonction", )
    date_sortie = models.DateTimeField(blank=True, null=True, verbose_name="Fin de fonction", )
    inactif = models.BooleanField(default=False, verbose_name="Desactivé")
    commentaire = models.TextField(max_length=500, null=True, blank=True)

    def __str__(self):
        return f"{self.aerd.membre.nom} {self.aerd.membre.prenom}"


class Coordonateur(models.Model):
    aerd = models.OneToOneField(Aerd, on_delete=models.CASCADE, blank=True, null=True, verbose_name="Nom",unique=True )
    date_entree = models.DateTimeField(blank=True, null=True, verbose_name="Prise de fonction", )
    date_sortie = models.DateTimeField(blank=True, null=True, verbose_name="Fin de fonction", )
    inactif = models.BooleanField(default=False, verbose_name="Desactivé")
    commentaire = models.TextField(max_length=500, null=True, blank=True, verbose_name="Commentaires")

    def __str__(self):
        return f"{self.aerd.membre.nom} {self.aerd.membre.prenom}"


class Ministre(models.Model):
    coordonateur = models.OneToOneField(Coordonateur, on_delete=models.CASCADE, null=True, blank=True,verbose_name="Nom", unique=True )
    date_entree = models.DateTimeField(blank=True, null=True, verbose_name="Prise de fonction", )
    date_sortie = models.DateTimeField(auto_now_add=True, blank=True, null=True, verbose_name="Fin de fonction", )
    inactif = models.BooleanField(default=False, verbose_name="Desactivé")
    commentaire = models.TextField(max_length=500, null=True, blank=True, verbose_name="Commentaires")

    def __str__(self):
        return f"{self.coordonateur.aerd.membre.nom} {self.coordonateur.aerd.membre.prenom}"

class Ministere(models.Model):
    designation = models.CharField(max_length=100, blank=True, null=True, verbose_name="Nom",)
    departement = models.ManyToManyField(Departement, verbose_name="Departement")
    ministre = models.ForeignKey(Ministre, on_delete=models.CASCADE, null=True, blank=True, verbose_name="Ministre")
    description = models.CharField(max_length=300, blank=True, null=True, verbose_name="Bref description",)
    def __str__(self):
        return self.designation



class Pasteur(models.Model):
    ministre = models.OneToOneField(Ministre,on_delete=models.CASCADE, blank=True, null=True, verbose_name="Nom", unique=True )
    extension = models.ForeignKey(Extension, on_delete=models.CASCADE, null=True, blank=True)
    date_entree = models.DateTimeField(blank=True, null=True, verbose_name="Prise de fonction", )
    date_sortie = models.DateTimeField(blank=True, null=True, verbose_name="Fin de fonction", )
    inactif = models.BooleanField(default=False, verbose_name="Desactivé")
    commentaire = models.TextField(max_length=500, null=True, blank=True, verbose_name="Commentaires")
    def __str__(self):
        return f"{self.ministre.coordonateur.aerd.membre.nom} {self.ministre.coordonateur.aerd.membre.prenom}"

class Leader(models.Model):
    pasteur = models.OneToOneField(Pasteur,on_delete=models.CASCADE, blank=True, null=True, verbose_name="Nom", unique=True)
    principal = models.BooleanField(default=False, verbose_name="Leader Principal")
    communaute = models.CharField(max_length=120,verbose_name="Communauté" , null=True, blank=True, choices=COMMUNAUTE)
    extension = models.ForeignKey(Extension, on_delete=models.CASCADE, null=True, blank=True, verbose_name="Extension")
    date_entree = models.DateTimeField(blank=True, null=True, verbose_name="Prise de fonction", )
    date_sortie = models.DateTimeField(blank=True, null=True, verbose_name="Fin de fonction", )
    inactif = models.BooleanField(default=False, verbose_name="Desactivé")
    commentaire = models.TextField(max_length=500, null=True, blank=True, verbose_name="Commentaires")
    def __str__(self):
        return f"{self.pasteur.ministre.coordonateur.aerd.membre.nom} {self.pasteur.ministre.coordonateur.aerd.membre.prenom}"



class AssistantPasteur(models.Model):
    coordonateur = models.OneToOneField(Coordonateur,on_delete=models.CASCADE, blank=True, null=True, verbose_name="Nom", unique=True )
    extension = models.ForeignKey(Extension, on_delete=models.CASCADE, null=True, blank=True, verbose_name="Extension")
    stagiaire = models.BooleanField(default=False, verbose_name="Adjoint")
    pasteur = models.ForeignKey(Pasteur, on_delete=models.CASCADE, null=True, blank=True)
    date_entree = models.DateTimeField(blank=True, null=True, verbose_name="Prise de fonction", )
    date_sortie = models.DateTimeField(blank=True, null=True, verbose_name="Fin de fonction", )
    inactif = models.BooleanField(default=False, verbose_name="Desactivé")
    commentaire = models.TextField(max_length=500, null=True, blank=True, verbose_name="Commentaires")
    def __str__(self):
        return f"{self.coordonateur.aerd.membre.nom} {self.coordonateur.aerd.membre.prenom}"

class Ancien(models.Model):
    coordonateur = models.OneToOneField(Coordonateur,on_delete=models.CASCADE, blank=True, null=True, verbose_name="Nom", unique=True)
    extension = models.ForeignKey(Extension, on_delete=models.CASCADE, null=True, blank=True, verbose_name="Extension")
    date_entree = models.DateTimeField(blank=True, null=True, verbose_name="Prise de fonction", )
    date_sortie = models.DateTimeField(blank=True, null=True, verbose_name="Fin de fonction", )
    inactif = models.BooleanField(default=False, verbose_name="Desactivé")
    commentaire = models.TextField(max_length=500, null=True, blank=True, verbose_name="Commentaires")
    def __str__(self):
        return f"{self.coordonateur.aerd.membre.nom} {self.coordonateur.aerd.membre.prenom}"

class Diacre(models.Model):
    charge = models.OneToOneField(Charge,on_delete=models.CASCADE, blank=True, null=True, verbose_name="Nom", unique=True)
    extension = models.ForeignKey(Extension, on_delete=models.CASCADE, null=True, blank=True, verbose_name="Extension")
    date_entree = models.DateTimeField(blank=True, null=True, verbose_name="Prise de fonction", )
    date_sortie = models.DateTimeField(blank=True, null=True, verbose_name="Fin de fonction", )
    inactif = models.BooleanField(default=False, verbose_name="Desactivé")
    commentaire = models.TextField(max_length=500, null=True, blank=True, verbose_name="Commentaires")
    def __str__(self):
        return f"{self.charge.aerd.membre.nom} {self.charge.aerd.membre.prenom}"


class AerdMinistere(models.Model):
    aerd = models.ForeignKey(Aerd, on_delete=models.CASCADE, null=True, blank=True, verbose_name="Ouvrier", )
    ministere = models.ForeignKey(Ministere, on_delete=models.CASCADE, null=True, blank=True, verbose_name="Departement", )

