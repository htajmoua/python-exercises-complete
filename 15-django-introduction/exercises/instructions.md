# Instructions - Django Introduction (Backend/API)

**🎯 Objectif** : Installer Django et créer votre premier projet Backend avec un endpoint API.

**📌 Note** : Formation **Backend/API** - Pas de templates ni formulaires web.

**📚 Format du module** :
- **Partie 1 (Exercices 1-9)** : Installation et configuration
- **Partie 2 (Exercices 10-12)** : Premier endpoint API (pratique)

**Durée** : 2-3 heures

---

# 📖 PARTIE 1 : EXEMPLES GUIDÉS

Suivez ces étapes pour installer et configurer Django.

---

## Exercice 1 - Installation de Django (EXEMPLE)

**Créez** un environnement virtuel :

```bash
# Créer l'environnement virtuel
python -m venv venv

# Activer l'environnement (macOS/Linux)
source venv/bin/activate

# Activer l'environnement (Windows)
venv\Scripts\activate
```

**Installez** Django et les outils Backend :

```bash
pip install django
pip install python-decouple  # Pour les variables d'environnement
pip install djangorestframework  # Pour les APIs (module 20)
pip install psycopg2-binary  # Pour PostgreSQL (optionnel)
```

**Vérifiez** l'installation :

```bash
python -m django --version
```

---

## Exercice 2 - Créer un projet Django (EXEMPLE)

**Créez** un nouveau projet :

```bash
django-admin startproject monprojet
cd monprojet
```

**Structure du projet** :

```
monprojet/
├── manage.py          # Commandes Django
└── monprojet/
    ├── __init__.py
    ├── settings.py    # Configuration
    ├── urls.py        # Routage principal
    ├── asgi.py        # Déploiement ASGI
    └── wsgi.py        # Déploiement WSGI
```

---

## Exercice 3 - Lancer le serveur de développement (EXEMPLE)

**Lancez** le serveur :

```bash
python manage.py runserver
```

**Accédez** à `http://127.0.0.1:8000/` dans votre navigateur.

Vous devriez voir la page de bienvenue Django !

---

## Exercice 4 - Créer une application (EXEMPLE)

Une **application** Django est un module réutilisable (ex: blog, api, users).

**Créez** une application `blog` :

```bash
python manage.py startapp blog
```

**Structure de l'application** :

```
blog/
├── migrations/     # Migrations de base de données
├── __init__.py
├── admin.py        # Configuration admin
├── apps.py         # Configuration app
├── models.py       # Modèles de données
├── tests.py        # Tests unitaires
└── views.py        # Vues/API endpoints
```

---

## Exercice 5 - Enregistrer l'application (EXEMPLE)

**Modifiez** `monprojet/settings.py` :

```python
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    
    # Vos applications
    'blog',
]
```

---

## Exercice 6 - Configuration de la base de données (EXEMPLE)

**Par défaut**, Django utilise SQLite. Pour PostgreSQL (production) :

**Modifiez** `settings.py` :

```python
# SQLite (développement)
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}

# PostgreSQL (production)
# DATABASES = {
#     'default': {
#         'ENGINE': 'django.db.backends.postgresql',
#         'NAME': 'monprojet_db',
#         'USER': 'postgres',
#         'PASSWORD': 'password',
#         'HOST': 'localhost',
#         'PORT': '5432',
#     }
# }
```

**Appliquez** les migrations initiales :

```bash
python manage.py migrate
```

---

## Exercice 7 - Créer un superutilisateur (EXEMPLE)

**Créez** un compte admin :

```bash
python manage.py createsuperuser
```

Entrez :
- Username
- Email
- Password

**Accédez** à l'admin : `http://127.0.0.1:8000/admin/`

---

## Exercice 8 - Configurer le fuseau horaire et la langue (EXEMPLE)

**Modifiez** `settings.py` :

```python
LANGUAGE_CODE = 'fr-fr'
TIME_ZONE = 'Europe/Paris'
USE_I18N = True
USE_TZ = True
```

**Redémarrez** le serveur et l'admin sera en français !

---

## Exercice 9 - Configuration avec variables d'environnement (EXEMPLE)

**Créez** un fichier `.env` :

```env
SECRET_KEY=votre-cle-secrete-django
DEBUG=True
DATABASE_URL=sqlite:///db.sqlite3
ALLOWED_HOSTS=localhost,127.0.0.1
```

**Modifiez** `settings.py` :

```python
from decouple import config

SECRET_KEY = config('SECRET_KEY')
DEBUG = config('DEBUG', default=False, cast=bool)
ALLOWED_HOSTS = config('ALLOWED_HOSTS', default='').split(',')
```

**Sécurité** : Ajoutez `.env` dans `.gitignore` !

---

# 🔨 PARTIE 2 : EXERCICES PRATIQUES

**À partir d'ici, c'est à vous de coder !** Les exercices suivants contiennent des squelettes avec des `TODO` à compléter.

---

## Exercice 10 - Créer un endpoint API simple (PRATIQUE)

**Objectif** : Créer votre premier endpoint API qui retourne du JSON.

**Consignes** :
1. Créez une vue `api_home` dans `blog/views.py` qui retourne un `JsonResponse`
2. Le JSON doit contenir 3 clés : `message`, `version`, `status`
3. Créez le fichier `blog/urls.py` avec le routage
4. Incluez les URLs de blog dans le fichier principal `urls.py`

**Squelette - `blog/views.py`** (à compléter) :

```python
from django.http import JsonResponse

def api_home(request):
    """Endpoint API simple qui retourne du JSON"""
    # TODO : Créez un dictionnaire avec :
    #   - message : "Bienvenue sur mon API Django !"
    #   - version : "1.0"
    #   - status : "active"
    
    data = {
        # VOTRE CODE ICI
    }
    
    # TODO : Retournez un JsonResponse avec le dictionnaire
    return # VOTRE CODE ICI
```

**Squelette - `blog/urls.py`** (fichier à créer) :

```python
from django.urls import path
from . import views

# TODO : Créez le urlpatterns avec une route vide ('') 
# qui pointe vers views.api_home avec le nom 'api-home'
urlpatterns = [
    # VOTRE CODE ICI
]
```

**Squelette - `monprojet/urls.py`** (à modifier) :

```python
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    # TODO : Ajoutez une route 'api/' qui inclut 'blog.urls'
    # VOTRE CODE ICI
]
```

**Indice** :
- `JsonResponse` prend un dictionnaire en paramètre
- `include('app.urls')` permet d'inclure les URLs d'une app

**Validation** :
1. Lancez le serveur : `python manage.py runserver`
2. Accédez à `http://127.0.0.1:8000/api/`
3. Vous devriez voir le JSON :
```json
{
  "message": "Bienvenue sur mon API Django !",
  "version": "1.0",
  "status": "active"
}
```

---

## Exercice 11 - Requirements.txt (PRATIQUE)

**Objectif** : Créer un fichier de dépendances pour votre projet.

**Consignes** :
1. Générez le fichier `requirements.txt` avec toutes les dépendances installées
2. Vérifiez que Django, python-decouple et djangorestframework sont présents
3. Testez l'installation des dépendances dans un nouvel environnement virtuel

**TODO** :
```bash
# TODO : Générez le fichier requirements.txt
# Commande à utiliser : pip freeze > requirements.txt
# VOTRE COMMANDE ICI
```

**Validation** :
1. Le fichier `requirements.txt` doit contenir au minimum :
   - `Django==...`
   - `python-decouple==...`
2. Pour tester (optionnel) :
```bash
# Créez un nouvel environnement virtuel
python -m venv test_env
source test_env/bin/activate  # ou test_env\Scripts\activate sur Windows

# TODO : Installez les dépendances depuis requirements.txt
# Utilisez : pip install -r requirements.txt
# VOTRE COMMANDE ICI
```

**Indice** :
- `pip freeze` liste toutes les dépendances installées
- `>` redirige la sortie vers un fichier

---

## Exercice 12 - Gitignore (PRATIQUE)

**Objectif** : Créer un fichier `.gitignore` pour éviter de versionner des fichiers inutiles.

**Consignes** :
1. Créez un fichier `.gitignore` à la racine du projet
2. Ajoutez les patterns pour ignorer :
   - Les fichiers Python compilés (`.pyc`, `__pycache__`)
   - La base de données SQLite
   - L'environnement virtuel
   - Le fichier `.env`
   - Les fichiers IDE

**Squelette - `.gitignore`** (fichier à créer) :

```
# TODO : Ajoutez les patterns pour Python
# Exemples : *.pyc, __pycache__/, *.py[cod]
# VOTRE CODE ICI

# TODO : Ajoutez les patterns pour Django
# Exemples : *.log, db.sqlite3, media/
# VOTRE CODE ICI

# TODO : Ajoutez le pattern pour l'environnement virtuel
# Exemples : venv/, env/, ENV/
# VOTRE CODE ICI

# TODO : Ajoutez les patterns pour IDE
# Exemples : .vscode/, .idea/
# VOTRE CODE ICI

# TODO : Ajoutez le pattern pour les variables d'environnement
# Exemple : .env
# VOTRE CODE ICI

# TODO : Ajoutez les patterns pour les fichiers OS
# Exemples : .DS_Store, Thumbs.db
# VOTRE CODE ICI
```

**Indice** :
- Consultez https://www.toptal.com/developers/gitignore/api/django,python
- Le fichier doit être nommé exactement `.gitignore` (avec le point au début)

**Validation** :
1. Créez le fichier `.gitignore`
2. Vérifiez que Git ignore bien les fichiers :
```bash
git status
# Les fichiers .pyc, db.sqlite3, .env ne doivent PAS apparaître
```

---

## Exercices bonus (PRATIQUE)

### Exercice 13 - Multiple applications (PRATIQUE)

**Objectif** : Organiser le code en créant une app dédiée aux API.

**Consignes** :
1. Créez une nouvelle application Django nommée `api`
2. Ajoutez-la à `INSTALLED_APPS` dans `settings.py`
3. Créez une vue `api_info` qui retourne les informations de l'API

**TODO** :
```bash
# TODO : Créez l'application api
# Commande : python manage.py startapp ...
# VOTRE COMMANDE ICI
```

**Validation** :
- L'application `api` apparaît dans le dossier du projet
- `api` est dans `INSTALLED_APPS`

---

### Exercice 14 - Custom management command (PRATIQUE)

**Objectif** : Créer une commande Django personnalisée.

**Consignes** :
1. Créez la structure de dossiers `blog/management/commands/`
2. Créez un fichier `seed_data.py` dans ce dossier
3. La commande doit afficher "Génération de données..." quand on l'exécute

**Structure à créer** :
```
blog/
├── management/
│   ├── __init__.py        # TODO : Créez ce fichier vide
│   └── commands/
│       ├── __init__.py    # TODO : Créez ce fichier vide
│       └── seed_data.py   # TODO : Créez ce fichier
```

**Squelette - `blog/management/commands/seed_data.py`** :

```python
from django.core.management.base import BaseCommand

class Command(BaseCommand):
    # TODO : Ajoutez l'attribut 'help' avec une description
    help = # VOTRE CODE ICI
    
    def handle(self, *args, **kwargs):
        # TODO : Utilisez self.stdout.write() pour afficher un message
        # VOTRE CODE ICI
        pass
```

**Validation** :
```bash
# TODO : Exécutez la commande
python manage.py seed_data
# Doit afficher : "Génération de données..."
```

**Indice** :
- Les fichiers `__init__.py` doivent être vides (pour que Python reconnaisse les dossiers comme des packages)
- `self.stdout.write()` affiche un message dans la console

---

### Exercice 15 - Configuration CORS pour frontend (PRATIQUE)

**Objectif** : Permettre à un frontend (React, Vue, etc.) d'accéder à votre API.

**Consignes** :
1. Installez le package `django-cors-headers`
2. Ajoutez `'corsheaders'` à `INSTALLED_APPS`
3. Ajoutez le middleware CORS
4. Configurez `CORS_ALLOW_ALL_ORIGINS = True` pour le développement

**TODO** :

```bash
# TODO : Installez django-cors-headers
# Commande : pip install ...
# VOTRE COMMANDE ICI
```

**Squelette - `settings.py`** (à modifier) :

```python
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    
    # TODO : Ajoutez 'corsheaders'
    # VOTRE CODE ICI
    
    'blog',
]

MIDDLEWARE = [
    # TODO : Ajoutez 'corsheaders.middleware.CorsMiddleware' EN PREMIER
    # VOTRE CODE ICI
    
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    # ... reste du middleware
]

# TODO : Ajoutez la configuration CORS pour le développement
# Créez la variable CORS_ALLOW_ALL_ORIGINS = True
# VOTRE CODE ICI
```

**Validation** :
1. Testez avec curl depuis un autre domaine
2. L'API doit répondre sans erreur CORS

**Indice** :
- CORS (Cross-Origin Resource Sharing) permet les requêtes depuis d'autres domaines
- En production, utilisez `CORS_ALLOWED_ORIGINS` avec la liste des domaines autorisés

---

## Checklist de validation

- ✅ Django installé dans un environnement virtuel
- ✅ Projet Django créé avec succès
- ✅ Application `blog` créée et enregistrée
- ✅ Base de données migrée (tables créées)
- ✅ Superutilisateur créé et accès admin OK
- ✅ Interface admin accessible et en français
- ✅ Endpoint API `/api/` retourne du JSON
- ✅ Variables d'environnement configurées (`.env`)
- ✅ `requirements.txt` et `.gitignore` créés
- ✅ Serveur de développement fonctionne

---

## 🚀 Prochaines étapes

Vous êtes maintenant prêt pour :
- **Module 15** : Créer vos premiers modèles Django
- **Module 16** : Maîtriser les QuerySets et l'optimisation
- **Module 17** : Techniques avancées de l'ORM
- **Module 18** : Projet ORM complet

🎉 **Félicitations !** Vous avez configuré votre environnement Backend Django !
