# Instructions - Django ORM : Projet Complet 🎯

**🎯 Objectif du module** : Intégrer TOUTES les techniques vues dans un projet réel.

Ce module est un projet fil rouge qui intègre :
- Modèles avec toutes les stratégies d'héritage
- Relations complexes
- Managers et QuerySets personnalisés
- Optimisation des requêtes
- Signals et validation
- Tests unitaires complets

C'est le **projet final** qui prouve votre maîtrise complète de l'ORM Django !

**📚 Format du module** :
- **Ce module est 100% PRATIQUE** - Un projet complet à réaliser
- Des squelettes et TODO sont fournis pour vous guider
- Chaque section correspond à une étape du projet

**Prérequis** : Avoir complété les modules 15, 16 et 17

**Durée estimée** : 6-8 heures

---

# 🔨 PROJET : Système de Blog Professionnel

**Contexte** : Vous devez créer un système de blog complet pour une plateforme de contenu. Le système doit gérer des articles, des auteurs, des commentaires, des catégories et des tags, avec des fonctionnalités avancées d'optimisation et de statistiques.

---

## Étape 1 : Classes abstraites et Managers (PRATIQUE)

**Consignes** :
1. Créez les classes abstraites `TimestampedModel` et `SoftDeleteModel`
2. Créez un `ArticleQuerySet` avec des méthodes pratiques
3. Créez un `ArticleManager` qui utilise le QuerySet

**Squelette - `blog/models.py`** (à compléter) :

```python
# models.py
from django.db import models
from django.contrib.auth.models import User
from django.core.validators import MinValueValidator, MaxValueValidator
from django.core.exceptions import ValidationError
from django.db.models import Q, F, Count, Avg
from django.utils import timezone
from django.utils.text import slugify

# TODO : Créez les classes abstraites (revoyez module 15 si besoin)

class TimestampedModel(models.Model):
    """Classe abstraite pour timestamps"""
    date_creation = models.DateTimeField(auto_now_add=True)
    date_modification = models.DateTimeField(auto_now=True)
    
    class Meta:
        abstract = True

class SoftDeleteModel(models.Model):
    """Classe abstraite pour soft delete"""
    supprime = models.BooleanField(default=False)
    date_suppression = models.DateTimeField(null=True, blank=True)
    
    class Meta:
        abstract = True
    
    def soft_delete(self):
        self.supprime = True
        self.date_suppression = timezone.now()
        self.save()

# TODO : Créez un QuerySet personnalisé avec méthodes chaînables

class ArticleQuerySet(models.QuerySet):
    def publies(self):
        # TODO : Filtrez articles publiés ET non supprimés
        return self.filter(publie=True, supprime=False)
    
    def brouillons(self):
        # TODO : Filtrez articles NON publiés ET non supprimés
        return # VOTRE CODE ICI
    
    def featured(self):
        # TODO : Filtrez articles featured ET publiés
        return # VOTRE CODE ICI
    
    def populaires(self, limite=10):
        # TODO : Retournez les N articles les plus vus
        # Triez par -nombre_vues et limitez
        return # VOTRE CODE ICI
    
    def avec_stats(self):
        # TODO : Annotez avec nb_commentaires, nb_likes, note_moyenne
        # Utilisez Count() et Avg()
        return self.annotate(
            nb_commentaires=Count('commentaires', filter=Q(commentaires__approuve=True)),
            # VOTRE CODE ICI pour nb_likes et note_moyenne
        )
    
    def optimise(self):
        # TODO : Optimisez avec select_related et prefetch_related
        # Relations FK : auteur, categorie
        # Relations M2M : tags, commentaires
        return # VOTRE CODE ICI

# TODO : Créez le Manager qui utilise le QuerySet

class ArticleManager(models.Manager):
    def get_queryset(self):
        return ArticleQuerySet(self.model, using=self._db)
    
    def publies(self):
        # TODO : Retournez get_queryset().publies()
        return # VOTRE CODE ICI
    
    def featured(self):
        # TODO : Retournez get_queryset().featured()
        return # VOTRE CODE ICI
```

**Indice** :
- Les QuerySets chaînables permettent : `Article.objects.publies().featured().populaires(5)`
- `get_queryset()` dans le Manager retourne votre QuerySet personnalisé
- Les méthodes du Manager appellent les méthodes du QuerySet

---

## Étape 2 : Modèles principaux (PRATIQUE)

**Consignes** :
1. Créez le modèle `Auteur` avec OneToOne vers User
2. Créez le modèle `Categorie` avec relation récursive (parent)
3. Créez le modèle `Tag`
4. Ajoutez des indexes appropriés

**Squelette - `blog/models.py`** (suite) :

```python

# ===== MODÈLES PRINCIPAUX =====

class Auteur(TimestampedModel):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    nom = models.CharField(max_length=100)
    prenom = models.CharField(max_length=100)
    bio = models.TextField(blank=True)
    avatar = models.ImageField(upload_to='avatars/', blank=True)
    site_web = models.URLField(blank=True)
    
    # Statistiques
    nombre_articles = models.PositiveIntegerField(default=0)
    nombre_followers = models.PositiveIntegerField(default=0)
    
    class Meta:
        verbose_name = "Auteur"
        verbose_name_plural = "Auteurs"
        ordering = ['nom', 'prenom']
        indexes = [
            models.Index(fields=['nom', 'prenom']),
        ]
    
    def __str__(self):
        return f"{self.prenom} {self.nom}"
    
    def mettre_a_jour_stats(self):
        """Mettre à jour les statistiques"""
        self.nombre_articles = self.articles.filter(publie=True).count()
        self.save(update_fields=['nombre_articles'])

class Categorie(TimestampedModel):
    nom = models.CharField(max_length=100, unique=True)
    slug = models.SlugField(unique=True)
    description = models.TextField(blank=True)
    parent = models.ForeignKey(
        'self',
        null=True,
        blank=True,
        on_delete=models.CASCADE,
        related_name='sous_categories'
    )
    ordre = models.PositiveIntegerField(default=0)
    
    class Meta:
        verbose_name = "Catégorie"
        verbose_name_plural = "Catégories"
        ordering = ['ordre', 'nom']
    
    def __str__(self):
        return self.nom
    
    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.nom)
        super().save(*args, **kwargs)

class Tag(models.Model):
    nom = models.CharField(max_length=50, unique=True)
    slug = models.SlugField(unique=True)
    couleur = models.CharField(max_length=7, default='#000000')
    
    class Meta:
        verbose_name = "Tag"
        ordering = ['nom']
    
    def __str__(self):
        return self.nom

class Article(TimestampedModel, SoftDeleteModel):
    # Champs de base
    titre = models.CharField(max_length=200, db_index=True)
    slug = models.SlugField(unique=True)
    chapeau = models.TextField(max_length=500, blank=True)
    contenu = models.TextField()
    image_principale = models.ImageField(upload_to='articles/', blank=True)
    
    # Relations
    auteur = models.ForeignKey(
        Auteur,
        on_delete=models.CASCADE,
        related_name='articles'
    )
    categorie = models.ForeignKey(
        Categorie,
        on_delete=models.PROTECT,
        related_name='articles'
    )
    tags = models.ManyToManyField(Tag, blank=True, related_name='articles')
    
    # Statut
    publie = models.BooleanField(default=False)
    featured = models.BooleanField(default=False)
    date_publication = models.DateTimeField(null=True, blank=True)
    
    # Statistiques
    nombre_vues = models.PositiveIntegerField(default=0)
    nombre_partages = models.PositiveIntegerField(default=0)
    
    # Metadata
    metadata = models.JSONField(default=dict, blank=True)
    
    # Managers
    objects = ArticleManager()
    tous = models.Manager()  # Manager incluant les supprimés
    
    class Meta:
        verbose_name = "Article"
        verbose_name_plural = "Articles"
        ordering = ['-date_publication', '-date_creation']
        indexes = [
            models.Index(fields=['publie', '-date_publication']),
            models.Index(fields=['auteur', 'publie']),
            models.Index(fields=['slug']),
        ]
        constraints = [
            models.CheckConstraint(
                check=Q(publie=False) | Q(date_publication__isnull=False),
                name='publie_avec_date'
            ),
        ]
    
    def __str__(self):
        return self.titre
    
    def clean(self):
        super().clean()
        
        # Article publié doit avoir du contenu
        if self.publie and len(self.contenu) < 100:
            raise ValidationError({
                'contenu': 'Un article publié doit avoir au moins 100 caractères'
            })
        
        # Slug unique par auteur
        if Article.tous.filter(
            auteur=self.auteur,
            slug=self.slug
        ).exclude(pk=self.pk).exists():
            raise ValidationError({
                'slug': 'Vous avez déjà un article avec ce slug'
            })
    
    def save(self, *args, **kwargs):
        # Générer le slug
        if not self.slug:
            self.slug = slugify(self.titre)
        
        # Date de publication automatique
        if self.publie and not self.date_publication:
            self.date_publication = timezone.now()
        
        # Validation
        self.full_clean()
        
        super().save(*args, **kwargs)
        
        # Mettre à jour les stats de l'auteur
        self.auteur.mettre_a_jour_stats()
    
    def incrementer_vues(self):
        """Incrémenter le nombre de vues (atomique)"""
        Article.objects.filter(pk=self.pk).update(nombre_vues=F('nombre_vues') + 1)
        self.refresh_from_db(fields=['nombre_vues'])
    
    def get_apercu(self, longueur=200):
        """Obtenir un aperçu du contenu"""
        if len(self.contenu) > longueur:
            return self.contenu[:longueur] + '...'
        return self.contenu

class Commentaire(TimestampedModel, SoftDeleteModel):
    article = models.ForeignKey(
        Article,
        on_delete=models.CASCADE,
        related_name='commentaires'
    )
    auteur = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        null=True,
        blank=True
    )
    auteur_nom = models.CharField(max_length=100)
    auteur_email = models.EmailField()
    contenu = models.TextField()
    approuve = models.BooleanField(default=False)
    
    parent = models.ForeignKey(
        'self',
        null=True,
        blank=True,
        on_delete=models.CASCADE,
        related_name='reponses'
    )
    
    class Meta:
        verbose_name = "Commentaire"
        ordering = ['-date_creation']
        indexes = [
            models.Index(fields=['article', 'approuve']),
        ]
    
    def __str__(self):
        return f"Commentaire de {self.auteur_nom} sur {self.article.titre}"
    
    def clean(self):
        super().clean()
        
        if len(self.contenu) < 10:
            raise ValidationError({
                'contenu': 'Le commentaire doit faire au moins 10 caractères'
            })

class Like(TimestampedModel):
    article = models.ForeignKey(Article, on_delete=models.CASCADE, related_name='likes')
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    
    class Meta:
        unique_together = ['article', 'user']
        verbose_name = "Like"
    
    def __str__(self):
        return f"{self.user.username} aime {self.article.titre}"

class Evaluation(TimestampedModel):
    article = models.ForeignKey(Article, on_delete=models.CASCADE, related_name='evaluations')
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    note = models.PositiveSmallIntegerField(
        validators=[MinValueValidator(1), MaxValueValidator(5)]
    )
    
    class Meta:
        unique_together = ['article', 'user']
        verbose_name = "Évaluation"
    
    def __str__(self):
        return f"{self.user.username} : {self.note}/5 sur {self.article.titre}"
```

#### Étape 2 : Signals

```python
# signals.py
from django.db.models.signals import post_save, pre_delete, m2m_changed
from django.dispatch import receiver
from .models import Article, Commentaire, Like

@receiver(post_save, sender=Article)
def article_publie(sender, instance, created, **kwargs):
    """Actions après publication d'un article"""
    if instance.publie and not created:
        # Notifier les followers
        # Envoyer email newsletter
        # Publier sur réseaux sociaux
        pass

@receiver(post_save, sender=Commentaire)
def nouveau_commentaire(sender, instance, created, **kwargs):
    """Notifier l'auteur d'un nouveau commentaire"""
    if created:
        # Envoyer email à l'auteur de l'article
        pass

@receiver(pre_delete, sender=Article)
def archiver_article(sender, instance, **kwargs):
    """Archiver avant suppression"""
    # Sauvegarder dans une table d'archive
    pass

@receiver(m2m_changed, sender=Article.tags.through)
def tags_changed(sender, instance, action, **kwargs):
    """Mettre à jour les stats quand les tags changent"""
    if action in ['post_add', 'post_remove', 'post_clear']:
        # Recalculer les stats de tags
        pass
```

#### Étape 3 : Tests

```python
# tests.py
from django.test import TestCase
from django.contrib.auth.models import User
from .models import Article, Auteur, Categorie, Tag

class ArticleModelTests(TestCase):
    def setUp(self):
        self.user = User.objects.create_user('test', 'test@test.com', 'password')
        self.auteur = Auteur.objects.create(
            user=self.user,
            nom='Test',
            prenom='User'
        )
        self.categorie = Categorie.objects.create(nom='Tech', slug='tech')
    
    def test_creation_article(self):
        """Tester la création d'un article"""
        article = Article.objects.create(
            titre="Test Article",
            contenu="Contenu de test" * 20,
            auteur=self.auteur,
            categorie=self.categorie
        )
        self.assertEqual(article.slug, 'test-article')
        self.assertFalse(article.publie)
    
    def test_slug_unique_par_auteur(self):
        """Tester l'unicité du slug par auteur"""
        Article.objects.create(
            titre="Test",
            slug="test",
            contenu="Contenu" * 20,
            auteur=self.auteur,
            categorie=self.categorie
        )
        
        # Deuxième article avec même slug doit échouer
        with self.assertRaises(ValidationError):
            article2 = Article(
                titre="Test 2",
                slug="test",
                contenu="Contenu" * 20,
                auteur=self.auteur,
                categorie=self.categorie
            )
            article2.full_clean()
    
    def test_manager_publies(self):
        """Tester le manager articles publiés"""
        Article.objects.create(
            titre="Publié",
            contenu="Contenu" * 20,
            auteur=self.auteur,
            categorie=self.categorie,
            publie=True
        )
        Article.objects.create(
            titre="Brouillon",
            contenu="Contenu" * 20,
            auteur=self.auteur,
            categorie=self.categorie,
            publie=False
        )
        
        self.assertEqual(Article.objects.publies().count(), 1)
        self.assertEqual(Article.objects.all().count(), 2)
```

---

## ✅ CHECKLIST COMPLÈTE DE VALIDATION

### Fondamentaux
- [ ] Créer des modèles avec tous les types de champs
- [ ] Implémenter les 3 types de relations (ForeignKey, ManyToMany, OneToOne)
- [ ] Comprendre les différentes options on_delete
- [ ] Créer des migrations et les appliquer

### Héritage
- [ ] Créer une classe abstraite
- [ ] Implémenter l'héritage multi-tables
- [ ] Utiliser des modèles proxy
- [ ] Choisir la bonne stratégie selon le cas d'usage

### QuerySets
- [ ] Maîtriser tous les lookups (contains, gte, range, etc.)
- [ ] Utiliser Q objects pour requêtes complexes
- [ ] Utiliser F expressions pour comparaisons de champs
- [ ] Créer des annotations et agrégations
- [ ] Utiliser Case/When pour logique conditionnelle

### Optimisation ⭐⭐⭐
- [ ] Identifier et résoudre le problème N+1
- [ ] Utiliser select_related correctement
- [ ] Utiliser prefetch_related correctement
- [ ] Optimiser avec only() et defer()
- [ ] Utiliser bulk_create/bulk_update
- [ ] Implémenter des transactions

### Avancé
- [ ] Créer des migrations de données avec RunPython
- [ ] Créer des indexes composites
- [ ] Implémenter des contraintes CHECK et UNIQUE
- [ ] Utiliser raw() et cursor.execute()
- [ ] Créer et utiliser des signals
- [ ] Créer des managers et QuerySets personnalisés

### Validation
- [ ] Implémenter clean() et clean_fields()
- [ ] Créer des validators personnalisés
- [ ] Utiliser les contraintes de base de données

### Projet
- [ ] Créer un système complet intégrant toutes les techniques
- [ ] Écrire des tests pour les modèles
- [ ] Optimiser les requêtes du projet
- [ ] Documenter le code et les choix techniques

---

## 📖 RESSOURCES COMPLÉMENTAIRES

**Documentation officielle** :
- https://docs.djangoproject.com/en/stable/topics/db/models/
- https://docs.djangoproject.com/en/stable/topics/db/queries/
- https://docs.djangoproject.com/en/stable/topics/db/optimization/

**Best practices** :
- Toujours utiliser select_related/prefetch_related pour les relations
- Préférer update() à save() pour les mises à jour en masse
- Utiliser transactions pour les opérations critiques
- Créer des indexes pour les champs fréquemment filtrés
- Toujours valider les données avec clean()

**Commandes utiles** :
```bash
# Créer des migrations
python manage.py makemigrations

# Appliquer les migrations
python manage.py migrate

# Shell Django
python manage.py shell

# Voir le SQL d'une migration
python manage.py sqlmigrate app_name migration_number

# Tests
python manage.py test

# Profiler les requêtes
python manage.py debugsqlshell
```

---

🎉 **Félicitations !** Vous maîtrisez maintenant l'ORM Django sur le bout des doigts. Vous êtes prêt pour développer des applications Backend professionnelles avec Django !
