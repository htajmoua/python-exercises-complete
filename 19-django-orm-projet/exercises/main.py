"""
Module 18 - Django ORM : Projet Complet
Projet fil rouge - Système de blog professionnel

Ce module est un projet complet qui intègre TOUTES les techniques vues.
"""

# ============= IMPORTS =============

from django.db import models
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError
from django.utils import timezone
from django.db.models import Q, F, Count

# Vos modèles sont définis dans blog/models.py
# from blog.models import Article, Auteur, Categorie, Tag, Commentaire, Like


# ============= EXERCICE 41 : PROJET COMPLET =============

def creer_donnees_test_projet():
    """Créer un jeu de données complet pour le projet"""
    pass
    # # Créer des auteurs
    # user1 = User.objects.create_user('jean', 'jean@example.com', 'password')
    # auteur1 = Auteur.objects.create(...)
    # 
    # # Créer des catégories
    # cat_tech = Categorie.objects.create(nom="Technologie", slug="tech")
    # 
    # # Créer des tags
    # tag_python = Tag.objects.create(nom="Python", slug="python")
    # 
    # # Créer des articles
    # article = Article.objects.create(...)
    # article.tags.add(tag_python)


def test_querysets_optimises():
    """Tester les requêtes optimisées du projet"""
    pass
    # # Récupérer articles avec stats
    # articles = Article.objects.avec_stats().optimise()
    # 
    # for article in articles:
    #     print(f"{article.titre}: {article.nb_commentaires} commentaires")


def test_managers_personnalises():
    """Tester les managers du projet"""
    pass
    # # Articles publiés
    # Article.objects.publies()
    # 
    # # Articles featured
    # Article.objects.featured()
    # 
    # # Chainable
    # Article.objects.publies().avec_stats().optimise()


def test_validation_modeles():
    """Tester la validation des modèles"""
    pass
    # article = Article(titre="Test", contenu="Court")
    # try:
    #     article.full_clean()
    # except ValidationError as e:
    #     print(f"Erreurs : {e.message_dict}")


def test_signals():
    """Tester les signals du projet"""
    pass
    # # Publier un article déclenche des signals
    # article = Article.objects.first()
    # article.publie = True
    # article.save()  # Signal post_save appelé


def test_transactions():
    """Tester les transactions complexes"""
    pass
    # from django.db import transaction
    # 
    # with transaction.atomic():
    #     # Créer article + mettre à jour stats auteur
    #     article = Article.objects.create(...)
    #     article.auteur.mettre_a_jour_stats()


def generer_rapport_statistiques():
    """Générer un rapport complet"""
    pass
    # # Statistiques générales
    # total_articles = Article.objects.count()
    # articles_publies = Article.objects.publies().count()
    # 
    # # Top auteurs
    # top_auteurs = Auteur.objects.annotate(
    #     nb=Count('articles')
    # ).order_by('-nb')[:10]
    # 
    # # Articles populaires
    # populaires = Article.objects.populaires(10)
    # 
    # return {
    #     'total': total_articles,
    #     'publies': articles_publies,
    #     'auteurs': list(top_auteurs),
    #     'populaires': list(populaires)
    # }


# ============= TESTS UNITAIRES =============

def run_tests():
    """Lancer les tests du projet"""
    pass
    # from django.test import TestCase
    # python manage.py test blog


# ============= EXÉCUTION =============

if __name__ == "__main__":
    print("=" * 60)
    print("Module 18 - Projet ORM Complet")
    print("=" * 60)
    
    print("\n🚀 Projet prêt !")
    print("\nÉtapes suivantes :")
    print("1. Créer les modèles dans blog/models.py")
    print("2. Créer les migrations : python manage.py makemigrations")
    print("3. Appliquer les migrations : python manage.py migrate")
    print("4. Créer des données de test")
    print("5. Tester les fonctionnalités")
    print("6. Écrire les tests unitaires")
    
    print("\n✅ Bon courage !")
