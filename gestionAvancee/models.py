from django.core.validators import RegexValidator
from django.db import models
from django_countries.fields import CountryField


class Extension(models.Model):
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Date d'ajout", blank=True, null=True)
    updated_at = models.DateTimeField(auto_now=True, verbose_name="Date de mise à jour", blank=True, null=True)
    nom = models.CharField(max_length=100)
    description = models.CharField(max_length=200)
    telephone_regex = RegexValidator(
        regex="[0-9]{9}", message="Veuillez entrer un numéro de téléphone valide"
    )
    telephone_1 = models.CharField(validators=[telephone_regex], max_length=100, blank=True, null=True,verbose_name="Téléphone" )
    adresse = models.CharField(max_length=200, verbose_name="Adresse", null=True, blank=True)
    ville = models.CharField(max_length=150, null=True, blank=True, verbose_name="Ville",)
    pays = CountryField(blank_label='(Choisir Pays)', null=True, blank=True, verbose_name="Pays",)

    def __str__(self):
        return f"{self.nom}/{self.description}"

    def get_nom_description_str(self):
        return f"{self.nom} - {self.description}, {self.ville}"
