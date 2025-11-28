# Instructions - Django REST API

Django REST Framework (DRF) permet de créer des APIs RESTful puissantes et flexibles.

## Exercice 1 - Installation et configuration

**Installez** Django REST Framework :

```bash
pip install djangorestframework
```

**Ajoutez** dans `settings.py` :

```python
INSTALLED_APPS = [
    # ... apps existantes ...
    'rest_framework',
]

REST_FRAMEWORK = {
    'DEFAULT_PAGINATION_CLASS': 'rest_framework.pagination.PageNumberPagination',
    'PAGE_SIZE': 10
}
```

## Exercice 2 - Premier Serializer

**Créez** `blog/serializers.py` :

```python
from rest_framework import serializers
from .models import Article, Auteur, Tag

class ArticleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Article
        fields = ['id', 'titre', 'contenu', 'auteur', 'publie', 'date_creation']
```

## Exercice 3 - APIView simple

**Créez** `blog/api_views.py` :

```python
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Article
from .serializers import ArticleSerializer

class ArticleListAPIView(APIView):
    def get(self, request):
        articles = Article.objects.filter(publie=True)
        serializer = ArticleSerializer(articles, many=True)
        return Response(serializer.data)
    
    def post(self, request):
        serializer = ArticleSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
```

**Configurez** `blog/urls.py` :

```python
from .api_views import ArticleListAPIView

urlpatterns = [
    # ... URLs existantes ...
    path('api/articles/', ArticleListAPIView.as_view(), name='api_article_list'),
]
```

## Exercice 4 - Generic Views

**Utilisez** les vues génériques :

```python
from rest_framework import generics

class ArticleListCreateAPIView(generics.ListCreateAPIView):
    queryset = Article.objects.filter(publie=True)
    serializer_class = ArticleSerializer

class ArticleDetailAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Article.objects.all()
    serializer_class = ArticleSerializer
```

## Exercice 5 - ViewSets et Routers

**Créez** un ViewSet :

```python
from rest_framework import viewsets

class ArticleViewSet(viewsets.ModelViewSet):
    queryset = Article.objects.all()
    serializer_class = ArticleSerializer
    
    def get_queryset(self):
        # Filtrer seulement les articles publiés pour les non-staff
        if self.request.user.is_staff:
            return Article.objects.all()
        return Article.objects.filter(publie=True)
```

**Configurez** le router dans `blog/urls.py` :

```python
from rest_framework.routers import DefaultRouter
from .api_views import ArticleViewSet

router = DefaultRouter()
router.register(r'articles', ArticleViewSet, basename='article')

urlpatterns = [
    # ... URLs existantes ...
    path('api/', include(router.urls)),
]
```

## Exercice 6 - Serializers imbriqués

**Créez** des serializers avec relations :

```python
class AuteurSerializer(serializers.ModelSerializer):
    class Meta:
        model = Auteur
        fields = ['id', 'nom', 'prenom', 'email']

class TagSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tag
        fields = ['id', 'nom', 'slug']

class ArticleDetailSerializer(serializers.ModelSerializer):
    auteur = AuteurSerializer(read_only=True)
    tags = TagSerializer(many=True, read_only=True)
    nombre_commentaires = serializers.SerializerMethodField()
    
    class Meta:
        model = Article
        fields = ['id', 'titre', 'slug', 'contenu', 'auteur', 'tags', 
                  'publie', 'date_creation', 'nombre_commentaires']
    
    def get_nombre_commentaires(self, obj):
        return obj.commentaires.count()
```

## Exercice 7 - Validation personnalisée

**Ajoutez** de la validation :

```python
class ArticleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Article
        fields = '__all__'
    
    def validate_titre(self, value):
        if len(value) < 10:
            raise serializers.ValidationError("Le titre doit avoir au moins 10 caractères")
        return value
    
    def validate(self, data):
        if data.get('publie') and not data.get('auteur'):
            raise serializers.ValidationError("Un article publié doit avoir un auteur")
        return data
```

## Exercice 8 - Authentification

**Configurez** l'authentification dans `settings.py` :

```python
REST_FRAMEWORK = {
    'DEFAULT_AUTHENTICATION_CLASSES': [
        'rest_framework.authentication.SessionAuthentication',
        'rest_framework.authentication.TokenAuthentication',
    ],
    'DEFAULT_PERMISSION_CLASSES': [
        'rest_framework.permissions.IsAuthenticatedOrReadOnly',
    ],
}

INSTALLED_APPS = [
    # ...
    'rest_framework.authtoken',
]
```

**Créez** les tokens :

```bash
python manage.py migrate
```

**Dans le code** :

```python
from rest_framework.authtoken.models import Token

# Créer un token pour un utilisateur
token = Token.objects.create(user=user)
print(token.key)
```

## Exercice 9 - Permissions personnalisées

**Créez** `blog/permissions.py` :

```python
from rest_framework import permissions

class IsAuteurOrReadOnly(permissions.BasePermission):
    """
    Permission personnalisée : seul l'auteur peut modifier/supprimer
    """
    def has_object_permission(self, request, view, obj):
        # Lecture autorisée pour tous
        if request.method in permissions.SAFE_METHODS:
            return True
        
        # Écriture seulement si utilisateur est l'auteur
        return obj.auteur.email == request.user.email
```

**Utilisez-la** :

```python
from .permissions import IsAuteurOrReadOnly

class ArticleViewSet(viewsets.ModelViewSet):
    queryset = Article.objects.all()
    serializer_class = ArticleSerializer
    permission_classes = [IsAuteurOrReadOnly]
```

## Exercice 10 - Filtrage et recherche

**Installez** django-filter :

```bash
pip install django-filter
```

**Configurez** :

```python
INSTALLED_APPS = [
    # ...
    'django_filters',
]

REST_FRAMEWORK = {
    'DEFAULT_FILTER_BACKENDS': [
        'django_filters.rest_framework.DjangoFilterBackend',
        'rest_framework.filters.SearchFilter',
        'rest_framework.filters.OrderingFilter',
    ],
}
```

**Utilisez-le** :

```python
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import filters

class ArticleViewSet(viewsets.ModelViewSet):
    queryset = Article.objects.all()
    serializer_class = ArticleSerializer
    filter_backends = [DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter]
    filterset_fields = ['publie', 'auteur', 'tags']
    search_fields = ['titre', 'contenu']
    ordering_fields = ['date_creation', 'titre']
```

## Exercice 11 - Pagination personnalisée

**Créez** `blog/pagination.py` :

```python
from rest_framework.pagination import PageNumberPagination

class ArticlePagination(PageNumberPagination):
    page_size = 5
    page_size_query_param = 'page_size'
    max_page_size = 100
```

**Utilisez-la** :

```python
class ArticleViewSet(viewsets.ModelViewSet):
    queryset = Article.objects.all()
    serializer_class = ArticleSerializer
    pagination_class = ArticlePagination
```

## Exercice 12 - Actions personnalisées

**Ajoutez** des actions au ViewSet :

```python
from rest_framework.decorators import action

class ArticleViewSet(viewsets.ModelViewSet):
    # ... configuration ...
    
    @action(detail=True, methods=['post'])
    def publier(self, request, pk=None):
        article = self.get_object()
        article.publie = True
        article.save()
        return Response({'status': 'article publié'})
    
    @action(detail=False, methods=['get'])
    def recents(self, request):
        recent_articles = Article.objects.filter(publie=True).order_by('-date_creation')[:5]
        serializer = self.get_serializer(recent_articles, many=True)
        return Response(serializer.data)
    
    @action(detail=True, methods=['get'])
    def commentaires(self, request, pk=None):
        article = self.get_object()
        commentaires = article.commentaires.all()
        # Serializer pour commentaires (à créer)
        return Response({'commentaires': list(commentaires.values())})
```

## Exercice 13 - Documentation automatique

**Installez** drf-spectacular :

```bash
pip install drf-spectacular
```

**Configurez** `settings.py` :

```python
INSTALLED_APPS = [
    # ...
    'drf_spectacular',
]

REST_FRAMEWORK = {
    # ...
    'DEFAULT_SCHEMA_CLASS': 'drf_spectacular.openapi.AutoSchema',
}
```

**Ajoutez** dans `urls.py` :

```python
from drf_spectacular.views import SpectacularAPIView, SpectacularSwaggerView

urlpatterns = [
    # ...
    path('api/schema/', SpectacularAPIView.as_view(), name='schema'),
    path('api/docs/', SpectacularSwaggerView.as_view(url_name='schema'), name='swagger-ui'),
]
```

## Exercice 14 - Throttling (limitation de requêtes)

**Configurez** dans `settings.py` :

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

## Exercices bonus

### Exercice 15 - Versioning de l'API
**Implémentez** le versioning de l'API (v1, v2).

### Exercice 16 - Websockets
**Ajoutez** Django Channels pour des updates en temps réel.

### Exercice 17 - Tests API
**Créez** des tests pour toutes les endpoints.

## Checklist de validation

- ✅ DRF installé et configuré
- ✅ Serializers créés pour tous les modèles
- ✅ ViewSets et Routers configurés
- ✅ Authentification par token implémentée
- ✅ Permissions personnalisées créées
- ✅ Filtrage et recherche fonctionnels
- ✅ Pagination configurée
- ✅ Actions personnalisées ajoutées
- ✅ Documentation automatique générée
- ✅ Throttling configuré
