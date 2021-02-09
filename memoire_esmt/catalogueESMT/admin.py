from django.contrib import admin
from .models import Formation, Participant, Gestionnaire, Animateur,User,Session,Animation,Participation,Avis

admin.site.register(User)
admin.site.register(Formation)
admin.site.register(Participant)
admin.site.register(Gestionnaire)
admin.site.register(Animateur)
admin.site.register(Session)
admin.site.register(Animation)
admin.site.register(Participation)
admin.site.register(Avis)
