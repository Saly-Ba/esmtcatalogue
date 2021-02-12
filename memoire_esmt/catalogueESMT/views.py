from django.shortcuts import render,redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .models import User,Participant,Animateur,Gestionnaire,Formation,Session,Avis,Participation,Animation
from .forms import ParticipantForm,AnimateurForm,GestionnaireForm,FormationForm,SessionForm,AnimationForm
import datetime


# General :
def accueil(request):
    user = None
    if 'pk' in request.session:
        user = User.objects.get(pk=request.session['pk'])
    return render(request,"catalogueESMT/accueil.html",{'user':user})

def login(request):
    if request.method == "POST":
        try:
            user = User.objects.get(username=request.POST['username'])
            if(user.username == request.POST['username'] and user.password == request.POST['password']):
                request.session['pk'] = user.pk
                if user.user_type == 1:
                    return redirect('catalogueESMT:gestionnaire')
                elif user.user_type == 2:
                    return redirect('catalogueESMT:animateur')
                else :
                    return redirect('catalogueESMT:participant')
            else:
                messages.error(request,'Le username ou le mot de passe est incorrect')
        except:
            messages.error(request,'Cette utilisateur n\'existe pas dans notre base donnees')
        
        
    return render(request,'registration/login.html')

def logout(request):
    try:
        del request.session['pk']
    except KeyError:
        pass
    return redirect('catalogueESMT:accueil')

def logged_verif(f):
    def access_denied(request,*args):
        if not('pk' in request.session):
            return redirect('catalogueESMT:login')
        else:
            return f(request,*args)
    return access_denied
            

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

@logged_verif
def espace_participant(request):
    participant = User.objects.get(pk=request.session['pk'])
    return render(request,'catalogueESMT/participant/espace_participant.html',{'participant':participant})

@logged_verif
def afficher_info_user(request):
    parti = User.objects.get(pk=request.session['pk'])
    if not (parti.user_type == 3) :
        return redirect('catalogueESMT:login')
    return render(request,'catalogueESMT/participant/afficher_info_user.html',{'parti': parti})

@logged_verif
def participation(request, id_formation, id_session_picked):
    parti = User.objects.get(pk=request.session['pk'])
    if not (parti.user_type == 3):
        return redirect('catalogueESMT:login')
    else:
        formation = Formation.objects.get(pk=id_formation)
        parti.formations_suivies  = formation
        Participation.participant = parti
        Participation.formation = formation
        Participation.date_participation = Session.objects.get(pk=id_session_picked).date
        Participation.save()
    return redirect('catalogueESMT:liste_formation')

#Animateurs Actions :
@logged_verif
def espace_animateur(request):
    animateur = User.objects.get(pk=request.session['pk'])
    return render(request,'catalogueESMT/animateur/espace_animateur.html',{'animateur':animateur})


#Formations Actions:
def liste_formation(request):
    formations = set()
    periode = datetime.datetime.now().year
    sessions = Session.objects.filter(date__year=periode)
    for i in sessions :
        formations.add(Formation.objects.get(pk=i.formation.pk))
        print(formations)
    return render(request,'catalogueESMT/formation/lister_formation.html',{'formations':formations, 'sessions':sessions})

#Gestionnaire Actions :
@logged_verif
def espace_gestionnaire(request):
    gestionnaire = User.objects.get(pk=request.session['pk'])
    return render(request,'catalogueESMT/gestionnaire/espace_gestionnaire.html',{'gestionnaire':gestionnaire})
        
@logged_verif
def ajout_animateur(request):
    connected_user = User.objects.get(pk=request.session['pk'])
    if connected_user.user_type == 1:
        if request.method == "POST":
            form = AnimateurForm(request.POST)
            if form.is_valid():
                animateur = form.save(commit=False)
                animateur.user_type=2
                animateur.save()
                return redirect('catalogueESMT:gestionnaire')
        else:
            form = AnimateurForm()
    else:
        return redirect('catalogueESMT:accueil')
    return render(request,'catalogueESMT/animateur/ajout_animateur.html',{'form':form})

@logged_verif
def ajout_formation(request):
    connected_user = User.objects.get(pk=request.session['pk'])
    if connected_user.user_type == 1:
        animateurs = Animateur.objects.all()
        if animateurs.exists():
            if request.method == "POST":
                form = FormationForm(request.POST)
                if form.is_valid():
                    form.save()
                    return redirect('catalogueESMT:gestionnaire')
            else:
                form = FormationForm()
        else:
            form = FormationForm()
            messages.error(request,'Aucun animateurs n\'est encore present dans votre base de donnees')
    else:
        return redirect('catalogueESMT:login')
    return render(request,'catalogueESMT/formation/ajout_formation.html',{'form':form,})

@logged_verif
def ajout_session(request):
    connected_user = User.objects.get(pk=request.session['pk'])
    if connected_user.user_type == 1:
        formations = Formation.objects.all()
        if formations.exists() :
            if request.method == "POST":
                form = SessionForm(request.POST)
                if form.is_valid():
                    session = form.save(commit = False)
                    formation_current = Formation.objects.get(pk=session.formation.id)
                    sessions_of_current_form = Session.objects.filter(formation=formation_current)
                    animations = formation_current.animation_set.all()
                    print(animations)
                    for i in animations:
                        if sessions_of_current_form.exists() :
                            i.debut = sessions_of_current_form[0].date
                        else:
                            i.debut = session.date
                        i.fin = session.date + datetime.timedelta(session.duree)
                        i.save()

                    session.save()
                    return redirect('catalogueESMT:gestionnaire')
            else :
                form = SessionForm()
        else:
            form = SessionForm()
            messages.error(request,'Il n\'y a, pour le moment, aucune formation enregistrer dans votre base de données')
    else:
        return redirect('catalogueESMT:login')
    return render(request,'catalogueESMT/formation/ajout_session.html',{'formations':formations})

@logged_verif
def animation(request,id_formation):
    connected_user = User.objects.get(pk=request.session['pk'])
#    if connected_user.user_type == 1:



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
