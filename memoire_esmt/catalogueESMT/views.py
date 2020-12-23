from django.shortcuts import render,redirect
from django.contrib.auth.decorators import login_required
from .models import User,Participant,Animateur,Gestionnaire,Formation,Session,Avis
from .forms import ParticipantForm,AnimateurForm,GestionnaireForm,FormationForm,SessionForm


# General :
def acceuil(request):
    return render(request,"catalogueESMT/acceuil.html")

def login(request):
    if request.method == "POST":
        user = User.objects.get(username=request.POST['username'])
        if(user.username == request.POST['username'] and user.password == request.POST['password']):
            request.session['pk'] = user.pk
            if user.user_type == 1:
                return redirect('catalogueESMT:gestionnaire')
            elif user.user_type == 2:
                return redirect('catalogueESMT:animateur')
            else :
                return redirect('catalogueESMT:participant')
        
    return render(request,'registration/login.html')

def logout(request):
    try:
        del request.session['pk']
    except KeyError:
        pass
    return redirect('catalogueESMT:acceuil')

#Participant Actions :
def inscription_participant(request):
    if request.method == "POST":
        form = ParticipantForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('catalogueESMT:acceuil')
    else:
        form = ParticipantForm()
    return render(request,'catalogueESMT/participant/inscriptionParticipant.html', {'form' : form})

def espace_participant(request):
    participant = User.objects.get(pk=request.session['pk'])
    return render(request,'catalogueESMT/participant/espace_participant.html',{'participant':participant})

#Animateurs Actions :
def espace_animateur(request):
    animateur = User.objects.get(pk=request.session['pk'])
    return render(request,'catalogueESMT/animateur/espace_animateur.html',{'animateur':animateur})

#Gestionnaire Actions :
def espace_gestionnaire(request):
    gestionnaire = User.objects.get(pk=request.session['pk'])
    return render(request,'catalogueESMT/gestionnaire/espace_gestionnaire.html',{'gestionnaire':gestionnaire})
        
def ajout_animateur(request):
    connected_user = User.objects.get(pk=request.session['pk'])
    if connected_user.user_type == 1:
        print("Heyyy !!!")
        if request.method == "POST":
            form = AnimateurForm(request.POST)
            if form.is_valid():
                form.save()
                return redirect('catalogueESMT:acceuil')
        else:
            form = AnimateurForm()
    return render(request,'catalogueESMT/animateur/ajout_animateur.html',{'form':form})