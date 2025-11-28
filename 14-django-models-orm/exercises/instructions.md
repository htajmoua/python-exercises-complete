# Instructions - Django Models et ORM

Les modèles Django définissent la structure de votre base de données. L'ORM (Object-Relational Mapping) permet d'interagir avec la base de données en Python.

## Exercice 1 - Premier modèle simple

**Créez** un modèle `Article` dans `blog/models.py` :

```python
from django.db import models

class Article(models.Model):
    titre = models.CharField(max_length=200)
    contenu = models.TextField()
    date_creation = models.DateTimeField(auto_now_add=True)
    date_modification = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return self.titre
```

**Créez** et appliquez la migration :

```bash
python manage.py makemigrations
python manage.py migrate
```

## Exercice 2 - Champs de modèle variés

**Créez** un modèle `Auteur` avec différents types de champs :

```python
class Auteur(models.Model):
    nom = models.CharField(max_length=100)
    prenom = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    bio = models.TextField(blank=True)
    date_naissance = models.DateField(null=True, blank=True)
    site_web = models.URLField(blank=True)
    est_actif = models.BooleanField(default=True)
    
    class Meta:
        verbose_name_plural = "Auteurs"
    
    def __str__(self):
        return f"{self.prenom} {self.nom}"
```

**Migrez** le nouveau modèle.

## Exercice 3 - Relations ForeignKey (One-to-Many)

**Modifiez** le modèle `Article` pour ajouter une relation avec `Auteur` :

```python
class Article(models.Model):
    titre = models.CharField(max_length=200)
    contenu = models.TextField()
    auteur = models.ForeignKey(Auteur, on_delete=models.CASCADE, related_name='articles')
    date_creation = models.DateTimeField(auto_now_add=True)
    date_modification = models.DateTimeField(auto_now=True)
    publie = models.BooleanField(default=False)
    
    def __str__(self):
        return self.titre
```

**Créez** et appliquez les migrations.

## Exercice 4 - Relation ManyToMany

**Créez** un modèle `Tag` :

```python
class Tag(models.Model):
    nom = models.CharField(max_length=50, unique=True)
    slug = models.SlugField(unique=True)
    
    def __str__(self):
        return self.nom
```

**Ajoutez** une relation ManyToMany dans `Article` :

```python
class Article(models.Model):
    # ... champs existants ...
    tags = models.ManyToManyField(Tag, blank=True, related_name='articles')
```

## Exercice 5 - Méthodes personnalisées du modèle

**Ajoutez** des méthodes personnalisées au modèle `Article` :

```python
class Article(models.Model):
    # ... champs existants ...
    
    def get_preview(self, longueur=100):
        """Retourne un aperçu du contenu"""
        if len(self.contenu) > longueur:
            return self.contenu[:longueur] + '...'
        return self.contenu
    
    def nombre_mots(self):
        """Compte le nombre de mots dans le contenu"""
        return len(self.contenu.split())
    
    class Meta:
        ordering = ['-date_creation']  # Tri par défaut
        verbose_name = "Article de blog"
        verbose_name_plural = "Articles de blog"
```

## Exercice 6 - QuerySets basiques (Django Shell)

**Ouvrez** le shell Django :

```bash
python manage.py shell
```

**Créez** des objets :

```python
from blog.models import Auteur, Article, Tag

# Créer un auteur
auteur = Auteur.objects.create(
    nom="Dupont",
    prenom="Jean",
    email="jean.dupont@example.com"
)

# Créer des tags
tag1 = Tag.objects.create(nom="Python", slug="python")
tag2 = Tag.objects.create(nom="Django", slug="django")

# Créer un article
article = Article.objects.create(
    titre="Introduction à Django",
    contenu="Django est un framework web Python...",
    auteur=auteur,
    publie=True
)

# Ajouter des tags
article.tags.add(tag1, tag2)
```

## Exercice 7 - Requêtes de lecture (Read)

Dans le shell Django, **exécutez** ces requêtes :

```python
# Récupérer tous les articles
Article.objects.all()

# Récupérer un article spécifique
Article.objects.get(id=1)

# Filtrer les articles publiés
Article.objects.filter(publie=True)

# Exclure des articles
Article.objects.exclude(publie=False)

# Compter les articles
Article.objects.count()

# Premier et dernier article
Article.objects.first()
Article.objects.last()

# Vérifier l'existence
Article.objects.filter(titre="Introduction à Django").exists()
```

## Exercice 8 - Requêtes de mise à jour (Update)

**Modifiez** des objets existants :

```python
# Récupérer et modifier un article
article = Article.objects.get(id=1)
article.titre = "Nouveau titre"
article.save()

# Mise à jour en masse
Article.objects.filter(auteur=auteur).update(publie=True)

# Incrémentation (si vous aviez un champ vues)
# Article.objects.filter(id=1).update(vues=F('vues') + 1)
```

## Exercice 9 - Requêtes de suppression (Delete)

**Supprimez** des objets :

```python
# Supprimer un article spécifique
article = Article.objects.get(id=5)
article.delete()

# Suppression en masse
Article.objects.filter(publie=False).delete()

# Supprimer tous les articles (ATTENTION !)
# Article.objects.all().delete()
```

## Exercice 10 - Requêtes avec relations

**Explorez** les relations :

```python
# Accéder aux articles d'un auteur
auteur = Auteur.objects.get(id=1)
auteur.articles.all()

# Filtrer par relation
Article.objects.filter(auteur__nom="Dupont")
Article.objects.filter(tags__nom="Python")

# Préchargement pour optimisation
Article.objects.select_related('auteur').all()
Article.objects.prefetch_related('tags').all()
```

## Exercice 11 - Lookups avancés

**Utilisez** des lookups complexes :

```python
# Contient (case-insensitive)
Article.objects.filter(titre__icontains="django")

# Commence par
Article.objects.filter(titre__startswith="Introduction")

# Date
from datetime import datetime, timedelta
date_limite = datetime.now() - timedelta(days=7)
Article.objects.filter(date_creation__gte=date_limite)

# In (liste)
Article.objects.filter(id__in=[1, 2, 3])

# Range
Article.objects.filter(id__range=(1, 10))
```

## Exercice 12 - Q objects (requêtes complexes)

**Créez** des requêtes avec OR et AND :

```python
from django.db.models import Q

# OR - Articles de Dupont OU publiés
Article.objects.filter(
    Q(auteur__nom="Dupont") | Q(publie=True)
)

# AND complexe
Article.objects.filter(
    Q(publie=True) & Q(tags__nom="Python")
)

# NOT
Article.objects.filter(~Q(auteur__nom="Dupont"))
```

## Exercice 13 - Agrégation et annotation

**Utilisez** les fonctions d'agrégation :

```python
from django.db.models import Count, Avg, Max, Min

# Compter les articles par auteur
Auteur.objects.annotate(nombre_articles=Count('articles'))

# Nombre de tags par article
Article.objects.annotate(nombre_tags=Count('tags'))

# Statistiques
Article.objects.aggregate(
    total=Count('id'),
    plus_recent=Max('date_creation')
)
```

## Exercice 14 - Modèle avec validation personnalisée

**Créez** un modèle `Commentaire` avec validation :

```python
from django.core.exceptions import ValidationError

class Commentaire(models.Model):
    article = models.ForeignKey(Article, on_delete=models.CASCADE, related_name='commentaires')
    auteur_nom = models.CharField(max_length=100)
    email = models.EmailField()
    contenu = models.TextField()
    date_creation = models.DateTimeField(auto_now_add=True)
    approuve = models.BooleanField(default=False)
    
    def clean(self):
        # Validation personnalisée
        if len(self.contenu) < 10:
            raise ValidationError("Le commentaire doit contenir au moins 10 caractères")
    
    def save(self, *args, **kwargs):
        self.full_clean()  # Appelle clean()
        super().save(*args, **kwargs)
    
    class Meta:
        ordering = ['-date_creation']
```

## Exercice 15 - Managers personnalisés

**Créez** un manager personnalisé pour `Article` :

```python
class ArticlePublieManager(models.Manager):
    def get_queryset(self):
        return super().get_queryset().filter(publie=True)

class Article(models.Model):
    # ... champs existants ...
    
    objects = models.Manager()  # Manager par défaut
    publies = ArticlePublieManager()  # Manager personnalisé
```

**Utilisez-le** :

```python
# Tous les articles
Article.objects.all()

# Seulement les articles publiés
Article.publies.all()
```

## Exercices bonus

### Exercice 16 - Signals
**Créez** un signal pour envoyer un email quand un article est publié.

### Exercice 17 - Abstract Base Class
**Créez** une classe abstraite `ModeleAvecTimestamp` avec `date_creation` et `date_modification`.

### Exercice 18 - Proxy Models
**Créez** un modèle proxy `ArticlePublie` basé sur `Article`.

## Checklist de validation

- ✅ Modèles créés avec différents types de champs
- ✅ Relations ForeignKey et ManyToMany fonctionnelles
- ✅ Migrations créées et appliquées
- ✅ CRUD complet testé dans le shell
- ✅ Requêtes avec filtres et lookups maîtrisées
- ✅ Q objects utilisés pour requêtes complexes
- ✅ Agrégation et annotation comprises
- ✅ Managers personnalisés implémentés
