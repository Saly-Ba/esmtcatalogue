from django.urls import path
from . import views

app_name = "catalogueESMT"

urlpatterns = [
    path('',views.accueil,name="accueil"),
    path('inscription/',views.inscription_participant,name="inscription_participant"),
    path('login/',views.login,name="login"),
    path('logout/',views.logout,name="logout"),
    path('participant/',views.espace_participant,name="participant"),
    path('info_participant',views.afficher_info_user,name="info_user"),
    path('animateur/',views.espace_animateur,name="animateur"),
    path('gestion/',views.espace_gestionnaire,name="gestionnaire"),
    path('gestion/animateur',views.action_animateur,name="action_animateur"),
    path('gestion/animateur/ajout',views.ajout_animateur,name="ajout_animateur"),
    path('gestion/formation',views.action_formation,name="action_formation"),
    path('gestion/formation/ajout',views.ajout_formation,name="ajout_formation"),
    path('liste_formation',views.liste_formation,name="liste_formation"),
    path('gestion/formation/ajout-session',views.ajout_session,name="ajout_session"),
    path('gestion/participant',views.action_participant,name="action_participant"),

]