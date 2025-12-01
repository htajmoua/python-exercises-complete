"""
Module 19 - Django Admin et Authentification API
Fichier de test pour les exercices

Utilisez le shell Django ou les commandes ci-dessous :
    python manage.py shell
"""

# ============= IMPORTS =============

from django.contrib.auth.models import User, Group, Permission
from django.contrib.contenttypes.models import ContentType
from rest_framework.authtoken.models import Token

# Vos imports
# from blog.models import Article, Auteur
# from api.models import Profil


# ============= EXERCICES ADMIN =============

def tester_admin():
    """Vérifier la configuration admin"""
    pass
    # 1. Accéder à /admin/
    # 2. Vérifier les ModelAdmin personnalisés
    # 3. Tester les filtres et recherches
    # 4. Tester les actions en masse


# ============= EXERCICES AUTHENTIFICATION API =============

def creer_utilisateur_test():
    """Créer un utilisateur pour tester l'API"""
    user = User.objects.create_user(
        username='testuser',
        email='test@example.com',
        password='testpass123'
    )
    print(f"Utilisateur créé : {user.username}")
    return user


def creer_token(username):
    """Créer un token pour un utilisateur"""
    user = User.objects.get(username=username)
    token, created = Token.objects.get_or_create(user=user)
    print(f"Token pour {username} : {token.key}")
    return token.key


def tester_permissions():
    """Tester les permissions"""
    # Créer des groupes
    editeurs = Group.objects.get_or_create(name='Éditeurs')[0]
    auteurs = Group.objects.get_or_create(name='Auteurs')[0]
    
    # Créer un utilisateur
    user = User.objects.get(username='testuser')
    
    # Ajouter au groupe
    user.groups.add(editeurs)
    
    # Vérifier les permissions
    print(f"User dans groupe Éditeurs : {user.groups.filter(name='Éditeurs').exists()}")
    
    # Permissions personnalisées
    # content_type = ContentType.objects.get_for_model(Article)
    # permission = Permission.objects.get(
    #     codename='can_publish',
    #     content_type=content_type
    # )
    # editeurs.permissions.add(permission)
    # print(f"Peut publier : {user.has_perm('blog.can_publish')}")


def creer_profil_utilisateur():
    """Créer un profil pour un utilisateur"""
    pass
    # user = User.objects.get(username='testuser')
    # profil = Profil.objects.get_or_create(user=user)[0]
    # profil.bio = "Développeur Backend"
    # profil.site_web = "https://example.com"
    # profil.save()
    # print(f"Profil créé pour {user.username}")


# ============= TESTS API AVEC REQUESTS =============

"""
# Installer requests si nécessaire
# pip install requests

import requests

BASE_URL = 'http://localhost:8000/api'

# Inscription
def test_register():
    response = requests.post(f'{BASE_URL}/auth/register/', json={
        'username': 'john',
        'email': 'john@example.com',
        'password': 'secret123'
    })
    print(response.json())
    return response.json()

# Login
def test_login():
    response = requests.post(f'{BASE_URL}/auth/login/', json={
        'username': 'john',
        'password': 'secret123'
    })
    print(response.json())
    return response.json()['token']

# Accéder à une ressource protégée
def test_protected_resource(token):
    headers = {'Authorization': f'Token {token}'}
    response = requests.get(f'{BASE_URL}/articles/', headers=headers)
    print(response.json())

# Pipeline de test
token_data = test_register()
token = test_login()
test_protected_resource(token)
"""


# ============= COMMANDES UTILES =============

"""
# Créer un token manuellement
python manage.py drf_create_token <username>

# Shell Django
python manage.py shell

# Créer un superutilisateur
python manage.py createsuperuser

# Vérifier les permissions d'un user
user = User.objects.get(username='john')
user.get_all_permissions()
user.has_perm('blog.can_publish')

# Lister tous les tokens
from rest_framework.authtoken.models import Token
for token in Token.objects.all():
    print(f"{token.user.username}: {token.key}")

# Supprimer tous les tokens
Token.objects.all().delete()

# Ajouter un user à un groupe
from django.contrib.auth.models import Group
group = Group.objects.get(name='Éditeurs')
user.groups.add(group)

# Permissions custom
from django.contrib.auth.models import Permission
from django.contrib.contenttypes.models import ContentType
from blog.models import Article

content_type = ContentType.objects.get_for_model(Article)
permission = Permission.objects.create(
    codename='can_feature',
    name='Peut mettre en avant',
    content_type=content_type
)
"""


# ============= EXÉCUTION =============

if __name__ == "__main__":
    print("=" * 60)
    print("Module 19 - Tests Admin et Authentification API")
    print("=" * 60)
    
    # Décommentez pour tester
    # user = creer_utilisateur_test()
    # token = creer_token('testuser')
    # tester_permissions()
    
    print("\n✅ Module prêt pour vos tests !")
    print("\n📌 Commandes utiles :")
    print("  - python manage.py createsuperuser")
    print("  - python manage.py drf_create_token <username>")
    print("  - Accéder à /admin/ dans le navigateur")
    print("  - Tester l'API avec curl ou Postman")
    print("=" * 60)
