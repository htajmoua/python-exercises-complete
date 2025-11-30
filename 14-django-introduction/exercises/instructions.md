# Instructions - Django Introduction

Bienvenue dans le monde de Django ! Ce module vous guidera à travers l'installation et la création de votre premier projet Django.

## Partie 0 - Rappels et Concepts Fondamentaux

### Rappel des Principes de la POO

Django s'appuie fortement sur la Programmation Orientée Objet. Voici les concepts clés utilisés :

**1. Classes et Objets**
```python
# Exemple : Modèle Django (classe)
class Article(models.Model):
    titre = models.CharField(max_length=200)
    contenu = models.TextField()

# Instance (objet)
mon_article = Article(titre="Django POO", contenu="...")
```

**2. Héritage**
```python
# Les modèles Django héritent de models.Model
class Article(models.Model):  # Héritage
    pass

# Les vues Django héritent de classes génériques
class ArticleListView(ListView):  # Héritage
    model = Article
```

**3. Encapsulation**
- Django encapsule la logique de base de données dans l'ORM
- Les propriétés et méthodes privées protègent les données

**4. Polymorphisme**
- Différentes vues peuvent hériter de la même classe de base
- Les modèles peuvent avoir des comportements différents via l'override

### Le Design Pattern MVC et MTV de Django

**MVC (Model-View-Controller)** est un pattern classique de séparation des responsabilités.

**MTV (Model-Template-View)** est l'adaptation Django du pattern MVC :

```
┌─────────────────────────────────────────────────┐
│           ARCHITECTURE MTV DJANGO               │
├─────────────────────────────────────────────────┤
│                                                 │
│  CLIENT (Navigateur)                            │
│       │                                         │
│       ↓                                         │
│  ┌─────────────┐         ┌──────────────┐     │
│  │   URLS.PY   │ ------> │    VIEW      │     │
│  │  (Routeur)  │         │  (Contrôleur)│     │
│  └─────────────┘         └──────────────┘     │
│                                 │               │
│                    ┌────────────┼────────────┐ │
│                    ↓                          ↓ │
│              ┌──────────┐            ┌──────────┐│
│              │  MODEL   │            │ TEMPLATE ││
│              │ (Données)│            │   (Vue)  ││
│              └──────────┘            └──────────┘│
│                    │                          │  │
│                    ↓                          ↓  │
│              ┌──────────┐            ┌──────────┐│
│              │   BDD    │            │   HTML   ││
│              └──────────┘            └──────────┘│
└─────────────────────────────────────────────────┘
```

**Correspondance MVC ↔ MTV** :

| MVC | MTV Django | Rôle |
|-----|------------|------|
| **Model** | **Model** | Gestion des données (ORM, DB) |
| **View** | **Template** | Présentation (HTML, CSS) |
| **Controller** | **View** | Logique métier |
| *Router* | **urls.py** | Routage des requêtes |

**Exemple de flux MTV** :

1. **URLs** : `/articles/` → Route vers la vue
2. **View** : Récupère les données du Model
3. **Model** : Interroge la base de données
4. **Template** : Reçoit les données et génère le HTML
5. **Réponse** : HTML renvoyé au client

```python
# urls.py (Routeur)
urlpatterns = [
    path('articles/', views.article_list, name='article-list'),
]

# views.py (Contrôleur/Logique)
def article_list(request):
    articles = Article.objects.all()  # MODEL
    return render(request, 'articles.html', {'articles': articles})  # TEMPLATE

# models.py (Données)
class Article(models.Model):
    titre = models.CharField(max_length=200)
    contenu = models.TextField()

# articles.html (Présentation)
# {% for article in articles %}
#   <h2>{{ article.titre }}</h2>
# {% endfor %}
```

### Présentation du Framework Django

**Origine et Historique**
- Créé en 2003 par Adrian Holovaty et Simon Willison
- Développé pour le journal Lawrence Journal-World
- Open source depuis 2005
- Nom inspiré par le guitariste Django Reinhardt

**Objectifs et Avantages**
- **Rapidité de développement** : "The web framework for perfectionists with deadlines"
- **Sécurité** : Protection contre CSRF, XSS, SQL Injection
- **Scalabilité** : Utilisé par Instagram, Pinterest, Mozilla
- **Batteries included** : ORM, Admin, Forms, Auth intégrés
- **DRY** (Don't Repeat Yourself) : Code réutilisable

**Les Composants du Framework Django**

| Composant | Description |
|-----------|-------------|
| **ORM** | Abstraction de base de données (PostgreSQL, MySQL, SQLite) |
| **Admin** | Interface d'administration automatique |
| **Forms** | Gestion et validation de formulaires |
| **Templates** | Moteur de templates (syntaxe {% %}) |
| **Auth** | Système d'authentification complet |
| **Middleware** | Traitement des requêtes/réponses |
| **Migrations** | Versioning de schéma de base de données |
| **URLconf** | Routage URL élégant |
| **Cache** | Framework de cache intégré |
| **Signals** | Système d'événements |

---

## Prérequis

- Python 3.8+ installé
- pip (gestionnaire de paquets Python)
- Environnement virtuel (venv)
- Connaissances en POO (voir rappels ci-dessus)

## Exercice 1 - Installation de Django

**Créez** un environnement virtuel et installez Django :

```bash
# Créer un environnement virtuel
python -m venv venv

# Activer l'environnement virtuel
# Sur Mac/Linux :
source venv/bin/activate
# Sur Windows :
venv\Scripts\activate

# Installer Django
pip install django

# Vérifier l'installation
python -m django --version
```

## Exercice 2 - Créer un projet Django

**Créez** votre premier projet Django nommé `monprojet` :

```bash
django-admin startproject monprojet
cd monprojet
```

**Explorez** la structure créée :
- `manage.py` : Script pour interagir avec le projet
- `monprojet/` : Package Python du projet
  - `__init__.py` : Fichier Python vide
  - `settings.py` : Configuration du projet
  - `urls.py` : Routes URL du projet
  - `asgi.py` : Point d'entrée ASGI
  - `wsgi.py` : Point d'entrée WSGI

## Exercice 3 - Lancer le serveur de développement

**Lancez** le serveur de développement :

```bash
python manage.py runserver
```

**Accédez** à `http://127.0.0.1:8000/` dans votre navigateur.  
Vous devriez voir la page d'accueil par défaut de Django 

## Exercice 4 - Créer une application

**Créez** une application Django nommée `blog` :

```bash
python manage.py startapp blog
```

**Explorez** la structure de l'application :
- `migrations/` : Dossier pour les migrations de base de données
- `__init__.py` : Fichier Python vide
- `admin.py` : Configuration de l'admin Django
- `apps.py` : Configuration de l'application
- `models.py` : Modèles de données
- `tests.py` : Tests unitaires
- `views.py` : Vues de l'application

## Exercice 5 - Enregistrer l'application

**Modifiez** `monprojet/settings.py` pour enregistrer l'application :

```python
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'blog',  # Ajoutez votre application
]
```

## Exercice 6 - Configuration de la base de données

**Explorez** la configuration par défaut dans `settings.py` :

```python
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}
```

**Créez** la base de données avec les migrations initiales :

```bash
python manage.py migrate
```

Observez le fichier `db.sqlite3` créé à la racine du projet.

## Exercice 7 - Créer un superutilisateur

**Créez** un compte administrateur :

```bash
python manage.py createsuperuser
```

Suivez les instructions pour définir :
- Username (nom d'utilisateur)
- Email
- Password (mot de passe)

**Accédez** à l'interface d'administration : `http://127.0.0.1:8000/admin/`

## Exercice 8 - Configurer le fuseau horaire et la langue

**Modifiez** `settings.py` :

```python
LANGUAGE_CODE = 'fr-fr'  # Français
TIME_ZONE = 'Europe/Paris'  # Fuseau horaire Paris
USE_I18N = True  # Internationalisation
USE_TZ = True  # Timezone aware
```

**Redémarrez** le serveur et vérifiez que l'admin est en français.

## Exercice 9 - Premier fichier de configuration personnalisé

**Créez** un fichier `.env` pour les variables d'environnement (à la racine) :

```
SECRET_KEY=votre-cle-secrete-ultra-longue-et-aleatoire
DEBUG=True
```

**Installez** python-decouple :

```bash
pip install python-decouple
```

**Modifiez** `settings.py` :

```python
from decouple import config

SECRET_KEY = config('SECRET_KEY')
DEBUG = config('DEBUG', default=False, cast=bool)
```

## Exercice 10 - Créer une page d'accueil simple

**Créez** une vue simple dans `blog/views.py` :

```python
from django.http import HttpResponse

def home(request):
    return HttpResponse("<h1>Bienvenue sur mon site Django !</h1>")
```

**Créez** un fichier `blog/urls.py` :

```python
from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
]
```

**Modifiez** `monprojet/urls.py` :

```python
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('blog.urls')),
]
```

**Accédez** à `http://127.0.0.1:8000/` et voyez votre message !

## Exercice 11 - Requirements.txt

**Créez** un fichier `requirements.txt` pour sauvegarder les dépendances :

```bash
pip freeze > requirements.txt
```

**Vérifiez** le contenu du fichier. Il devrait contenir Django et python-decouple.

## Exercice 12 - Gitignore

**Créez** un fichier `.gitignore` :

```
# Python
*.pyc
__pycache__/
*.py[cod]
*$py.class

# Django
*.log
db.sqlite3
media/

# Environnement virtuel
venv/
env/

# IDE
.vscode/
.idea/

# Environnement
.env
```

## Exercices bonus

### Exercice 13 - Multiple applications
**Créez** une deuxième application `portfolio` et configurez-la.

### Exercice 14 - Custom management command
**Créez** une commande personnalisée dans `blog/management/commands/hello.py` qui affiche "Hello Django!".

### Exercice 15 - Serveur sur un port personnalisé
**Lancez** le serveur sur le port 8080 au lieu de 8000.

## Checklist de validation

-  Django installé dans un environnement virtuel
-  Projet Django créé avec succès
-  Application `blog` créée et enregistrée
-  Base de données migrée
-  Superutilisateur créé
-  Interface admin accessible et en français
-  Page d'accueil personnalisée fonctionnelle
-  Variables d'environnement configurées
-  `requirements.txt` et `.gitignore` créés
