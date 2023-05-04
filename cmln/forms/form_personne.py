from django.forms import ModelForm, Form, CharField

from cmln.models.model_membre import *

class MembreBaseForm:

    def clean(self):

        cleaned_data = ModelForm.clean(self)

        baptise = cleaned_data.get("baptise")
        if baptise == OuiNonChoice.OUI.name:
            date_bapteme = cleaned_data.get("date_bapteme")
            if not date_bapteme:
                msg = (
                    "Veuillez preciser la date de baptème"
                )
                self._errors["date_bapteme"] =self.error_class([msg])
                del cleaned_data["date_bapteme"]

        return cleaned_data

class MembreForm(MembreBaseForm, ModelForm):
    required_css_class = "required"
    class Meta:
        model = Membre
        fields = (
            'nom',
            'prenom',
            'sexe',
            'date_naissance',
            'date_arrivee',
            'baptise',
            'date_bapteme',
            'situation',
            'email',
            'adresse',
            'ville',
            'extension',
            'telephone',
            'commentaire',
        )
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['date_naissance'].widget.attrs['class'] = "datePicker"
        self.fields['date_arrivee'].widget.attrs['class'] = "datePicker"
        self.fields['date_bapteme'].widget.attrs['class'] = "datePicker"

