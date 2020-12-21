from django.shortcuts import render,redirect
from .models import *
from .forms import ParticipantForm


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
