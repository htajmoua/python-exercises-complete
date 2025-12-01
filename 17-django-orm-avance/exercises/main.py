"""
Module 17 - Django ORM : Techniques Avancées
Fichier de test pour les exercices

Utilisez le shell Django pour tester :
    python manage.py shell
"""

# ============= IMPORTS =============

from django.db import models, connection
from django.db.models import Q, F, Count
from django.contrib.postgres.search import SearchVector, SearchQuery
from django.db.models.signals import pre_save, post_save
from django.dispatch import receiver

# Vos imports de modèles
# from blog.models import Article, Auteur


# ============= EXERCICES MIGRATIONS =============

def test_migration_donnees():
    """Exercices 23-25 : Migrations de données"""
    pass
    # Créer une migration personnalisée avec RunPython
    # python manage.py makemigrations --empty blog


# ============= EXERCICES INDEXES =============

def test_indexes():
    """Exercices 26-27 : Indexes et contraintes"""
    pass
    # Vérifier les indexes créés en BDD
    # Tester les performances avec/sans index


# ============= EXERCICES RAW SQL =============

def test_raw_sql():
    """Exercices 28-30 : Raw SQL"""
    pass
    # articles = Article.objects.raw(
    #     'SELECT * FROM blog_article WHERE publie = %s',
    #     [True]
    # )
    # 
    # with connection.cursor() as cursor:
    #     cursor.execute("SELECT COUNT(*) FROM blog_article")
    #     count = cursor.fetchone()[0]


# ============= EXERCICES SIGNALS =============

def test_signals():
    """Exercices 31-33 : Signals"""
    pass
    # @receiver(post_save, sender=Article)
    # def mon_signal(sender, instance, created, **kwargs):
    #     if created:
    #         print(f"Nouvel article : {instance.titre}")


# ============= EXERCICES MANAGERS =============

def test_managers_personnalises():
    """Exercices 34-37 : Managers"""
    pass
    # Article.publies.all()
    # Article.objects.populaires(10)


# ============= EXERCICES VALIDATION =============

def test_validation():
    """Exercices 38-40 : Validation"""
    pass
    # article = Article(titre="Test", contenu="...")
    # try:
    #     article.full_clean()
    # except ValidationError as e:
    #     print(e)


# ============= EXÉCUTION =============

if __name__ == "__main__":
    print("=" * 60)
    print("Module 17 - Tests Techniques Avancées")
    print("=" * 60)
    
    print("\n✅ Module prêt pour vos tests !")
