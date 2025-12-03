<div align="center">

# Formation Python

[Démarrage](#démarrage-rapide) • [Modules](#programme) • [Projets](#projets)

</div>

---

## Table des Matières

- [Aperçu](#aperçu)
- [Démarrage Rapide](#démarrage-rapide)
- [Programme](#programme)
  - [Fondamentaux](#fondamentaux-01-08)
  - [Regex & Base de Données](#regex--base-de-données-09)
  - [Outils de Qualité de Code](#outils-de-qualité-de-code-10)
  - [Programmation Orientée Objet](#programmation-orientée-objet-11-14)
  - [Framework Django](#framework-django-15-19)
  - [Python Avancé](#python-avancé-20-25)
- [Projets](#projets)

---

## Aperçu

Ce dépôt contient **25 modules complets** couvrant Python des fondamentaux aux concepts experts, incluant le développement web avec Django et des sujets avancés comme la métaprogrammation et le calcul distribué.

## Démarrage Rapide

### Prérequis

```bash
# Python 3.8 ou supérieur
python --version

# Gestionnaire de paquets pip
pip --version
```

### Installation

```bash
# Cloner le dépôt
git clone https://github.com/htajmoua/python-exercises-complete.git
cd python-exercises-complete

# Naviguer vers un module
cd 01-introduction/exercises

# Lire les instructions: instructions.md

# Exécuter les exercices
python main.py
```

### Structure du Projet

```
nom-module/
└── exercises/
    ├── instructions.md    # Exercices détaillés et théorie
    ├── main.py           # Code de départ avec exemples
    └── [fichiers annexes] # Fichiers supports (CSV, DB, etc.)
```

---

## Programme

### Fondamentaux (01-08)

Construisez des bases solides avec les concepts essentiels de Python.

<details>
<summary><b>Module 01 : Introduction</b> - Premiers pas avec Python</summary>

- Utilisation de la fonction `print()`
- Opérations arithmétiques et priorités
- Opérateurs mathématiques (puissance, modulo)
- Défis bonus

</details>

<details>
<summary><b>Module 02 : Variables</b> - Stockage et manipulation de données</summary>

- Déclaration et affectation de variables
- Formatage de chaînes (f-strings)
- Calculs de prix (réductions, TVA)
- Gestion des devises

</details>

<details>
<summary><b>Module 03 : Types de Données</b> - Système de types</summary>

- Types primitifs (str, int, float, bool)
- Fonction `type()` et conversion de types
- Calculs sur les stocks
- Opérateurs de comparaison

</details>

<details>
<summary><b>Module 04 : Listes</b> - Structures de données séquentielles</summary>

- Création et manipulation de listes
- Méthodes : `append`, `remove`, `insert`, `sort`, `reverse`
- Indexation et slicing
- **List comprehensions** : filtrage, transformation

</details>

<details>
<summary><b>Module 05 : Dictionnaires</b> - Paires clé-valeur</summary>

- Opérations sur les dictionnaires
- Méthodes : `keys()`, `values()`, `items()`
- Calculs statistiques (moyenne)
- **Dict comprehensions** : création dynamique

</details>

<details>
<summary><b>Module 06 : Boucles</b> - Itération et algorithmes</summary>

- Boucles `for` et `while`
- Exercices algorithmiques : nombres premiers, factorielle, Fibonacci
- Recherche et traitement de données
- Motifs et pyramides

</details>

<details>
<summary><b>Module 07 : Fonctions</b> - Réutilisabilité du code</summary>

- Définition et appels de fonctions
- Paramètres et valeurs de retour
- Récursivité et mémoïsation
- Algorithmes classiques : tri, PGCD, palindromes

</details>

<details>
<summary><b>Module 08 : Fichiers & CSV</b> - Persistance des données</summary>

- Lecture et écriture de fichiers
- Utilisation du module CSV
- Pattern ETL (Extract-Transform-Load)
- Pipelines de traitement de données

</details>

---

### Regex & Base de Données (09)

Maîtrisez les expressions régulières et la persistance des données.

<details>
<summary><b>Module 09 : Expressions Régulières & SQLite</b> - Pattern matching et base de données</summary>

**Expressions Régulières** :
- Validation (email, téléphone, dates)
- Extraction de données (URLs, IPs, emails)
- Parsing de logs
- Validation de mots de passe

**Base de Données SQLite** :
- Conception de base de données (3 tables avec relations)
- Opérations CRUD (Create, Read, Update, Delete)
- Requêtes SQL et jointures
- Application CLI (gestion de bibliothèque)

</details>

---

### Outils de Qualité de Code (10)

Apprenez à écrire du code Python professionnel et maintenable.

<details>
<summary><b>Module 10 : Outils de Qualité de Code</b> - Black, Ruff, Mypy, Pytest</summary>

**Outils essentiels** :
- **Black** : Formatage automatique de code
- **Ruff** : Linting ultra-rapide (erreurs, mauvaises pratiques)
- **Mypy** : Vérification de types statique
- **Pytest** : Framework de tests automatisés

**Configuration** :
- Fichier `pyproject.toml` centralisé
- Script d'automatisation
- Pre-commit hooks (bonus)
- Intégration CI/CD

**Compétences acquises** :
- Code formaté selon PEP 8
- Détection automatique des bugs
- Type hints Python
- Tests avec couverture de code
- Workflow professionnel

⏱️ **Durée** : 45 min - 1h

</details>

---

### Programmation Orientée Objet (11-14)

Maîtrisez les principes de la POO et les design patterns.

<details>
<summary><b>Module 11 : Classes & Objets</b> - Introduction à la POO</summary>

- Création de classes et d'objets
- Attributs d'instance et de classe
- Méthodes et constructeur `__init__`
- Méthodes spéciales (`__str__`, `__repr__`)
- Interactions entre objets

</details>

<details>
<summary><b>Module 12 : Encapsulation & Propriétés</b> - Protection des données</summary>

- Attributs protégés et privés (`_`, `__`)
- Getters et setters
- Décorateur `@property`
- Validation des données
- Propriétés calculées et en lecture seule

</details>

<details>
<summary><b>Module 13 : Héritage & Polymorphisme</b> - Réutilisation du code</summary>

- Héritage simple et multiple
- Override de méthodes
- Fonction `super()`
- Polymorphisme et duck typing
- Composition vs héritage

</details>

<details>
<summary><b>Module 14 : Projets POO Complets</b> - Intégration</summary>

**4 Projets Complets** :
1. **Système de Gestion de Bibliothèque** - Livres, auteurs, emprunts
2. **Système de Gestion d'École** - Étudiants, cours, notes
3. **Plateforme E-commerce** - Produits, panier, commandes
4. **Jeu de Combat RPG** - Personnages, combats, inventaire

Intégration de tous les concepts POO dans des applications réelles.

</details>

---

### Framework Django (15-19)

Construisez des applications Backend professionnelles avec Django et PostgreSQL.

<details>
<summary><b>Module 15 : Introduction à Django</b> - Premiers pas</summary>

**Théorie** :
- Rappel des principes POO
- **Pattern MVC/MTV**
- Architecture et composants Django
- Virtualenv et gestion de dépendances

**Pratique** :
- Installation et configuration
- Création de projet et application
- Serveur de développement
- Interface d'administration
- Migrations de base de données
- Variables d'environnement
- Premier endpoint API (JSON)

</details>

<details>
<summary><b>Module 16 : Modèles & ORM Django</b> - Architecture de données</summary>

**Tutoriels guidés** (Exercices 1-8) :
- Types de champs Django
- Relations **ForeignKey** (1-N)
- Relations **ManyToMany** (N-N) - Tutoriel complet
- Relations **OneToOne** (1-1) - Tutoriel complet
- **Héritage Abstract** - Tutoriel complet
- **Héritage Multi-table** - Tutoriel complet
- **Modèles Proxy** - Tutoriel complet

**Exercices pratiques** (Exercices 9+) :
- Validation personnalisée
- Méthodes de modèles
- Meta options

**Format** : 5 tutoriels guidés + exercices autonomes

</details>

<details>
<summary><b>Module 17 : QuerySets & Optimisation ORM</b> - Performance</summary>

**Théorie** :
- Lazy evaluation
- QuerySet API complète
- Problème N+1

**Exercices pratiques** :
- **Q objects** pour requêtes complexes (avec hints)
- **select_related** pour ForeignKey/OneToOne (avec hints)
- **prefetch_related** pour ManyToMany (avec hints)
- Annotations et agrégations
- **only()** / **defer()** pour optimisation
- Transactions
- Raw SQL

**Fichier SOLUTIONS.md** fourni avec code complet et exemples

</details>

<details>
<summary><b>Module 18 : Projet ORM Complet avec PostgreSQL</b> - Production ⭐</summary>

**Format** : **100% Tutoriel guidé** - Projet fil rouge complet

**Projet** : BlogPro - Plateforme de blog professionnelle

**6 Parties progressives** :
1. **Setup PostgreSQL** - Docker, configuration Django
2. **Architecture** - Classes abstraites, managers, relations
3. **PostgreSQL Features** - Full-text search, statistiques, indexes
4. **Signals & Cache** - Automatisation
5. **Tests** - Tests unitaires complets (>80% coverage)
6. **Admin & Production** - Interface personnalisée, backup

**Stack** : Django 5.0 + PostgreSQL 15 + Docker

**Fonctionnalités** :
- 4 classes abstraites réutilisables (Timestamped, UUID, SoftDelete, Publishable)
- Managers et QuerySets personnalisés avec méthodes chaînables
- ArrayField et SearchVectorField (PostgreSQL)
- Full-text search performant
- Analytics et statistiques complexes
- Signals pour cache automatique
- Indexes optimisés
- Admin Django personnalisé
- Commande de gestion pour données de test

**Dossier SOLUTION/** : Code complet fonctionnel (16 fichiers)

⏱️ **Durée** : 8-10 heures

</details>

<details>
<summary><b>Module 19 : Admin & Authentification Django</b> - Gestion</summary>

- Personnalisation complète de l'admin
- Configuration ModelAdmin avancée
- Inlines et relations
- Actions personnalisées bulk
- Filtres et recherche
- Système d'authentification Django
- Login, logout, inscription
- Permissions et groupes
- Profils utilisateur étendus
- Décorateurs de permissions

</details>

---

### Python Avancé (20-25)

Concepts experts et optimisation des performances.

<details>
<summary><b>Module 20 : Fondamentaux Python Avancés</b> - Approfondissement</summary>

- Références vs copies (mutable/immutable)
- Arguments avancés (`*args`, `**kwargs`)
- Variables de classe vs d'instance
- Techniques de slicing avancées
- Introspection (dir, type, inspect)
- Clause else dans for/while/try
- Complexité algorithmique (notation Big O)

</details>

<details>
<summary><b>Module 21 : Décorateurs & Closures</b> - Métaprogrammation</summary>

- Closures et portées
- Décorateurs simples et paramétrés
- Décorateurs de classe
- Chaînage de décorateurs
- Design patterns (Observer, Factory)
- Générateurs avec `yield`
- Système d'événements

</details>

<details>
<summary><b>Module 22 : POO Avancée</b> - Patterns experts</summary>

- Itérateurs personnalisés (`__iter__`, `__next__`)
- Générateurs (`yield`, `yield from`)
- Héritage multiple et MRO
- Mixins
- Context managers (`__enter__`, `__exit__`)
- Classes abstraites (ABC)
- **Métaclasses**
- Descriptors
- **TP** : Métaclasse Singleton, ORM simplifié

</details>

<details>
<summary><b>Module 23 : Packaging & Déploiement</b> - Distribution</summary>

- Structure de package Python
- `setup.py` et setuptools
- `pyproject.toml` (approche moderne)
- Environnements virtuels (venv, poetry, pipenv)
- Tests avec pytest
- Publication sur PyPI
- Entry points et outils CLI

</details>

<details>
<summary><b>Module 24 : Performance & Profiling</b> - Optimisation</summary>

- `timeit` pour micro-benchmarks
- `cProfile` pour profiling complet
- `line_profiler` (analyse ligne par ligne)
- `memory_profiler` (usage mémoire)
- Techniques d'optimisation du code
- Structures de données optimales
- Mémoïsation et caching
- Complexité algorithmique en pratique

</details>

<details>
<summary><b>Module 25 : Parallélisme & Calcul Distribué</b> - Scalabilité</summary>

- GIL (Global Interpreter Lock) expliqué
- `threading` pour tâches I/O-bound
- `multiprocessing` pour tâches CPU-bound
- `concurrent.futures` (ThreadPoolExecutor, ProcessPoolExecutor)
- **Celery** : tâches async, queues, workers
- Chaînes et groupes de tâches
- Implémentation Map-Reduce
- Calcul distribué de nombres premiers

</details>

---

## Projets

Ce cours inclut **6 projets complets** :

### Projets POO (Module 14)
- 🏛️ **Système de Gestion de Bibliothèque** - Livres, auteurs, emprunts
- 🎓 **Système de Gestion d'École** - Étudiants, cours, notes
- 🛒 **Plateforme E-commerce** - Produits, panier, commandes
- ⚔️ **Jeu de Combat RPG** - Personnages, combats, inventaire

### Projet Django ORM avec PostgreSQL (Module 18)
- 📝 **BlogPro** - Plateforme de blog professionnelle
  - Architecture complète (classes abstraites, managers, relations)
  - PostgreSQL avec Docker
  - Full-text search performant
  - Analytics et statistiques
  - Tests unitaires (>80% coverage)
  - Interface admin personnalisée
  - **Dossier SOLUTION/** avec code complet

### Projets Python Avancé
- 🔧 **ORM Personnalisé** avec Métaclasses (Module 22)
- 🚀 **Système Map-Reduce Distribué** (Module 25)

---

<div align="center">

**Bon apprentissage !**


[⬆ Retour en haut](#formation-python)

</div>
