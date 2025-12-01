# Instructions - Django ORM : QuerySets et Optimisation ⭐⭐⭐

**🎯 Objectif du module** : Maîtriser les requêtes Django ORM et les techniques d'optimisation.

Ce module est le **CŒUR** de votre maîtrise de l'ORM Django. Vous apprendrez à :
- Écrire des requêtes complexes avec Q objects et F expressions
- Optimiser les performances avec select_related et prefetch_related
- Éviter les pièges classiques (problème N+1)
- Utiliser les transactions efficacement

**📚 Format du module** :
- **Partie 1 (Exercices 1-2)** : Exemples guidés - QuerySets de base et lookups
- **Partie 2 (Exercices 3-6)** : Exercices pratiques - Q/F, Optimisation, Agrégation

**Prérequis** : Avoir complété le module 15 (Fondamentaux des modèles)

---

# 📖 PARTIE 1 : EXEMPLES GUIDÉS

Les exercices 1 à 2 sont des exemples complets pour comprendre les QuerySets.

---

## Exercice 1 - QuerySets de base (EXEMPLE)

**Requêtes basiques** :

```python
from blog.models import Article, Auteur, Tag

# Tous les articles
Article.objects.all()

# Un article spécifique (lève DoesNotExist si absent)
Article.objects.get(id=1)
Article.objects.get(slug='introduction-django')

# Filtrer
Article.objects.filter(publie=True)
Article.objects.filter(publie=True, featured=True)  # AND implicite

# Exclure
Article.objects.exclude(publie=False)

# Compter
Article.objects.count()
Article.objects.filter(publie=True).count()

# Premier et dernier
Article.objects.first()
Article.objects.last()
Article.objects.filter(publie=True).first()

# Vérifier l'existence
Article.objects.filter(slug='test').exists()  # Retourne True/False

# Valeurs spécifiques (retourne des dictionnaires)
Article.objects.values('id', 'titre', 'auteur__nom')
Article.objects.values_list('id', 'titre', flat=False)
Article.objects.values_list('titre', flat=True)  # Liste simple

# Distinct
Article.objects.values('auteur').distinct()
```

## Exercice 2 - Lookups avancés (EXEMPLE)

```python
from datetime import datetime, timedelta

# Exactement égal
Article.objects.filter(titre__exact="Django")
Article.objects.filter(titre__iexact="django")  # Case-insensitive

# Contient
Article.objects.filter(titre__contains="Django")
Article.objects.filter(titre__icontains="django")  # Case-insensitive

# Commence/Termine par
Article.objects.filter(titre__startswith="Introduction")
Article.objects.filter(titre__istartswith="introduction")
Article.objects.filter(titre__endswith="Python")
Article.objects.filter(titre__iendswith="python")

# Nombres
Article.objects.filter(nombre_vues__gt=1000)  # Greater than
Article.objects.filter(nombre_vues__gte=1000)  # Greater than or equal
Article.objects.filter(nombre_vues__lt=100)  # Less than
Article.objects.filter(nombre_vues__lte=100)  # Less than or equal

# Range
Article.objects.filter(nombre_vues__range=(100, 1000))
Article.objects.filter(id__in=[1, 2, 3, 5, 8])

# Dates
Article.objects.filter(date_creation__year=2024)
Article.objects.filter(date_creation__month=12)
Article.objects.filter(date_creation__day=25)
Article.objects.filter(date_creation__week=52)
Article.objects.filter(date_creation__week_day=2)  # 1=dimanche, 2=lundi

# Plages de dates
date_limite = datetime.now() - timedelta(days=7)
Article.objects.filter(date_creation__gte=date_limite)

# Date précise
Article.objects.filter(date_creation__date=datetime.now().date())

# NULL
Article.objects.filter(date_suppression__isnull=True)
Article.objects.filter(date_suppression__isnull=False)

# Regex
Article.objects.filter(titre__regex=r'^[A-Z]')  # Titre commence par majuscule
Article.objects.filter(titre__iregex=r'python|django')  # Case-insensitive
```

### Exercice 11 - Relations et lookups

```python
# Filtrer par champ de relation (double underscore)
Article.objects.filter(auteur__nom="Dupont")
Article.objects.filter(auteur__email__endswith="@example.com")
Article.objects.filter(auteur__date_naissance__year__gte=1990)

# ManyToMany
Article.objects.filter(tags__nom="Python")
Article.objects.filter(tags__nom__in=["Python", "Django"])

# Relations inverses
Auteur.objects.filter(articles__publie=True)
Auteur.objects.filter(articles__nombre_vues__gt=1000)

# Relations profondes
Article.objects.filter(auteur__profil__twitter__isnull=False)
Article.objects.filter(categorie__parent__nom="Technologie")

# Compter les relations
from django.db.models import Count
Auteur.objects.annotate(nb_articles=Count('articles'))
Auteur.objects.filter(articles__count__gt=5)  # ERREUR: ne fonctionne pas ainsi
# Correct :
Auteur.objects.annotate(nb_articles=Count('articles')).filter(nb_articles__gt=5)
```

---

# 🔨 PARTIE 2 : EXERCICES PRATIQUES

**À partir d'ici, c'est à vous de coder !** Les exercices suivants contiennent des squelettes avec des `TODO` à compléter.

---

## Exercice 3 - Q objects / Requêtes complexes (PRATIQUE)

**Objectif** : Maîtriser les Q objects pour créer des requêtes OR, AND, NOT complexes.

**Consignes** :
1. Créez une requête avec un OR : articles publiés OU avec plus de 1000 vues
2. Créez une requête avec un NOT : articles NON écrits par "Dupont"
3. Créez une fonction de recherche dynamique

**Squelette - `blog/views.py` ou shell** (à compléter) :

```python
from django.db.models import Q
from blog.models import Article

def exercice_q_objects():
    # TODO : Récupérez les articles publiés OU avec plus de 1000 vues
    # Utilisez : Q(publie=True) | Q(nombre_vues__gt=1000)
    articles_or = # VOTRE CODE ICI
    
    # TODO : Récupérez les articles NON écrits par "Dupont"
    # Utilisez : ~Q(auteur__nom="Dupont")
    articles_not = # VOTRE CODE ICI
    
    # TODO : Requête complexe
    # (publie=True AND featured=True) OR (nombre_vues > 1000)
    # Utilisez des parenthèses : (Q(...) & Q(...)) | Q(...)
    articles_complexe = # VOTRE CODE ICI
    
    return articles_or, articles_not, articles_complexe

# TODO : Créez une fonction de recherche dynamique
def rechercher_articles(titre=None, auteur=None, publie=None):
    """Recherche multi-critères avec Q objects"""
    # TODO : Initialisez un Q object vide
    q = # VOTRE CODE ICI
    
    # TODO : Si titre fourni, ajoutez la condition avec &=
    # Recherchez dans titre OU contenu : Q(titre__icontains=...) | Q(contenu__icontains=...)
    if titre:
        q &= # VOTRE CODE ICI
    
    # TODO : Si auteur fourni, ajoutez la condition
    # Utilisez : Q(auteur__nom__icontains=auteur)
    if auteur:
        q &= # VOTRE CODE ICI
    
    # TODO : Si publie fourni (peut être True ou False), ajoutez la condition
    if publie is not None:
        q &= # VOTRE CODE ICI
    
    # TODO : Retournez le QuerySet filtré avec .distinct()
    return # VOTRE CODE ICI
```

**Indice** :
- `|` = OR
- `&` = AND
- `~` = NOT
- Utilisez des parenthèses pour la priorité

**Validation** :

```python
# TODO : Testez dans le shell
python manage.py shell

from blog.models import Article

# TODO : Testez la fonction de recherche
resultats = rechercher_articles(titre="Django", publie=True)
print(f"Trouvés : {resultats.count()} articles")

# TODO : Testez la requête complexe
articles = exercice_q_objects()
print(articles)
```

---

## Exercice 4 - F expressions (EXEMPLE) 

**Comprendre les F expressions** pour manipuler les champs côté base de données.

```python
from django.db.models import F

# Comparer des champs entre eux
Article.objects.filter(nombre_vues__gt=F('nombre_likes') * 10)

# Incrémenter un champ (évite race condition)
# MAUVAIS (race condition possible):
article = Article.objects.get(id=1)
article.nombre_vues += 1
article.save()

# BON (atomique):
Article.objects.filter(id=1).update(nombre_vues=F('nombre_vues') + 1)

# Opérations arithmétiques
Article.objects.update(score=F('nombre_vues') + F('nombre_likes') * 2)

# Avec dates
from django.utils import timezone
from datetime import timedelta
Article.objects.update(
    date_expiration=F('date_publication') + timedelta(days=30)
)

# Références à travers relations
Article.objects.filter(nombre_vues__gt=F('auteur__profil__nombre_followers'))

# Annotations avec F
from django.db.models import Count
Article.objects.annotate(
    ratio=F('nombre_likes') * 100.0 / F('nombre_vues')
).filter(ratio__gt=5)
```

### Exercice 14 - Agrégation

```python
from django.db.models import Count, Sum, Avg, Max, Min, StdDev, Variance

# Agrégation simple (retourne un dictionnaire)
stats = Article.objects.aggregate(
    total=Count('id'),
    vues_totales=Sum('nombre_vues'),
    vues_moyenne=Avg('nombre_vues'),
    max_vues=Max('nombre_vues'),
    min_vues=Min('nombre_vues')
)
# {'total': 150, 'vues_totales': 45000, 'vues_moyenne': 300.0, ...}

# Agrégation avec filtre
Article.objects.filter(publie=True).aggregate(
    total_publie=Count('id'),
    vues_moyennes_publie=Avg('nombre_vues')
)

# Agrégation sur relations
Auteur.objects.aggregate(
    total_articles=Count('articles'),
    total_vues=Sum('articles__nombre_vues')
)

# Annotation (ajoute le résultat à chaque objet)
auteurs_avec_stats = Auteur.objects.annotate(
    nb_articles=Count('articles'),
    vues_totales=Sum('articles__nombre_vues'),
    vues_moyennes=Avg('articles__nombre_vues')
)

for auteur in auteurs_avec_stats:
    print(f"{auteur.nom}: {auteur.nb_articles} articles, {auteur.vues_totales} vues")

# Annotation avec filtre
Auteur.objects.annotate(
    nb_articles_publies=Count('articles', filter=Q(articles__publie=True))
)

# Grouper par et annoter
from django.db.models.functions import TruncMonth

articles_par_mois = Article.objects.annotate(
    mois=TruncMonth('date_creation')
).values('mois').annotate(
    total=Count('id'),
    vues=Sum('nombre_vues')
).order_by('mois')
```

### Exercice 15 - Fonctions de base de données

```python
from django.db.models.functions import (
    Concat, Upper, Lower, Length, Substr,
    Coalesce, Greatest, Least, Now,
    TruncDate, TruncYear, TruncMonth, ExtractYear
)
from django.db.models import Value, CharField

# Concaténation
Auteur.objects.annotate(
    nom_complet=Concat('prenom', Value(' '), 'nom')
)

# Transformation de texte
Article.objects.annotate(
    titre_majuscule=Upper('titre'),
    titre_minuscule=Lower('titre'),
    longueur_titre=Length('titre')
)

# Coalesce (première valeur non nulle)
Auteur.objects.annotate(
    affichage=Coalesce('pseudo', 'nom', Value('Anonyme'))
)

# Extraction de date
Article.objects.annotate(
    annee=ExtractYear('date_creation')
).values('annee').annotate(count=Count('id'))

# Substring
Article.objects.annotate(
    apercu=Substr('contenu', 1, 100)
)

# Greatest / Least
Article.objects.annotate(
    meilleur_score=Greatest('nombre_vues', 'nombre_likes', 'nombre_partages')
)
```

### Exercice 16 - Case/When (Conditions)

```python
from django.db.models import Case, When, Value, IntegerField

# Ajouter un champ calculé selon des conditions
Article.objects.annotate(
    popularite=Case(
        When(nombre_vues__gte=10000, then=Value('Viral')),
        When(nombre_vues__gte=1000, then=Value('Populaire')),
        When(nombre_vues__gte=100, then=Value('Moyen')),
        default=Value('Faible'),
        output_field=CharField()
    )
)

# Avec des calculs
Article.objects.annotate(
    score=Case(
        When(featured=True, then=F('nombre_vues') * 2),
        When(publie=True, then=F('nombre_vues')),
        default=Value(0),
        output_field=IntegerField()
    )
).order_by('-score')

# Tri conditionnel
Article.objects.annotate(
    priorite=Case(
        When(featured=True, then=Value(1)),
        When(publie=True, then=Value(2)),
        default=Value(3)
    )
).order_by('priorite', '-date_creation')

# Compter avec conditions
Auteur.objects.annotate(
    articles_publies=Count(
        Case(When(articles__publie=True, then=1))
    ),
    articles_brouillon=Count(
        Case(When(articles__publie=False, then=1))
    )
)
```

---

## Exercice 5 - Optimisation : select_related (PRATIQUE) ⭐⭐⭐

**Objectif** : Optimiser les requêtes ForeignKey/OneToOne avec select_related (le problème N+1).

**Le problème N+1** :
Sans optimisation, chaque accès à une relation ForeignKey génère une requête SQL supplémentaire !

**Consignes** :
1. Identifiez un problème N+1 dans votre code
2. Optimisez avec `select_related()`
3. Comparez le nombre de requêtes

**Squelette - `blog/views.py` ou shell** (à compléter) :

```python
from django.db import connection, reset_queries
from blog.models import Article
import time

def demonstrer_probleme_n1():
    """Démontre le problème N+1"""
    # TODO : Réinitialisez les requêtes
    reset_queries()
    
    # TODO : Récupérez tous les articles (sans optimisation)
    articles = # VOTRE CODE ICI
    
    # TODO : Parcourez les articles et affichez le nom de l'auteur
    for article in articles:
        print(article.auteur.nom)  # Chaque accès = 1 requête !
    
    # TODO : Affichez le nombre total de requêtes
    print(f"Nombre de requêtes : {len(connection.queries)}")
    # Devrait afficher : 1 + N requêtes (N = nombre d'articles)

def optimiser_avec_select_related():
    """Optimise avec select_related"""
    # TODO : Réinitialisez les requêtes
    reset_queries()
    
    # TODO : Récupérez tous les articles AVEC select_related('auteur')
    articles = # VOTRE CODE ICI
    
    # TODO : Parcourez les articles et affichez le nom de l'auteur
    for article in articles:
        print(article.auteur.nom)  # Pas de requête supplémentaire !
    
    # TODO : Affichez le nombre total de requêtes
    print(f"Nombre de requêtes : {len(connection.queries)}")
    # Devrait afficher : 1 seule requête avec JOIN !

def comparer_performances():
    """Compare les performances"""
    # TODO : Test sans optimisation
    start = time.time()
    reset_queries()
    articles = Article.objects.all()[:50]
    for article in articles:
        _ = article.auteur.nom
    temps_sans = time.time() - start
    nb_queries_sans = len(connection.queries)
    
    # TODO : Test avec select_related
    start = time.time()
    reset_queries()
    # Utilisez : Article.objects.select_related('auteur').all()[:50]
    articles = # VOTRE CODE ICI
    for article in articles:
        _ = article.auteur.nom
    temps_avec = time.time() - start
    nb_queries_avec = len(connection.queries)
    
    # TODO : Affichez les résultats
    print(f"Sans : {temps_sans:.3f}s, {nb_queries_sans} requêtes")
    print(f"Avec : {temps_avec:.3f}s, {nb_queries_avec} requêtes")
    print(f"Gain : {((temps_sans - temps_avec) / temps_sans * 100):.1f}%")

# TODO : Relations multiples
def optimiser_relations_multiples():
    """Optimise plusieurs relations à la fois"""
    # TODO : Utilisez select_related avec plusieurs relations
    # Exemple : .select_related('auteur', 'categorie')
    articles = # VOTRE CODE ICI
    
    for article in articles:
        print(f"{article.titre} - {article.auteur.nom} - {article.categorie.nom}")
```

**Indice** :
- `select_related()` utilise un JOIN SQL
- Fonctionne pour ForeignKey et OneToOne
- Peut chaîner : `select_related('auteur__profil')`
- N'utilisez PAS pour ManyToMany (utilisez prefetch_related)

**Validation** :

```python
# TODO : Testez dans le shell
python manage.py shell

# TODO : Activez le debug pour voir les requêtes SQL
from django.conf import settings
settings.DEBUG = True

# TODO : Testez la fonction
demonstrer_probleme_n1()  # Devrait afficher beaucoup de requêtes
optimiser_avec_select_related()  # Devrait afficher 1 seule requête
comparer_performances()  # Devrait montrer un gain significatif
```

---

## Exercice 6 - Optimisation : prefetch_related (PRATIQUE) ⭐⭐⭐

**Objectif** : Optimiser les requêtes ManyToMany avec prefetch_related.

**Différence avec select_related** :
- `select_related` : JOIN (pour ForeignKey/OneToOne)
- `prefetch_related` : 2 requêtes séparées (pour ManyToMany/Reverse FK)

**Consignes** :
1. Identifiez un problème N+1 avec ManyToMany
2. Optimisez avec `prefetch_related()`
3. Comparez les performances

**Squelette - `blog/views.py` ou shell** (à compléter) :

```python
from django.db import connection, reset_queries
from blog.models import Article, Auteur

def demonstrer_n1_manytomany():
    """Problème N+1 avec ManyToMany"""
    # TODO : Réinitialisez les requêtes
    reset_queries()
    
    # TODO : Récupérez tous les articles (sans optimisation)
    articles = # VOTRE CODE ICI
    
    # TODO : Affichez les tags de chaque article
    for article in articles:
        print(f"{article.titre} : {list(article.tags.all())}")  # N requêtes !
    
    print(f"Requêtes : {len(connection.queries)}")

def optimiser_avec_prefetch():
    """Optimise avec prefetch_related"""
    # TODO : Réinitialisez les requêtes
    reset_queries()
    
    # TODO : Utilisez prefetch_related('tags')
    articles = # VOTRE CODE ICI
    
    # TODO : Affichez les tags (pas de requête supplémentaire)
    for article in articles:
        print(f"{article.titre} : {list(article.tags.all())}")
    
    print(f"Requêtes : {len(connection.queries)}")
    # Devrait afficher : 2 requêtes (1 pour articles + 1 pour tous les tags)

# TODO : Optimiser les relations inverses (Reverse ForeignKey)
def optimiser_relation_inverse():
    """Optimise la relation inverse (auteur.articles)"""
    # TODO : Récupérez les auteurs avec leurs articles
    # Utilisez : Auteur.objects.prefetch_related('articles')
    auteurs = # VOTRE CODE ICI
    
    # TODO : Affichez les articles de chaque auteur
    for auteur in auteurs:
        print(f"{auteur.nom} : {auteur.articles.count()} articles")
        # VOTRE CODE ICI

# TODO : Combiner select_related ET prefetch_related
def optimisation_combinee():
    """Combine les deux techniques"""
    # TODO : Optimisez à la fois auteur (FK) ET tags (M2M)
    # Utilisez : .select_related('auteur').prefetch_related('tags')
    articles = # VOTRE CODE ICI
    
    for article in articles:
        tags_str = ", ".join([t.nom for t in article.tags.all()])
        print(f"{article.titre} par {article.auteur.nom} - Tags: {tags_str}")
```

**Indice** :
- `prefetch_related()` fait 2 requêtes : 1 pour les objets principaux + 1 pour les relations
- Fonctionne pour ManyToMany et Reverse ForeignKey
- Peut combiner avec select_related

**Validation** :

```python
# TODO : Testez dans le shell
demonstrer_n1_manytomany()  # Beaucoup de requêtes
optimiser_avec_prefetch()  # 2 requêtes seulement !
optimisation_combinee()  # Le meilleur des deux mondes

# ✅ BON : 2 requêtes (1 pour articles + 1 pour tous les tags)
articles = Article.objects.prefetch_related('tags').all()
for article in articles:
    print(list(article.tags.all()))  # Pas de requête, données en cache

# Relation inverse (auteur.articles)
auteurs = Auteur.objects.prefetch_related('articles').all()
for auteur in auteurs:
    for article in auteur.articles.all():
        print(article.titre)

# Prefetch avec filtrage personnalisé
from django.db.models import Prefetch

articles_publies = Prefetch(
    'articles',
    queryset=Article.objects.filter(publie=True).order_by('-date_creation')
)
auteurs = Auteur.objects.prefetch_related(articles_publies)

# Combiner select_related et prefetch_related
articles = Article.objects.select_related(
    'auteur'  # ForeignKey → JOIN
).prefetch_related(
    'tags',  # ManyToMany → Requête séparée
    'commentaires'  # Reverse FK → Requête séparée
).all()

# Prefetch imbriqué
auteurs = Auteur.objects.prefetch_related(
    'articles',  # Articles de l'auteur
    'articles__tags',  # Tags de chaque article
    'articles__commentaires'  # Commentaires de chaque article
)

# Prefetch avec annotations
articles_avec_nb_commentaires = Prefetch(
    'articles',
    queryset=Article.objects.annotate(nb_commentaires=Count('commentaires'))
)
auteurs = Auteur.objects.prefetch_related(articles_avec_nb_commentaires)
```

### Exercice 20 - only() et defer()

**Cas d'usage** : Charger seulement certains champs pour réduire la taille des données.

```python
# only() : Charge SEULEMENT les champs spécifiés
articles = Article.objects.only('id', 'titre', 'slug')
# Accéder à un champ non chargé génère une requête supplémentaire
for article in articles:
    print(article.titre)  # OK, pas de requête
    print(article.contenu)  # ⚠️ Requête supplémentaire !

# defer() : Charge TOUS les champs SAUF ceux spécifiés  
articles = Article.objects.defer('contenu', 'metadata')
for article in articles:
    print(article.titre)  # OK
    # article.contenu générerait une requête

# Utilisation pratique
# Pour une liste : only ID et titre
liste = Article.objects.only('id', 'titre', 'auteur__nom').select_related('auteur')

# Pour un export : tous les champs
export = Article.objects.all()

# defer pour champs volumineux
articles_liste = Article.objects.defer('contenu', 'contenu_html')  # Évite charger le HTML
```

### Exercice 21 - Bulk operations (Opérations en masse)

```python
# ❌ MAUVAIS : N requêtes
for i in range(1000):
    Article.objects.create(titre=f"Article {i}", ...)

# ✅ BON : 1 seule requête
articles = [
    Article(titre=f"Article {i}", contenu="...", auteur=auteur)
    for i in range(1000)
]
Article.objects.bulk_create(articles, batch_size=500)

# bulk_update
articles = Article.objects.all()[:1000]
for article in articles:
    article.nombre_vues += 1
Article.objects.bulk_update(articles, ['nombre_vues'], batch_size=500)

# update() pour mise à jour en masse
Article.objects.filter(auteur=auteur).update(publie=True)
Article.objects.all().update(nombre_vues=F('nombre_vues') + 1)

# get_or_create
article, created = Article.objects.get_or_create(
    slug='introduction-django',
    defaults={
        'titre': 'Introduction à Django',
        'contenu': '...',
        'auteur': auteur
    }
)
if created:
    print("Article créé")
else:
    print("Article existant")

# update_or_create
article, created = Article.objects.update_or_create(
    slug='introduction-django',
    defaults={
        'titre': 'Introduction à Django (mis à jour)',
        'contenu': '...',
        'publie': True
    }
)
```

### Exercice 22 - Transactions

```python
from django.db import transaction

# Méthode 1 : Décorateur
@transaction.atomic
def creer_article_complet(titre, contenu, auteur, tags):
    article = Article.objects.create(
        titre=titre,
        contenu=contenu,
        auteur=auteur
    )
    article.tags.set(tags)
    
    # Si erreur ici, TOUT est annulé (rollback)
    article.auteur.profil.nombre_articles += 1
    article.auteur.profil.save()
    
    return article

# Méthode 2 : Context manager
def publier_articles(auteur):
    with transaction.atomic():
        # Toutes ces opérations sont atomiques
        articles = Article.objects.filter(
            auteur=auteur,
            publie=False
        )
        
        for article in articles:
            article.publie = True
            article.date_publication = timezone.now()
            article.save()
        
        auteur.profil.derniere_publication = timezone.now()
        auteur.profil.save()
        
        # Si erreur, rollback automatique

# Savepoints (points de sauvegarde)
with transaction.atomic():
    article = Article.objects.create(...)
    
    sid = transaction.savepoint()  # Créer un savepoint
    
    try:
        # Opération risquée
        article.tags.set(tags)
    except Exception:
        transaction.savepoint_rollback(sid)  # Rollback au savepoint
    else:
        transaction.savepoint_commit(sid)  # Commit le savepoint

# select_for_update (verrouillage)
with transaction.atomic():
    # Verrouille les lignes jusqu'à la fin de la transaction
    article = Article.objects.select_for_update().get(id=1)
    article.nombre_vues += 1
    article.save()
    # Évite les race conditions
```
