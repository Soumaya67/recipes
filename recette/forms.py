from django import forms

from recette.models import Recette


class LoginForm(forms.Form):
    username = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput)
    widgets = {
        'username': forms.TextInput(attrs={'class': 'form-control mb-2'}),
        'password': forms.TextInput(attrs={'class': 'form-control'}),
    }

class RecetteForm(forms.ModelForm):
    class Meta:
        model = Recette
        fields = ['titre' , 'ingredients', 'description','date_creation', 'auteur']

