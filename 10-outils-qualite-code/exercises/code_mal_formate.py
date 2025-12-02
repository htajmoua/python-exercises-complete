# Fichier intentionnellement mal formaté
# À formatter avec Black

def calculer_moyenne(notes):
    """Calcule la moyenne d'une liste de notes"""
    if len(notes)==0:return 0
    return sum( notes )/len( notes )

def filtrer_notes_sup(notes,seuil):
    return [ note for note in notes if note>=seuil ]


class Etudiant:
    def __init__(self,nom,prenom,age,notes):
        self.nom=nom
        self.prenom=prenom
        self.age=age
        self.notes=notes
    
    def moyenne(self):
        return calculer_moyenne(self.notes)
    
    def meilleure_note(self): return max(self.notes) if self.notes else 0
    
    def __str__(self):
        return f'{self.prenom} {self.nom} ({self.age} ans) - Moyenne: {self.moyenne():.2f}'


# Dictionnaire mal formaté
etudiants_data={'Alice':{'notes':[15,17,14],'age':20},'Bob':{'notes':[12,13,11],'age':21},'Charlie':{'notes':[18,19,17],'age':19}}

# Liste mal formatée
matieres=['Mathématiques','Physique','Chimie','Informatique','Anglais']

# Ligne trop longue
description = "Ceci est une très longue ligne qui dépasse largement la limite recommandée de 79 ou 88 caractères et qui devrait être reformatée par Black pour respecter les conventions de style Python."


def fonction_avec_beaucoup_arguments(arg1,arg2,arg3,arg4,arg5,arg6,arg7,arg8):
    """Fonction avec trop d'arguments sur une ligne"""
    return arg1+arg2+arg3+arg4+arg5+arg6+arg7+arg8


# Strings avec différents types de quotes
message1='Hello'
message2="World"
message3='''Long
message'''

# Opérateurs mal espacés
resultat=10+20*30-5/2
comparaison=resultat>100 and resultat<500

# Imports mal triés (à ne pas mettre en haut normalement, juste pour l'exemple)
import sys
from os import path
import re
from typing import List, Dict
import json
