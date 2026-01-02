from datetime import date
from .models import Utilisateur, Ressource, Reservation, Notification
from django.db import connection

# =============================================
# Utilitaire pour récupérer NEXTVAL d'une séquence Oracle
# =============================================
def get_nextval_seq(seq_name):
    """
    Récupère la prochaine valeur d'une séquence Oracle
    """
    with connection.cursor() as cursor:
        cursor.execute(f"SELECT {seq_name}.NEXTVAL FROM dual")
        return cursor.fetchone()[0]

# =============================================
# Créer un utilisateur
# =============================================
def creer_utilisateur(nom, prenom, email, role):
    """
    Crée un utilisateur et retourne l'objet Utilisateur
    """
    user_id = get_nextval_seq('seq_Utilisateur')
    user = Utilisateur(
        id_user=user_id,
        nom=nom,
        prenom=prenom,
        email=email,
        role=role
    )
    user.save()
    return user

# =============================================
# Créer une ressource
# =============================================
def creer_ressource(nom_ressource, type_ressource, etat):
    """
    Crée une ressource et retourne l'objet Ressource
    """
    ressource_id = get_nextval_seq('seq_Ressource')
    ressource = Ressource(
        id_ressource=ressource_id,
        nom_ressource=nom_ressource,
        type_ressource=type_ressource,
        etat=etat
    )
    ressource.save()
    return ressource

# =============================================
# Créer une réservation
# =============================================
def creer_reservation(id_user, id_ressource, date_debut, date_fin):
    """
    Crée une réservation pour un utilisateur et une ressource
    """
    reservation_id = get_nextval_seq('seq_Reservation')
    user = Utilisateur.objects.get(id_user=id_user)
    ressource = Ressource.objects.get(id_ressource=id_ressource)
    
    reservation = Reservation(
        id_reservation=reservation_id,
        date_reservation=date.today(),
        date_debut=date_debut,
        date_fin=date_fin,
        statut='EN_ATTENTE',  # par défaut
        id_user=user,
        id_ressource=ressource
    )
    reservation.save()
    return reservation

# =============================================
# Créer une notification
# =============================================
def creer_notification(type_notification, message, id_user, id_reservation=None):
    """
    Crée une notification pour un utilisateur et éventuellement une réservation
    """
    notif_id = get_nextval_seq('seq_Notification')
    user = Utilisateur.objects.get(id_user=id_user)
    reservation = None
    if id_reservation:
        reservation = Reservation.objects.get(id_reservation=id_reservation)
    
    notif = Notification(
        id_notification=notif_id,
        type_notification=type_notification,
        message=message,
        date_notification=date.today(),
        statut='ENVOYEE',
        id_user=user,
        id_reservation=reservation
    )
    notif.save()
    return notif