from django.shortcuts import render,redirect
from django.contrib.auth.decorators import login_required
from .models import User,Participant,Animateur,Gestionnaire,Formation,Session,Avis
from .forms import ParticipantForm,AnimateurForm,GestionnaireForm,FormationForm,SessionForm


# General :
def accueil(request):
    if 'pk' in request.session:
        user = User.objects.get(pk=request.session['pk'])
    else :
        user = None
    return render(request,"catalogueESMT/accueil.html",{'user':user})

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
    return redirect('catalogueESMT:accueil')

#Participant Actions :
def inscription_participant(request):
    if request.method == "POST":
        form = ParticipantForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('catalogueESMT:accueil')
    else:
        form = ParticipantForm()
    return render(request,'catalogueESMT/participant/inscriptionParticipant.html', {'form' : form})

def espace_participant(request):
    participant = User.objects.get(pk=request.session['pk'])
    return render(request,'catalogueESMT/participant/espace_participant.html',{'participant':participant})

def afficher_info_user(request):
    if not('pk' in request.session):
        return redirect('catalogueESMT:login')
    else:
        parti = User.objects.get(pk=request.session['pk'])
        if not (parti.user_type == 3) :
            return redirect('catalogueESMT:login')
    return render(request,'catalogueESMT/participant/afficher_info_user.html',{'parti': parti})

#Animateurs Actions :
def espace_animateur(request):
    if not ('pk' in request.session):
        animateur = None
        return redirect('catalogueESMT:login')
    else :
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
                return redirect('catalogueESMT:accueil')
        else:
            form = AnimateurForm()
    return render(request,'catalogueESMT/animateur/ajout_animateur.html',{'form':form})

def ajout_formation(request):
    if not ('pk' in request.session):
        return redirect('catalogueESMT:login')
    else :
        connected_user = User.objects.get(pk=request.session['pk'])
        if connected_user.user_type == 1:
            print("Heyyy !!!")
            if request.method == "POST":
                form = FormationForm(request.POST)
                if form.is_valid():
                    form.save()
                    return redirect('catalogueESMT:accueil')
            else:
                form = FormationForm()
    return render(request,'catalogueESMT/formation/ajout_formation.html',{'form':form})

def action_animateur(request):
    connected_user = User.objects.get(pk=request.session['pk'])
    if not (connected_user.user_type == 1):
        return redirect('catalogueESMT:accueil')
    return render(request,'catalogueESMT/gestionnaire/action_animateur.html')

def action_formation(request):
    connected_user = User.objects.get(pk=request.session['pk'])
    if not (connected_user.user_type == 1):
        return redirect('catalogueESMT:accueil')
    return render(request,'catalogueESMT/gestionnaire/action_formations.html')

def action_participant(request):
    connected_user = User.objects.get(pk=request.session['pk'])
    if not (connected_user.user_type == 1):
        redirect('catalogueESMT:accueil')
    return render(request,'catalogueESMT/gestionnaire/action_participant.html')
