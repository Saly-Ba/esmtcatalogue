from django.db import models
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    USER_TYPE_CHOICES = [(1,"Gestionnaire"),(2,"Animateur"),(3,"Participant")]

    user_type = models.IntegerField(choices=USER_TYPE_CHOICES,default=3)
    telephone = models.CharField(max_length=50,null=True,blank=True)


class Participant(User):
    formations_suivies = models.ManyToManyField("Formation",through="Participation",related_name="participants")
    profession = models.CharField(max_length=50)
    entreprise = models.CharField(max_length=50)

class Gestionnaire(User):
   pass

class Animateur(User):
    profession = models.CharField(max_length=50)

class Formation(models.Model):
    intitule = models.CharField(max_length=50) 
    public_cible = models.CharField( max_length=90)
    prerequis = models.ForeignKey("Formation",on_delete=models.CASCADE,null=True,blank=True)
    montant = models.IntegerField(default=0)
    animateurs = models.ManyToManyField("Animateur", through="Animation",related_name="formations")
    fiche_programme = models.CharField(max_length=255)
    
    DOMAINE_A_CHOISIR = [(1,"Objets connectés"),(2,"Panorama des réseaux et services"),(3,"Réseaux mobiles et évolutions"),(4,"Multimédia et Audiovisuel"),
                                    (5,"Radiofréquences et Environnement"),(6,"Réseaux d’Infrastructure"),(7,"Energies nouvelles et renouvelables"),(8,"Développement Web & Mobile"),
                                    (9,"Développement Web & Mobile"),(10,"Economie et Régulation du numérique"),(11,"Réseaux Informatiques et IoT"),(12,"Administration Système"),
                                    (13,"Cloud Computing & Virtualisation"),(14,"Big data"),(15,"Sécurité des Réseaux et des Systèmes d’Information"),(16,"Bases de Données et Applications"),
                                    (18,"Intelligence Artificielle"),(19,"Cyber Security"),(20,"Management de la transformation digitale"),]
    domaine_choisi = models.IntegerField(choices=DOMAINE_A_CHOISIR)

    def __str__(self):
        return self.intitule

class Session(models.Model):
    date = models.DateField()
    duree = models.IntegerField(default=0)
    lieu = models.CharField(max_length=50)
    formation = models.ForeignKey("Formation",on_delete=models.CASCADE)
    

class Avis(models.Model):
    #Une table associative en la table Participant et celle de Formation
    commentaire = models.CharField(max_length=50,default="")
    note = models.IntegerField(default=0)
    avis_participant = models.ForeignKey(Participant, on_delete=models.CASCADE,null=True,blank=True)
    avis_formation = models.ForeignKey(Formation, on_delete=models.CASCADE,null=True,blank=True)
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)

class Participation(models.Model):
    date_participation = models.DateField()
    participant = models.ForeignKey("Participant",on_delete=models.CASCADE)
    formation = models.ForeignKey("Formation",on_delete=models.CASCADE)

class Animation(models.Model):
    debut = models.DateField()
    fin = models.DateField()
    formation = models.ForeignKey("Formation",on_delete=models.CASCADE)
    animateur = models.ForeignKey("Animateur",on_delete=models.CASCADE)