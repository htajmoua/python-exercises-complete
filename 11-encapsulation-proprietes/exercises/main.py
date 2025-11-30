# Écrivez votre code ici !
# Consultez le fichier instructions.md pour les consignes

"""
Module 11 - Encapsulation et Propriétés
Concepts avancés de POO : protection des données et @property
"""

# ============= EXERCICES DE BASE =============

# Exercice 1 - Attributs protégés
class CompteBancaire:
    """Classe avec attributs protégés"""
    
    def __init__(self, titulaire, solde):
        # À compléter avec attributs protégés (_titulaire, _solde)
        pass
    
    def deposer(self, montant):
        """Dépose un montant sur le compte"""
        # À compléter
        pass
    
    def retirer(self, montant):
        """Retire un montant du compte"""
        # À compléter avec validation
        pass
    
    def consulter_solde(self):
        """Retourne le solde actuel"""
        # À compléter
        pass


# Exercice 2 - Getters et Setters manuels
class Temperature:
    """Classe avec getters/setters manuels"""
    
    def __init__(self, celsius=0):
        # À compléter avec attribut privé __celsius
        pass
    
    def get_celsius(self):
        """Retourne la température en Celsius"""
        # À compléter
        pass
    
    def set_celsius(self, valeur):
        """Définit la température en Celsius (validation >= -273.15)"""
        # À compléter
        pass
    
    def get_fahrenheit(self):
        """Retourne la température en Fahrenheit"""
        # À compléter (F = C × 9/5 + 32)
        pass
    
    def set_fahrenheit(self, valeur):
        """Définit la température via Fahrenheit"""
        # À compléter
        pass


# Exercice 3 - Décorateur @property (basique)
class Personne:
    """Classe avec @property"""
    
    def __init__(self):
        self._age = 0
    
    @property
    def age(self):
        """Getter pour l'âge"""
        # À compléter
        pass
    
    @age.setter
    def age(self, valeur):
        """Setter avec validation (0 <= age <= 150)"""
        # À compléter
        pass


# Exercice 4 - Properties avec calculs
class Rectangle:
    """Classe avec properties calculées"""
    
    def __init__(self, longueur, largeur):
        # À compléter avec attributs protégés
        pass
    
    @property
    def longueur(self):
        """Getter pour la longueur"""
        # À compléter
        pass
    
    @longueur.setter
    def longueur(self, valeur):
        """Setter avec validation (> 0)"""
        # À compléter
        pass
    
    @property
    def largeur(self):
        """Getter pour la largeur"""
        # À compléter
        pass
    
    @largeur.setter
    def largeur(self, valeur):
        """Setter avec validation (> 0)"""
        # À compléter
        pass
    
    @property
    def aire(self):
        """Property read-only : aire calculée"""
        # À compléter
        pass
    
    @property
    def perimetre(self):
        """Property read-only : périmètre calculé"""
        # À compléter
        pass


# Exercice 5 - Validation complexe
class Email:
    """Classe avec validation complexe"""
    
    def __init__(self, adresse=""):
        # À compléter avec attribut privé __adresse
        pass
    
    @property
    def adresse(self):
        """Getter pour l'adresse email"""
        # À compléter
        pass
    
    @adresse.setter
    def adresse(self, valeur):
        """Setter avec validation (contient @, ., pas d'espaces, min 5 caractères)"""
        # À compléter - lever ValueError si invalide
        pass


# Exercice 6 - Property read-only (calculée)
class Produit:
    """Classe avec property calculée read-only"""
    
    def __init__(self, nom, prix_ht, tva=0.20):
        # À compléter
        pass
    
    @property
    def prix_ttc(self):
        """Property read-only : calcule prix_ht × (1 + tva)"""
        # À compléter
        pass


# Exercice 7 - Encapsulation avec méthodes privées
class MotDePasse:
    """Classe avec méthode privée"""
    
    def __init__(self):
        # À compléter avec attribut privé __hash
        pass
    
    def __hasher(self, texte):
        """Méthode privée : simule un hash (inverser le texte)"""
        # À compléter
        pass
    
    def definir(self, mdp):
        """Définit le mot de passe (validation 8+ caractères)"""
        # À compléter
        pass
    
    def verifier(self, mdp):
        """Vérifie si le mot de passe correspond"""
        # À compléter
        pass


# Exercice 8 - Propriété avec cache
class Calcul:
    """Classe avec property et cache"""
    
    def __init__(self, nombre):
        self._nombre = nombre
        self.__cache_factorielle = None
    
    @property
    def nombre(self):
        """Getter pour nombre"""
        # À compléter
        pass
    
    @nombre.setter
    def nombre(self, valeur):
        """Setter qui invalide le cache"""
        # À compléter
        pass
    
    @property
    def factorielle(self):
        """Property avec cache : calcule la factorielle"""
        # À compléter
        pass


# Exercice 9 - Classe avec validation multiple
class Utilisateur:
    """Classe avec multiples validations"""
    
    def __init__(self):
        # À compléter avec attributs protégés
        pass
    
    @property
    def nom(self):
        """Getter pour nom"""
        # À compléter
        pass
    
    @nom.setter
    def nom(self, valeur):
        """Setter avec validation (2-50 caractères, pas de chiffres)"""
        # À compléter
        pass
    
    @property
    def age(self):
        """Getter pour age"""
        # À compléter
        pass
    
    @age.setter
    def age(self, valeur):
        """Setter avec validation (13-120 ans)"""
        # À compléter
        pass
    
    @property
    def email(self):
        """Getter pour email"""
        # À compléter
        pass
    
    @email.setter
    def email(self, valeur):
        """Setter avec validation (format valide)"""
        # À compléter
        pass
    
    @property
    def telephone(self):
        """Getter pour telephone"""
        # À compléter
        pass
    
    @telephone.setter
    def telephone(self, valeur):
        """Setter avec validation (10 chiffres exactement)"""
        # À compléter
        pass
    
    def afficher_profil(self):
        """Affiche toutes les informations"""
        # À compléter
        pass


# ============= EXERCICE 10 : MINI-PROJET =============

class CarteBancaire:
    """Mini-projet : Carte bancaire sécurisée"""
    
    def __init__(self, numero, code, solde):
        # À compléter avec attributs privés
        pass
    
    @property
    def numero_masque(self):
        """Property read-only : affiche **** **** **** 1234"""
        # À compléter
        pass
    
    @property
    def solde(self):
        """Getter pour solde"""
        # À compléter
        pass
    
    @solde.setter
    def solde(self, valeur):
        """Setter avec validation (>= 0)"""
        # À compléter
        pass
    
    def valider_code(self, code):
        """Vérifie si le code est correct"""
        # À compléter
        pass
    
    def payer(self, montant, code):
        """Effectue un paiement (vérifie code et solde)"""
        # À compléter
        pass


# ============= EXERCICES BONUS =============

# Exercice 11 - Property avec délégation
class Moteur:
    """Classe auxiliaire pour l'exercice 11"""
    
    def __init__(self, puissance):
        # À compléter
        pass


class Voiture:
    """Bonus : Property avec délégation"""
    
    def __init__(self, marque, puissance_moteur):
        # À compléter
        pass
    
    @property
    def puissance(self):
        """Property qui délègue à moteur.puissance"""
        # À compléter
        pass


# Exercice 12 - Classe immuable
class Point:
    """Bonus : Classe immuable"""
    
    def __init__(self, x, y):
        # À compléter avec attributs privés
        pass
    
    @property
    def x(self):
        """Property read-only pour x"""
        # À compléter
        pass
    
    @property
    def y(self):
        """Property read-only pour y"""
        # À compléter
        pass
    
    def deplacer(self, dx, dy):
        """Retourne un nouveau Point (ne modifie pas l'actuel)"""
        # À compléter
        pass


# Exercice 13 - Validation en chaîne
class FormulaireInscription:
    """Bonus : Formulaire avec validation complète"""
    
    def __init__(self):
        # À compléter
        pass
    
    @property
    def nom(self):
        # À compléter
        pass
    
    @nom.setter
    def nom(self, valeur):
        # À compléter avec validation
        pass
    
    @property
    def prenom(self):
        # À compléter
        pass
    
    @prenom.setter
    def prenom(self, valeur):
        # À compléter avec validation
        pass
    
    @property
    def age(self):
        # À compléter
        pass
    
    @age.setter
    def age(self, valeur):
        # À compléter avec validation
        pass
    
    @property
    def email(self):
        # À compléter
        pass
    
    @email.setter
    def email(self, valeur):
        # À compléter avec validation
        pass
    
    @property
    def telephone(self):
        # À compléter
        pass
    
    @telephone.setter
    def telephone(self, valeur):
        # À compléter avec validation
        pass
    
    def est_valide(self):
        """Retourne True si tous les champs sont valides"""
        # À compléter
        pass
    
    @property
    def erreurs(self):
        """Retourne la liste des erreurs de validation"""
        # À compléter
        pass


# ============= TESTS =============

if __name__ == "__main__":
    print("=== Module 11 : Encapsulation et Propriétés ===\n")
    print("Testez vos classes ici !")
    
    # Exemple :
    # compte = CompteBancaire("Alice", 1000)
    # compte.deposer(500)
    # print(compte.consulter_solde())
