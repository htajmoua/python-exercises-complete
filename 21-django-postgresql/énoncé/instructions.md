# Instructions - Django avec PostgreSQL

PostgreSQL est une base de données relationnelle avancée, recommandée pour la production Django. Ce module vous guidera dans l'installation, la configuration et l'utilisation de PostgreSQL avec Django.

## Partie 1 - Installation et Configuration

### Exercice 1 - Installation de PostgreSQL

**Sur macOS** :
```bash
# Avec Homebrew
brew install postgresql@15
brew services start postgresql@15

# Vérifier l'installation
psql --version
```

**Sur Linux (Ubuntu/Debian)** :
```bash
sudo apt update
sudo apt install postgresql postgresql-contrib
sudo systemctl start postgresql
sudo systemctl enable postgresql
```

**Sur Windows** :
- Téléchargez l'installeur depuis https://www.postgresql.org/download/windows/
- Installez avec les options par défaut
- Notez le mot de passe du superuser `postgres`

### Exercice 2 - Créer une base de données PostgreSQL

**Connectez-vous** à PostgreSQL :
```bash
# Sur Mac/Linux
psql postgres

# Sur Windows (depuis pgAdmin ou cmd)
psql -U postgres
```

**Créez** une base de données et un utilisateur :
```sql
-- Créer un utilisateur
CREATE USER djangouser WITH PASSWORD 'django123';

-- Créer une base de données
CREATE DATABASE blogdb OWNER djangouser;

-- Donner tous les privilèges
GRANT ALL PRIVILEGES ON DATABASE blogdb TO djangouser;

-- Quitter
\q
```

**Vérifiez** la connexion :
```bash
psql -U djangouser -d blogdb -h localhost
```

### Exercice 3 - Installer psycopg2

**Installez** le driver PostgreSQL pour Python :

```bash
# Activez votre environnement virtuel
source venv/bin/activate  # Mac/Linux
# venv\Scripts\activate  # Windows

# Installez psycopg2-binary (pour développement)
pip install psycopg2-binary

# Pour production, utilisez psycopg2
# pip install psycopg2
```

### Exercice 4 - Configurer Django pour PostgreSQL

**Modifiez** `settings.py` :

```python
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'blogdb',
        'USER': 'djangouser',
        'PASSWORD': 'django123',
        'HOST': 'localhost',
        'PORT': '5432',
    }
}
```

**Testez** la connexion :
```bash
python manage.py migrate
```

### Exercice 5 - Variables d'environnement pour les credentials

**Modifiez** votre `.env` :
```
DB_NAME=blogdb
DB_USER=djangouser
DB_PASSWORD=django123
DB_HOST=localhost
DB_PORT=5432
```

**Mettez à jour** `settings.py` :
```python
from decouple import config

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': config('DB_NAME'),
        'USER': config('DB_USER'),
        'PASSWORD': config('DB_PASSWORD'),
        'HOST': config('DB_HOST', default='localhost'),
        'PORT': config('DB_PORT', default='5432'),
    }
}
```

### Exercice 6 - Configuration avancée de la connexion

**Ajoutez** des options de connexion :

```python
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': config('DB_NAME'),
        'USER': config('DB_USER'),
        'PASSWORD': config('DB_PASSWORD'),
        'HOST': config('DB_HOST', default='localhost'),
        'PORT': config('DB_PORT', default='5432'),
        'OPTIONS': {
            'connect_timeout': 10,
            'options': '-c statement_timeout=30000',  # 30 secondes
        },
        'CONN_MAX_AGE': 600,  # Connexions persistantes (10 minutes)
    }
}
```

## Partie 2 - Migrations et Types de Données PostgreSQL

### Exercice 7 - Migrer depuis SQLite vers PostgreSQL

**Exportez** les données de SQLite :
```bash
python manage.py dumpdata > data.json
```

**Changez** la configuration vers PostgreSQL (comme exercice 4-5)

**Créez** les tables :
```bash
python manage.py migrate
```

**Importez** les données :
```bash
python manage.py loaddata data.json
```

### Exercice 8 - Types de champs spécifiques PostgreSQL

**Créez** un modèle avec des types PostgreSQL :

```python
from django.contrib.postgres.fields import ArrayField, JSONField
from django.db import models

class Article(models.Model):
    titre = models.CharField(max_length=200)
    contenu = models.TextField()
    
    # Champ tableau (liste)
    tags = ArrayField(
        models.CharField(max_length=50),
        blank=True,
        default=list
    )
    
    # Champ JSON
    metadata = models.JSONField(
        default=dict,
        blank=True
    )
    
    # Champ date range (plage de dates)
    from django.contrib.postgres.fields import DateTimeRangeField
    periode_publication = DateTimeRangeField(null=True, blank=True)
```

**Migrez** :
```bash
python manage.py makemigrations
python manage.py migrate
```

### Exercice 9 - Utiliser ArrayField

**Dans le shell Django** :

```python
from blog.models import Article

# Créer un article avec tags
article = Article.objects.create(
    titre="Introduction à PostgreSQL",
    contenu="PostgreSQL est une base de données...",
    tags=["PostgreSQL", "Django", "Database"]
)

# Filtrer par tags
Article.objects.filter(tags__contains=["Django"])

# Rechercher dans le tableau
Article.objects.filter(tags__overlap=["PostgreSQL", "Python"])

# Articles avec un tag spécifique à une position
Article.objects.filter(tags__0="PostgreSQL")  # Premier tag
```

### Exercice 10 - Utiliser JSONField

```python
# Créer avec metadata JSON
article = Article.objects.create(
    titre="Article avec metadata",
    contenu="Contenu...",
    metadata={
        "auteur_id": 1,
        "categorie": "Tech",
        "vues": 150,
        "featured": True
    }
)

# Filtrer par clé JSON
Article.objects.filter(metadata__categorie="Tech")

# Filtrer par valeur numérique
Article.objects.filter(metadata__vues__gte=100)

# Filtrer par boolean
Article.objects.filter(metadata__featured=True)

# Accéder à des clés imbriquées
# metadata = {"details": {"priority": "high"}}
Article.objects.filter(metadata__details__priority="high")
```

### Exercice 11 - Full Text Search

**Créez** un modèle avec recherche full-text :

```python
from django.contrib.postgres.search import SearchVector, SearchQuery, SearchRank

# Recherche simple
from blog.models import Article

# Rechercher dans plusieurs champs
Article.objects.annotate(
    search=SearchVector('titre', 'contenu'),
).filter(search='django')

# Recherche avec ranking
search_query = SearchQuery('django')
Article.objects.annotate(
    search=SearchVector('titre', 'contenu'),
    rank=SearchRank(SearchVector('titre', 'contenu'), search_query)
).filter(search=search_query).order_by('-rank')
```

**Ajoutez** un index de recherche :

```python
from django.contrib.postgres.indexes import GinIndex
from django.contrib.postgres.search import SearchVectorField

class Article(models.Model):
    titre = models.CharField(max_length=200)
    contenu = models.TextField()
    search_vector = SearchVectorField(null=True)
    
    class Meta:
        indexes = [
            GinIndex(fields=['search_vector']),
        ]
```

## Partie 3 - Indexes et Performance

### Exercice 12 - Créer des indexes

**Ajoutez** des indexes pour performance :

```python
from django.db import models

class Article(models.Model):
    titre = models.CharField(max_length=200, db_index=True)  # Index simple
    slug = models.SlugField(unique=True)  # Unique = index automatique
    publie = models.BooleanField(default=False)
    date_creation = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        indexes = [
            models.Index(fields=['publie', 'date_creation']),  # Index composite
            models.Index(fields=['-date_creation']),  # Index descendant
        ]
```

### Exercice 13 - Index spécifiques PostgreSQL

```python
from django.contrib.postgres.indexes import BTreeIndex, HashIndex, GinIndex, GistIndex

class Article(models.Model):
    titre = models.CharField(max_length=200)
    tags = ArrayField(models.CharField(max_length=50))
    
    class Meta:
        indexes = [
            BTreeIndex(fields=['titre']),  # Index B-tree
            GinIndex(fields=['tags']),  # GIN pour tableaux
        ]
```

### Exercice 14 - Analyser les performances avec EXPLAIN

**Activez** le logging des requêtes dans `settings.py` :

```python
LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'handlers': {
        'console': {
            'class': 'logging.StreamHandler',
        },
    },
    'loggers': {
        'django.db.backends': {
            'handlers': ['console'],
            'level': 'DEBUG',
        },
    },
}
```

**Dans le shell** :
```python
from django.db import connection

articles = Article.objects.filter(publie=True).order_by('-date_creation')

# Voir le SQL généré
print(articles.query)

# Voir EXPLAIN
with connection.cursor() as cursor:
    cursor.execute('EXPLAIN ANALYZE ' + str(articles.query))
    print(cursor.fetchall())
```

### Exercice 15 - Optimiser les requêtes

**Utilisez** `select_related` et `prefetch_related` :

```python
# Mauvais - N+1 queries
articles = Article.objects.all()
for article in articles:
    print(article.auteur.nom)  # Requête pour chaque article

# Bon - 1 seule requête supplémentaire
articles = Article.objects.select_related('auteur').all()
for article in articles:
    print(article.auteur.nom)

# Pour ManyToMany
articles = Article.objects.prefetch_related('tags').all()
```

## Partie 4 - Fonctionnalités Avancées

### Exercice 16 - Contraintes PostgreSQL

**Ajoutez** des contraintes au niveau base de données :

```python
from django.db import models
from django.contrib.postgres.constraints import ExclusionConstraint
from django.contrib.postgres.fields import DateTimeRangeField, RangeOperators

class Reservation(models.Model):
    salle = models.CharField(max_length=100)
    periode = DateTimeRangeField()
    
    class Meta:
        constraints = [
            # Empêcher chevauchement de réservations
            ExclusionConstraint(
                name='exclude_overlapping_reservations',
                expressions=[
                    ('salle', RangeOperators.EQUAL),
                    ('periode', RangeOperators.OVERLAPS),
                ],
            ),
        ]
```

### Exercice 17 - Triggers et fonctions PostgreSQL

**Créez** une migration personnalisée :

```python
# Dans migrations/XXXX_custom_trigger.py
from django.db import migrations

class Migration(migrations.Migration):
    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.RunSQL(
            sql="""
                CREATE OR REPLACE FUNCTION update_modified_column()
                RETURNS TRIGGER AS $$
                BEGIN
                    NEW.date_modification = now();
                    RETURN NEW;
                END;
                $$ language 'plpgsql';
                
                CREATE TRIGGER update_article_modtime
                BEFORE UPDATE ON blog_article
                FOR EACH ROW
                EXECUTE FUNCTION update_modified_column();
            """,
            reverse_sql="""
                DROP TRIGGER IF EXISTS update_article_modtime ON blog_article;
                DROP FUNCTION IF EXISTS update_modified_column();
            """
        ),
    ]
```

### Exercice 18 - Vues matérialisées

**Créez** une vue matérialisée pour les statistiques :

```python
# Migration personnalisée
migrations.RunSQL(
    sql="""
        CREATE MATERIALIZED VIEW article_stats AS
        SELECT 
            auteur_id,
            COUNT(*) as nombre_articles,
            AVG(CHAR_LENGTH(contenu)) as longueur_moyenne
        FROM blog_article
        WHERE publie = true
        GROUP BY auteur_id;
        
        CREATE INDEX ON article_stats (auteur_id);
    """,
    reverse_sql="DROP MATERIALIZED VIEW IF EXISTS article_stats;"
)

# Rafraîchir la vue
migrations.RunSQL("REFRESH MATERIALIZED VIEW article_stats;")
```

### Exercice 19 - Connexions multiples

**Configurez** plusieurs bases de données :

```python
# settings.py
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'blogdb',
        'USER': 'djangouser',
        'PASSWORD': 'django123',
        'HOST': 'localhost',
    },
    'analytics': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'analyticsdb',
        'USER': 'djangouser',
        'PASSWORD': 'django123',
        'HOST': 'localhost',
    }
}
```

**Utilisez** les databases :
```python
# Lire depuis analytics
Article.objects.using('analytics').all()

# Sauvegarder dans analytics
article.save(using='analytics')
```

### Exercice 20 - Backup et Restore

**Backup de la base de données** :
```bash
# Dump complet
pg_dump -U djangouser -h localhost blogdb > backup.sql

# Dump avec format custom (compressé)
pg_dump -U djangouser -h localhost -Fc blogdb > backup.dump

# Dump seulement les données
pg_dump -U djangouser -h localhost --data-only blogdb > data.sql
```

**Restore** :
```bash
# Depuis SQL
psql -U djangouser -h localhost -d blogdb < backup.sql

# Depuis format custom
pg_restore -U djangouser -h localhost -d blogdb backup.dump
```

## Partie 5 - Docker et PostgreSQL

### Exercice 21 - PostgreSQL avec Docker

**Créez** `docker-compose.yml` :

```yaml
version: '3.8'

services:
  db:
    image: postgres:15
    environment:
      POSTGRES_DB: blogdb
      POSTGRES_USER: djangouser
      POSTGRES_PASSWORD: django123
    ports:
      - "5432:5432"
    volumes:
      - postgres_data:/var/lib/postgresql/data

volumes:
  postgres_data:
```

**Lancez** :
```bash
docker-compose up -d

# Vérifier
docker-compose ps

# Logs
docker-compose logs db
```

**Connectez Django** (même configuration qu'exercice 4)

### Exercice 22 - PgAdmin avec Docker

**Ajoutez** PgAdmin dans `docker-compose.yml` :

```yaml
services:
  db:
    # ... config existante ...
  
  pgadmin:
    image: dpage/pgadmin4
    environment:
      PGADMIN_DEFAULT_EMAIL: admin@example.com
      PGADMIN_DEFAULT_PASSWORD: admin
    ports:
      - "5050:80"
    depends_on:
      - db
```

**Accédez** à http://localhost:5050

## Exercices bonus

### Exercice 23 - Partitioning de tables
**Créez** des tables partitionnées par date pour les gros volumes.

### Exercice 24 - Réplication
**Configurez** une réplication master-slave PostgreSQL.

### Exercice 25 - Connection Pooling
**Installez** et configurez pgBouncer pour le pooling de connexions.

## Checklist de validation

- ✅ PostgreSQL installé et configuré
- ✅ Base de données et utilisateur créés
- ✅ Django connecté à PostgreSQL
- ✅ Credentials dans variables d'environnement
- ✅ Types PostgreSQL utilisés (ArrayField, JSONField)
- ✅ Full-text search implémenté
- ✅ Indexes créés et optimisés
- ✅ Migrations depuis SQLite réussies
- ✅ Backup/Restore testés
- ✅ Docker configuré (optionnel)

## Ressources

- [Documentation PostgreSQL](https://www.postgresql.org/docs/)
- [Django PostgreSQL features](https://docs.djangoproject.com/en/stable/ref/contrib/postgres/)
- [psycopg2 documentation](https://www.psycopg.org/docs/)
