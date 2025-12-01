# Instructions - Django ORM : Techniques Avancées

**🎯 Objectif du module** : Maîtriser les techniques avancées de l'ORM Django pour des applications professionnelles.

Ce module couvre les techniques utilisées dans des projets professionnels :
- Migrations de données complexes
- Indexes et contraintes pour optimiser les performances
- Raw SQL et requêtes PostgreSQL avancées
- Signals pour automatiser des actions
- Managers personnalisés pour encapsuler la logique métier
- Validation personnalisée

**📚 Format du module** :
- **Partie 1 (Exercices 1-3)** : Exemples guidés - Migrations, Indexes, Raw SQL
- **Partie 2 (Exercices 4-6)** : Exercices pratiques - Signals, Managers, Validation

**Prérequis** : Avoir complété les modules 15 et 16

---

# 📖 PARTIE 1 : EXEMPLES GUIDÉS

Les exercices 1 à 3 sont des exemples complets pour comprendre les techniques avancées.

---

## Exercice 1 - Migrations de données (EXEMPLE)

```python
# migrations/0010_populate_slugs.py
from django.db import migrations
from django.utils.text import slugify

def generate_slugs(apps, schema_editor):
    """Générer les slugs pour les articles existants"""
    Article = apps.get_model('blog', 'Article')
    for article in Article.objects.all():
        if not article.slug:
            article.slug = slugify(article.titre)
            article.save()

def reverse_slugs(apps, schema_editor):
    """Migration inverse (optionnel)"""
    Article = apps.get_model('blog', 'Article')
    Article.objects.all().update(slug='')

class Migration(migrations.Migration):
    dependencies = [
        ('blog', '0009_article_slug'),
    ]

    operations = [
        migrations.RunPython(generate_slugs, reverse_slugs),
    ]
```

**Migration avec données complexes** :

```python
def migrer_categories(apps, schema_editor):
    """Migrer les anciennes catégories vers le nouveau système"""
    Article = apps.get_model('blog', 'Article')
    Categorie = apps.get_model('blog', 'Categorie')
    ArticleCategorie = apps.get_model('blog', 'ArticleCategorie')
    
    # Créer les nouvelles catégories
    categories_mapping = {}
    for old_cat in ['tech', 'business', 'lifestyle']:
        nouvelle_cat, created = Categorie.objects.get_or_create(
            nom=old_cat.capitalize(),
            slug=old_cat
        )
        categories_mapping[old_cat] = nouvelle_cat
    
    # Migrer les articles
    for article in Article.objects.all():
        if article.categorie_ancienne:
            cat = categories_mapping.get(article.categorie_ancienne)
            if cat:
                ArticleCategorie.objects.create(
                    article=article,
                    categorie=cat,
                    principale=True
                )

class Migration(migrations.Migration):
    dependencies = [
        ('blog', '0011_new_category_system'),
    ]

    operations = [
        migrations.RunPython(migrer_categories, migrations.RunPython.noop),
    ]
```

### Exercice 24 - Migrations SQL personnalisées (RunSQL)

```python
class Migration(migrations.Migration):
    dependencies = [
        ('blog', '0012_data_migration'),
    ]

    operations = [
        migrations.RunSQL(
            # Migration forward
            sql="""
                CREATE INDEX idx_article_titre_trgm 
                ON blog_article 
                USING gin(titre gin_trgm_ops);
            """,
            # Migration reverse
            reverse_sql="""
                DROP INDEX IF EXISTS idx_article_titre_trgm;
            """
        ),
    ]
```

**Migration avec fonction PostgreSQL** :

```python
class Migration(migrations.Migration):
    dependencies = [
        ('blog', '0013_custom_index'),
    ]

    operations = [
        migrations.RunSQL(
            sql="""
                CREATE OR REPLACE FUNCTION update_article_search_vector()
                RETURNS trigger AS $$
                BEGIN
                    NEW.search_vector := 
                        setweight(to_tsvector('french', COALESCE(NEW.titre, '')), 'A') ||
                        setweight(to_tsvector('french', COALESCE(NEW.contenu, '')), 'B');
                    RETURN NEW;
                END;
                $$ LANGUAGE plpgsql;

                CREATE TRIGGER article_search_vector_update
                BEFORE INSERT OR UPDATE ON blog_article
                FOR EACH ROW EXECUTE FUNCTION update_article_search_vector();
            """,
            reverse_sql="""
                DROP TRIGGER IF EXISTS article_search_vector_update ON blog_article;
                DROP FUNCTION IF EXISTS update_article_search_vector();
            """
        ),
    ]
```

### Exercice 25 - Squashing migrations

```bash
# Compresser les migrations 0001 à 0015 en une seule
python manage.py squashmigrations blog 0001 0015

# Résultat : création de 0001_squashed_0015.py
```

**Quand squasher ?**
- Trop de migrations (> 50)
- Développement local uniquement
- Après un jalon important du projet

---

## 📚 PARTIE 7 : INDEXES ET CONTRAINTES

## Exercice 2 - Indexes pour optimisation (EXEMPLE)

```python
class Article(models.Model):
    titre = models.CharField(max_length=200, db_index=True)  # Index simple
    slug = models.SlugField(unique=True)  # Unique crée automatiquement un index
    date_creation = models.DateTimeField(auto_now_add=True)
    publie = models.BooleanField(default=False)
    
    class Meta:
        # Index composites
        indexes = [
            # Index sur plusieurs champs
            models.Index(fields=['publie', '-date_creation'], name='idx_publie_date'),
            
            # Index partiel (PostgreSQL uniquement)
            models.Index(
                fields=['titre'],
                name='idx_titre_publie',
                condition=Q(publie=True)
            ),
            
            # Index pour recherche full-text
            models.Index(fields=['slug', 'titre'], name='idx_slug_titre'),
        ]

# Migration générée :
# CREATE INDEX "idx_publie_date" ON "blog_article" ("publie", "date_creation" DESC);
```

**Indexes GIN/GIST (PostgreSQL)** :

```python
from django.contrib.postgres.indexes import GinIndex, GistIndex
from django.contrib.postgres.search import SearchVectorField

class Article(models.Model):
    titre = models.CharField(max_length=200)
    contenu = models.TextField()
    search_vector = SearchVectorField(null=True)
    tags = models.JSONField(default=list)
    
    class Meta:
        indexes = [
            # GIN pour full-text search
            GinIndex(fields=['search_vector'], name='idx_search_vector'),
            
            # GIN pour JSONField
            GinIndex(fields=['tags'], name='idx_tags_gin'),
        ]
```

### Exercice 27 - Contraintes de base de données

```python
from django.db.models import Q, CheckConstraint, UniqueConstraint

class Article(models.Model):
    titre = models.CharField(max_length=200)
    slug = models.SlugField()
    date_publication = models.DateField(null=True, blank=True)
    publie = models.BooleanField(default=False)
    prix = models.DecimalField(max_digits=10, decimal_places=2, null=True)
    prix_promo = models.DecimalField(max_digits=10, decimal_places=2, null=True)
    
    class Meta:
        constraints = [
            # Contrainte CHECK : prix promotionnel < prix normal
            CheckConstraint(
                check=Q(prix_promo__lt=F('prix')) | Q(prix_promo__isnull=True),
                name='prix_promo_inferieur'
            ),
            
            # Contrainte CHECK : article publié doit avoir une date
            CheckConstraint(
                check=Q(publie=False) | Q(date_publication__isnull=False),
                name='publie_avec_date'
            ),
            
            # Contrainte UNIQUE composite
            UniqueConstraint(
                fields=['slug', 'annee'],
                name='unique_slug_annee'
            ),
            
            # Contrainte UNIQUE conditionnelle
            UniqueConstraint(
                fields=['titre'],
                condition=Q(publie=True),
                name='unique_titre_si_publie'
            ),
        ]
```

**Contraintes complexes** :

```python
class Reservation(models.Model):
    hotel = models.ForeignKey('Hotel', on_delete=models.CASCADE)
    chambre = models.CharField(max_length=10)
    date_debut = models.DateField()
    date_fin = models.DateField()
    
    class Meta:
        constraints = [
            # Date de fin après date de début
            CheckConstraint(
                check=Q(date_fin__gt=F('date_debut')),
                name='dates_coherentes'
            ),
            
            # Pas de chevauchement de réservations
            # (Nécessite extension btree_gist sur PostgreSQL)
            # migrations.RunSQL(
            #     "CREATE EXTENSION IF NOT EXISTS btree_gist;",
            #     reverse_sql="DROP EXTENSION IF EXISTS btree_gist;"
            # )
            # EXCLUDE USING gist (
            #     hotel WITH =,
            #     chambre WITH =,
            #     daterange(date_debut, date_fin) WITH &&
            # )
        ]
```

---

## 📚 PARTIE 8 : RAW SQL ET REQUÊTES PERSONNALISÉES

## Exercice 3 - Raw SQL (EXEMPLE)

```python
# Requête SQL brute qui retourne des objets du modèle
articles = Article.objects.raw(
    'SELECT * FROM blog_article WHERE publie = %s ORDER BY nombre_vues DESC',
    [True]
)

for article in articles:
    print(article.titre)  # Objets Article normaux

# Avec paramètres nommés
articles = Article.objects.raw(
    '''
    SELECT * FROM blog_article 
    WHERE publie = %(publie)s 
    AND date_creation > %(date)s
    ''',
    {'publie': True, 'date': '2024-01-01'}
)

# Mapping de colonnes
articles = Article.objects.raw(
    'SELECT id, titre as titre_article FROM blog_article'
)

# Annotations personnalisées
articles = Article.objects.raw(
    '''
    SELECT a.*, COUNT(c.id) as nb_commentaires
    FROM blog_article a
    LEFT JOIN blog_commentaire c ON c.article_id = a.id
    GROUP BY a.id
    '''
)
for article in articles:
    print(f"{article.titre}: {article.nb_commentaires} commentaires")
```

### Exercice 29 - cursor.execute() pour SQL pur

```python
from django.db import connection

def statistiques_avancees():
    """Requête SQL complexe qui ne retourne pas de modèles"""
    with connection.cursor() as cursor:
        cursor.execute("""
            SELECT 
                a.nom AS auteur,
                COUNT(DISTINCT ar.id) as nb_articles,
                SUM(ar.nombre_vues) as total_vues,
                AVG(ar.nombre_vues) as moyenne_vues,
                MAX(ar.date_creation) as dernier_article
            FROM blog_auteur a
            JOIN blog_article ar ON ar.auteur_id = a.id
            WHERE ar.publie = %s
            GROUP BY a.id, a.nom
            HAVING COUNT(ar.id) > %s
            ORDER BY total_vues DESC
        """, [True, 5])
        
        columns = [col[0] for col in cursor.description]
        results = [dict(zip(columns, row)) for row in cursor.fetchall()]
        
    return results

# Utilisation
stats = statistiques_avancees()
for stat in stats:
    print(f"{stat['auteur']}: {stat['nb_articles']} articles, {stat['total_vues']} vues")
```

**Requêtes avec plusieurs curseurs** :

```python
def rapport_complet():
    with connection.cursor() as cursor:
        # Requête 1 : Top auteurs
        cursor.execute("""
            SELECT nom, COUNT(articles.id) as nb
            FROM blog_auteur 
            JOIN blog_article articles ON articles.auteur_id = blog_auteur.id
            GROUP BY blog_auteur.id, nom
            ORDER BY nb DESC
            LIMIT 10
        """)
        top_auteurs = cursor.fetchall()
        
        # Requête 2 : Articles populaires
        cursor.execute("""
            SELECT titre, nombre_vues
            FROM blog_article
            WHERE publie = TRUE
            ORDER BY nombre_vues DESC
            LIMIT 10
        """)
        top_articles = cursor.fetchall()
        
    return {
        'auteurs': top_auteurs,
        'articles': top_articles
    }
```

### Exercice 30 - Fonctions PostgreSQL avancées

```python
# Full-text search avec PostgreSQL
from django.contrib.postgres.search import SearchVector, SearchQuery, SearchRank

# Recherche simple
Article.objects.filter(titre__search='django python')

# Recherche pondérée
Article.objects.annotate(
    search=SearchVector('titre', weight='A') + SearchVector('contenu', weight='B')
).filter(search=SearchQuery('django'))

# Recherche avec ranking
Article.objects.annotate(
    search=SearchVector('titre', weight='A') + SearchVector('contenu', weight='B'),
    rank=SearchRank(F('search'), SearchQuery('django python'))
).filter(search=SearchQuery('django python')).order_by('-rank')

# Recherche avec trigrams (similarité)
from django.contrib.postgres.search import TrigramSimilarity

Article.objects.annotate(
    similarity=TrigramSimilarity('titre', 'djngo'),  # Typo volontaire
).filter(similarity__gt=0.3).order_by('-similarity')

# JSONField queries
Article.objects.filter(metadata__auteur='Jean')
Article.objects.filter(metadata__tags__contains=['python'])
Article.objects.filter(metadata__stats__vues__gte=1000)

# ArrayField (PostgreSQL)
from django.contrib.postgres.fields import ArrayField

class Tag(models.Model):
    couleurs = ArrayField(models.CharField(max_length=7), default=list)

Tag.objects.filter(couleurs__contains=['#FF0000'])
Tag.objects.filter(couleurs__overlap=['#FF0000', '#00FF00'])
```

---

# 🔨 PARTIE 2 : EXERCICES PRATIQUES

**À partir d'ici, c'est à vous de coder !** Les exercices suivants contiennent des squelettes avec des `TODO` à compléter.

---

## Exercice 4 - Signals (PRATIQUE)

**Objectif** : Utiliser les signals pour automatiser des actions (générer slug, mettre à jour stats).

**Les signals Django** : Réagir automatiquement aux événements (save, delete, etc.)

**Consignes** :
1. Créez un fichier `blog/signals.py`
2. Créez un signal `pre_save` pour générer automatiquement le slug
3. Créez un signal `post_save` pour mettre à jour les stats de l'auteur
4. Activez les signals dans `blog/apps.py`

**Squelette - `blog/signals.py`** (fichier à créer) :

```python
from django.db.models.signals import pre_save, post_save, pre_delete
from django.dispatch import receiver
from django.utils.text import slugify
from .models import Article

# TODO : Créez un signal pre_save pour générer le slug automatiquement
@receiver(pre_save, sender=Article)
def generer_slug(sender, instance, **kwargs):
    """Générer automatiquement le slug avant sauvegarde"""
    # TODO : Si instance.slug est vide, générez-le avec slugify(instance.titre)
    if not instance.slug:
        instance.slug = # VOTRE CODE ICI

# TODO : Créez un signal post_save pour mettre à jour les stats de l'auteur
@receiver(post_save, sender=Article)
def mettre_a_jour_stats_auteur(sender, instance, created, **kwargs):
    """Mettre à jour les statistiques de l'auteur"""
    # TODO : Récupérez l'auteur de l'article
    auteur = # VOTRE CODE ICI
    
    # TODO : Mettez à jour le nombre d'articles dans auteur.profil
    # Utilisez : auteur.articles.count()
    # VOTRE CODE ICI
    
    # TODO : Sauvegardez le profil
    # VOTRE CODE ICI

# TODO BONUS : Créez un signal pre_delete pour archiver avant suppression
@receiver(pre_delete, sender=Article)
def archiver_avant_suppression(sender, instance, **kwargs):
    """Archiver l'article avant suppression"""
    # TODO : Créez un log ou une archive
    # Exemple : print(f"Suppression de {instance.titre}")
    # VOTRE CODE ICI
    pass
```

**Squelette - `blog/apps.py`** (à modifier) :

```python
from django.apps import AppConfig

class BlogConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'blog'

    def ready(self):
        # TODO : Importez les signals pour les activer
        # Utilisez : import blog.signals
        # VOTRE CODE ICI
        pass
```

**Indice** :
- `pre_save` : Avant la sauvegarde (modifiez l'instance)
- `post_save` : Après la sauvegarde (utilisez `created` pour savoir si c'est un nouvel objet)
- `pre_delete` : Avant la suppression
- `receiver` : Décorateur pour connecter le signal

**Validation** :

```python
# TODO : Testez dans le shell
python manage.py shell

from blog.models import Article, Auteur

# TODO : Créez un article SANS slug
auteur = Auteur.objects.first()
article = Article(titre="Test Signal", contenu="...", auteur=auteur)
article.save()

# TODO : Vérifiez que le slug a été généré automatiquement
print(article.slug)  # Devrait afficher "test-signal"

# TODO : Vérifiez que les stats de l'auteur ont été mises à jour
print(auteur.profil.nombre_articles)
```

---

## Exercice 5 - Managers personnalisés (PRATIQUE)

**Objectif** : Créer des managers personnalisés pour encapsuler la logique métier.

**Les Managers** : Encapsulent les requêtes courantes pour réutiliser le code.

**Consignes** :
1. Créez un manager `PublieManager` pour filtrer les articles publiés
2. Créez un manager `ArticleManager` avec des méthodes personnalisées
3. Utilisez les managers dans vos vues

**Squelette - `blog/models.py`** (à compléter) :

```python
from django.db import models

# TODO : Créez un manager pour les articles publiés
class PublieManager(models.Manager):
    def get_queryset(self):
        # TODO : Retournez seulement les articles publiés
        # Utilisez : super().get_queryset().filter(publie=True)
        return # VOTRE CODE ICI

# TODO : Créez un manager avec des méthodes personnalisées
class ArticleManager(models.Manager):
    def publies(self):
        """Retourne les articles publiés"""
        # TODO : Filtrez par publie=True
        return # VOTRE CODE ICI
    
    def recents(self, nombre=5):
        """Retourne les N articles les plus récents"""
        # TODO : Triez par -date_creation et limitez
        return # VOTRE CODE ICI
    
    def populaires(self, min_vues=1000):
        """Retourne les articles populaires"""
        # TODO : Filtrez par nombre_vues__gte=min_vues
        return # VOTRE CODE ICI

class Article(models.Model):
    titre = models.CharField(max_length=200)
    contenu = models.TextField()
    publie = models.BooleanField(default=False)
    nombre_vues = models.PositiveIntegerField(default=0)
    date_creation = models.DateTimeField(auto_now_add=True)
    
    # TODO : Ajoutez le manager par défaut
    objects = ArticleManager()
    
    # TODO : Ajoutez le manager 'publies' (optionnel)
    # publies = PublieManager()
```

**Indice** :
- Le manager par défaut est `objects`
- Vous pouvez avoir plusieurs managers
- Les méthodes du manager encapsulent les QuerySets

**Validation** :

```python
# TODO : Testez dans le shell
from blog.models import Article

# TODO : Utilisez le manager personnalisé
recents = Article.objects.recents(10)
print(list(recents))

populaires = Article.objects.populaires(min_vues=500)
print(f"Articles populaires : {populaires.count()}")

# TODO : Chaînez les méthodes
top_recents = Article.objects.publies().recents(5)
```

---

## Exercice 6 - Validation personnalisée (PRATIQUE)

**Objectif** : Ajouter de la validation personnalisée au niveau du modèle.

**Validation Django** : Valider les données avant la sauvegarde en BDD.

**Consignes** :
1. Ajoutez une méthode `clean()` au modèle Article
2. Créez un validator personnalisé pour valider le contenu
3. Testez la validation

**Squelette - `blog/models.py`** (à compléter) :

```python
from django.core.exceptions import ValidationError
from django.core.validators import MinLengthValidator

# TODO : Créez un validator personnalisé
def valider_contenu_min(value):
    """Valide que le contenu a au moins 100 caractères"""
    # TODO : Si len(value) < 100, levez ValidationError
    if len(value) < 100:
        raise ValidationError(
            # VOTRE MESSAGE D'ERREUR ICI
        )

class Article(models.Model):
    titre = models.CharField(max_length=200)
    # TODO : Ajoutez le validator au champ contenu
    contenu = models.TextField(
        validators=[valider_contenu_min]
    )
    publie = models.BooleanField(default=False)
    nombre_vues = models.PositiveIntegerField(default=0)
    
    # TODO : Ajoutez une méthode clean() pour validation personnalisée
    def clean(self):
        """Validation personnalisée du modèle"""
        # TODO : Vérifiez que le titre ne contient pas "spam" (exemple)
        if 'spam' in self.titre.lower():
            raise ValidationError({
                'titre': "Le titre ne peut pas contenir 'spam'"
            })
        
        # TODO : Vérifiez que si publie=True, le contenu est renseigné
        if self.publie and not self.contenu.strip():
            raise ValidationError({
                'contenu': # VOTRE MESSAGE D'ERREUR ICI
            })
    
    def save(self, *args, **kwargs):
        # TODO : Appelez full_clean() avant la sauvegarde (optionnel mais recommandé)
        # self.full_clean()
        super().save(*args, **kwargs)
```

**Indice** :
- `clean()` : Validation au niveau du modèle
- `validators` : Liste de fonctions de validation pour un champ
- `full_clean()` : Exécute toutes les validations
- `ValidationError` : Exception à lever pour les erreurs de validation

**Validation** :

```python
# TODO : Testez dans le shell
from blog.models import Article
from django.core.exceptions import ValidationError

# TODO : Essayez de créer un article invalide
try:
    article = Article(titre="SPAM Article", contenu="x" * 50)
    article.full_clean()  # Déclenche la validation
except ValidationError as e:
    print(f"Erreurs : {e.message_dict}")

# TODO : Créez un article valide
article = Article(
    titre="Article valide",
    contenu="x" * 150  # Plus de 100 caractères
)
article.full_clean()  # Pas d'erreur
article.save()
print("Article sauvegardé !")
```

---

**⚠️ Attention** : 
- `full_clean()` n'est PAS appelé automatiquement par `save()`
- Dans les formulaires Django, `full_clean()` est appelé automatiquement
- En production, appelez toujours `full_clean()` avant `save()` ou utilisez des formulaires

---

## Exercice 32 - Signals ManyToMany

```python
from django.db.models.signals import m2m_changed

@receiver(m2m_changed, sender=Article.tags.through)
def tags_changed(sender, instance, action, **kwargs):
    """Réagir aux changements de tags"""
    if action == "post_add":
        print(f"Tags ajoutés à {instance.titre}")
        # Mettre à jour un cache, recalculer des stats, etc.
    
    elif action == "post_remove":
        print(f"Tags retirés de {instance.titre}")
    
    elif action == "post_clear":
        print(f"Tous les tags retirés de {instance.titre}")

# Actions possibles :
# - pre_add : Avant l'ajout
# - post_add : Après l'ajout
# - pre_remove : Avant le retrait
# - post_remove : Après le retrait
# - pre_clear : Avant clear()
# - post_clear : Après clear()
```

### Exercice 33 - Signals personnalisés

```python
# blog/signals.py
from django.dispatch import Signal

# Définir un signal personnalisé
article_viewed = Signal()  # providing_args=['article', 'user'] (deprecated)

# Émettre le signal
from .signals import article_viewed

def voir_article(request, article_id):
    article = Article.objects.get(id=article_id)
    
    # Émettre le signal
    article_viewed.send(
        sender=Article,
        article=article,
        user=request.user
    )
    
    return render(request, 'article.html', {'article': article})

# Recevoir le signal
@receiver(article_viewed)
def incrementer_vues(sender, article, user, **kwargs):
    """Incrémenter le nombre de vues"""
    article.nombre_vues += 1
    article.save(update_fields=['nombre_vues'])

@receiver(article_viewed)
def logger_vue(sender, article, user, **kwargs):
    """Logger la vue dans une table d'analytics"""
    VueArticle.objects.create(
        article=article,
        user=user if user.is_authenticated else None,
        date=timezone.now()
    )
```

---

## 📚 PARTIE 10 : MANAGERS PERSONNALISÉS

### Exercice 34 - Managers basiques

```python
class ArticlePublieManager(models.Manager):
    """Manager pour articles publiés uniquement"""
    def get_queryset(self):
        return super().get_queryset().filter(publie=True)

class ArticleFeaturedManager(models.Manager):
    """Manager pour articles mis en avant"""
    def get_queryset(self):
        return super().get_queryset().filter(featured=True, publie=True)

class Article(models.Model):
    # ... champs ...
    publie = models.BooleanField(default=False)
    featured = models.BooleanField(default=False)
    
    # Managers
    objects = models.Manager()  # Manager par défaut (IMPORTANT : à garder)
    publies = ArticlePublieManager()
    featured = ArticleFeaturedManager()

# Utilisation
Article.objects.all()  # Tous
Article.publies.all()  # Seulement publiés
Article.featured.all()  # Seulement featured
```

### Exercice 35 - Managers avec méthodes personnalisées

```python
class ArticleManager(models.Manager):
    def publies(self):
        """Articles publiés"""
        return self.filter(publie=True)
    
    def brouillons(self):
        """Articles en brouillon"""
        return self.filter(publie=False)
    
    def par_auteur(self, auteur):
        """Articles d'un auteur spécifique"""
        return self.filter(auteur=auteur)
    
    def populaires(self, limite=10):
        """Articles les plus populaires"""
        return self.filter(publie=True).order_by('-nombre_vues')[:limite]
    
    def recents(self, jours=7):
        """Articles récents"""
        depuis = timezone.now() - timedelta(days=jours)
        return self.filter(date_creation__gte=depuis, publie=True)
    
    def avec_stats(self):
        """Articles avec statistiques annotées"""
        return self.annotate(
            nb_commentaires=Count('commentaires'),
            nb_likes=Count('likes')
        )
    
    def recherche(self, query):
        """Recherche dans titre et contenu"""
        return self.filter(
            Q(titre__icontains=query) | Q(contenu__icontains=query),
            publie=True
        )

class Article(models.Model):
    # ... champs ...
    objects = ArticleManager()

# Utilisation
Article.objects.populaires(5)
Article.objects.recents(jours=30)
Article.objects.recherche('django')
Article.objects.par_auteur(auteur).avec_stats()
```

### Exercice 36 - Managers chainables

```python
class ArticleQuerySet(models.QuerySet):
    """QuerySet personnalisé (chainable)"""
    def publies(self):
        return self.filter(publie=True)
    
    def brouillons(self):
        return self.filter(publie=False)
    
    def featured(self):
        return self.filter(featured=True)
    
    def par_tag(self, tag_slug):
        return self.filter(tags__slug=tag_slug)
    
    def avec_auteur(self):
        return self.select_related('auteur', 'auteur__profil')
    
    def avec_tags(self):
        return self.prefetch_related('tags')
    
    def optimise(self):
        return self.select_related('auteur').prefetch_related('tags', 'commentaires')

class ArticleManager(models.Manager):
    def get_queryset(self):
        return ArticleQuerySet(self.model, using=self._db)
    
    # Proxy methods
    def publies(self):
        return self.get_queryset().publies()
    
    def brouillons(self):
        return self.get_queryset().brouillons()
    
    def featured(self):
        return self.get_queryset().featured()

class Article(models.Model):
    # ... champs ...
    objects = ArticleManager()

# Utilisation chainable ⭐
Article.objects.publies().featured().par_tag('python').optimise()
Article.objects.brouillons().avec_auteur().order_by('-date_creation')[:10]
```

### Exercice 37 - Manager as_manager()

```python
class ArticleQuerySet(models.QuerySet):
    def publies(self):
        return self.filter(publie=True)
    
    def populaires(self):
        return self.filter(nombre_vues__gte=1000)
    
    def recents(self, jours=7):
        depuis = timezone.now() - timedelta(days=jours)
        return self.filter(date_creation__gte=depuis)

class Article(models.Model):
    # ... champs ...
    
    # Convertir le QuerySet en Manager automatiquement
    objects = ArticleQuerySet.as_manager()

# Les méthodes du QuerySet deviennent disponibles sur objects
Article.objects.publies().populaires().recents(30)
```
## 📚 PARTIE 11 : VALIDATION PERSONNALISÉE

### Exercice 38 - Validation au niveau du modèle

```python
from django.core.exceptions import ValidationError
from django.core.validators import MinValueValidator, MaxValueValidator, RegexValidator

class Article(models.Model):
    titre = models.CharField(
        max_length=200,
        validators=[
            RegexValidator(
                regex=r'^[A-Z]',
                message='Le titre doit commencer par une majuscule'
            )
        ]
    )
    contenu = models.TextField()
    prix = models.DecimalField(
        max_digits=10,
        decimal_places=2,
        validators=[MinValueValidator(0), MaxValueValidator(10000)]
    )
    prix_promo = models.DecimalField(
        max_digits=10,
        decimal_places=2,
        null=True,
        blank=True
    )
    
    def clean(self):
        """Validation personnalisée au niveau du modèle"""
        super().clean()
        
        # Le prix promo doit être inférieur au prix normal
        if self.prix_promo and self.prix_promo >= self.prix:
            raise ValidationError({
                'prix_promo': 'Le prix promotionnel doit être inférieur au prix normal'
            })
        
        # Article publié doit avoir un contenu de 100 caractères minimum
        if self.publie and len(self.contenu) < 100:
            raise ValidationError({
                'contenu': 'Un article publié doit avoir au moins 100 caractères'
            })
        
        # Titre unique par auteur
        if Article.objects.filter(
            auteur=self.auteur,
            titre=self.titre
        ).exclude(pk=self.pk).exists():
            raise ValidationError({
                'titre': 'Vous avez déjà un article avec ce titre'
            })
    
    def clean_fields(self, exclude=None):
        """Validation par champ"""
        super().clean_fields(exclude=exclude)
        
        if 'titre' not in (exclude or []):
            if 'spam' in self.titre.lower():
                raise ValidationError({
                    'titre': 'Le titre ne peut pas contenir le mot "spam"'
                })
    
    def save(self, *args, **kwargs):
        """Appeler la validation avant sauvegarde"""
        self.full_clean()  # Appelle clean_fields() puis clean()
        super().save(*args, **kwargs)
```

### Exercice 39 - Validators personnalisés

```python
from django.core.exceptions import ValidationError
import re

def validate_no_profanity(value):
    """Vérifier qu'il n'y a pas de mots interdits"""
    forbidden_words = ['spam', 'arnaque', 'gratuit']
    value_lower = value.lower()
    for word in forbidden_words:
        if word in value_lower:
            raise ValidationError(
                f'Le texte ne peut pas contenir le mot "{word}"',
                code='profanity_detected'
            )

def validate_file_size(value):
    """Vérifier la taille du fichier (max 5MB)"""
    limit = 5 * 1024 * 1024  # 5MB
    if value.size > limit:
        raise ValidationError(
            f'La taille du fichier ne peut pas dépasser {limit/1024/1024}MB',
            code='file_too_large'
        )

def validate_image_dimensions(value):
    """Vérifier les dimensions de l'image"""
    from PIL import Image
    img = Image.open(value)
    width, height = img.size
    
    if width < 800 or height < 600:
        raise ValidationError(
            'L\'image doit avoir au moins 800x600 pixels',
            code='image_too_small'
        )

class Article(models.Model):
    titre = models.CharField(
        max_length=200,
        validators=[validate_no_profanity]
    )
    contenu = models.TextField(validators=[validate_no_profanity])
    image = models.ImageField(
        upload_to='articles/',
        validators=[validate_file_size, validate_image_dimensions]
    )
```

### Exercice 40 - Validation conditionnelle

```python
class Commande(models.Model):
    STATUS_CHOICES = [
        ('brouillon', 'Brouillon'),
        ('validee', 'Validée'),
        ('expediee', 'Expédiée'),
        ('livree', 'Livrée'),
    ]
    
    client = models.ForeignKey('Client', on_delete=models.CASCADE)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='brouillon')
    adresse_livraison = models.TextField(blank=True)
    date_expedition = models.DateField(null=True, blank=True)
    date_livraison = models.DateField(null=True, blank=True)
    
    def clean(self):
        super().clean()
        
        # Adresse obligatoire si status >= validee
        if self.status in ['validee', 'expediee', 'livree']:
            if not self.adresse_livraison:
                raise ValidationError({
                    'adresse_livraison': 'L\'adresse de livraison est obligatoire pour une commande validée'
                })
        
        # Date expedition obligatoire si expediee
        if self.status in ['expediee', 'livree']:
            if not self.date_expedition:
                raise ValidationError({
                    'date_expedition': 'La date d\'expédition est obligatoire'
                })
        
        # Date livraison obligatoire si livree
        if self.status == 'livree':
            if not self.date_livraison:
                raise ValidationError({
                    'date_livraison': 'La date de livraison est obligatoire'
                })
            
            # Date livraison >= date expedition
            if self.date_livraison < self.date_expedition:
                raise ValidationError({
                    'date_livraison': 'La date de livraison ne peut pas être antérieure à la date d\'expédition'
                })
```

---

