from dal import autocomplete
from django import forms
#from django.contrib.admin.views import autocomplete
from django.forms import ModelForm

from activite.models import Activite
from cmlnGestion.models.model_aerd import Aerd
from cmlnGestion.models.model_membre import Membre

class ActiviteBaseForm:

    def clean(self):

        cleaned_data = ModelForm.clean(self)

        heure_debut = cleaned_data.get("heure_debut")
        if heure_debut :
            heure_fin = cleaned_data.get("heure_fin")
            if not heure_fin:
                msg = (
                    "Veuillez indiquer l'heure de fin'"
                )
                self._errors["heure_fin"] =self.error_class([msg])
                del cleaned_data["heure_fin"]

            return cleaned_data

class ActiviteForm(ActiviteBaseForm, ModelForm):
    #membre = forms.ModelChoiceField(queryset=Membre.objects.all(), label="Selectionner un membre")
    required_css_class = "required"

    def clean(self):

        cleaned_data = ModelForm.clean(self)
        heure_debut= cleaned_data.get('heure_debut')
    class Meta:
        model = Activite
        fields = [
            'extension',
            'type',
            'date',
            'heure_debut',
            'heure_fin',
            'theme',
            'ref_biblique',
            'moderateur',
            'intervenant',
            'resume',
            'nbre_hommes',
            'nbre_femmes',
            'nbre_enfants',
            'nouveaux_venus',
            'offrande',
            'dime',
            'premices',
            'action_grace',
            'achat_parcelle',
            'construction',
            'autres',
        ]

        widgets = {
            'resume': forms.Textarea(attrs={'class': 'bg-light'}),
            #'membre': autocomplete.ModelSelect2(url='membre_autocomplete'),

        }
