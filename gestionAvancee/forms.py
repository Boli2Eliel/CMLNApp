
from django.forms import ModelForm

from cmlnGestion.models.model_aerd import Ministere
from gestionAvancee.models import Extension


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

class MinistereForm(ModelForm):
    class Meta:
        model = Ministere
        fields = [
            'designation',
            'departement',
            'ministre',
            'description',
        ]



