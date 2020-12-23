from django.shortcuts import render,redirect
from django.contrib.auth.decorators import login_required
from .models import User,Participant,Animateur,Gestionnaire,Formation,Session,Avis
from .forms import ParticipantForm,AnimateurForm,GestionnaireForm,FormationForm,SessionForm


# General :
def acceuil(request):
    return render(request,"catalogueESMT/acceuil.html")

def inscription_participant(request):
    if request.method == "POST":
        form = ParticipantForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('catalogueESMT:acceuil')
    else:
        form = ParticipantForm()
    return render(request,'catalogueESMT/participant/inscriptionParticipant.html', {'form' : form})

def login(request):
    if request.method == "POST":
        user = User.objects.get(username=request.POST['username'])
        for user in users:
            if(user.login == request.POST['login'] and user.pwd == request.POST['pwd']):
                request.session['pk'] = user.pk
                return redirect('gestionnaire_depenses:espace_utilisateur')
        
        #print("On a pu nous connecter, veuillez verifier vous identifiants...")
    return render(request,'registration/login.html')

def logout(request):
    try:
        del request.session['pk']
    except KeyError:
        pass
    return redirect('gestionnaire_depenses:home')


def ajout_animateur(request):
    #connected_user = User.objects.get(pk=request.session['pk'])
   # if connected_user.user_type == 1:
    print("Heyyy !!!")
    if request.method == "POST":
        form = AnimateurForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('catalogueESMT:acceuil')
    else:
        form = AnimateurForm()
    return render(request,'catalogueESMT/animateur/ajout_animateur.html',{'form':form})
        

