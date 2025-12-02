"""
Module 14 - Django Introduction
Template pour tester la configuration Django

Ce fichier sert de référence pour les commandes de base Django.
Utilisez les commandes ci-dessous dans votre terminal.
"""

# ============= COMMANDES DJANGO DE BASE =============

"""
# 1. Créer un environnement virtuel
python -m venv venv
source venv/bin/activate  # macOS/Linux
venv\Scripts\activate  # Windows

# 2. Installer Django et dépendances
pip install django python-decouple djangorestframework

# 3. Créer un projet
django-admin startproject monprojet
cd monprojet

# 4. Créer une application
python manage.py startapp blog

# 5. Lancer le serveur
python manage.py runserver

# 6. Créer les migrations
python manage.py makemigrations

# 7. Appliquer les migrations
python manage.py migrate

# 8. Créer un superutilisateur
python manage.py createsuperuser

# 9. Shell Django (interactif)
python manage.py shell

# 10. Sauvegarder les dépendances
pip freeze > requirements.txt

# 11. Installer les dépendances
pip install -r requirements.txt
"""

# ============= EXEMPLE DE CONFIGURATION =============

"""
# settings.py - Configuration de base

# Applications installées
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    
    # Applications tierces
    'rest_framework',
    
    # Vos applications
    'blog',
]

# Internationalisation
LANGUAGE_CODE = 'fr-fr'
TIME_ZONE = 'Europe/Paris'
USE_I18N = True
USE_TZ = True

# Base de données (SQLite par défaut)
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}
"""

# ============= EXEMPLE D'ENDPOINT API SIMPLE =============

"""
# blog/views.py

from django.http import JsonResponse

def api_home(request):
    return JsonResponse({
        'message': 'API Django fonctionnelle !',
        'version': '1.0',
        'endpoints': {
            'admin': '/admin/',
            'api': '/api/',
        }
    })
"""

"""
# blog/urls.py

from django.urls import path
from . import views

urlpatterns = [
    path('', views.api_home, name='api-home'),
]
"""

"""
# monprojet/urls.py

from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('blog.urls')),
]
"""

# ============= EXEMPLE DE MODÈLE =============

"""
# blog/models.py

from django.db import models

class Article(models.Model):
    titre = models.CharField(max_length=200)
    contenu = models.TextField()
    date_creation = models.DateTimeField(auto_now_add=True)
    publie = models.BooleanField(default=False)
    
    def __str__(self):
        return self.titre
    
    class Meta:
        ordering = ['-date_creation']
        verbose_name = "Article"
        verbose_name_plural = "Articles"
"""

# ============= EXEMPLE .ENV =============

"""
# .env

SECRET_KEY=votre-cle-secrete-django-ici
DEBUG=True
ALLOWED_HOSTS=localhost,127.0.0.1
DATABASE_URL=sqlite:///db.sqlite3
"""

# ============= EXEMPLE .GITIGNORE =============

"""
# .gitignore

# Python
*.pyc
__pycache__/
*.py[cod]

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
"""

# ============= COMMANDES UTILES =============

"""
# Lancer le serveur sur un port spécifique
python manage.py runserver 8080

# Voir les migrations
python manage.py showmigrations

# Créer une migration vide
python manage.py makemigrations --empty blog

# Voir le SQL d'une migration
python manage.py sqlmigrate blog 0001

# Tests
python manage.py test

# Créer un superutilisateur sans interaction
python manage.py createsuperuser --noinput --username=admin --email=admin@example.com

# Collecter les fichiers statiques
python manage.py collectstatic

# Vider la base de données
python manage.py flush
"""

if __name__ == "__main__":
    print("=" * 60)
    print("Module 14 - Django Introduction")
    print("=" * 60)
    print("\n📖 Ce fichier contient des références de commandes Django.")
    print("📌 Consultez les commandes ci-dessus et utilisez-les dans votre terminal.")
    print("\n✅ Configuration terminée ? Passez au Module 15 (Modèles Django) !")
    print("=" * 60)
