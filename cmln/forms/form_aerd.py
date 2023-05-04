
from django import forms
from django.forms import ModelForm

from cmln.models.model_aerd import Aerd
from cmln.models.model_membre import Membre

class AerdBaseForm:

    def clean(self):

        cleaned_data = ModelForm.clean(self)

        membre = cleaned_data.get("membre")
        if membre :
            ministere = cleaned_data.get("ministere")
            if not ministere:
                msg = (
                    "Veuillez choisir un ministère"
                )
                self._errors["ministere"] =self.error_class([msg])
                del cleaned_data["ministere"]

        return cleaned_data

class AerdForm(AerdBaseForm, ModelForm):
    #membre = forms.ModelChoiceField(queryset=Membre.objects.all(), label="Selectionner un membre")
    required_css_class = "required"
    class Meta:
        model = Aerd
        fields = [
            'membre',
            'position',
            'situation',
            'niveau_formation',
            'responsabilite',
            'extension',
            'commentaire',
        ]



