"""
Module 15 - Django Models et ORM
Fichier de test pour les exercices

Ce fichier est un template pour tester vos modèles et requêtes.
Utilisez le shell Django pour exécuter ce code :
    python manage.py shell < main.py

Ou copiez-collez les sections dans le shell interactif :
    python manage.py shell
"""

# ============= IMPORTS =============

from django.db import models
from django.db.models import Q, F, Count, Sum, Avg, Max, Min, Case, When, Value
from django.db.models.functions import Concat, Upper, Lower, TruncMonth
from django.utils import timezone
from datetime import timedelta

# Vos imports de modèles
# from blog.models import Article, Auteur, Tag, Categorie, Commentaire, Like


# ============= PARTIE 1 : CRÉATION DE DONNÉES DE TEST =============

def creer_donnees_test():
    """Créer des données de test pour les exercices"""
    pass
    # Exemple :
    # auteur = Auteur.objects.create(
    #     nom="Dupont",
    #     prenom="Jean",
    #     email="jean@example.com"
    # )
    # 
    # tag_python = Tag.objects.create(nom="Python", slug="python")
    # tag_django = Tag.objects.create(nom="Django", slug="django")
    # 
    # article = Article.objects.create(
    #     titre="Introduction à Django",
    #     contenu="Django est un framework..." * 20,
    #     auteur=auteur,
    #     publie=True
    # )
    # article.tags.add(tag_python, tag_django)


# ============= PARTIE 2 : QUERYSETS BASIQUES =============

def test_querysets_basiques():
    """Tester les requêtes basiques"""
    pass
    # # Tous les articles
    # articles = Article.objects.all()
    # print(f"Nombre total d'articles : {articles.count()}")
    # 
    # # Articles publiés
    # publies = Article.objects.filter(publie=True)
    # print(f"Articles publiés : {publies.count()}")
    # 
    # # Premier article
    # premier = Article.objects.first()
    # print(f"Premier article : {premier.titre if premier else 'Aucun'}")


# ============= PARTIE 3 : RELATIONS =============

def test_relations():
    """Tester les relations entre modèles"""
    pass
    # # Articles d'un auteur
    # auteur = Auteur.objects.first()
    # if auteur:
    #     articles = auteur.articles.all()
    #     print(f"{auteur.nom} a {articles.count()} article(s)")
    # 
    # # Filtrer par relation
    # articles_dupont = Article.objects.filter(auteur__nom="Dupont")
    # print(f"Articles de Dupont : {articles_dupont.count()}")


# ============= PARTIE 4 : OPTIMISATION =============

def test_optimisation():
    """Tester les techniques d'optimisation"""
    pass
    # from django.db import connection, reset_queries
    # 
    # # Sans optimisation (N+1 queries)
    # reset_queries()
    # articles = Article.objects.all()[:10]
    # for article in articles:
    #     print(f"{article.titre} par {article.auteur.nom}")
    # print(f"Requêtes sans optimisation : {len(connection.queries)}")
    # 
    # # Avec select_related
    # reset_queries()
    # articles = Article.objects.select_related('auteur').all()[:10]
    # for article in articles:
    #     print(f"{article.titre} par {article.auteur.nom}")
    # print(f"Requêtes avec select_related : {len(connection.queries)}")


# ============= PARTIE 5 : AGRÉGATION =============

def test_agregation():
    """Tester les agrégations"""
    pass
    # # Statistiques globales
    # stats = Article.objects.aggregate(
    #     total=Count('id'),
    #     vues_totales=Sum('nombre_vues'),
    #     vues_moyenne=Avg('nombre_vues'),
    #     max_vues=Max('nombre_vues')
    # )
    # print(f"Statistiques : {stats}")
    # 
    # # Auteurs avec nombre d'articles
    # auteurs = Auteur.objects.annotate(
    #     nb_articles=Count('articles')
    # ).filter(nb_articles__gt=0)
    # 
    # for auteur in auteurs:
    #     print(f"{auteur.nom} : {auteur.nb_articles} article(s)")


# ============= PARTIE 6 : Q OBJECTS =============

def test_q_objects():
    """Tester les requêtes complexes avec Q"""
    pass
    # # OR
    # articles = Article.objects.filter(
    #     Q(publie=True) | Q(featured=True)
    # )
    # print(f"Articles publiés OU featured : {articles.count()}")
    # 
    # # AND et NOT
    # articles = Article.objects.filter(
    #     Q(publie=True) & ~Q(auteur__nom="Dupont")
    # )
    # print(f"Articles publiés mais pas de Dupont : {articles.count()}")


# ============= PARTIE 7 : F EXPRESSIONS =============

def test_f_expressions():
    """Tester les F expressions"""
    pass
    # # Incrémenter les vues (atomique)
    # Article.objects.filter(id=1).update(nombre_vues=F('nombre_vues') + 1)
    # 
    # # Comparer des champs
    # articles = Article.objects.filter(nombre_vues__gt=F('nombre_likes') * 10)
    # print(f"Articles avec vues > 10x likes : {articles.count()}")


# ============= PARTIE 8 : BULK OPERATIONS =============

def test_bulk_operations():
    """Tester les opérations en masse"""
    pass
    # # bulk_create
    # articles = [
    #     Article(
    #         titre=f"Article {i}",
    #         contenu="Contenu..." * 20,
    #         auteur=Auteur.objects.first()
    #     )
    #     for i in range(100)
    # ]
    # Article.objects.bulk_create(articles, batch_size=50)
    # print(f"100 articles créés en masse")
    # 
    # # update en masse
    # updated = Article.objects.filter(publie=False).update(publie=True)
    # print(f"{updated} articles mis à jour")


# ============= PARTIE 9 : TRANSACTIONS =============

def test_transactions():
    """Tester les transactions"""
    pass
    # from django.db import transaction
    # 
    # with transaction.atomic():
    #     article = Article.objects.create(
    #         titre="Test Transaction",
    #         contenu="Contenu..." * 20,
    #         auteur=Auteur.objects.first()
    #     )
    #     article.tags.add(*Tag.objects.all()[:3])
    #     # Si erreur ici, tout est rollback
    #     print("Transaction réussie")


# ============= PARTIE 10 : MANAGERS PERSONNALISÉS =============

def test_managers():
    """Tester les managers personnalisés"""
    pass
    # # Manager par défaut
    # tous = Article.objects.all().count()
    # print(f"Tous les articles : {tous}")
    # 
    # # Manager personnalisé
    # publies = Article.publies.all().count()
    # print(f"Articles publiés : {publies}")
    # 
    # # Manager avec méthodes chainables
    # featured = Article.objects.publies().featured().count()
    # print(f"Articles publiés ET featured : {featured}")


# ============= EXÉCUTION DES TESTS =============

if __name__ == "__main__":
    print("=" * 60)
    print("Module 15 - Tests Django ORM")
    print("=" * 60)
    
    # Décommentez les fonctions que vous voulez tester
    
    # print("\n1. Création de données de test...")
    # creer_donnees_test()
    
    # print("\n2. QuerySets basiques...")
    # test_querysets_basiques()
    
    # print("\n3. Relations...")
    # test_relations()
    
    # print("\n4. Optimisation...")
    # test_optimisation()
    
    # print("\n5. Agrégation...")
    # test_agregation()
    
    # print("\n6. Q Objects...")
    # test_q_objects()
    
    # print("\n7. F Expressions...")
    # test_f_expressions()
    
    # print("\n8. Bulk Operations...")
    # test_bulk_operations()
    
    # print("\n9. Transactions...")
    # test_transactions()
    
    # print("\n10. Managers...")
    # test_managers()
    
    print("\n" + "=" * 60)
    print("Tests terminés !")
    print("=" * 60)
