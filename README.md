# Exercices Python

Ce dépôt contient des exercices pratiques pour apprendre les bases du langage Python. Chaque exercice comprend :
- Un dossier **énoncé/** avec les instructions détaillées et fichiers de départ
- Un dossier **correction/** avec la solution complète

## Liste des exercices

### 01-introduction
**Découverte de Python**
- Utilisation de la fonction `print()`
- Opérations arithmétiques et priorités
- Opérateurs mathématiques (puissance, modulo)
- Questions bonus pour approfondir

### 02-variables
**Gestion d'un catalogue de produits**
- Déclaration et manipulation de variables
- Formatage avec f-strings
- Calculs de prix (réductions, TVA)
- Gestion de devises

### 03-types
**Système d'inventaire**
- Types de données primitifs (str, int, float, bool)
- Fonction `type()` et conversion de types
- Calculs sur les stocks
- Opérateurs de comparaison

### 04-listes
**Gestion de langages de programmation**
- Création et manipulation de listes
- Méthodes : append, remove, insert, sort, reverse
- Indexation et slicing
- Opérateurs et vérifications
- **List comprehensions** : filtrage, transformation, conditions ternaires

### 05-dictionnaires
**Système de notation d'étudiants**
- Création et manipulation de dictionnaires
- Méthodes : keys, values, items
- Calculs statistiques (moyenne)
- Vérification d'existence de clés
- **Dictionary comprehensions** : création, filtrage, transformation conditionnelle

### 06-boucles
**Boucles et Algorithmes**
- Boucles `for` et `while`
- Exercices algorithmiques : nombres premiers, factorielle, Fibonacci
- Recherche et traitement de données
- Pyramides et patterns
- Optimisation algorithmique

### 07-fonctions
**Fonctions et Algorithmes avancés**
- Définition et appel de fonctions
- Paramètres et valeurs de retour
- Récursivité et mémoïsation
- Algorithmes classiques : tri, PGCD, palindromes
- FizzBuzz et anagrammes
- Conversion et formatage

### 08-fichiers-csv
**Gestion de bibliothèque**
- Lecture et écriture de fichiers CSV
- Pattern Extract-Transform-Load (ETL)
- Calculs conditionnels
- Fonctions de traitement de données

---

## Programmation Orientée Objet (POO)

### 09-classes-objets
**Introduction à la POO**
- Création de classes et objets
- Attributs d'instance et de classe
- Méthodes et constructeur `__init__`
- Méthodes spéciales (`__str__`, `__repr__`)
- Interactions entre objets
- Gestion de collections d'objets

### 10-encapsulation-proprietes
**Encapsulation et contrôle d'accès**
- Attributs protégés et privés (`_`, `__`)
- Getters et setters
- Décorateur `@property`
- Validation des données
- Properties calculées et read-only
- Méthodes privées

### 11-heritage-polymorphisme
**Héritage et polymorphisme**
- Héritage simple et multiple
- Classes parentes et enfants
- Override de méthodes
- Fonction `super()`
- Polymorphisme et duck typing
- Hiérarchies de classes complexes
- Composition vs héritage

### 12-projet-poo-complet
**Projets intégrateurs**
- Projet 1 : Système de gestion de bibliothèque
- Projet 2 : Système de gestion d'école
- Projet 3 : Plateforme e-commerce
- Projet 4 : Jeu de combat RPG
- Intégration de tous les concepts POO
- Architecture logicielle complète

---

## Django Web Framework

### 13-django-introduction
**Premiers pas avec Django**
- Installation et configuration
- Structure d'un projet Django
- Applications Django
- Serveur de développement
- Base de données et migrations
- Interface d'administration
- Configuration de l'environnement

### 14-django-models-orm
**Modèles et ORM**
- Création de modèles
- Types de champs
- Relations (ForeignKey, ManyToMany, OneToOne)
- Migrations de base de données
- QuerySets et requêtes ORM
- Filtrage et agrégation
- Managers personnalisés
- Signaux

### 15-django-views-urls
**Vues et routage**
- Function-Based Views (FBV)
- Class-Based Views (CBV)
- ListView, DetailView, CreateView, UpdateView, DeleteView
- Configuration des URLs
- Paramètres d'URL (int, slug, str)
- Redirections et reverse
- Mixins réutilisables
- Pagination

### 16-django-templates
**Système de templates**
- Template inheritance
- Variables et filtres
- Tags conditionnels et boucles
- Template tags personnalisés
- Filtres personnalisés
- Static files (CSS, JS, images)
- Inclusion de templates
- Context processors
- Messages framework

### 17-django-forms-validation
**Formulaires et validation**
- Django Forms
- ModelForms
- Validation de données
- Widgets personnalisés
- Formsets et inline formsets
- Upload de fichiers
- Rendu manuel de formulaires
- Messages d'erreur
- CSRF protection

### 18-django-admin-auth
**Administration et authentification**
- Personnalisation de l'admin Django
- ModelAdmin et configurations
- Inline admin
- Actions personnalisées
- Système d'authentification
- Login, Logout, Register
- Permissions et groupes
- Profil utilisateur
- Reset de mot de passe

### 19-django-rest-api
**API REST avec DRF**
- Installation Django REST Framework
- Serializers et ModelSerializers
- APIView et Generic Views
- ViewSets et Routers
- Authentification (Token, Session)
- Permissions personnalisées
- Filtrage et recherche
- Pagination
- Throttling
- Documentation Swagger

### 20-django-projet-complet
**Projets Django complets**
- Projet 1 : Plateforme de Blog avancée
- Projet 2 : Plateforme E-learning
- Projet 3 : Réseau Social
- Projet 4 : Task Manager (type Trello)
- Intégration complète (Models, Views, Templates, Forms, API)
- Tests et déploiement
- Best practices Django

### 21-django-postgresql
**Django avec PostgreSQL**
- Installation et configuration PostgreSQL
- Migration SQLite vers PostgreSQL
- Types de données PostgreSQL (ArrayField, JSONField)
- Full-text search
- Indexes et optimisation de performance
- Contraintes et triggers PostgreSQL
- Vues matérialisées
- Connexions multiples
- Backup et restore
- Docker et PostgreSQL
- PgAdmin

---

## Python Perfectionnement

### 22-python-avance-rappels
**Fondamentaux avancés**
- Affectation par référence vs copie
- Types mutables vs immutables
- Passage d'arguments avancé (*args, **kwargs)
- Variables de classe vs instance
- Slices avancés
- Introspection (dir, type, inspect)
- Clause else dans for/while/try
- **TP** : Optimisation intersection de listes
- Complexité algorithmique (Big O)

### 23-decorateurs-closures
**Fonctions avancées**
- Closures et scope
- Décorateurs simples et paramétrés
- Décorateurs de classe
- Chaînage de décorateurs
- Design Patterns (Observer, Factory)
- Générateurs et yield
- Pipeline de consommateurs
- **TP** : Système d'événements avec décorateurs
- **TP** : Pipeline de traitement de données

### 24-poo-avancee
**POO niveau expert**
- Itérateurs personnalisés (`__iter__`, `__next__`)
- Générateurs (yield, yield from)
- Héritage multiple et MRO
- Mixins
- Context Managers (`__enter__`, `__exit__`)
- Classes abstraites (ABC)
- Métaclasses
- Descriptors
- **TP** : Métaclasse Singleton
- **TP** : ORM simplifié avec métaclasse

### 25-packaging-deploiement
**Distribution et environnements**
- Structure de package Python
- setup.py et setuptools
- pyproject.toml (moderne)
- virtualenv, venv, poetry, pipenv
- Tests avec pytest
- PyPI et TestPyPI
- Buildout
- Entry points et CLI
- **TP** : Publier un package sur PyPI

### 26-performance-profiling
**Optimisation et mesure**
- timeit pour micro-benchmarks
- cProfile pour profiling complet
- line_profiler (ligne par ligne)
- memory_profiler (analyse mémoire)
- Optimisation de code (comprehensions, générateurs)
- Structures de données optimales
- Complexité algorithmique pratique
- Memoization et caching
- **TP** : Profiler et optimiser un algorithme

### 27-parallelisme-distribue
**Calcul parallèle et distribué**
- GIL (Global Interpreter Lock)
- Threading pour I/O-bound
- Multiprocessing pour CPU-bound
- concurrent.futures (ThreadPoolExecutor, ProcessPoolExecutor)
- Celery : installation et configuration
- Tâches asynchrones et retry
- Chaînes et groupes de tâches
- Flower pour monitoring
- **TP** : Map-Reduce avec Celery
- **TP** : Calcul distribué de nombres premiers
