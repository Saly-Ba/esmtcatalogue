from django.urls import path
from . import views

app_name = "catalogueESMT"

urlpatterns = [
    path('',views.acceuil,name="acceuil"),
    path('inscription/',views.inscription_participant,name="inscription_participant"),
]