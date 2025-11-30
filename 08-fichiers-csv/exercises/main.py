# Écrivez votre code ici !

"""
Module 08 - Fichiers CSV
Exercices sur la manipulation de fichiers CSV - Système de bibliothèque
"""

import csv


# ============= EXERCICE 1 : EXTRACTION =============

def extract():
    """
    Exercice 1 : Lire le fichier input.csv
    
    Retourne une liste de dictionnaires avec les colonnes :
    - titre : titre du livre
    - jours_emprunt : nombre de jours d'emprunt
    """
    # À compléter
    # Conseil : utilisez csv.DictReader
    pass


# ============= EXERCICE 2 : TRANSFORMATION =============

def transform(data):
    """
    Exercice 2 : Transformer les données et calculer les frais
    
    Paramètres :
    - data : liste de dictionnaires avec titre et jours_emprunt
    
    Retourne une liste de dictionnaires avec :
    - titre : titre du livre
    - frais : frais de retard calculés
    
    Règles de calcul :
    - Si jours_emprunt <= 14 : frais = 0
    - Si jours_emprunt > 14 : frais = (jours_emprunt - 14) × 0.50
    """
    # À compléter
    pass


def load(data):
    """
    Exercice 2 (suite) : Charger les données dans output.csv
    
    Paramètres :
    - data : liste de dictionnaires avec titre et frais
    
    Crée un fichier output.csv avec les données transformées
    """
    # À compléter
    # Conseil : utilisez csv.DictWriter
    pass


# ============= EXERCICE 3 : ORCHESTRATION =============

def main():
    """
    Exercice 3 : Fonction principale qui orchestre le processus ETL
    
    Appelle dans l'ordre :
    1. extract() pour lire les données
    2. transform() pour calculer les frais
    3. load() pour sauvegarder le résultat
    """
    # À compléter
    pass


# ============= EXERCICE 4 : AJOUT STATUT =============

def transform_avec_statut(data):
    """
    Exercice 4 : Transformer les données avec ajout du statut
    
    Paramètres :
    - data : liste de dictionnaires avec titre et jours_emprunt
    
    Retourne une liste de dictionnaires avec :
    - titre : titre du livre
    - frais : frais de retard calculés
    - statut : "À temps" si frais = 0, "En retard" sinon
    """
    # À compléter
    pass


# ============= EXERCICE 5 : STATISTIQUES (BONUS) =============

def statistiques():
    """
    Bonus : Afficher des statistiques sur output.csv
    
    Lit le fichier output.csv et affiche :
    - Le nombre total de livres
    - Le montant total des frais
    - Le nombre de livres en retard
    """
    # À compléter
    pass


# ============= TESTS =============

if __name__ == "__main__":
    print("=== Module 08 : Fichiers CSV ===\n")
    print("Testez vos fonctions ici !")
    
    # Décommentez pour tester :
    # main()
    # statistiques()
