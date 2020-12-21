from django.contrib import admin
from .models import Formation, Participant, Gestionnaire, Animateur,User

admin.site.register(User)
admin.site.register(Formation)
admin.site.register(Participant)
admin.site.register(Gestionnaire)
admin.site.register(Animateur)
