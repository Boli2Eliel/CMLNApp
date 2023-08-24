from django import forms
from django.forms import ModelForm, Form, CharField
from cmlnGestion.models.model_membre import *

class MembreBaseForm:

    def clean(self):

        cleaned_data = ModelForm.clean(self)

        baptise = cleaned_data.get('baptise')
        if baptise == OuiNonChoice.OUI.name:
            date_bapteme = cleaned_data.get('date_bapteme')
            if not date_bapteme:
                msg = ("Veuillez préciser la date de bapteme.")
                self._errors["date_bapteme"] = self.error_class([msg])
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
            'etat_civil',
            'email',
            'adresse',
            'ville',
            'extension',
            'telephone_1',
            'telephone_2',
            'profile_image',
            'commentaire',
        )
        widgets ={
            'nom': forms.TextInput(attrs={'class':'bg-light border-1'}),
            'prenom': forms.TextInput(attrs={'class':'bg-light border-1'}),
            'date_naissance': forms.DateInput(attrs={'class':'bg-light date'}),
            'date_arrivee': forms.DateInput(attrs={'class':'bg-light date'}),
            'date_bapteme': forms.DateInput(attrs={'class':'bg-light date'}),
            'email': forms.EmailInput(attrs={'class':'bg-light'}),
            'adresse': forms.TextInput(attrs={'class':'bg-light'}),
            'ville': forms.TextInput(attrs={'class':'bg-light '}),
            'telephone_1': forms.TextInput(attrs={'class':'bg-light '}),
            'telephone_2': forms.TextInput(attrs={'class':'bg-light '}),
            #'commentaire': forms.TextInput(attrs={'class': 'bg-light'}),

        }
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['date_naissance'].widget.attrs['class'] = "datePicker"
        self.fields['date_arrivee'].widget.attrs['class'] = "datePicker"
        self.fields['date_bapteme'].widget.attrs['class'] = "datePicker"

