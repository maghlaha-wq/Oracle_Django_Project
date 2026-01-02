from django.db import models
from django.db import models

# =============================================
# Table Utilisateur
# =============================================
class Utilisateur(models.Model):
    id_user = models.IntegerField(primary_key=True)
    nom = models.CharField(max_length=50)
    prenom = models.CharField(max_length=50)
    email = models.CharField(max_length=100)
    role = models.CharField(max_length=20)

    class Meta:
        managed = False
        db_table = 'UTILISATEUR'

# =============================================
# Table Ressource
# =============================================
class Ressource(models.Model):
    id_ressource = models.IntegerField(primary_key=True)
    nom_ressource = models.CharField(max_length=100)
    type_ressource = models.CharField(max_length=50)
    etat = models.CharField(max_length=20)

    class Meta:
        managed = False
        db_table = 'RESSOURCE'

# =============================================
# Table Reservation
# =============================================
class Reservation(models.Model):
    id_reservation = models.IntegerField(primary_key=True)
    date_reservation = models.DateField()
    date_debut = models.DateField()
    date_fin = models.DateField()
    statut = models.CharField(max_length=20)
    id_ressource = models.ForeignKey(Ressource, on_delete=models.DO_NOTHING, db_column='id_ressource')
    id_user = models.ForeignKey(Utilisateur, on_delete=models.DO_NOTHING, db_column='id_user')

    class Meta:
        managed = False
        db_table = 'RESERVATION'

# =============================================
# Table Historique
# =============================================
class Historique(models.Model):
    id_historique = models.IntegerField(primary_key=True)
    action = models.CharField(max_length=50)
    date_action = models.DateField()
    id_reservation = models.ForeignKey(Reservation, on_delete=models.DO_NOTHING, db_column='id_reservation')

    class Meta:
        managed = False
        db_table = 'HISTORIQUE'

# =============================================
# Table Notification
# =============================================
class Notification(models.Model):
    id_notification = models.IntegerField(primary_key=True)
    type_notification = models.CharField(max_length=50)
    message = models.CharField(max_length=500)
    date_notification = models.DateField()
    statut = models.CharField(max_length=20)
    id_user = models.ForeignKey(Utilisateur, on_delete=models.DO_NOTHING, db_column='id_user')
    id_reservation = models.ForeignKey(Reservation, on_delete=models.DO_NOTHING, db_column='id_reservation', null=True, blank=True)

    class Meta:
        managed = False
        db_table = 'NOTIFICATION'
# Create your models here.
