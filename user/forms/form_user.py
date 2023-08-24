from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

from authentication.models import Account
from user.models.model_user import Profile


class CreateUserForm(UserCreationForm):
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ('username','email','password1', 'password2',)
        labels = {
            'username': 'Pseudo',
            'email': 'Votre adresse e-mail',
            'password1': 'Mot de passe',
            'password2': 'Confirmation de mot de passe',
        }


class UserUpdateForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['username', 'email','password']
        labels = {
            'username': 'Pseudo',
            'email': 'Votre adresse e-mail',
            'password': 'Mot de passe',
        }
        widgets = {
            'password': forms.PasswordInput(attrs={'class': 'form-group'}),

        }
class ProfileUpdateForm(forms.ModelForm):
    class Meta:
        model = Account
        fields = ['username','email','first_name','last_name','job_function','extension','profile_image']
        labels = {
            'username': 'Pseudo',
            'email': 'Votre adresse e-mail',
            'first_name': 'Prénom',
            'last_name': 'Nom',
            'job_function': 'Profession',
        }
