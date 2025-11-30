# Écrivez votre code ici !
# Consultez le fichier instructions.md pour les consignes

"""
Module 09 - Expressions Régulières et Bases de Données
Exercices sur regex et SQLite
"""

import re
import sqlite3
from datetime import datetime
import os

# ============= PARTIE 1 : EXPRESSIONS RÉGULIÈRES =============

# Exercice 1 : Validation
def valider_email(email):
    """Valide une adresse email"""
    # À compléter
    pass


def valider_telephone(telephone):
    """Valide un numéro de téléphone français"""
    # Formats acceptés: 06 12 34 56 78, 06-12-34-56-78, 0612345678
    # À compléter
    pass


def valider_code_postal(code_postal):
    """Valide un code postal français (5 chiffres)"""
    # À compléter
    pass


def valider_date(date_str):
    """Valide une date au format JJ/MM/AAAA"""
    # À compléter
    pass


# Exercice 2 : Extraction
def extraire_emails(texte):
    """Extrait tous les emails d'un texte"""
    # À compléter
    pass


def extraire_telephones(texte):
    """Extrait tous les numéros de téléphone"""
    # À compléter
    pass


def extraire_urls(texte):
    """Extrait toutes les URLs"""
    # À compléter
    pass


# Exercice 3 : Remplacement
def masquer_carte_bancaire(numero):
    """Masque un numéro de carte bancaire"""
    # Garde seulement les 4 derniers chiffres
    # À compléter
    pass


def nettoyer_texte(texte):
    """Supprime les caractères spéciaux"""
    # À compléter
    pass


def convertir_date_format(date_str):
    """Convertit JJ/MM/AAAA en AAAA-MM-JJ"""
    # À compléter
    pass


# Exercice 4 : Validation de mot de passe
def valider_mot_de_passe(mdp):
    """
    Vérifie qu'un mot de passe contient:
    - Au moins 8 caractères
    - Au moins une majuscule
    - Au moins une minuscule
    - Au moins un chiffre
    - Au moins un caractère spécial
    """
    # À compléter
    pass


# Exercice 5 : Parsing de logs
def parser_log(ligne_log):
    """Parse une ligne de log"""
    # À compléter
    pass


def extraire_ips(texte):
    """Extrait les adresses IP d'un texte"""
    # À compléter
    pass


# ============= PARTIE 2 : BASE DE DONNÉES SQLITE =============

class BibliothequeDB:
    """Classe pour gérer la base de données de la bibliothèque"""
    
    def __init__(self, db_name='bibliotheque.db'):
        """Initialise la connexion à la base de données"""
        self.db_name = db_name
        self.conn = None
        self.cursor = None
    
    def connecter(self):
        """Établit la connexion à la base de données"""
        self.conn = sqlite3.connect(self.db_name)
        self.cursor = self.conn.cursor()
        self.cursor.execute("PRAGMA foreign_keys = ON")
    
    def deconnecter(self):
        """Ferme la connexion"""
        if self.conn:
            self.conn.close()
    
    def creer_tables(self):
        """Crée les tables de la bibliothèque"""
        # À compléter
        # Créer 3 tables : auteurs, livres, emprunts
        pass
    
    def inserer_donnees_exemple(self):
        """Insère des données d'exemple"""
        # À compléter
        # Insérer des auteurs, livres et emprunts
        pass
    
    # Exercice 7 : Ajouter des données
    def ajouter_auteur(self, nom, prenom, date_naissance=None, nationalite=None):
        """Ajoute un auteur"""
        # À compléter
        pass
    
    def ajouter_livre(self, titre, auteur_id, annee=None, isbn=None, genre=None):
        """Ajoute un livre"""
        # À compléter
        pass
    
    # Exercice 8 : Requêtes SELECT
    def afficher_tous_livres(self):
        """Affiche tous les livres"""
        # À compléter
        pass
    
    def livres_par_auteur(self, auteur_id):
        """Affiche les livres d'un auteur"""
        # À compléter
        pass
    
    def livres_apres_annee(self, annee):
        """Livres publiés après une année"""
        # À compléter
        pass
    
    def emprunts_en_cours(self):
        """Emprunts actuellement en cours"""
        # À compléter
        pass
    
    # Exercice 9 : Jointures
    def livres_avec_auteurs(self):
        """Livres avec nom de l'auteur"""
        # À compléter
        pass
    
    def emprunts_avec_details(self):
        """Emprunts avec détails du livre et auteur"""
        # À compléter
        pass
    
    # Exercice 10 : UPDATE et DELETE
    def retourner_livre(self, emprunt_id, date_retour=None):
        """Marque un emprunt comme retourné"""
        # À compléter
        pass
    
    def supprimer_livre(self, livre_id):
        """Supprime un livre"""
        # À compléter
        pass
    
    def modifier_auteur(self, auteur_id, **kwargs):
        """Modifie les informations d'un auteur"""
        # À compléter
        pass
    
    # Exercice 12 : Recherche avec regex
    def rechercher_livres_regex(self, pattern, champ='titre'):
        """Recherche des livres avec une expression régulière"""
        # À compléter
        pass
    
    # Statistiques
    def afficher_statistiques(self):
        """Affiche des statistiques"""
        # À compléter
        pass


# ============= TESTS =============

def test_regex():
    """Tests des fonctions regex"""
    # À compléter
    # Testez vos fonctions regex ici
    pass


def test_database():
    """Tests de la base de données"""
    # À compléter
    # Testez vos fonctions de base de données ici
    pass


if __name__ == "__main__":
    print("=== Module 09 : Regex et Base de Données ===\n")
    print("Testez vos fonctions ici !")
    
    # Décommentez pour tester :
    # test_regex()
    # test_database()
