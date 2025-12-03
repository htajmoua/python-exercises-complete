# Instructions - Django ORM : QuerySets et Optimisation ⭐⭐⭐

**🎯 Objectif du module** : Maîtriser les requêtes Django ORM et les techniques d'optimisation.

Ce module est le **CŒUR** de votre maîtrise de l'ORM Django. Vous apprendrez à :
- Écrire des requêtes complexes avec Q objects et F expressions
- Optimiser les performances avec select_related et prefetch_related
- Éviter les pièges classiques (problème N+1)
- Utiliser les transactions efficacement

**📚 Format du module** : **100% EXEMPLES GUIDÉS**

Tous les exercices contiennent du code complet et fonctionnel. Suivez les exemples, testez-les dans le shell Django, et adaptez-les à vos besoins.

**Prérequis** : Avoir complété le module 16 (Django Models : Fondamentaux)

---

## 📦 Préparation des données

Avant de commencer les exercices, créez des données de test dans le **shell Django** :

```bash
python manage.py shell
```

```python
from blog.models import Article, Auteur, Tag
from datetime import date

# Créer des auteurs
auteur1, _ = Auteur.objects.get_or_create(
    email="alice@example.com",
    defaults={
        'nom': "Dupont",
        'prenom': "Alice",
        'pseudo': "alice"
    }
)

auteur2, _ = Auteur.objects.get_or_create(
    email="bob@example.com",
    defaults={
        'nom': "Martin",
        'prenom': "Bob",
        'pseudo': "bob"
    }
)

# Créer des tags
tag_python, _ = Tag.objects.get_or_create(
    slug="python",
    defaults={'nom': "Python", 'description': "Langage Python"}
)

tag_django, _ = Tag.objects.get_or_create(
    slug="django",
    defaults={'nom': "Django", 'description': "Framework Django"}
)

tag_web, _ = Tag.objects.get_or_create(
    slug="web",
    defaults={'nom': "Web", 'description': "Développement web"}
)

# Créer des articles
article1, _ = Article.objects.get_or_create(
    slug="introduction-django",
    defaults={
        'titre': "Introduction à Django",
        'contenu': "Django est un framework web puissant...",
        'auteur': auteur1,
        'publie': True,
        'nombre_vues': 1500
    }
)
article1.tags.add(tag_django, tag_python)

article2, _ = Article.objects.get_or_create(
    slug="python-debutant",
    defaults={
        'titre': "Python pour débutants",
        'contenu': "Apprenez les bases de Python...",
        'auteur': auteur1,
        'publie': True,
        'nombre_vues': 2500
    }
)
article2.tags.add(tag_python)

article3, _ = Article.objects.get_or_create(
    slug="optimisation-django",
    defaults={
        'titre': "Optimisation Django",
        'contenu': "Comment optimiser vos requêtes Django...",
        'auteur': auteur2,
        'publie': True,
        'nombre_vues': 800
    }
)
article3.tags.add(tag_django, tag_web)

article4, _ = Article.objects.get_or_create(
    slug="brouillon",
    defaults={
        'titre': "Article en cours",
        'contenu': "Ceci est un brouillon...",
        'auteur': auteur2,
        'publie': False,
        'nombre_vues': 50
    }
)

print("Données créées avec succès!")
print(f"  - {Auteur.objects.count()} auteurs")
print(f"  - {Article.objects.count()} articles")
print(f"  - {Tag.objects.count()} tags")
```

Vous êtes maintenant prêt pour les exercices ! 🚀

---

## Exercice 1 - QuerySets de base (EXEMPLE)

**Requêtes basiques** :

```python
from blog.models import Article, Auteur, Tag

# Tous les articles
articles = Article.objects.all()
print(f"Total : {articles.count()} articles")

# Un article spécifique (utilisez le slug, pas l'ID)
article = Article.objects.get(slug='introduction-django')
print(f"Article trouvé : {article.titre}")

# Filtrer
articles_publies = Article.objects.filter(publie=True)
print(f"Articles publiés : {articles_publies.count()}")

# Exclure (articles publiés uniquement)
articles_sans_brouillon = Article.objects.exclude(publie=False)
print(f"Sans brouillons : {articles_sans_brouillon.count()}")

# Compter
total = Article.objects.count()
publies = Article.objects.filter(publie=True).count()
print(f"Total : {total}, Publiés : {publies}")

# Premier et dernier
premier = Article.objects.first()
dernier = Article.objects.last()
premier_publie = Article.objects.filter(publie=True).first()
print(f"Premier : {premier.titre if premier else 'Aucun'}")

# Vérifier l'existence
existe = Article.objects.filter(slug='introduction-django').exists()
print(f"Article 'introduction-django' existe : {existe}")

# Valeurs spécifiques (retourne des dictionnaires)
valeurs = Article.objects.values('id', 'titre', 'auteur__nom')
print(f"Valeurs : {list(valeurs)[:2]}")  # Affiche 2 premiers

# Liste simple de titres
titres = Article.objects.values_list('titre', flat=True)
print(f"Titres : {list(titres)}")

# Distinct (auteurs ayant au moins 1 article)
auteurs_distincts = Article.objects.values('auteur').distinct()
print(f"Nombre d'auteurs distincts : {auteurs_distincts.count()}")
```

## Exercice 2 - Lookups avancés (EXEMPLE)

```python
from datetime import datetime, timedelta
from django.utils import timezone

# Contient (case-sensitive et insensitive)
avec_django = Article.objects.filter(titre__contains="Django")
print(f"Contient 'Django' : {avec_django.count()} articles")

avec_django_i = Article.objects.filter(titre__icontains="django")
print(f"Contient 'django' (insensitive) : {avec_django_i.count()} articles")

# Commence par
commence_intro = Article.objects.filter(titre__startswith="Introduction")
print(f"Commence par 'Introduction' : {commence_intro.count()}")

# Termine par
termine_django = Article.objects.filter(titre__endswith="Django")
print(f"Termine par 'Django' : {termine_django.count()}")

# Nombres (comparaisons)
plus_1000_vues = Article.objects.filter(nombre_vues__gt=1000)
print(f"Plus de 1000 vues : {plus_1000_vues.count()}")

entre_500_2000 = Article.objects.filter(nombre_vues__range=(500, 2000))
print(f"Entre 500 et 2000 vues : {entre_500_2000.count()}")

moins_100_vues = Article.objects.filter(nombre_vues__lt=100)
print(f"Moins de 100 vues : {moins_100_vues.count()}")

# Dates (année courante)
annee_actuelle = timezone.now().year
articles_annee = Article.objects.filter(date_creation__year=annee_actuelle)
print(f"Articles de {annee_actuelle} : {articles_annee.count()}")

# Articles récents (derniers 7 jours)
date_limite = timezone.now() - timedelta(days=7)
articles_recents = Article.objects.filter(date_creation__gte=date_limite)
print(f"Articles des 7 derniers jours : {articles_recents.count()}")

# Regex (titres commençant par majuscule)
majuscule = Article.objects.filter(titre__regex=r'^[A-Z]')
print(f"Titres avec majuscule : {majuscule.count()}")

# Recherche multiple avec regex
python_ou_django = Article.objects.filter(titre__iregex=r'python|django')
print(f"Contient 'python' OU 'django' : {python_ou_django.count()}")
for article in python_ou_django:
    print(f"  - {article.titre}")
```

## Exercice 3 - Relations et lookups (EXEMPLE)

```python
# Filtrer par champ de relation (double underscore)
articles_dupont = Article.objects.filter(auteur__nom="Dupont")
print(f"Articles de Dupont : {articles_dupont.count()}")
for article in articles_dupont:
    print(f"  - {article.titre}")

# Email se terminant par @example.com
articles_example = Article.objects.filter(auteur__email__endswith="@example.com")
print(f"\nArticles d'auteurs @example.com : {articles_example.count()}")

# ManyToMany - Articles avec tag Python
avec_python = Article.objects.filter(tags__nom="Python")
print(f"\nArticles avec tag Python : {avec_python.count()}")
for article in avec_python:
    print(f"  - {article.titre}")

# ManyToMany - Articles avec plusieurs tags
avec_python_ou_django = Article.objects.filter(tags__nom__in=["Python", "Django"])
print(f"\nArticles Python OU Django : {avec_python_ou_django.count()}")

# Relations inverses - Auteurs ayant des articles publiés
from django.db.models import Count

auteurs_publies = Auteur.objects.filter(articles__publie=True).distinct()
print(f"\nAuteurs avec articles publiés : {auteurs_publies.count()}")
for auteur in auteurs_publies:
    print(f"  - {auteur.prenom} {auteur.nom}")

# Auteurs avec articles populaires (>1000 vues)
auteurs_populaires = Auteur.objects.filter(articles__nombre_vues__gt=1000).distinct()
print(f"\nAuteurs avec articles >1000 vues : {auteurs_populaires.count()}")

# Compter les articles par auteur
auteurs_avec_count = Auteur.objects.annotate(nb_articles=Count('articles'))
for auteur in auteurs_avec_count:
    print(f"{auteur.prenom} {auteur.nom} : {auteur.nb_articles} article(s)")

# Auteurs avec plus de 1 article
auteurs_prolifiques = Auteur.objects.annotate(
    nb_articles=Count('articles')
).filter(nb_articles__gt=1)
print(f"\nAuteurs avec >1 article : {auteurs_prolifiques.count()}")
```

---

## Exercice 4 - Q objects / Requêtes complexes (EXEMPLE)

**Les Q objects** permettent de créer des requêtes complexes avec OR, AND, NOT.

```python
from django.db.models import Q
from blog.models import Article

# OR : Articles publiés OU avec plus de 1000 vues
articles_or = Article.objects.filter(
    Q(publie=True) | Q(nombre_vues__gt=1000)
)
print(f"Articles (OR) : {articles_or.count()}")

# AND : Articles publiés ET avec plus de 800 vues
articles_and = Article.objects.filter(
    Q(publie=True) & Q(nombre_vues__gt=800)
)
print(f"Articles (AND) : {articles_and.count()}")
# Équivalent à :
articles_and = Article.objects.filter(publie=True, nombre_vues__gt=800)

# NOT : Articles NON écrits par "Dupont"
articles_not = Article.objects.filter(
    ~Q(auteur__nom="Dupont")
)
print(f"Articles NOT Dupont : {articles_not.count()}")

# Requête complexe avec parenthèses
# (publie=True AND nombre_vues > 800) OR (auteur Martin)
articles_complexe = Article.objects.filter(
    (Q(publie=True) & Q(nombre_vues__gt=800)) | Q(auteur__nom="Martin")
)
print(f"Articles complexe : {articles_complexe.count()}")

# Plusieurs conditions OR
articles = Article.objects.filter(
    Q(auteur__nom="Dupont") | Q(auteur__nom="Martin") | Q(auteur__nom="Bernard")
)

# Combiner plusieurs Q objects
q1 = Q(publie=True)
q2 = Q(nombre_vues__gt=1000)
q3 = Q(auteur__nom="Dupont")
articles = Article.objects.filter(q1 & (q2 | q3))
print(f"Combinaison Q : {articles.count()}")
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

# Combinaison tags
articles_python_ou_django = Article.objects.filter(
    Q(tags__nom="Python") | Q(tags__nom="Django")
).distinct()
print(f"Articles Python OU Django : {articles_python_ou_django.count()}")
```

---

## Exercice 5 - F expressions (EXEMPLE) 

**Comprendre les F expressions** pour manipuler les champs côté base de données.

```python
from django.db.models import F
from django.utils import timezone

# Incrémenter un champ (évite race condition)
# MAUVAIS (race condition possible):
article = Article.objects.get(slug='introduction-django')
article.nombre_vues += 1
article.save()
print(f"Vues après incrémentation : {article.nombre_vues}")

# BON (atomique, évite race condition):
Article.objects.filter(slug='introduction-django').update(
    nombre_vues=F('nombre_vues') + 1
)
article.refresh_from_db()
print(f"Vues après update atomique : {article.nombre_vues}")

# Incrémenter tous les articles publiés
Article.objects.filter(publie=True).update(
    nombre_vues=F('nombre_vues') + 10
)
print(f"Tous les articles publiés ont +10 vues")

# Comparer des champs entre eux (date_modification > date_creation)
articles_modifies = Article.objects.filter(
    date_modification__gt=F('date_creation')
)
print(f"Articles modifiés après création : {articles_modifies.count()}")

# Filtrer les articles où l'auteur a plusieurs articles
from django.db.models import Count
auteurs_prolifiques = Auteur.objects.annotate(
    nb=Count('articles')
).filter(nb__gt=1)

articles = Article.objects.filter(
    auteur__in=auteurs_prolifiques
)
print(f"Articles d'auteurs prolifiques : {articles.count()}")
```

## Exercice 6 - Agrégation (EXEMPLE)

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
print(f"Stats : {stats}")

# Agrégation avec filtre
stats_publies = Article.objects.filter(publie=True).aggregate(
    total_publie=Count('id'),
    vues_moyennes_publie=Avg('nombre_vues')
)
print(f"Stats articles publiés : {stats_publies}")

# Agrégation sur relations
stats_auteurs = Auteur.objects.aggregate(
    total_articles=Count('articles'),
    total_vues=Sum('articles__nombre_vues')
)
print(f"Stats tous auteurs : {stats_auteurs}")

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

# Greatest (exemple avec dates)
from django.db.models.functions import Greatest, Least

articles = Article.objects.annotate(
    derniere_modif=Greatest('date_creation', 'date_modification')
)
for article in articles[:2]:
    print(f"{article.titre} - Dernière modif: {article.derniere_modif}")
```

## Exercice 8 - Case/When (Conditions) (EXEMPLE)

```python
from django.db.models import Case, When, Value, IntegerField, CharField, F

# Ajouter un champ calculé selon des conditions
articles_avec_popularite = Article.objects.annotate(
    popularite=Case(
        When(nombre_vues__gte=2000, then=Value('Viral')),
        When(nombre_vues__gte=1000, then=Value('Populaire')),
        When(nombre_vues__gte=500, then=Value('Moyen')),
        default=Value('Faible'),
        output_field=CharField()
    )
)

for article in articles_avec_popularite:
    print(f"{article.titre}: {article.popularite} ({article.nombre_vues} vues)")

# Tri conditionnel selon statut
articles_tries = Article.objects.annotate(
    priorite=Case(
        When(publie=True, nombre_vues__gte=1000, then=Value(1)),
        When(publie=True, then=Value(2)),
        default=Value(3)
    )
).order_by('priorite', '-date_creation')

print("\nArticles triés par priorité:")
for article in articles_tries[:3]:
    statut = "Publié" if article.publie else "Brouillon"
    print(f"  - {article.titre} ({statut}, {article.nombre_vues} vues)")

# Compter avec conditions
auteurs_avec_stats = Auteur.objects.annotate(
    articles_publies=Count(
        Case(When(articles__publie=True, then=1))
    ),
    articles_brouillon=Count(
        Case(When(articles__publie=False, then=1))
    )
)

for auteur in auteurs_avec_stats:
    print(f"{auteur.prenom} {auteur.nom}: {auteur.articles_publies} publiés, {auteur.articles_brouillon} brouillons")
```

---

## Exercice 9 - Optimisation : select_related (EXEMPLE) ⭐⭐⭐

**Le problème N+1** : Sans optimisation, chaque accès à une relation ForeignKey génère une requête SQL supplémentaire !

**Démonstration du problème** :

```python
from django.db import connection, reset_queries
from blog.models import Article

# PROBLÈME N+1
reset_queries()

articles = Article.objects.all()[:10]  # 1 requête

for article in articles:
    print(article.auteur.nom)  # N requêtes supplémentaires !

print(f"Nombre de requêtes : {len(connection.queries)}")
# Résultat : 11 requêtes (1 + 10)
```

**Solution avec select_related** :

```python
# OPTIMISÉ avec select_related
reset_queries()

articles = Article.objects.select_related('auteur').all()[:10]  # 1 requête avec JOIN

for article in articles:
    print(article.auteur.nom)  # Pas de requête supplémentaire !

print(f"Nombre de requêtes : {len(connection.queries)}")
# Résultat : 1 seule requête !
```

**Utilisation pratique** :

```python
# select_related pour éviter le N+1
articles = Article.objects.select_related('auteur').all()

for article in articles:
    # Accès à l'auteur sans nouvelle requête
    print(f"{article.titre} par {article.auteur.prenom} {article.auteur.nom}")
    print(f"  Email: {article.auteur.email}")

# Une seule requête au total !
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

## 🎉 Félicitations !

Vous avez complété le module Django ORM QuerySets et Optimisation. Vous maîtrisez maintenant :

✅ **QuerySets de base** : filter, exclude, get, count, exists  
✅ **Lookups avancés** : contains, startswith, gt, lt, range, regex  
✅ **Q objects** : Requêtes complexes avec OR, AND, NOT  
✅ **F expressions** : Comparaisons et opérations côté base de données  
✅ **Agrégations** : Count, Sum, Avg, Max, Min, annotations  
✅ **Fonctions de base de données** : Concat, Upper, Lower, TruncDate  
✅ **Case/When** : Conditions et logique conditionnelle  
✅ **select_related** : Optimisation ForeignKey (JOINs)  

### 📚 Pour aller plus loin

- **Django Documentation** : https://docs.djangoproject.com/en/stable/topics/db/queries/
- **QuerySet API Reference** : https://docs.djangoproject.com/en/stable/ref/models/querysets/
- **Database Optimization** : https://docs.djangoproject.com/en/stable/topics/db/optimization/

**Prochain module** : 18 - Django ORM PostgreSQL & Projet complet 🚀
