"""
Module 16 - Django ORM : QuerySets et Optimisation
Fichier de test pour les exercices

Utilisez le shell Django pour tester vos requêtes :
    python manage.py shell
"""

# ============= IMPORTS =============

from django.db import models, connection, reset_queries
from django.db.models import Q, F, Count, Sum, Avg, Max, Min, Case, When, Value
from django.db.models.functions import Concat, Upper, Lower, TruncMonth
from django.utils import timezone
from datetime import timedelta

# Vos imports de modèles
# from blog.models import Article, Auteur, Tag


# ============= EXERCICES QUERYSETS AVANCÉS =============

def test_lookups_avances():
    """Exercices 9-11 : Tester les lookups avancés"""
    pass
    # Article.objects.filter(titre__icontains="django")
    # Article.objects.filter(nombre_vues__gte=1000)
    # Article.objects.filter(date_creation__year=2024)


def test_q_objects():
    """Exercice 12 : Q objects pour requêtes complexes"""
    pass
    # Article.objects.filter(Q(publie=True) | Q(featured=True))
    # Article.objects.filter(~Q(auteur__nom="Dupont"))


def test_f_expressions():
    """Exercice 13 : F expressions"""
    pass
    # Article.objects.filter(nombre_vues__gt=F('nombre_likes') * 10)
    # Article.objects.filter(id=1).update(nombre_vues=F('nombre_vues') + 1)


def test_agregation():
    """Exercices 14-16 : Agrégation et annotation"""
    pass
    # stats = Article.objects.aggregate(
    #     total=Count('id'),
    #     vues_totales=Sum('nombre_vues')
    # )
    # 
    # auteurs = Auteur.objects.annotate(nb_articles=Count('articles'))


# ============= EXERCICES OPTIMISATION =============

def test_probleme_n_plus_1():
    """Exercice 17 : Identifier le problème N+1"""
    pass
    # reset_queries()
    # articles = Article.objects.all()
    # for article in articles:
    #     print(article.auteur.nom)  # N+1 queries !
    # print(f"Requêtes : {len(connection.queries)}")


def test_select_related():
    """Exercice 18 : Optimiser avec select_related"""
    pass
    # reset_queries()
    # articles = Article.objects.select_related('auteur').all()
    # for article in articles:
    #     print(article.auteur.nom)  # 1 seule requête !
    # print(f"Requêtes : {len(connection.queries)}")


def test_prefetch_related():
    """Exercice 19 : Optimiser avec prefetch_related"""
    pass
    # articles = Article.objects.prefetch_related('tags').all()
    # for article in articles:
    #     print(list(article.tags.all()))


def test_only_defer():
    """Exercice 20 : only() et defer()"""
    pass
    # articles = Article.objects.only('id', 'titre')
    # articles = Article.objects.defer('contenu')


def test_bulk_operations():
    """Exercice 21 : Opérations en masse"""
    pass
    # articles = [Article(...) for i in range(100)]
    # Article.objects.bulk_create(articles, batch_size=50)
    # 
    # Article.objects.filter(auteur=auteur).update(publie=True)


def test_transactions():
    """Exercice 22 : Transactions"""
    pass
    # from django.db import transaction
    # 
    # with transaction.atomic():
    #     article = Article.objects.create(...)
    #     article.tags.add(...)


# ============= EXÉCUTION =============

if __name__ == "__main__":
    print("=" * 60)
    print("Module 16 - Tests QuerySets et Optimisation")
    print("=" * 60)
    
    # Décommentez les fonctions à tester
    
    print("\n✅ Module prêt pour vos tests !")
