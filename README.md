<div align="center">

# Formation Python

[Démarrage](#-démarrage-rapide) • [Modules](#-programme) • [Projets](#-projets)

</div>

---

## Table des Matières

- [Aperçu](#-aperçu)
- [Démarrage Rapide](#-démarrage-rapide)
- [Programme](#-programme)
  - [Fondamentaux](#-fondamentaux-01-08)
  - [Regex & Base de Données](#-regex--base-de-données-09)
  - [Programmation Orientée Objet](#-programmation-orientée-objet-10-13)
  - [Framework Django](#-framework-django-14-22)
  - [Python Avancé](#-python-avancé-23-28)
- [Projets](#-projets)

---

## Aperçu

Ce dépôt contient **28 modules complets** couvrant Python des fondamentaux aux concepts experts, incluant le développement web avec Django et des sujets avancés comme la métaprogrammation et le calcul distribué.

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

### Programmation Orientée Objet (10-13)

Maîtrisez les principes de la POO et les design patterns.

<details>
<summary><b>Module 10 : Classes & Objets</b> - Introduction à la POO</summary>

- Création de classes et d'objets
- Attributs d'instance et de classe
- Méthodes et constructeur `__init__`
- Méthodes spéciales (`__str__`, `__repr__`)
- Interactions entre objets

</details>

<details>
<summary><b>Module 11 : Encapsulation & Propriétés</b> - Protection des données</summary>

- Attributs protégés et privés (`_`, `__`)
- Getters et setters
- Décorateur `@property`
- Validation des données
- Propriétés calculées et en lecture seule

</details>

<details>
<summary><b>Module 12 : Héritage & Polymorphisme</b> - Réutilisation du code</summary>

- Héritage simple et multiple
- Override de méthodes
- Fonction `super()`
- Polymorphisme et duck typing
- Composition vs héritage

</details>

<details>
<summary><b>Module 13 : Projets POO Complets</b> - Intégration</summary>

**4 Projets Complets** :
1. **Système de Gestion de Bibliothèque** - Livres, auteurs, emprunts
2. **Système de Gestion d'École** - Étudiants, cours, notes
3. **Plateforme E-commerce** - Produits, panier, commandes
4. **Jeu de Combat RPG** - Personnages, combats, inventaire

Intégration de tous les concepts POO dans des applications réelles.

</details>

---

### Framework Django (14-22)

Construisez des applications web modernes avec Django.

<details>
<summary><b>Module 14 : Introduction à Django</b> - Premiers pas</summary>

**Théorie** :
- Rappel des principes POO
- **Pattern MVC/MTV**
- Architecture et composants Django

**Pratique** :
- Installation et configuration
- Structure du projet
- Serveur de développement
- Interface d'administration
- Migrations de base de données

</details>

<details>
<summary><b>Module 15 : Modèles & ORM</b> - Couche base de données</summary>

- Création de modèles et types de champs
- Relations : **ForeignKey** (1-N), **ManyToMany** (N-N), **OneToOne** (1-1)
- Migrations de base de données
- QuerySets et requêtes ORM
- **Héritage de Modèles** :
  - Classes de base abstraites
  - Héritage multi-table
  - Modèles Proxy
- Managers personnalisés et signaux

</details>

<details>
<summary><b>Module 16 : Vues & URLs</b> - Gestion des requêtes</summary>

- Function-Based Views (FBV)
- Class-Based Views (CBV)
- Vues génériques : ListView, DetailView, CreateView, UpdateView, DeleteView
- Configuration des URLs et routage
- Paramètres d'URL (int, slug, str)
- Redirections et `reverse()`

</details>

<details>
<summary><b>Module 17 : Templates</b> - Couche de présentation</summary>

- Héritage de templates
- Variables, filtres et tags
- Structures de contrôle (if, for)
- Tags et filtres personnalisés
- Fichiers statiques (CSS, JS, images)
- Context processors

</details>

<details>
<summary><b>Module 18 : Formulaires & Validation</b> - Entrées utilisateur</summary>

- Django Forms
- ModelForms
- Validation et nettoyage des données
- Widgets personnalisés
- Formsets et inline formsets
- Upload de fichiers
- Protection CSRF

</details>

<details>
<summary><b>Module 19 : Admin & Authentification</b> - Gestion des utilisateurs</summary>

- Personnalisation de l'admin
- Configuration ModelAdmin
- Inline admin
- Actions personnalisées
- Système d'authentification
- Login, logout, inscription
- Permissions et groupes
- Profils utilisateur

</details>

<details>
<summary><b>Module 20 : API REST</b> - Django REST Framework</summary>

- Serializers et ModelSerializers
- API Views et ViewSets
- Routers
- Authentification (Token, Session)
- Permissions personnalisées
- Filtrage, recherche et pagination
- Throttling
- Documentation Swagger

</details>

<details>
<summary><b>Module 21 : Projets Django Complets</b> - Applications full-stack</summary>

**4 Projets Production-Ready** :
1. **Plateforme de Blog Avancée** - Multi-utilisateurs, commentaires, tags
2. **Plateforme E-learning** - Cours, leçons, quiz
3. **Réseau Social** - Posts, amis, messagerie
4. **Gestionnaire de Tâches** (type Trello) - Tableaux, listes, cartes

Applications complètes avec toutes les fonctionnalités Django intégrées.

</details>

<details>
<summary><b>Module 22 : Django & PostgreSQL</b> - Base de données de production</summary>

- Installation et configuration de PostgreSQL
- Migration de SQLite vers PostgreSQL
- Types spécifiques PostgreSQL (ArrayField, JSONField)
- Recherche full-text
- Optimisation des performances (indexes)
- Contraintes et triggers
- Intégration Docker
- Configuration PgAdmin

</details>

---

### Python Avancé (23-28)

Concepts experts et optimisation des performances.

<details>
<summary><b>Module 23 : Fondamentaux Python Avancés</b> - Approfondissement</summary>

- Références vs copies (mutable/immutable)
- Arguments avancés (`*args`, `**kwargs`)
- Variables de classe vs d'instance
- Techniques de slicing avancées
- Introspection (dir, type, inspect)
- Clause else dans for/while/try
- Complexité algorithmique (notation Big O)

</details>

<details>
<summary><b>Module 24 : Décorateurs & Closures</b> - Métaprogrammation</summary>

- Closures et portées
- Décorateurs simples et paramétrés
- Décorateurs de classe
- Chaînage de décorateurs
- Design patterns (Observer, Factory)
- Générateurs avec `yield`
- Système d'événements

</details>

<details>
<summary><b>Module 25 : POO Avancée</b> - Patterns experts</summary>

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
<summary><b>Module 26 : Packaging & Déploiement</b> - Distribution</summary>

- Structure de package Python
- `setup.py` et setuptools
- `pyproject.toml` (approche moderne)
- Environnements virtuels (venv, poetry, pipenv)
- Tests avec pytest
- Publication sur PyPI
- Entry points et outils CLI

</details>

<details>
<summary><b>Module 27 : Performance & Profiling</b> - Optimisation</summary>

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
<summary><b>Module 28 : Parallélisme & Calcul Distribué</b> - Scalabilité</summary>

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

Ce cours inclut **12 projets complets** :

### Projets POO
- Système de Gestion de Bibliothèque
- Système de Gestion d'École
- Plateforme E-commerce
- Jeu de Combat RPG

### Projets Django
- Plateforme de Blog Avancée
- Plateforme E-learning
- Réseau Social
- Gestionnaire de Tâches (type Trello)

### Projets Avancés
- ORM Personnalisé avec Métaclasses
- Pipeline de Traitement de Données
- Système Map-Reduce Distribué
- Études de Cas d'Optimisation

---

<div align="center">

**Bon apprentissage !**

[⬆ Retour en haut](#formation-python---programme-complet)

</div>
