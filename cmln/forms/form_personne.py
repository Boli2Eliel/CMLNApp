from django.forms import ModelForm, Form, CharField

from cmln.models.model_membre import *


class MembreForm(ModelForm):
    class Meta:
        model = Membre
        fields = ('nom', 'prenom', 'email', 'date_naissance', 'adresse', 'ville','extension', 'telephone', 'commentaire')

