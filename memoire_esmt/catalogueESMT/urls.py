from django.urls import path
from . import views

app_name = "catalogueESMT"

urlpatterns = [
    path('',views.acceuil,name="acceuil"),
    path('inscription/',views.inscription_participant,name="inscription_participant"),
    path('login/',views.login,name="login"),
    path('participant/',views.espace_participant,name="participant"),
    path('animateur/',views.espace_animateur,name="animateur"),
    path('gestion/',views.espace_gestionnaire,name="gestionnaire"),
    path('gestion/ajout/animateur',views.ajout_animateur,name="ajout_animateur"),

]