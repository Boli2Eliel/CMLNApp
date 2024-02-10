from dal import autocomplete
from django import forms
#from django.contrib.admin.views import autocomplete
from django.forms import ModelForm

from cmlnGestion.models.model_aerd import Aerd, AerdMinistere, Ministere
from cmlnGestion.models.model_membre import Membre

class AerdBaseForm:

    def clean(self):

        cleaned_data = ModelForm.clean(self)

        membre = cleaned_data.get("membre")
        if membre :
            position = cleaned_data.get("position")
            if not position:
                msg = (
                    "Veuillez indiquer la position qu'occupe ce AERD"
                )
                self._errors["position"] =self.error_class([msg])
                del cleaned_data["position"]

            return cleaned_data



class AerdForm(AerdBaseForm, ModelForm):
    #membre = forms.ModelChoiceField(queryset=Membre.objects.all(), label="Selectionner un membre")
    required_css_class = "required"

    def clean(self):

        cleaned_data = ModelForm.clean(self)
        membre= cleaned_data.get('membre')
    class Meta:
        model = Aerd
        fields = [
            'membre',
            'position',
            'situation',
            'niveau_formation',
            'ministere_1',
            'ministere_2',
            #'departement',
            'responsabilite',
            'extension',
            'commentaire',
        ]

        widgets = {
            'commentaire': forms.Textarea(attrs={'class': 'bg-light'}),
            #'membre': autocomplete.ModelSelect2(url='membre_autocomplete'),

        }

class AerdMinistereForm(ModelForm):
    class Meta:
        model = Ministere
        fields = [
            'designation',
        ]



