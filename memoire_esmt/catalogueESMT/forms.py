from django import forms
from .models import Formation, Participant, Gestionnaire, Animateur,Avis,Session

class FormationForm(forms.ModelForm):
    class Meta:
        model = Formation
        exclude = ('pk',)

class ParticipantForm(forms.ModelForm):
    class Meta:
        model = Participant
        fields = ('first_name','last_name','username','email','password','telephone')

class AnimateurForm(forms.ModelForm):
    class Meta:
        model = Animateur
        exclude = ('pk',)

class GestionnaireForm(forms.ModelForm):
    class Meta:
        model = Gestionnaire
        exclude = ('pk',)

class SessionForm(forms.ModelForm):
    class Meta:
        model = Session
        exclude = ('pk',)