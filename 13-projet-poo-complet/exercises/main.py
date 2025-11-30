# Écrivez votre code ici !
# Consultez le fichier instructions.md pour les consignes

"""
Choisissez un des 4 projets proposés :
1. Système de gestion de bibliothèque
2. Système de gestion d'école
3. Système de e-commerce
4. Jeu de combat RPG

Implémentez toutes les classes demandées avec :
- Encapsulation (attributs protégés/privés)
- Properties avec validation
- Héritage et polymorphisme
- Méthodes spéciales (__str__, __repr__, etc.)
- Documentation (docstrings)
"""

# Exemple de structure pour le Projet 1 - Bibliothèque

class Livre:
    """Représente un livre dans la bibliothèque."""
    
    def __init__(self, titre, auteur, isbn):
        # À compléter
        pass
    
    def __str__(self):
        # À compléter
        pass


class Membre:
    """Représente un membre de la bibliothèque."""
    prochain_numero = 1
    
    def __init__(self, nom):
        # À compléter
        pass


class Emprunt:
    """Représente un emprunt de livre."""
    
    def __init__(self, livre, membre, date_emprunt, date_retour_prevue):
        # À compléter
        pass
    
    def calculer_penalite(self):
        # À compléter
        pass


class Bibliotheque:
    """Gère l'ensemble de la bibliothèque."""
    
    def __init__(self, nom):
        # À compléter
        pass
    
    def emprunter_livre(self, isbn, numero_membre):
        # À compléter
        pass
    
    def retourner_livre(self, isbn, numero_membre):
        # À compléter
        pass


# Script de démonstration
if __name__ == "__main__":
    # Créez un scénario complet de démonstration
    # Exemple :
    # biblio = Bibliotheque("Bibliothèque Centrale")
    # ...
    pass
