from enum import Enum

from django.core.validators import RegexValidator
from django_countries.fields import CountryField
from django.db import models


def get_profile_image_filepath(self, filename):
    return f'profile_images/{str(self.pk)}/{"profile_image.png"}'

def get_default_profile_image():
    return 'img/avatar.jpg'
class SexeChoice(Enum):
    F = "Féminin"
    M = "Masculin"

class OuiNonChoice(Enum):
    OUI = "OUI"
    NON = "NON"

class SituationChoice(Enum):

    NOUVEAU = "Nouvel arrivant"
    INTEGRATION = "En cours d'intégration - N1"
    AERD = 'Aerd'

class Extension(models.Model):
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Date d'ajout", blank=True, null=True)
    updated_at = models.DateTimeField(auto_now=True, verbose_name="Date de mise à jour", blank=True, null=True)
    nom = models.CharField(max_length=100)
    description = models.CharField(max_length=200)
    telephone_regex = RegexValidator(
        regex="[0-9]{9}", message="Veuillez entrer un numéro de téléphone valide"
    )
    telephone_1 = models.CharField(validators=[telephone_regex], max_length=100, blank=True, null=True,verbose_name="Standard" )
    adresse = models.CharField(max_length=200, verbose_name="Adresse", null=True, blank=True)
    ville = models.CharField(max_length=150, null=True, blank=True, verbose_name="Ville",)
    pays = CountryField(blank_label='(Choisir Pays)', null=True, blank=True, verbose_name="Pays",)

    def __str__(self):
        return f"{self.nom}/{self.description}"

    def get_nom_description_str(self):
        return f"{self.nom} - {self.description}, {self.ville}"

class Membre(models.Model):
    ETAT_CIVIL = (
        ('Célibataire', 'Célibataire'),
        ('Marié(e)', 'Marié(e)'),
        ('Divorcé(e)', 'Divorcé(e)'),
        ('Veuf(ve)', 'Veuf(ve)'),
    )

    SEXE = (
        ('Féminin', 'Féminin'),
        ('Masculin', 'Masculin'),

    )

    created_at= models.DateTimeField(auto_now_add=True, blank=True, null=True)
    updated_at = models.DateTimeField(auto_now=True, blank=True, null=True)
    prenom = models.CharField( max_length=100, blank=True, null=True)
    nom = models.CharField( max_length=100, )
    sexe = models.CharField(max_length=20, blank=True, null=True, verbose_name="Sexe", choices=[(tag.name, tag.value) for tag in SexeChoice])
    date_naissance = models.DateField(null=True, blank=True)
    date_arrivee = models.DateField(verbose_name="Date d'arrivée à CMLN", blank=True, null=True)
    baptise = models.CharField(max_length=100, blank=True, null=True, verbose_name="Baptisé", choices=[(tag.name, tag.value) for tag in OuiNonChoice])
    date_bapteme = models.DateField(verbose_name="Date de bapteme(par immersion)", null=True, blank=True)
    situation = models.CharField(max_length=100, blank=True, null=True, verbose_name="Situation actuelle",
                                choices=[(tag.name, tag.value) for tag in SituationChoice])
    etat_civil = models.CharField(max_length=60, null=True, blank=True, choices=ETAT_CIVIL)
    email = models.CharField(max_length=150, blank=True, null=True)
    adresse = models.CharField(max_length=100, blank=True, null=True)
    ville = models.CharField(max_length=100, blank=True, null=True)
    extension = models.ForeignKey(Extension, on_delete=models.CASCADE, null=True, blank=True)
    telephone_regex = RegexValidator(
        regex="[0-9]{9}", message="Veuillez entrer un numéro de téléphone valide"
    )
    telephone_1 = models.CharField(validators=[telephone_regex], max_length=100, blank=True, null=True)
    telephone_2 = models.CharField(validators=[telephone_regex], max_length=100, blank=True, null=True)
    date_inscription = models.DateField(auto_now_add=True, verbose_name="Date d'inscription", blank=True, null=True)
    commentaire = models.CharField(max_length=500, default='RAS')
    profile_image = models.ImageField(max_length=255, upload_to=get_profile_image_filepath, null=True, blank=True,
                                      default=get_default_profile_image)

    class Meta:
        unique_together = [[ 'prenom', 'nom']]

    def __str__(self):
        return f"{self.prenom} {self.nom}"

    def get_nom_complet_str(self):
        return f"{self.prenom} , {self.nom}"

    def get_adresse_complete_str(self):
        return f"{self.adresse} , {self.ville}"

    def get_extension_str(self):
        return f"{self.extension.description}"
    

    def is_from_nouveau(self):
        return self.situation == SituationChoice.NOUVEAU.name

    def is_from_integration(self):
        return self.situation == SituationChoice.INTEGRATION.name

    def is_from_oui(self):
        return self.baptise == OuiNonChoice.OUI.name