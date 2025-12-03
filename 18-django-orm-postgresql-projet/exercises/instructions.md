# Instructions - Django ORM : Projet Complet avec PostgreSQL 🚀

**🎯 Objectif du module** : Créer **BlogPro**, un système de blog professionnel complet intégrant PostgreSQL et toutes les techniques Django ORM avancées.

**📚 Format** : **100% TUTORIEL GUIDÉ** - Suivez les étapes pour construire le projet complet.

**Prérequis** : Modules 15-17 (Django, Models, QuerySets)

**Durée estimée** : 8-10 heures

---

# 🎬 Contexte du Projet

**BlogPro** est une plateforme de blog professionnelle avec :
- Articles, catégories, tags
- Auteurs avec profils enrichis
- Commentaires et système de modération
- Likes et notes (1-5 étoiles)
- Recherche full-text performante
- Dashboard analytics en temps réel
- Statistiques par auteur/catégorie
- Interface admin personnalisée

**Stack technique** :
- Django 5.0+
- PostgreSQL 15+
- Docker (optionnel)
- Python 3.10+

---

# 📖 PARTIE 1 : SETUP POSTGRESQL

## Étape 1 : Installation PostgreSQL avec Docker

**Créez** `docker-compose.yml` à la racine du projet :

```yaml
version: '3.8'

services:
  db:
    image: postgres:15-alpine
    container_name: blogpro_db
    environment:
      POSTGRES_DB: blogpro
      POSTGRES_USER: bloguser
      POSTGRES_PASSWORD: blogpass123
    ports:
      - "5432:5432"
    volumes:
      - postgres_data:/var/lib/postgresql/data
    healthcheck:
      test: ["CMD-SHELL", "pg_isready -U bloguser -d blogpro"]
      interval: 10s
      timeout: 5s
      retries: 5

volumes:
  postgres_data:
```

**Démarrez** PostgreSQL :

```bash
# Démarrer
docker-compose up -d

# Vérifier
docker-compose ps

# Logs
docker-compose logs -f db
```

---

## Étape 2 : Configuration Django

### Installer les dépendances

**Créez** `requirements.txt` :

```txt
Django==5.0.1
psycopg2-binary==2.9.9
django-environ==0.11.2
```

**Installez** :

```bash
python -m venv venv
source venv/bin/activate  # Windows: venv\Scripts\activate
pip install -r requirements.txt
```

### Configuration des variables d'environnement

**Créez** `.env` :

```bash
DEBUG=True
SECRET_KEY=django-insecure-change-this-in-production-123456789
DATABASE_URL=postgresql://bloguser:blogpass123@localhost:5432/blogpro
```

**Créez** `.env.example` (version publique) :

```bash
DEBUG=True
SECRET_KEY=your-secret-key-here
DATABASE_URL=postgresql://user:password@localhost:5432/dbname
```

**Ajoutez** au `.gitignore` :

```bash
echo ".env" >> .gitignore
echo "venv/" >> .gitignore
echo "__pycache__/" >> .gitignore
echo "*.pyc" >> .gitignore
echo "db.sqlite3" >> .gitignore
```

### Configurer settings.py

**Créez** le projet :

```bash
django-admin startproject blogpro .
python manage.py startapp blog
```

**Modifiez** `blogpro/settings.py` :

```python
import environ
import os
from pathlib import Path

env = environ.Env(DEBUG=(bool, False))

BASE_DIR = Path(__file__).resolve().parent.parent

# Lire .env
environ.Env.read_env(os.path.join(BASE_DIR, '.env'))

SECRET_KEY = env('SECRET_KEY')
DEBUG = env('DEBUG')

ALLOWED_HOSTS = ['localhost', '127.0.0.1']

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.postgres',  # PostgreSQL features
    'blog',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'blogpro.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'blogpro.wsgi.application'

# Database - PostgreSQL
DATABASES = {
    'default': env.db()  # Parse DATABASE_URL
}

AUTH_PASSWORD_VALIDATORS = [
    {'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator'},
    {'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator'},
    {'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator'},
    {'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator'},
]

LANGUAGE_CODE = 'fr-fr'
TIME_ZONE = 'Europe/Paris'
USE_I18N = True
USE_TZ = True

STATIC_URL = 'static/'

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'
```

**Testez** la connexion :

```bash
python manage.py migrate
# Si succès, PostgreSQL est configuré ! ✅
```

---

# 📖 PARTIE 2 : ARCHITECTURE DES MODÈLES

## Étape 3 : Classes abstraites réutilisables

**Créez** `blog/models.py` :

```python
from django.db import models
from django.contrib.auth.models import User
from django.contrib.postgres.fields import ArrayField
from django.contrib.postgres.search import SearchVectorField
from django.contrib.postgres.indexes import GinIndex
from django.core.validators import MinValueValidator, MaxValueValidator
from django.db.models import Q, F, Count, Avg, Sum
from django.utils import timezone
from django.utils.text import slugify
import uuid


# ============================================================================
# CLASSES ABSTRAITES
# ============================================================================

class TimestampedModel(models.Model):
    """Timestamps automatiques"""
    date_creation = models.DateTimeField(auto_now_add=True, db_index=True)
    date_modification = models.DateTimeField(auto_now=True)
    
    class Meta:
        abstract = True
        ordering = ['-date_creation']


class UUIDModel(models.Model):
    """UUID comme clé primaire"""
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    
    class Meta:
        abstract = True


class SoftDeleteModel(models.Model):
    """Suppression logique"""
    supprime = models.BooleanField(default=False, db_index=True)
    date_suppression = models.DateTimeField(null=True, blank=True)
    supprime_par = models.ForeignKey(
        User,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name='%(class)s_supprimes'
    )
    
    class Meta:
        abstract = True
    
    def soft_delete(self, user=None):
        self.supprime = True
        self.date_suppression = timezone.now()
        self.supprime_par = user
        self.save(update_fields=['supprime', 'date_suppression', 'supprime_par'])
    
    def restore(self):
        self.supprime = False
        self.date_suppression = None
        self.supprime_par = None
        self.save(update_fields=['supprime', 'date_suppression', 'supprime_par'])


class PublishableModel(models.Model):
    """Contenu publiable"""
    publie = models.BooleanField(default=False, db_index=True)
    date_publication = models.DateTimeField(null=True, blank=True, db_index=True)
    
    class Meta:
        abstract = True
    
    def publier(self):
        self.publie = True
        if not self.date_publication:
            self.date_publication = timezone.now()
        self.save(update_fields=['publie', 'date_publication'])
    
    def depublier(self):
        self.publie = False
        self.save(update_fields=['publie'])
```

---

## Étape 4 : Managers et QuerySets personnalisés

**Ajoutez** dans `blog/models.py` :

```python
# ============================================================================
# MANAGERS ET QUERYSETS
# ============================================================================

class ArticleQuerySet(models.QuerySet):
    """QuerySet personnalisé avec méthodes chaînables"""
    
    def actifs(self):
        return self.filter(supprime=False)
    
    def publies(self):
        return self.filter(
            publie=True,
            supprime=False,
            date_publication__lte=timezone.now()
        )
    
    def brouillons(self):
        return self.filter(publie=False, supprime=False)
    
    def featured(self):
        return self.filter(featured=True).publies()
    
    def par_auteur(self, auteur):
        return self.filter(auteur=auteur).actifs()
    
    def populaires(self, limite=10):
        return self.publies().order_by('-nombre_vues')[:limite]
    
    def tendance(self, jours=7):
        date_limite = timezone.now() - timezone.timedelta(days=jours)
        return self.publies().filter(
            date_publication__gte=date_limite
        ).order_by('-nombre_vues', '-date_publication')
    
    def avec_stats(self):
        return self.annotate(
            nb_commentaires=Count('commentaires', filter=Q(commentaires__approuve=True)),
            nb_likes=Count('likes'),
            note_moyenne=Avg('notes__valeur')
        )
    
    def recherche(self, query):
        return self.filter(
            Q(titre__icontains=query) | Q(contenu__icontains=query)
        ).publies()


class ArticleManager(models.Manager):
    """Manager personnalisé"""
    
    def get_queryset(self):
        return ArticleQuerySet(self.model, using=self._db)
    
    def actifs(self):
        return self.get_queryset().actifs()
    
    def publies(self):
        return self.get_queryset().publies()
    
    def brouillons(self):
        return self.get_queryset().brouillons()
    
    def featured(self):
        return self.get_queryset().featured()
    
    def populaires(self, limite=10):
        return self.get_queryset().populaires(limite)
    
    def tendance(self, jours=7):
        return self.get_queryset().tendance(jours)
    
    def avec_stats(self):
        return self.get_queryset().avec_stats()
    
    def recherche(self, query):
        return self.get_queryset().recherche(query)
```

---

## Étape 5 : Modèles principaux

**Ajoutez** dans `blog/models.py` :

```python
# ============================================================================
# MODÈLES
# ============================================================================

class Categorie(TimestampedModel):
    nom = models.CharField(max_length=100, unique=True)
    slug = models.SlugField(unique=True, max_length=100)
    description = models.TextField(blank=True)
    parent = models.ForeignKey(
        'self',
        on_delete=models.CASCADE,
        null=True,
        blank=True,
        related_name='sous_categories'
    )
    icone = models.CharField(max_length=50, blank=True)
    couleur = models.CharField(max_length=7, default='#000000')
    ordre = models.PositiveIntegerField(default=0)
    
    class Meta:
        verbose_name = 'Catégorie'
        ordering = ['ordre', 'nom']
    
    def __str__(self):
        return self.nom
    
    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.nom)
        super().save(*args, **kwargs)


class Tag(models.Model):
    nom = models.CharField(max_length=50, unique=True)
    slug = models.SlugField(unique=True, max_length=50)
    
    class Meta:
        ordering = ['nom']
    
    def __str__(self):
        return self.nom
    
    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.nom)
        super().save(*args, **kwargs)


class ProfilAuteur(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='profil')
    bio = models.TextField(blank=True)
    avatar = models.URLField(blank=True)
    site_web = models.URLField(blank=True)
    
    # PostgreSQL ArrayField
    competences = ArrayField(
        models.CharField(max_length=50),
        blank=True,
        default=list
    )
    
    # Stats
    articles_publies = models.PositiveIntegerField(default=0)
    total_vues = models.PositiveIntegerField(default=0)
    total_likes = models.PositiveIntegerField(default=0)
    
    certifie = models.BooleanField(default=False)
    badge = models.CharField(max_length=20, blank=True, choices=[
        ('bronze', 'Bronze'),
        ('silver', 'Argent'),
        ('gold', 'Or'),
    ])
    
    class Meta:
        verbose_name = 'Profil Auteur'
    
    def __str__(self):
        return f"Profil de {self.user.username}"
    
    def mettre_a_jour_stats(self):
        articles = self.user.articles.filter(publie=True)
        self.articles_publies = articles.count()
        self.total_vues = articles.aggregate(total=Sum('nombre_vues'))['total'] or 0
        self.total_likes = articles.aggregate(total=Sum('nb_likes_cache'))['total'] or 0
        self.save(update_fields=['articles_publies', 'total_vues', 'total_likes'])


class Article(TimestampedModel, SoftDeleteModel, PublishableModel, UUIDModel):
    # Base
    titre = models.CharField(max_length=200, db_index=True)
    slug = models.SlugField(unique=True, max_length=200)
    contenu = models.TextField()
    contenu_longueur = models.PositiveIntegerField(default=0, editable=False)
    extrait = models.TextField(max_length=500, blank=True)
    
    # Relations
    auteur = models.ForeignKey(User, on_delete=models.CASCADE, related_name='articles')
    categorie = models.ForeignKey(Categorie, on_delete=models.SET_NULL, null=True, related_name='articles')
    tags = models.ManyToManyField(Tag, blank=True, related_name='articles')
    
    # Media
    image_principale = models.URLField(blank=True)
    
    # SEO
    meta_description = models.CharField(max_length=160, blank=True)
    meta_keywords = ArrayField(models.CharField(max_length=50), blank=True, default=list)
    
    # Status
    featured = models.BooleanField(default=False, db_index=True)
    
    # Stats (cache)
    nombre_vues = models.PositiveIntegerField(default=0, db_index=True)
    nb_likes_cache = models.PositiveIntegerField(default=0)
    nb_commentaires_cache = models.PositiveIntegerField(default=0)
    note_moyenne_cache = models.DecimalField(max_digits=3, decimal_places=2, default=0.00)
    
    # Full-text search
    search_vector = SearchVectorField(null=True, editable=False)
    
    objects = ArticleManager()
    
    class Meta:
        ordering = ['-date_publication', '-date_creation']
        indexes = [
            models.Index(fields=['-date_publication', 'publie']),
            models.Index(fields=['-nombre_vues']),
            GinIndex(fields=['search_vector']),
        ]
    
    def __str__(self):
        return self.titre
    
    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.titre)
        self.contenu_longueur = len(self.contenu.split())
        if not self.extrait and self.contenu:
            self.extrait = self.contenu[:500] + '...'
        super().save(*args, **kwargs)
    
    def incrementer_vues(self):
        Article.objects.filter(pk=self.pk).update(nombre_vues=F('nombre_vues') + 1)
        self.nombre_vues += 1
    
    def temps_lecture(self):
        return max(1, self.contenu_longueur // 200)


class Commentaire(TimestampedModel, SoftDeleteModel):
    article = models.ForeignKey(Article, on_delete=models.CASCADE, related_name='commentaires')
    auteur = models.ForeignKey(User, on_delete=models.CASCADE, related_name='commentaires')
    parent = models.ForeignKey('self', on_delete=models.CASCADE, null=True, blank=True, related_name='reponses')
    contenu = models.TextField()
    approuve = models.BooleanField(default=False, db_index=True)
    
    class Meta:
        ordering = ['date_creation']
    
    def __str__(self):
        return f"Commentaire de {self.auteur.username}"


class Like(models.Model):
    article = models.ForeignKey(Article, on_delete=models.CASCADE, related_name='likes')
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='likes')
    date_creation = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        unique_together = ['article', 'user']


class Note(models.Model):
    article = models.ForeignKey(Article, on_delete=models.CASCADE, related_name='notes')
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='notes')
    valeur = models.PositiveSmallIntegerField(
        validators=[MinValueValidator(1), MaxValueValidator(5)]
    )
    date_creation = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        unique_together = ['article', 'user']
```

**Migrations** :

```bash
python manage.py makemigrations
python manage.py migrate
```

---

# 📖 PARTIE 3 : FONCTIONNALITÉS POSTGRESQL

## Étape 6 : Full-text Search

**Créez** `blog/signals.py` :

```python
from django.db.models.signals import post_save, post_delete, m2m_changed
from django.dispatch import receiver
from django.contrib.auth.models import User
from django.contrib.postgres.search import SearchVector
from blog.models import Article, Commentaire, Like, Note, ProfilAuteur


@receiver(post_save, sender=User)
def create_profil_auteur(sender, instance, created, **kwargs):
    if created:
        ProfilAuteur.objects.create(user=instance)


@receiver(post_save, sender=Article)
def update_search_vector(sender, instance, **kwargs):
    if not kwargs.get('raw', False):
        Article.objects.filter(pk=instance.pk).update(
            search_vector=(
                SearchVector('titre', weight='A', config='french') +
                SearchVector('contenu', weight='B', config='french')
            )
        )


@receiver(post_save, sender=Like)
@receiver(post_delete, sender=Like)
def update_article_likes_cache(sender, instance, **kwargs):
    article = instance.article
    nb_likes = article.likes.count()
    Article.objects.filter(pk=article.pk).update(nb_likes_cache=nb_likes)


@receiver(post_save, sender=Commentaire)
@receiver(post_delete, sender=Commentaire)
def update_article_commentaires_cache(sender, instance, **kwargs):
    article = instance.article
    nb = article.commentaires.filter(approuve=True).count()
    Article.objects.filter(pk=article.pk).update(nb_commentaires_cache=nb)


@receiver(post_save, sender=Note)
@receiver(post_delete, sender=Note)
def update_article_note_cache(sender, instance, **kwargs):
    from django.db.models import Avg
    article = instance.article
    moyenne = article.notes.aggregate(m=Avg('valeur'))['m'] or 0
    Article.objects.filter(pk=article.pk).update(note_moyenne_cache=round(moyenne, 2))
```

**Enregistrez** dans `blog/apps.py` :

```python
from django.apps import AppConfig

class BlogConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'blog'
    
    def ready(self):
        import blog.signals
```

**Ajoutez** la recherche full-text au manager (dans `blog/models.py`) :

```python
# Dans ArticleManager, ajouter :
def recherche_fulltext(self, query):
    from django.contrib.postgres.search import SearchQuery, SearchRank
    search_query = SearchQuery(query, config='french')
    return self.filter(search_vector=search_query).annotate(
        rank=SearchRank(models.F('search_vector'), search_query)
    ).order_by('-rank')
```

---

## Étape 7 : Analytics et statistiques

**Créez** `blog/analytics.py` :

```python
from django.db.models import Count, Sum, Avg, Q
from django.db.models.functions import TruncDate
from django.utils import timezone
from datetime import timedelta
from blog.models import Article, Categorie
from django.contrib.auth.models import User


class BlogAnalytics:
    
    @staticmethod
    def stats_globales():
        return {
            'total_articles': Article.objects.publies().count(),
            'total_vues': Article.objects.publies().aggregate(
                total=Sum('nombre_vues')
            )['total'] or 0,
            'total_likes': Article.objects.publies().aggregate(
                total=Sum('nb_likes_cache')
            )['total'] or 0,
            'note_moyenne': Article.objects.publies().aggregate(
                moyenne=Avg('note_moyenne_cache')
            )['moyenne'] or 0,
        }
    
    @staticmethod
    def top_articles(limite=10):
        return Article.objects.publies().avec_stats().order_by('-nombre_vues')[:limite]
    
    @staticmethod
    def articles_tendance(jours=7):
        return Article.objects.tendance(jours)[:10]
    
    @staticmethod
    def stats_par_categorie():
        return Categorie.objects.annotate(
            nb_articles=Count('articles', filter=Q(articles__publie=True)),
            total_vues=Sum('articles__nombre_vues', filter=Q(articles__publie=True)),
        ).order_by('-nb_articles')
    
    @staticmethod
    def stats_par_auteur():
        return User.objects.annotate(
            nb_articles=Count('articles', filter=Q(articles__publie=True)),
            total_vues=Sum('articles__nombre_vues', filter=Q(articles__publie=True)),
            note_moyenne=Avg('articles__note_moyenne_cache'),
        ).filter(nb_articles__gt=0).order_by('-total_vues')
    
    @staticmethod
    def articles_par_jour(jours=30):
        date_limite = timezone.now() - timedelta(days=jours)
        return Article.objects.filter(
            date_publication__gte=date_limite
        ).annotate(
            jour=TruncDate('date_publication')
        ).values('jour').annotate(
            nb_articles=Count('id')
        ).order_by('jour')
```

---

## Étape 8 : Optimisation et indexes

**Créez** une migration pour les indexes :

```bash
python manage.py makemigrations --empty blog --name add_custom_indexes
```

**Modifiez** la migration :

```python
from django.db import migrations

class Migration(migrations.Migration):
    dependencies = [
        ('blog', '0001_initial'),  # Ajustez selon votre dernière migration
    ]
    
    operations = [
        migrations.RunSQL(
            """
            CREATE INDEX idx_article_publie_featured 
            ON blog_article (publie, featured, date_publication DESC)
            WHERE supprime = FALSE;
            """,
            reverse_sql="DROP INDEX IF EXISTS idx_article_publie_featured;"
        ),
        migrations.RunSQL(
            """
            CREATE INDEX idx_article_auteur_date 
            ON blog_article (auteur_id, date_publication DESC)
            WHERE publie = TRUE AND supprime = FALSE;
            """,
            reverse_sql="DROP INDEX IF EXISTS idx_article_auteur_date;"
        ),
    ]
```

```bash
python manage.py migrate
```

**Créez** `blog/utils.py` pour analyser les requêtes :

```python
from django.db import connection

def explain_query(queryset):
    """Afficher EXPLAIN ANALYZE"""
    sql, params = queryset.query.sql_with_params()
    with connection.cursor() as cursor:
        cursor.execute(f'EXPLAIN ANALYZE {sql}', params)
        for row in cursor.fetchall():
            print(row[0])
```

---

# 📖 PARTIE 4 : DONNÉES DE TEST ET ADMIN

## Étape 9 : Créer des données de test

**Créez** `blog/management/commands/create_test_data.py` :

```python
from django.core.management.base import BaseCommand
from django.contrib.auth.models import User
from blog.models import Categorie, Tag, Article, ProfilAuteur
from django.utils import timezone
import random

class Command(BaseCommand):
    help = 'Créer des données de test'
    
    def handle(self, *args, **kwargs):
        # Créer utilisateurs
        users = []
        for i in range(5):
            user, _ = User.objects.get_or_create(
                username=f'auteur{i+1}',
                defaults={
                    'email': f'auteur{i+1}@example.com',
                    'first_name': f'Prénom{i+1}',
                }
            )
            user.set_password('password123')
            user.save()
            users.append(user)
            
            ProfilAuteur.objects.get_or_create(
                user=user,
                defaults={'competences': ['Python', 'Django']}
            )
        
        # Créer catégories
        categories = []
        for nom in ['Python', 'Django', 'PostgreSQL', 'DevOps']:
            cat, _ = Categorie.objects.get_or_create(nom=nom)
            categories.append(cat)
        
        # Créer tags
        tags = []
        for nom in ['Tutorial', 'Débutant', 'Avancé', 'Best Practices']:
            tag, _ = Tag.objects.get_or_create(nom=nom)
            tags.append(tag)
        
        # Créer articles
        for i in range(20):
            article = Article.objects.create(
                titre=f'Article sur Django #{i+1}',
                contenu=f'Contenu de l\'article {i+1}. ' * 100,
                auteur=random.choice(users),
                categorie=random.choice(categories),
                featured=random.choice([True, False]),
                publie=True,
                date_publication=timezone.now(),
                nombre_vues=random.randint(100, 5000),
            )
            article.tags.set(random.sample(tags, k=2))
        
        self.stdout.write(self.style.SUCCESS('✅ Données créées !'))
```

**Exécutez** :

```bash
mkdir -p blog/management/commands
touch blog/management/__init__.py
touch blog/management/commands/__init__.py

python manage.py create_test_data
```

---

## Étape 10 : Admin Django personnalisé

**Créez** `blog/admin.py` :

```python
from django.contrib import admin
from django.db.models import Count
from django.utils.html import format_html
from blog.models import Categorie, Tag, Article, ProfilAuteur, Commentaire, Like, Note


@admin.register(Categorie)
class CategorieAdmin(admin.ModelAdmin):
    list_display = ['nom', 'icone', 'couleur_display', 'ordre']
    list_editable = ['ordre']
    prepopulated_fields = {'slug': ('nom',)}
    
    def couleur_display(self, obj):
        return format_html(
            '<span style="background:{}; padding:5px 10px; color:white;">{}</span>',
            obj.couleur, obj.couleur
        )
    couleur_display.short_description = 'Couleur'


@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    list_display = ['nom', 'slug', 'nb_articles']
    prepopulated_fields = {'slug': ('nom',)}
    
    def get_queryset(self, request):
        return super().get_queryset(request).annotate(nb=Count('articles'))
    
    def nb_articles(self, obj):
        return obj.nb
    nb_articles.short_description = 'Articles'


class CommentaireInline(admin.TabularInline):
    model = Commentaire
    extra = 0
    fields = ['auteur', 'contenu', 'approuve']


@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):
    list_display = ['titre', 'auteur', 'categorie', 'publie', 'featured', 'nombre_vues', 'date_publication']
    list_filter = ['publie', 'featured', 'categorie', 'date_creation']
    search_fields = ['titre', 'contenu']
    prepopulated_fields = {'slug': ('titre',)}
    date_hierarchy = 'date_publication'
    list_editable = ['featured']
    inlines = [CommentaireInline]
    
    fieldsets = (
        ('Contenu', {
            'fields': ('titre', 'slug', 'contenu', 'extrait', 'image_principale')
        }),
        ('Classification', {
            'fields': ('auteur', 'categorie', 'tags')
        }),
        ('Publication', {
            'fields': ('publie', 'date_publication', 'featured')
        }),
        ('SEO', {
            'fields': ('meta_description', 'meta_keywords'),
            'classes': ('collapse',)
        }),
        ('Statistiques', {
            'fields': ('nombre_vues', 'nb_likes_cache', 'nb_commentaires_cache', 'note_moyenne_cache'),
            'classes': ('collapse',)
        }),
    )
    
    def get_queryset(self, request):
        return super().get_queryset(request).select_related('auteur', 'categorie')


@admin.register(ProfilAuteur)
class ProfilAuteurAdmin(admin.ModelAdmin):
    list_display = ['user', 'articles_publies', 'total_vues', 'certifie', 'badge']
    list_filter = ['certifie', 'badge']
    search_fields = ['user__username', 'user__email']


@admin.register(Commentaire)
class CommentaireAdmin(admin.ModelAdmin):
    list_display = ['auteur', 'article', 'approuve', 'date_creation']
    list_filter = ['approuve', 'date_creation']
    actions = ['approuver_commentaires']
    
    def approuver_commentaires(self, request, queryset):
        queryset.update(approuve=True)
    approuver_commentaires.short_description = "Approuver les commentaires sélectionnés"


admin.site.register(Like)
admin.site.register(Note)
```

**Créez** un superuser :

```bash
python manage.py createsuperuser
# Username: admin
# Email: admin@example.com
# Password: admin123

python manage.py runserver
# Visitez http://localhost:8000/admin/
```

---

# 📖 PARTIE 5 : TESTS UNITAIRES

## Étape 11 : Tests complets

**Créez** `blog/tests.py` :

```python
from django.test import TestCase
from django.contrib.auth.models import User
from django.utils import timezone
from blog.models import Article, Categorie, Tag, ProfilAuteur, Like, Commentaire


class ArticleModelTest(TestCase):
    
    def setUp(self):
        self.user = User.objects.create_user('test', 'test@test.com', 'pass')
        self.cat = Categorie.objects.create(nom='Python')
        self.article = Article.objects.create(
            titre='Test Article',
            contenu='Contenu ' * 100,
            auteur=self.user,
            categorie=self.cat,
            publie=True,
            date_publication=timezone.now()
        )
    
    def test_creation(self):
        self.assertEqual(self.article.titre, 'Test Article')
        self.assertEqual(self.article.slug, 'test-article')
    
    def test_temps_lecture(self):
        self.assertGreater(self.article.temps_lecture(), 0)
    
    def test_incrementer_vues(self):
        vues_avant = self.article.nombre_vues
        self.article.incrementer_vues()
        self.assertEqual(self.article.nombre_vues, vues_avant + 1)
    
    def test_soft_delete(self):
        self.article.soft_delete(self.user)
        self.assertTrue(self.article.supprime)


class ArticleManagerTest(TestCase):
    
    def setUp(self):
        self.user = User.objects.create_user('test', 'test@test.com', 'pass')
        self.cat = Categorie.objects.create(nom='Tech')
        
        Article.objects.create(
            titre='Publié',
            contenu='...' * 50,
            auteur=self.user,
            categorie=self.cat,
            publie=True,
            date_publication=timezone.now()
        )
        
        Article.objects.create(
            titre='Brouillon',
            contenu='...' * 50,
            auteur=self.user,
            categorie=self.cat,
            publie=False
        )
    
    def test_publies(self):
        self.assertEqual(Article.objects.publies().count(), 1)
    
    def test_brouillons(self):
        self.assertEqual(Article.objects.brouillons().count(), 1)
    
    def test_chainabilite(self):
        result = Article.objects.publies().actifs()
        self.assertGreater(result.count(), 0)


class SignalTest(TestCase):
    
    def test_profil_auto_create(self):
        user = User.objects.create_user('newuser', 'new@test.com', 'pass')
        self.assertTrue(hasattr(user, 'profil'))
    
    def test_like_cache_update(self):
        user = User.objects.create_user('test', 'test@test.com', 'pass')
        article = Article.objects.create(
            titre='Test',
            contenu='...',
            auteur=user,
            publie=True,
            date_publication=timezone.now()
        )
        
        self.assertEqual(article.nb_likes_cache, 0)
        Like.objects.create(article=article, user=user)
        article.refresh_from_db()
        self.assertEqual(article.nb_likes_cache, 1)
```

**Exécutez** :

```bash
# Tous les tests
python manage.py test blog

# Tests spécifiques
python manage.py test blog.tests.ArticleModelTest

# Avec coverage
pip install coverage
coverage run --source='blog' manage.py test blog
coverage report
```

---

# 📖 PARTIE 6 : COMMANDES UTILES ET PRODUCTION

## Étape 12 : Commandes de gestion

**Backup PostgreSQL** :

```bash
# Backup
docker exec blogpro_db pg_dump -U bloguser blogpro > backup.sql

# Restore
docker exec -i blogpro_db psql -U bloguser blogpro < backup.sql
```

**Shell Django avec contexte** :

```python
python manage.py shell

from blog.models import *
from blog.analytics import BlogAnalytics

# Stats globales
stats = BlogAnalytics.stats_globales()
print(stats)

# Top articles
top = BlogAnalytics.top_articles(5)
for a in top:
    print(f"{a.titre}: {a.nombre_vues} vues")

# Recherche full-text
resultats = Article.objects.recherche_fulltext('django postgresql')
for a in resultats:
    print(f"{a.titre} (rank: {a.rank})")

# Stats par catégorie
cats = BlogAnalytics.stats_par_categorie()
for c in cats:
    print(f"{c.nom}: {c.nb_articles} articles")
```

---

# ✅ CHECKLIST FINALE

- ✅ PostgreSQL installé et configuré
- ✅ Modèles avec classes abstraites créés
- ✅ Managers et QuerySets personnalisés
- ✅ Signals configurés
- ✅ Full-text search fonctionnel
- ✅ Analytics et statistiques
- ✅ Indexes optimisés
- ✅ Admin personnalisé
- ✅ Tests unitaires (>80% coverage)
- ✅ Données de test générées

---

# 🚀 PROCHAINES ÉTAPES

Maintenant que vous maîtrisez Django ORM avec PostgreSQL, vous pouvez :

1. **Ajouter une API REST** avec Django REST Framework
2. **Déployer en production** avec Docker + Nginx + Gunicorn
3. **Ajouter du caching** avec Redis
4. **Implémenter Celery** pour tâches asynchrones
5. **Créer un frontend** avec React/Vue.js

---

🎉 **Félicitations !** Vous avez créé un système de blog professionnel complet avec Django et PostgreSQL !

**Votre projet inclut** :
- Architecture robuste et maintenable
- Optimisations PostgreSQL avancées
- Tests complets
- Interface admin professionnelle
- Prêt pour la production

Pour aller plus loin, consultez :
- Documentation Django : https://docs.djangoproject.com/
- Documentation PostgreSQL : https://www.postgresql.org/docs/
- Django Best Practices : https://django-best-practices.readthedocs.io/
