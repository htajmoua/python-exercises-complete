# Écrivez votre code ici !
# Consultez le fichier instructions.md pour les consignes

"""
Module 12 - Héritage et Polymorphisme
Concepts avancés de POO : réutilisation et spécialisation du code
"""

# ============= EXERCICE 1 : HÉRITAGE SIMPLE =============

class Animal:
    """Classe parent Animal"""
    
    def __init__(self, nom, age):
        # À compléter
        pass
    
    def se_presenter(self):
        """Affiche la présentation de l'animal"""
        # À compléter
        pass
    
    def faire_bruit(self):
        """Fait un bruit générique"""
        # À compléter
        pass


class Chien(Animal):
    """Classe Chien qui hérite d'Animal"""
    
    def __init__(self, nom, age, race):
        # À compléter - utiliser super()
        pass
    
    def faire_bruit(self):
        """Override : le chien aboie"""
        # À compléter
        pass
    
    def rapporter(self):
        """Méthode spécifique au chien"""
        # À compléter
        pass


# ============= EXERCICE 2 : UTILISER SUPER() =============

class Vehicule:
    """Classe parent Vehicule"""
    
    def __init__(self, marque, modele):
        # À compléter
        pass
    
    def afficher_info(self):
        """Affiche les infos du véhicule"""
        # À compléter
        pass


class Voiture(Vehicule):
    """Classe Voiture qui hérite de Vehicule"""
    
    def __init__(self, marque, modele, nombre_portes):
        # À compléter - utiliser super()
        pass
    
    def afficher_info(self):
        """Override avec appel à super()"""
        # À compléter
        pass


# ============= EXERCICE 3 : HIÉRARCHIE À PLUSIEURS NIVEAUX =============

class Employe:
    """Classe de base Employe"""
    
    def __init__(self, nom, salaire_base):
        # À compléter
        pass
    
    def calculer_salaire(self):
        """Calcule le salaire"""
        # À compléter
        pass


class Manager(Employe):
    """Manager hérite d'Employe"""
    
    def __init__(self, nom, salaire_base, bonus):
        # À compléter
        pass
    
    def calculer_salaire(self):
        """Override : ajoute le bonus"""
        # À compléter
        pass


class Directeur(Manager):
    """Directeur hérite de Manager"""
    
    def __init__(self, nom, salaire_base, bonus, actions):
        # À compléter
        pass
    
    def calculer_salaire(self):
        """Override : ajoute la valeur des actions"""
        # À compléter
        pass


# ============= EXERCICE 4 : POLYMORPHISME =============

class Forme:
    """Classe parent abstraite pour les formes"""
    
    def calculer_aire(self):
        """À override dans les sous-classes"""
        # À compléter
        pass
    
    def calculer_perimetre(self):
        """À override dans les sous-classes"""
        # À compléter
        pass


class Rectangle(Forme):
    """Rectangle hérite de Forme"""
    
    def __init__(self, longueur, largeur):
        # À compléter
        pass
    
    def calculer_aire(self):
        """Override : aire du rectangle"""
        # À compléter
        pass
    
    def calculer_perimetre(self):
        """Override : périmètre du rectangle"""
        # À compléter
        pass


class Cercle(Forme):
    """Cercle hérite de Forme"""
    PI = 3.14159
    
    def __init__(self, rayon):
        # À compléter
        pass
    
    def calculer_aire(self):
        """Override : aire du cercle"""
        # À compléter
        pass
    
    def calculer_perimetre(self):
        """Override : circonférence"""
        # À compléter
        pass


class Triangle(Forme):
    """Triangle hérite de Forme"""
    
    def __init__(self, base, hauteur, cote1, cote2, cote3):
        # À compléter
        pass
    
    def calculer_aire(self):
        """Override : aire du triangle"""
        # À compléter
        pass
    
    def calculer_perimetre(self):
        """Override : périmètre du triangle"""
        # À compléter
        pass


# ============= EXERCICE 5 : MÉTHODE ABSTRAITE (SIMULATION) =============

class Paiement:
    """Classe parent pour les paiements"""
    
    def __init__(self, montant):
        # À compléter
        pass
    
    def traiter(self):
        """Lève NotImplementedError - à override"""
        # À compléter
        pass
    
    def afficher_recu(self):
        """Affiche le reçu"""
        # À compléter
        pass


class PaiementCarte(Paiement):
    """Paiement par carte"""
    
    def traiter(self):
        """Override : traite le paiement par carte"""
        # À compléter
        pass


class PaiementPaypal(Paiement):
    """Paiement par PayPal"""
    
    def traiter(self):
        """Override : traite le paiement par PayPal"""
        # À compléter
        pass


class PaiementEspeces(Paiement):
    """Paiement en espèces"""
    
    def traiter(self):
        """Override : traite le paiement en espèces"""
        # À compléter
        pass


# ============= EXERCICE 6 : HÉRITAGE AVEC ATTRIBUTS DE CLASSE =============

class Personnage:
    """Classe parent Personnage avec compteur"""
    nombre_personnages = 0
    
    def __init__(self, nom, points_vie):
        # À compléter - incrémenter nombre_personnages
        pass


class Guerrier(Personnage):
    """Guerrier hérite de Personnage"""
    
    def __init__(self, nom, points_vie, force):
        # À compléter
        pass


class Mage(Personnage):
    """Mage hérite de Personnage"""
    
    def __init__(self, nom, points_vie, mana):
        # À compléter
        pass


class Archer(Personnage):
    """Archer hérite de Personnage"""
    
    def __init__(self, nom, points_vie, precision):
        # À compléter
        pass


# ============= EXERCICE 7 : OVERRIDE AVEC VALIDATION =============

class CompteBancaire:
    """Compte bancaire de base"""
    
    def __init__(self, titulaire, solde):
        # À compléter
        pass
    
    def retirer(self, montant):
        """Retire un montant"""
        # À compléter
        pass


class CompteEpargne(CompteBancaire):
    """Compte épargne avec contraintes"""
    
    def __init__(self, titulaire, solde, taux_interet):
        # À compléter
        pass
    
    def retirer(self, montant):
        """Override : garde minimum 100"""
        # À compléter
        pass
    
    def appliquer_interets(self):
        """Applique les intérêts"""
        # À compléter
        pass


class CompteJeune(CompteBancaire):
    """Compte jeune avec limite"""
    
    def retirer(self, montant):
        """Override : limite à 500 par retrait"""
        # À compléter
        pass


# ============= EXERCICE 8 : COMPOSITION VS HÉRITAGE =============

class Moteur:
    """Classe Moteur (composition)"""
    
    def __init__(self, puissance, type_carburant):
        # À compléter
        pass
    
    def demarrer(self):
        """Démarre le moteur"""
        # À compléter
        pass


class VoitureAvecMoteur:
    """Voiture avec composition (contient un Moteur)"""
    
    def __init__(self, marque, moteur):
        # À compléter
        pass
    
    def demarrer(self):
        """Délègue au moteur"""
        # À compléter
        pass


class VoitureElectrique(VoitureAvecMoteur):
    """Voiture électrique"""
    
    def __init__(self, marque, puissance, autonomie_batterie):
        # À compléter
        pass


# ============= EXERCICE 9 : MÉTHODES DE CLASSE HÉRITÉES =============

class Produit:
    """Produit avec TVA"""
    tva = 0.20
    
    @classmethod
    def definir_tva(cls, nouveau_taux):
        """Définit le taux de TVA"""
        # À compléter
        pass
    
    def calculer_prix_ttc(self, prix_ht):
        """Calcule le prix TTC"""
        # À compléter
        pass


class ProduitReduit(Produit):
    """Produit à taux réduit"""
    tva = 0.055


# ============= EXERCICE 10 : MINI-PROJET RPG =============

class PersonnageRPG:
    """Classe de base pour personnages RPG"""
    
    def __init__(self, nom, points_vie, niveau):
        # À compléter
        pass
    
    def attaquer(self, cible):
        """Attaque de base"""
        # À compléter
        pass
    
    def recevoir_degats(self, degats):
        """Reçoit des dégâts"""
        # À compléter
        pass
    
    def est_vivant(self):
        """Vérifie si le personnage est vivant"""
        # À compléter
        pass
    
    def monter_niveau(self):
        """Monte d'un niveau"""
        # À compléter
        pass


class GuerrierRPG(PersonnageRPG):
    """Guerrier RPG"""
    
    def __init__(self, nom, points_vie, niveau, force):
        # À compléter
        pass
    
    def attaquer(self, cible):
        """Override : attaque avec force"""
        # À compléter
        pass
    
    def coup_puissant(self, cible):
        """Coup spécial puissant"""
        # À compléter
        pass


class MageRPG(PersonnageRPG):
    """Mage RPG"""
    
    def __init__(self, nom, points_vie, niveau, mana):
        # À compléter
        pass
    
    def attaquer(self, cible):
        """Override : attaque normale"""
        # À compléter
        pass
    
    def lancer_sort(self, cible):
        """Lance un sort (consomme mana)"""
        # À compléter
        pass
    
    def regenerer_mana(self):
        """Régénère le mana"""
        # À compléter
        pass


class ArcherRPG(PersonnageRPG):
    """Archer RPG"""
    
    def __init__(self, nom, points_vie, niveau, precision):
        # À compléter
        pass
    
    def attaquer(self, cible):
        """Override : peut rater selon précision"""
        # À compléter
        pass
    
    def tir_multiple(self, cibles):
        """Attaque plusieurs cibles"""
        # À compléter
        pass


# ============= EXERCICES BONUS =============

# Exercice 11 - Héritage multiple
class Volant:
    """Mixin pour voler"""
    
    def voler(self):
        """Vole dans les airs"""
        # À compléter
        pass


class Nageur:
    """Mixin pour nager"""
    
    def nager(self):
        """Nage dans l'eau"""
        # À compléter
        pass


class Canard(Volant, Nageur):
    """Canard avec héritage multiple"""
    
    def __init__(self, nom):
        # À compléter
        pass


# Exercice 12 - Duck typing
class Guitare:
    """Instrument : Guitare"""
    
    def jouer(self):
        """Joue de la guitare"""
        # À compléter
        pass


class Piano:
    """Instrument : Piano"""
    
    def jouer(self):
        """Joue du piano"""
        # À compléter
        pass


class Violon:
    """Instrument : Violon"""
    
    def jouer(self):
        """Joue du violon"""
        # À compléter
        pass


def concert(instruments):
    """Fonction polymorphe (duck typing)"""
    # À compléter
    pass


# Exercice 13 - Système de notifications
class Notification:
    """Classe parent pour notifications"""
    
    def envoyer(self, message):
        """À override"""
        # À compléter
        pass


class EmailNotification(Notification):
    """Notification par email"""
    
    def envoyer(self, message):
        """Override : envoie par email"""
        # À compléter
        pass


class SMSNotification(Notification):
    """Notification par SMS"""
    
    def envoyer(self, message):
        """Override : envoie par SMS"""
        # À compléter
        pass


class PushNotification(Notification):
    """Notification push"""
    
    def envoyer(self, message):
        """Override : envoie notification push"""
        # À compléter
        pass


# ============= TESTS =============

if __name__ == "__main__":
    print("=== Module 12 : Héritage et Polymorphisme ===\n")
    print("Testez vos classes ici !")
    
    # Exemple :
    # chien = Chien("Rex", 5, "Labrador")
    # chien.se_presenter()
    # chien.faire_bruit()
