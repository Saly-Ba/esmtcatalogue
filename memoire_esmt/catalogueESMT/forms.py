from django import forms
from .models import Formation, Participant, Gestionnaire, Animateur,Avis,Session,Participation,Animation

class FormationForm(forms.ModelForm):
    class Meta:
        model = Formation
        exclude = ('pk','session')

class ParticipantForm(forms.ModelForm):
    class Meta:
        model = Participant
        fields = ('first_name','last_name','username','email','password','telephone','profession','entreprise')

class AnimateurForm(forms.ModelForm):
    class Meta:
        model = Animateur
        fields = ('first_name','last_name','username','email','password','telephone','profession')

class GestionnaireForm(forms.ModelForm):
    class Meta:
        model = Gestionnaire
        fields = ('first_name','last_name','username','email','password','telephone')

class SessionForm(forms.ModelForm):
    class Meta:
        model = Session
        exclude = ('pk',)

