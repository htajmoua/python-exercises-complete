# Instructions - Django ORM : QuerySets et Optimisation ⭐⭐⭐

**🎯 Objectif du module** : Maîtriser les requêtes Django ORM et les techniques d'optimisation.

Ce module est le **CŒUR** de votre maîtrise de l'ORM Django. Vous apprendrez à :
- Écrire des requêtes complexes avec Q objects et F expressions
- Optimiser les performances avec select_related et prefetch_related
- Éviter les pièges classiques (problème N+1)
- Utiliser les transactions efficacement

**📚 Format du module** : **100% EXEMPLES GUIDÉS**

Tous les exercices contiennent du code complet et fonctionnel. Suivez les exemples, testez-les dans le shell Django, et adaptez-les à vos besoins.

**Prérequis** : Avoir complété le module 15 (Fondamentaux des modèles)

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

### Exercice 2bis - Relations et lookups (EXEMPLE)

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

## Exercice 3 - Q objects / Requêtes complexes (EXEMPLE)

**Les Q objects** permettent de créer des requêtes complexes avec OR, AND, NOT.

```python
from django.db.models import Q
from blog.models import Article

# OR : Articles publiés OU avec plus de 1000 vues
articles_or = Article.objects.filter(
    Q(publie=True) | Q(nombre_vues__gt=1000)
)
print(f"Articles (OR) : {articles_or.count()}")

# AND : Articles publiés ET featured
articles_and = Article.objects.filter(
    Q(publie=True) & Q(featured=True)
)
# Équivalent à :
articles_and = Article.objects.filter(publie=True, featured=True)

# NOT : Articles NON écrits par "Dupont"
articles_not = Article.objects.filter(
    ~Q(auteur__nom="Dupont")
)
print(f"Articles NOT Dupont : {articles_not.count()}")

# Requête complexe avec parenthèses
# (publie=True AND featured=True) OR (nombre_vues > 1000)
articles_complexe = Article.objects.filter(
    (Q(publie=True) & Q(featured=True)) | Q(nombre_vues__gt=1000)
)

# Plusieurs conditions OR
articles = Article.objects.filter(
    Q(auteur__nom="Dupont") | Q(auteur__nom="Martin") | Q(auteur__nom="Bernard")
)

# Combiner plusieurs Q objects
q1 = Q(publie=True)
q2 = Q(featured=True)
q3 = Q(nombre_vues__gt=500)
articles = Article.objects.filter(q1 & (q2 | q3))
```

**Fonction de recherche dynamique** :

```python
def rechercher_articles(titre=None, auteur=None, publie=None, tags=None):
    """Recherche multi-critères avec Q objects"""
    # Initialiser un Q object vide
    q = Q()
    
    # Si titre fourni, rechercher dans titre OU contenu
    if titre:
        q &= Q(titre__icontains=titre) | Q(contenu__icontains=titre)
    
    # Si auteur fourni, filtrer par nom d'auteur
    if auteur:
        q &= Q(auteur__nom__icontains=auteur)
    
    # Si publie fourni (peut être True ou False)
    if publie is not None:
        q &= Q(publie=publie)
    
    # Si tags fourni
    if tags:
        q &= Q(tags__nom__in=tags)
    
    # Retourner le QuerySet filtré avec distinct
    return Article.objects.filter(q).distinct()

# Utilisation
resultats = rechercher_articles(titre="Django", publie=True)
print(f"Trouvés : {resultats.count()} articles")

resultats = rechercher_articles(auteur="Dupont", tags=["Python", "Django"])
for article in resultats:
    print(f"- {article.titre}")
```

**Q objects avec relations** :

```python
# Recherche dans les relations
articles = Article.objects.filter(
    Q(auteur__nom__icontains="Dupont") | Q(auteur__email__endswith="@example.com")
)

# Avec ManyToMany
articles = Article.objects.filter(
    Q(tags__nom="Python") | Q(tags__nom="Django")
).distinct()

# Relations profondes
articles = Article.objects.filter(
    Q(auteur__profil__twitter__isnull=False) | 
    Q(categorie__parent__nom="Technologie")
)
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

### Exercice 4bis - Agrégation (EXEMPLE)

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

### Exercice 7 - Fonctions de base de données (EXEMPLE)

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

### Exercice 8 - Case/When (Conditions) (EXEMPLE)

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

## Exercice 5 - Optimisation : select_related (EXEMPLE) ⭐⭐⭐

**Le problème N+1** : Sans optimisation, chaque accès à une relation ForeignKey génère une requête SQL supplémentaire !

**Démonstration du problème** :

```python
from django.db import connection, reset_queries
from blog.models import Article

# ❌ PROBLÈME N+1
reset_queries()

articles = Article.objects.all()[:10]  # 1 requête

for article in articles:
    print(article.auteur.nom)  # N requêtes supplémentaires !

print(f"Nombre de requêtes : {len(connection.queries)}")
# Résultat : 11 requêtes (1 + 10)
```

**Solution avec select_related** :

```python
# ✅ OPTIMISÉ avec select_related
reset_queries()

articles = Article.objects.select_related('auteur').all()[:10]  # 1 requête avec JOIN

for article in articles:
    print(article.auteur.nom)  # Pas de requête supplémentaire !

print(f"Nombre de requêtes : {len(connection.queries)}")
# Résultat : 1 seule requête !
```

**Relations multiples** :

```python
# Optimiser auteur ET categorie
articles = Article.objects.select_related('auteur', 'categorie').all()

for article in articles:
    categorie = article.categorie.nom if article.categorie else "Sans catégorie"
    print(f"{article.titre} - {article.auteur.nom} - {categorie}")

# 1 seule requête avec 2 JOINs
```

**Relations imbriquées (nested)** :

```python
# Suivre les relations : article → auteur → profil
articles = Article.objects.select_related('auteur__profil').all()

for article in articles:
    if hasattr(article.auteur, 'profil'):
        print(f"{article.titre} - Twitter: {article.auteur.profil.twitter}")

# 1 seule requête avec JOINs imbriqués
```

**Comparaison de performances** :

```python
import time

# Test sans optimisation
start = time.time()
reset_queries()
articles = Article.objects.all()[:50]
for article in articles:
    _ = article.auteur.nom
temps_sans = time.time() - start
nb_queries_sans = len(connection.queries)

# Test avec select_related
start = time.time()
reset_queries()
articles = Article.objects.select_related('auteur').all()[:50]
for article in articles:
    _ = article.auteur.nom
temps_avec = time.time() - start
nb_queries_avec = len(connection.queries)

# Résultats
print(f"Sans : {temps_sans:.3f}s, {nb_queries_sans} requêtes")
print(f"Avec : {temps_avec:.3f}s, {nb_queries_avec} requêtes")
gain = ((temps_sans - temps_avec) / temps_sans * 100) if temps_sans > 0 else 0
print(f"Gain : {gain:.1f}%")
```

**Points clés** :
- ✅ `select_related()` utilise un **JOIN SQL**
- ✅ Fonctionne pour **ForeignKey** et **OneToOne**
- ✅ Réduit N+1 requêtes à **1 seule requête**
- ❌ Ne fonctionne PAS pour ManyToMany (utilisez `prefetch_related`)

---

## Exercice 6 - Optimisation : prefetch_related (EXEMPLE) ⭐⭐⭐

**Différence avec select_related** :
- `select_related` : JOIN SQL (pour ForeignKey/OneToOne)
- `prefetch_related` : 2+ requêtes séparées (pour ManyToMany/Reverse FK)

**Problème N+1 avec ManyToMany** :

```python
from django.db import connection, reset_queries
from blog.models import Article, Auteur

# ❌ PROBLÈME N+1 avec ManyToMany
reset_queries()

articles = Article.objects.all()[:10]  # 1 requête

for article in articles:
    tags = list(article.tags.all())  # N requêtes !
    print(f"{article.titre} : {[t.nom for t in tags]}")

print(f"Requêtes : {len(connection.queries)}")
# Résultat : 11 requêtes (1 + 10)
```

**Solution avec prefetch_related** :

```python
# ✅ OPTIMISÉ avec prefetch_related
reset_queries()

articles = Article.objects.prefetch_related('tags').all()[:10]

for article in articles:
    tags = list(article.tags.all())  # Pas de requête !
    print(f"{article.titre} : {[t.nom for t in tags]}")

print(f"Requêtes : {len(connection.queries)}")
# Résultat : 2 requêtes (1 pour articles + 1 pour tous les tags)
```

**Relation inverse (Reverse ForeignKey)** :

```python
# Optimiser auteur.articles
auteurs = Auteur.objects.prefetch_related('articles').all()

for auteur in auteurs:
    articles = list(auteur.articles.all())
    print(f"{auteur.nom} : {len(articles)} articles")
    for article in articles[:3]:
        print(f"  - {article.titre}")

# 2 requêtes : 1 pour auteurs + 1 pour tous leurs articles
```

**Combiner select_related ET prefetch_related** :

```python
# Le meilleur des deux mondes !
articles = Article.objects.select_related(
    'auteur'  # ForeignKey → JOIN SQL
).prefetch_related(
    'tags'  # ManyToMany → Requête séparée
).all()

for article in articles:
    tags_str = ", ".join([t.nom for t in article.tags.all()])
    print(f"{article.titre} par {article.auteur.nom} - Tags: {tags_str}")

# 2 requêtes : 1 avec JOIN pour articles+auteurs + 1 pour tous les tags
```

**Prefetch imbriqué (nested)** :

```python
# Charger auteurs → articles → tags en une fois
auteurs = Auteur.objects.prefetch_related(
    'articles',  # Articles de l'auteur
    'articles__tags',  # Tags de chaque article
    'articles__commentaires'  # Commentaires de chaque article
).all()

for auteur in auteurs:
    print(f"\n{auteur.nom}")
    for article in auteur.articles.all()[:2]:
        tags = [t.nom for t in article.tags.all()]
        nb_comm = article.commentaires.count()
        print(f"  - {article.titre} : {tags} ({nb_comm} commentaires)")

# 4 requêtes : auteurs + articles + tags + commentaires
```

**Prefetch personnalisé avec filtrage** :

```python
from django.db.models import Prefetch, Count

# Prefetch seulement les articles publiés
articles_publies = Prefetch(
    'articles',
    queryset=Article.objects.filter(publie=True).order_by('-date_publication')
)

auteurs = Auteur.objects.prefetch_related(articles_publies).all()

for auteur in auteurs:
    print(f"{auteur.nom} : {auteur.articles.count()} articles publiés")

# Prefetch avec annotations
articles_avec_stats = Prefetch(
    'articles',
    queryset=Article.objects.annotate(nb_commentaires=Count('commentaires'))
)

auteurs = Auteur.objects.prefetch_related(articles_avec_stats).all()
```

**Points clés** :
- ✅ `prefetch_related()` fait **2+ requêtes séparées**
- ✅ Fonctionne pour **ManyToMany** et **Reverse ForeignKey**
- ✅ Peut se combiner avec `select_related`
- ✅ Supporte le filtrage et les annotations personnalisées
- ✅ Évite le problème N+1 : N+1 requêtes → 2+ requêtes

### Exercice 9 - only() et defer() (EXEMPLE)

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

### Exercice 10 - Bulk operations (Opérations en masse) (EXEMPLE)

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

### Exercice 11 - Transactions (EXEMPLE)

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
