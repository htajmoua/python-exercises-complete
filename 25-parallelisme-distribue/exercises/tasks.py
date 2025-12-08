"""
Fichier tasks.py - Exercices Celery (Exercices 8 à 12)

Ce fichier contient la structure et les hints pour compléter les exercices Celery.
Suivez les instructions dans instructions.md pour chaque exercice.

Astuce : Décommentez progressivement le code en complétant chaque exercice !
"""

# ========================================
# Exercice 8 - Première tâche Celery
# ========================================
#
# Objectif : Créer deux tâches de base
#
# TODO 1: Importer l'application Celery
# from celery_app import app
# import time
#
# TODO 2: Créer la tâche addition
# @app.task
# def addition(x, y):
#     """Additionne deux nombres"""
#     # TODO: Retourner x + y
#
# TODO 3: Créer la tâche tache_longue
# @app.task
# def tache_longue(duree):
#     """Simule une tâche longue"""
#     # TODO: Utiliser time.sleep(duree)
#     # TODO: Retourner un message avec la durée


# ========================================
# Exercice 9 - Chaînes de tâches
# ========================================
#
# Objectif : Créer une tâche multiplication pour les chaînes
#
# TODO: Créer la tâche multiplication
# @app.task
# def multiplication(x, y):
#     """Multiplie deux nombres"""
#     # TODO: Retourner x * y


# ========================================
# Exercice 10 - Groupes de tâches
# ========================================
#
# Note : Vous utiliserez les tâches déjà créées (addition, multiplication)
#        avec group() pour les exécuter en parallèle.
#
# Pas de nouvelle tâche à créer pour cet exercice !


# ========================================
# Exercice 11 - Map-Reduce avec Celery
# ========================================
#
# Objectif : Implémenter Map-Reduce distribué
#
# TODO 1: Créer la tâche map_task
# @app.task
# def map_task(data):
#     """
#     Map : Transforme une portion des données
#     
#     Args:
#         data (list): Une portion des données (ex: [1, 2, 3, 4, 5])
#     
#     Returns:
#         list: Les données transformées (ex: [1, 4, 9, 16, 25])
#     """
#     # TODO: Calculer le carré de chaque nombre et retourner la liste
#
# TODO 2: Créer la tâche reduce_task
# @app.task
# def reduce_task(results):
#     """
#     Reduce : Combine tous les résultats
#     
#     Args:
#         results (list): Liste de listes [[1,4,9], [16,25,36], ...]
#     
#     Returns:
#         int: La somme totale
#     """
#     # TODO: Aplatir la liste de listes
#     # TODO: Calculer et retourner la somme totale


# ========================================
# Exercice 12 - Pipeline de traitement
# ========================================
#
# Objectif : Créer un pipeline de traitement de fichier
#
# TODO 1: Créer la tâche lire_fichier
# @app.task
# def lire_fichier(filepath):
#     """
#     Étape 1 : Lire le fichier
#     
#     Args:
#         filepath (str): Chemin du fichier
#     
#     Returns:
#         str: Contenu du fichier
#     """
#     # TODO: Ouvrir et lire le fichier
#     # TODO: Retourner le contenu
#
# TODO 2: Créer la tâche traiter_texte
# @app.task
# def traiter_texte(texte):
#     """
#     Étape 2 : Analyser le texte
#     
#     Args:
#         texte (str): Le contenu du fichier
#     
#     Returns:
#         dict: Statistiques du texte
#     """
#     # TODO: Découper le texte en mots
#     # TODO: Retourner un dictionnaire avec:
#     #       - nombre_mots
#     #       - nombre_lignes  
#     #       - mots_uniques
#
# TODO 3: Créer la tâche sauvegarder_resultats
# @app.task
# def sauvegarder_resultats(stats):
#     """
#     Étape 3 : Sauvegarder les statistiques
#     
#     Args:
#         stats (dict): Dictionnaire des statistiques
#     
#     Returns:
#         str: Message de confirmation
#     """
#     # TODO: Ouvrir 'resultats.txt' en écriture
#     # TODO: Écrire chaque statistique sur une ligne
#     # TODO: Retourner un message de confirmation


if __name__ == '__main__':
    print("=" * 70)
    print("Fichier tasks.py - Exercices Celery")
    print("=" * 70)
    print()
    print("Instructions :")
    print("   1. Décommentez progressivement le code pour chaque exercice")
    print("   2. Complétez les TODOs marqués dans le code")
    print("   3. Consultez instructions.md pour les détails")
    print()
    print("Pour lancer le worker Celery :")
    print("   celery -A tasks worker --loglevel=info")
    print()
    print("Pour tester vos tâches :")
    print("   python  # Lancer Python interactif")
    print("   >>> from tasks import addition")
    print("   >>> result = addition.delay(4, 6)")
    print("   >>> print(result.get())")
    print()
    print("=" * 70)
