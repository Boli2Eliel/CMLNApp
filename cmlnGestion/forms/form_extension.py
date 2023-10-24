from django.forms import ModelForm
from cmlnGestion.models.model_membre import Extension


class ExtensionForm(ModelForm):
    class Meta:
        model = Extension
        fields = [
            'nom',
            'description',
            'telephone_1',
            'adresse',
            'ville',
            'pays',
        ]
