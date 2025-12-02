# Fichier avec des problèmes que Ruff va détecter

import os  # Import inutilisé
import sys  # Import inutilisé
from typing import List
import json  # Import inutilisé


def calculer_somme(nombres: List[int]) -> int:
    """Calcule la somme d'une liste de nombres"""
    total = 0
    for nombre in nombres:
        total += nombre
    return total


def verifier_age(age):
    """Vérifie si l'âge est valide"""
    # Variable non utilisée
    age_minimum = 18
    age_maximum = 120
    
    if age < 0:
        print("L'âge ne peut pas être négatif")
        return False
    elif age > 150:
        print("L'âge semble irréaliste")
        return False
    else:
        return True


def diviser(a, b):
    """Division avec gestion d'erreur"""
    try:
        resultat = a / b
        return resultat
    except ZeroDivisionError:
        print("Division par zéro!")
        return None
    except:  # Bare except (mauvaise pratique)
        print("Erreur inconnue")
        return None


def fonction_avec_code_mort():
    """Fonction avec du code mort (unreachable)"""
    x = 10
    
    if x > 5:
        return "Grand"
    else:
        return "Petit"
    
    # Code mort - jamais exécuté
    print("Ce code ne sera jamais exécuté")
    x = 20


# Variable globale non utilisée
CONSTANTE_INUTILISEE = 42


def fonction_complexe(data):
    """Fonction trop complexe (complexité cyclomatique élevée)"""
    if data is None:
        return None
    
    if len(data) == 0:
        return []
    
    if len(data) == 1:
        return data[0]
    
    if len(data) == 2:
        return data[0] + data[1]
    
    if len(data) == 3:
        return data[0] + data[1] + data[2]
    
    if len(data) > 3:
        if data[0] > 0:
            if data[1] > 0:
                if data[2] > 0:
                    return sum(data)
    
    return None


def comparaison_incorrecte(value):
    """Comparaisons problématiques"""
    # Comparaison avec True/False (anti-pattern)
    if value == True:
        return "Vrai"
    
    if value == False:
        return "Faux"
    
    # Comparaison avec None (devrait utiliser 'is')
    if value == None:
        return "None"
    
    return "Autre"


# Lambda inutilement complexe
calculer = lambda x, y, z: x + y + z if x > 0 and y > 0 and z > 0 else 0


def fonction_avec_mutable_default(items=[]):  # Mutable default argument
    """Argument par défaut mutable (bug classique)"""
    items.append(1)
    return items


# F-string non utilisé correctement
nom = "Alice"
message = "Bonjour %s" % nom  # Devrait utiliser f-string


# Print statement (devrait utiliser logging)
def traiter_donnees(data):
    print(f"Traitement de {len(data)} éléments")  # Devrait utiliser logging
    return [x * 2 for x in data]


# Nom de variable non conforme PEP8
MaVariable = 10  # Devrait être ma_variable
AUTRECONSTANTE = 20  # Ok pour constante mais manque underscore


# Fonction jamais utilisée
def fonction_inutilisee():
    """Cette fonction n'est jamais appelée"""
    return "Je ne sers à rien"
