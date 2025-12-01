# Instructions - Django Admin et Authentification (Backend/API)

**🎯 Objectif du module** : Maîtriser l'interface Admin Django et l'authentification API pour applications Backend.

**📌 Note importante** : Ce module est axé **Backend/API**. Nous couvrons :
- L'interface d'administration Django (pour gérer les données)
- L'authentification API (Token, JWT)
- Les permissions et groupes
- Pas de templates HTML ni formulaires web

**📚 Format du module** :
- **Partie 1 (Exercices 1-3)** : Exemples guidés - Admin Django
- **Partie 2 (Exercices 4-6)** : Exercices pratiques - Auth API (Token, JWT)

**Prérequis** : Avoir complété les modules 14-18 (ORM maîtrisé)

---

# 📖 PARTIE 1 : EXEMPLES GUIDÉS - Django Admin

L'admin Django est une interface puissante pour gérer vos données Backend sans créer d'interface custom.

---

## Exercice 1 - Enregistrer les modèles (EXEMPLE)

### Exercice 1 - Enregistrer les modèles

**Modifiez** `blog/admin.py` :

```python
from django.contrib import admin
from .models import Article, Auteur, Tag, Commentaire

# Enregistrement simple
admin.site.register(Article)
admin.site.register(Auteur)
admin.site.register(Tag)
admin.site.register(Commentaire)
```

**Accédez** à `http://127.0.0.1:8000/admin/` et explorez l'interface.

**Actions disponibles** :
- Créer, modifier, supprimer des objets
- Filtrer et rechercher
- Actions en masse

---

### Exercice 2 - ModelAdmin basique

**Personnalisez** l'affichage des listes :

```python
from django.contrib import admin
from .models import Article, Auteur, Tag, Commentaire

@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):
    # Colonnes affichées dans la liste
    list_display = ['titre', 'auteur', 'publie', 'date_creation', 'nombre_vues']
    
    # Filtres latéraux
    list_filter = ['publie', 'date_creation', 'auteur', 'tags']
    
    # Barre de recherche
    search_fields = ['titre', 'contenu', 'auteur__nom']
    
    # Hiérarchie de dates
    date_hierarchy = 'date_creation'
    
    # Tri par défaut
    ordering = ['-date_creation']
```

**Testez** dans l'admin : les colonnes, filtres et recherche sont maintenant disponibles !

---

### Exercice 3 - Admin avancé avec méthodes personnalisées

**Ajoutez** des colonnes calculées et plus de fonctionnalités :

```python
from django.utils.html import format_html

@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):
    list_display = [
        'titre', 
        'auteur', 
        'statut_badge',  # Méthode personnalisée
        'nombre_commentaires',  # Méthode personnalisée
        'popularite',  # Méthode personnalisée
        'date_creation'
    ]
    list_filter = ['publie', 'featured', 'date_creation', 'auteur', 'tags']
    search_fields = ['titre', 'contenu', 'auteur__nom', 'auteur__email']
    
    # Génération automatique du slug
    prepopulated_fields = {'slug': ('titre',)}
    
    # Widget horizontal pour ManyToMany
    filter_horizontal = ['tags']
    
    # Champs éditables directement dans la liste
    list_editable = ['publie']
    
    # Pagination
    list_per_page = 25
    
    # Organisation en fieldsets
    fieldsets = (
        ('Informations principales', {
            'fields': ('titre', 'slug', 'auteur', 'categorie')
        }),
        ('Contenu', {
            'fields': ('chapeau', 'contenu', 'image_principale')
        }),
        ('Taxonomie', {
            'fields': ('tags',)
        }),
        ('Publication', {
            'fields': ('publie', 'featured', 'date_publication')
        }),
        ('Statistiques', {
            'fields': ('nombre_vues', 'nombre_partages'),
            'classes': ('collapse',)  # Section repliable
        }),
    )
    
    # Champs en lecture seule
    readonly_fields = ['date_creation', 'date_modification', 'nombre_vues']
    
    # Méthodes personnalisées
    def statut_badge(self, obj):
        """Badge coloré pour le statut"""
        if obj.publie:
            if obj.featured:
                return format_html(
                    '<span style="background:gold;padding:3px 10px;border-radius:3px;color:black;">⭐ Featured</span>'
                )
            return format_html(
                '<span style="background:green;padding:3px 10px;border-radius:3px;color:white;">✓ Publié</span>'
            )
        return format_html(
            '<span style="background:gray;padding:3px 10px;border-radius:3px;color:white;">✗ Brouillon</span>'
        )
    statut_badge.short_description = 'Statut'
    
    def nombre_commentaires(self, obj):
        """Compter les commentaires"""
        count = obj.commentaires.count()
        return f"{count} commentaire(s)"
    nombre_commentaires.short_description = 'Commentaires'
    nombre_commentaires.admin_order_field = 'commentaires'  # Tri possible
    
    def popularite(self, obj):
        """Indicateur de popularité"""
        if obj.nombre_vues > 10000:
            return "🔥 Viral"
        elif obj.nombre_vues > 1000:
            return "📈 Populaire"
        elif obj.nombre_vues > 100:
            return "👍 Moyen"
        return "📝 Nouveau"
    popularite.short_description = 'Popularité'
    popularite.admin_order_field = 'nombre_vues'
```

---

### Exercice 4 - Inline admin (Relations)

**Affichez** les objets liés directement dans le formulaire parent :

```python
class CommentaireInline(admin.TabularInline):
    """Commentaires affichés dans l'article"""
    model = Commentaire
    extra = 1  # Nombre de formulaires vides à afficher
    fields = ['auteur_nom', 'contenu', 'approuve', 'date_creation']
    readonly_fields = ['date_creation']
    can_delete = True

class LikeInline(admin.TabularInline):
    """Likes affichés dans l'article"""
    model = Like
    extra = 0
    fields = ['user', 'date_creation']
    readonly_fields = ['date_creation']

@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):
    inlines = [CommentaireInline, LikeInline]
    # ... autres options ...
```

**Alternatives** :
- `TabularInline` : Format tabulaire (compact)
- `StackedInline` : Format empilé (détaillé)

---

### Exercice 5 - Actions personnalisées

**Créez** des actions en masse pour traiter plusieurs objets :

```python
from django.contrib import messages

@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):
    actions = [
        'publier_articles', 
        'depublier_articles',
        'mettre_en_featured',
        'reinitialiser_vues'
    ]
    
    def publier_articles(self, request, queryset):
        """Publier les articles sélectionnés"""
        from django.utils import timezone
        count = queryset.update(
            publie=True,
            date_publication=timezone.now()
        )
        self.message_user(
            request, 
            f'{count} article(s) ont été publiés.',
            messages.SUCCESS
        )
    publier_articles.short_description = "✓ Publier les articles sélectionnés"
    
    def depublier_articles(self, request, queryset):
        """Dépublier les articles sélectionnés"""
        count = queryset.update(publie=False)
        self.message_user(
            request, 
            f'{count} article(s) ont été dépubliés.',
            messages.WARNING
        )
    depublier_articles.short_description = "✗ Dépublier les articles sélectionnés"
    
    def mettre_en_featured(self, request, queryset):
        """Mettre en avant les articles"""
        count = queryset.filter(publie=True).update(featured=True)
        self.message_user(
            request,
            f'{count} article(s) mis en avant.',
            messages.SUCCESS
        )
    mettre_en_featured.short_description = "⭐ Mettre en avant"
    
    def reinitialiser_vues(self, request, queryset):
        """Remettre les vues à zéro"""
        count = queryset.update(nombre_vues=0)
        self.message_user(
            request,
            f'Vues réinitialisées pour {count} article(s).',
            messages.INFO
        )
    reinitialiser_vues.short_description = "🔄 Réinitialiser les vues"
```

---

### Exercice 6 - Personnalisation visuelle de l'admin

**Modifiez** les textes et l'apparence :

```python
# Dans urls.py principal ou admin.py
from django.contrib import admin

# Titres de l'admin
admin.site.site_header = "Administration Backend Blog API"
admin.site.site_title = "Admin Blog"
admin.site.index_title = "Tableau de bord"

# Message de bienvenue personnalisé
admin.site.site_url = "/api/"  # Lien vers votre API
```

**Créez** un fichier `admin.py` personnalisé pour chaque app :

```python
# blog/admin.py
from django.contrib import admin

class BlogAdminSite(admin.AdminSite):
    site_header = "Blog Administration"
    site_title = "Blog Admin"
    index_title = "Gestion du Blog"

blog_admin_site = BlogAdminSite(name='blog_admin')
```

---

# 🔨 PARTIE 2 : EXERCICES PRATIQUES - Authentification API ⭐⭐⭐

**À partir d'ici, c'est à vous de coder !** L'authentification API est cruciale pour sécuriser vos endpoints.

Pour une API Backend, l'authentification se fait via **Tokens** ou **JWT**, pas via sessions/cookies web.

---

## Exercice 4 - Token Authentication (PRATIQUE)

**Installez** Django REST Framework :

```bash
pip install djangorestframework
```

**Configurez** `settings.py` :

```python
INSTALLED_APPS = [
    ...
    'rest_framework',
    'rest_framework.authtoken',  # Token auth
]

REST_FRAMEWORK = {
    'DEFAULT_AUTHENTICATION_CLASSES': [
        'rest_framework.authentication.TokenAuthentication',
        'rest_framework.authentication.SessionAuthentication',
    ],
    'DEFAULT_PERMISSION_CLASSES': [
        'rest_framework.permissions.IsAuthenticatedOrReadOnly',
    ],
}
```

**Migrez** pour créer la table des tokens :

```bash
python manage.py migrate
```

**Créez** les endpoints d'authentification dans `api/views.py` :

```python
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from rest_framework.authtoken.models import Token
from rest_framework.permissions import AllowAny
from rest_framework import status
from django.contrib.auth.models import User
from django.contrib.auth import authenticate

@api_view(['POST'])
@permission_classes([AllowAny])
def register(request):
    """Inscription d'un nouvel utilisateur"""
    username = request.data.get('username')
    email = request.data.get('email')
    password = request.data.get('password')
    
    if not username or not password:
        return Response(
            {'error': 'Username et password requis'},
            status=status.HTTP_400_BAD_REQUEST
        )
    
    if User.objects.filter(username=username).exists():
        return Response(
            {'error': 'Username déjà utilisé'},
            status=status.HTTP_400_BAD_REQUEST
        )
    
    user = User.objects.create_user(
        username=username,
        email=email,
        password=password
    )
    token, created = Token.objects.get_or_create(user=user)
    
    return Response({
        'token': token.key,
        'user_id': user.id,
        'username': user.username,
        'email': user.email
    }, status=status.HTTP_201_CREATED)

@api_view(['POST'])
@permission_classes([AllowAny])
def login(request):
    """Connexion et obtention du token"""
    username = request.data.get('username')
    password = request.data.get('password')
    
    user = authenticate(username=username, password=password)
    
    if user is None:
        return Response(
            {'error': 'Identifiants invalides'},
            status=status.HTTP_401_UNAUTHORIZED
        )
    
    token, created = Token.objects.get_or_create(user=user)
    
    return Response({
        'token': token.key,
        'user_id': user.id,
        'username': user.username
    })

@api_view(['POST'])
def logout(request):
    """Déconnexion (suppression du token)"""
    if request.user.is_authenticated:
        request.user.auth_token.delete()
        return Response({'message': 'Déconnecté avec succès'})
    return Response(
        {'error': 'Non authentifié'},
        status=status.HTTP_401_UNAUTHORIZED
    )

@api_view(['GET'])
def profile(request):
    """Profil de l'utilisateur connecté"""
    if not request.user.is_authenticated:
        return Response(
            {'error': 'Authentification requise'},
            status=status.HTTP_401_UNAUTHORIZED
        )
    
    return Response({
        'id': request.user.id,
        'username': request.user.username,
        'email': request.user.email,
        'is_staff': request.user.is_staff,
        'date_joined': request.user.date_joined
    })
```

**Routes** dans `api/urls.py` :

```python
from django.urls import path
from . import views

app_name = 'api'

urlpatterns = [
    path('auth/register/', views.register, name='register'),
    path('auth/login/', views.login, name='login'),
    path('auth/logout/', views.logout, name='logout'),
    path('auth/profile/', views.profile, name='profile'),
]
```

**Testez** avec curl ou Postman :

```bash
# Inscription
curl -X POST http://localhost:8000/api/auth/register/ \
  -H "Content-Type: application/json" \
  -d '{"username":"john","email":"john@example.com","password":"secret123"}'

# Réponse :
# {"token":"9944b09199c62bcf9418ad846dd0e4bbdfc6ee4b","user_id":2,"username":"john","email":"john@example.com"}

# Login
curl -X POST http://localhost:8000/api/auth/login/ \
  -H "Content-Type: application/json" \
  -d '{"username":"john","password":"secret123"}'

# Utiliser le token pour accéder à une ressource protégée
curl -X GET http://localhost:8000/api/articles/ \
  -H "Authorization: Token 9944b09199c62bcf9418ad846dd0e4bbdfc6ee4b"
```

---

### Exercice 8 - JWT Authentication (Recommandé pour production)

**Installez** djangorestframework-simplejwt :

```bash
pip install djangorestframework-simplejwt
```

**Configurez** `settings.py` :

```python
REST_FRAMEWORK = {
    'DEFAULT_AUTHENTICATION_CLASSES': [
        'rest_framework_simplejwt.authentication.JWTAuthentication',
    ],
}

from datetime import timedelta

SIMPLE_JWT = {
    'ACCESS_TOKEN_LIFETIME': timedelta(hours=1),
    'REFRESH_TOKEN_LIFETIME': timedelta(days=7),
    'ROTATE_REFRESH_TOKENS': True,
    'BLACKLIST_AFTER_ROTATION': True,
}
```

**Routes** dans `urls.py` :

```python
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
    TokenVerifyView,
)

urlpatterns = [
    path('api/auth/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/auth/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('api/auth/token/verify/', TokenVerifyView.as_view(), name='token_verify'),
]
```

**Testez JWT** :

```bash
# Obtenir les tokens
curl -X POST http://localhost:8000/api/auth/token/ \
  -H "Content-Type: application/json" \
  -d '{"username":"john","password":"secret123"}'

# Réponse :
# {
#   "access":"eyJ0eXAiOiJKV1QiLCJhbGc...",
#   "refresh":"eyJ0eXAiOiJKV1QiLCJhbGc..."
# }

# Utiliser l'access token
curl -X GET http://localhost:8000/api/articles/ \
  -H "Authorization: Bearer eyJ0eXAiOiJKV1QiLCJhbGc..."

# Rafraîchir le token
curl -X POST http://localhost:8000/api/auth/token/refresh/ \
  -H "Content-Type: application/json" \
  -d '{"refresh":"eyJ0eXAiOiJKV1QiLCJhbGc..."}'
```

---

### Exercice 9 - Protéger les endpoints API

**Avec décorateurs** (Function-Based Views) :

```python
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated

@api_view(['POST'])
@permission_classes([IsAuthenticated])
def create_article(request):
    """Créer un article (authentification requise)"""
    # Seuls les utilisateurs authentifiés peuvent accéder
    pass
```

**Avec ViewSets/Classes** :

```python
from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAuthenticated, IsAuthenticatedOrReadOnly

class ArticleViewSet(ModelViewSet):
    queryset = Article.objects.all()
    serializer_class = ArticleSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]  # Lecture publique, écriture authentifiée
```

---

### Exercice 10 - Permissions personnalisées

**Créez** des permissions custom dans `permissions.py` :

```python
from rest_framework import permissions

class IsAuthorOrReadOnly(permissions.BasePermission):
    """Seul l'auteur peut modifier"""
    
    def has_object_permission(self, request, view, obj):
        # Lecture autorisée pour tous
        if request.method in permissions.SAFE_METHODS:
            return True
        
        # Écriture autorisée seulement pour l'auteur
        return obj.auteur.user == request.user

class IsAdminOrReadOnly(permissions.BasePermission):
    """Seuls les admins peuvent modifier"""
    
    def has_permission(self, request, view):
        if request.method in permissions.SAFE_METHODS:
            return True
        return request.user and request.user.is_staff
```

**Utilisez-les** :

```python
class ArticleViewSet(ModelViewSet):
    queryset = Article.objects.all()
    serializer_class = ArticleSerializer
    permission_classes = [IsAuthorOrReadOnly]
```

---

### Exercice 11 - Permissions dans les modèles

**Créez** des permissions personnalisées dans `models.py` :

```python
class Article(models.Model):
    # ... champs ...
    
    class Meta:
        permissions = [
            ("can_publish", "Peut publier des articles"),
            ("can_feature", "Peut mettre en avant des articles"),
            ("can_view_stats", "Peut voir les statistiques"),
        ]
```

**Appliquez les migrations** :

```bash
python manage.py makemigrations
python manage.py migrate
```

**Utilisez-les** :

```python
from rest_framework import permissions

class CanPublishPermission(permissions.BasePermission):
    def has_permission(self, request, view):
        return request.user.has_perm('blog.can_publish')

class ArticleViewSet(ModelViewSet):
    queryset = Article.objects.all()
    serializer_class = ArticleSerializer
    
    def get_permissions(self):
        if self.action == 'publish':
            return [CanPublishPermission()]
        return [permissions.IsAuthenticated()]
    
    @action(detail=True, methods=['post'])
    def publish(self, request, pk=None):
        article = self.get_object()
        article.publie = True
        article.save()
        return Response({'status': 'publié'})
```

---

### Exercice 12 - Groupes d'utilisateurs

**Créez des groupes** dans le shell ou via l'admin :

```python
from django.contrib.auth.models import Group, Permission, User
from django.contrib.contenttypes.models import ContentType
from blog.models import Article

# Créer des groupes
editeurs = Group.objects.create(name='Éditeurs')
auteurs = Group.objects.create(name='Auteurs')
moderateurs = Group.objects.create(name='Modérateurs')

# Ajouter des permissions
content_type = ContentType.objects.get_for_model(Article)

# Permission de publication
permission_publish = Permission.objects.get(
    codename='can_publish',
    content_type=content_type
)
editeurs.permissions.add(permission_publish)

# Permission de featured
permission_feature = Permission.objects.get(
    codename='can_feature',
    content_type=content_type
)
moderateurs.permissions.add(permission_feature)

# Ajouter un utilisateur à un groupe
user = User.objects.get(username='john')
user.groups.add(editeurs)

# Vérifier les permissions
user.has_perm('blog.can_publish')  # True si dans le groupe Éditeurs
```

---

### Exercice 13 - Profil utilisateur étendu

**Créez** un modèle `Profil` avec signal :

```python
from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver

class Profil(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='profil')
    bio = models.TextField(blank=True)
    photo = models.ImageField(upload_to='profiles/', blank=True)
    site_web = models.URLField(blank=True)
    twitter = models.CharField(max_length=100, blank=True)
    github = models.CharField(max_length=100, blank=True)
    
    # Notifications
    notifications_email = models.BooleanField(default=True)
    
    def __str__(self):
        return f'Profil de {self.user.username}'

# Signal pour créer automatiquement un profil
@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        Profil.objects.create(user=instance)

@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
    if hasattr(instance, 'profil'):
        instance.profil.save()
```

**Serializer pour le profil** :

```python
from rest_framework import serializers

class ProfilSerializer(serializers.ModelSerializer):
    class Meta:
        model = Profil
        fields = ['bio', 'photo', 'site_web', 'twitter', 'github']

class UserSerializer(serializers.ModelSerializer):
    profil = ProfilSerializer()
    
    class Meta:
        model = User
        fields = ['id', 'username', 'email', 'profil']
```

---

## Exercices bonus

### Exercice 14 - Custom User Model
**Créez** un modèle User personnalisé pour ajouter des champs (téléphone, adresse, etc.).

### Exercice 15 - Throttling (limitation de requêtes)
**Configurez** le throttling pour limiter les requêtes API :

```python
REST_FRAMEWORK = {
    'DEFAULT_THROTTLE_CLASSES': [
        'rest_framework.throttling.AnonRateThrottle',
        'rest_framework.throttling.UserRateThrottle'
    ],
    'DEFAULT_THROTTLE_RATES': {
        'anon': '100/day',
        'user': '1000/day'
    }
}
```

### Exercice 16 - OAuth2 / Social Auth
**Intégrez** l'authentification via Google/GitHub avec `drf-social-oauth2`.

---

## Checklist de validation

### Admin
- ✅ Admin personnalisé pour tous les modèles
- ✅ list_display, list_filter, search_fields configurés
- ✅ Inlines configurés pour relations
- ✅ Actions personnalisées créées
- ✅ Méthodes admin personnalisées ajoutées
- ✅ Fieldsets organisés

### Authentification API
- ✅ Token Authentication configuré ET testé
- ✅ JWT Authentication configuré (optionnel mais recommandé)
- ✅ Endpoints register/login/logout fonctionnels
- ✅ Permissions par endpoint configurées
- ✅ Permissions personnalisées créées
- ✅ Groupes d'utilisateurs utilisés
- ✅ Profil utilisateur créé avec signal

---

## 🚀 Commandes utiles

```bash
# Créer un token manuellement
python manage.py drf_create_token <username>

# Supprimer tous les tokens
python manage.py shell
from rest_framework.authtoken.models import Token
Token.objects.all().delete()

# Créer un superutilisateur rapidement
python manage.py createsuperuser --noinput --username=admin --email=admin@example.com

# Tester l'API avec httpie (alternative à curl)
pip install httpie
http POST localhost:8000/api/auth/login/ username=john password=secret123
```

---

🎉 **Félicitations !** Vous maîtrisez maintenant l'administration Django et l'authentification API !

**Prochaine étape** : Module 22 (PostgreSQL et optimisation)
