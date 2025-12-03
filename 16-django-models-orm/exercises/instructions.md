# Instructions - Django Models : Fondamentaux

**🎯 Objectif du module** : Maîtriser les bases des modèles Django - champs, relations et héritage.

Les modèles Django définissent la structure de votre base de données. L'ORM (Object-Relational Mapping) permet d'interagir avec la base de données en Python sans écrire de SQL.

**📚 Format du module** :
- **Partie 1 (Exercices 1-3)** : Exemples guidés - Création de modèles et relations de base
- **Partie 2 (Exercices 4-8)** : Exercices pratiques - À compléter par vos soins

**Prérequis** : Avoir complété le module 15 (Introduction à Django)

---

# 📖 PARTIE 1 : EXEMPLES GUIDÉS

Les exercices 1 à 3 sont des exemples complets pour comprendre les concepts de base.

---

## Exercice 1 - Premier modèle simple (EXEMPLE)

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

**Analysez** le SQL généré :

```bash
python manage.py sqlmigrate blog 0001
```

### Utiliser l'interface admin Django

**Enregistrez** le modèle dans `blog/admin.py` :

```python
from django.contrib import admin
from .models import Article

admin.site.register(Article)
```

**Créez** un superuser pour accéder à l'admin :

```bash
python manage.py createsuperuser
# Username: admin
# Email: admin@example.com
# Password: admin123 (choisissez un mot de passe)
```

**Lancez** le serveur et accédez à l'admin :

```bash
python manage.py runserver
```

Ouvrez `http://127.0.0.1:8000/admin/` dans votre navigateur et connectez-vous.

**Ajoutez des articles** via l'interface admin :
- Cliquez sur "Articles" → "Ajouter Article"
- Remplissez le titre et le contenu
- Cliquez sur "Enregistrer"

Vous pouvez maintenant **consulter, modifier et supprimer** vos articles via l'admin !

**Testez** dans le shell Django :

```bash
python manage.py shell
```

```python
from blog.models import Article

# Afficher tous les articles
articles = Article.objects.all()
for article in articles:
    print(f"- {article.titre}")

# Créer un article via le code
Article.objects.create(
    titre="Mon premier article",
    contenu="Contenu de l'article créé via le shell"
)

# Vérifier qu'il apparaît dans l'admin
```

---

## Exercice 2 - Tous les types de champs (EXEMPLE)

**Créez** un modèle exhaustif avec tous les types de champs :

```python
from django.core.validators import MinValueValidator, MaxValueValidator
from django.utils import timezone

class Auteur(models.Model):
    # Champs texte
    nom = models.CharField(max_length=100, db_index=True)
    prenom = models.CharField(max_length=100)
    pseudo = models.SlugField(unique=True)
    bio = models.TextField(blank=True)
    
    # Champs email et URL
    email = models.EmailField(unique=True)
    site_web = models.URLField(blank=True)
    
    # Champs numériques
    age = models.IntegerField(
        validators=[MinValueValidator(18), MaxValueValidator(120)],
        null=True, blank=True
    )
    note_moyenne = models.DecimalField(
        max_digits=3, decimal_places=2,
        default=0.00
    )
    salaire = models.FloatField(null=True, blank=True)
    
    # Champs date/temps
    date_naissance = models.DateField(null=True, blank=True)
    heure_contact = models.TimeField(null=True, blank=True)
    derniere_connexion = models.DateTimeField(default=timezone.now)
    
    # Champs booléens
    est_actif = models.BooleanField(default=True)
    newsletter = models.BooleanField(default=False)
    
    # Champs binaires
    avatar = models.ImageField(upload_to='avatars/', blank=True)
    cv = models.FileField(upload_to='cv/', blank=True)
    
    # Champs JSON (PostgreSQL)
    metadata = models.JSONField(default=dict, blank=True)
    
    # Champs de choix
    GENRE_CHOICES = [
        ('M', 'Masculin'),
        ('F', 'Féminin'),
        ('A', 'Autre'),
    ]
    genre = models.CharField(max_length=1, choices=GENRE_CHOICES, blank=True)
    
    class Meta:
        verbose_name = "Auteur"
        verbose_name_plural = "Auteurs"
        ordering = ['nom', 'prenom']
        indexes = [
            models.Index(fields=['nom', 'prenom']),
        ]
    
    def __str__(self):
        return f"{self.prenom} {self.nom}"
```

**Migrez** et testez dans le shell.

---

## Exercice 3 - Relations ForeignKey (EXEMPLE)

**Modifiez** le modèle `Article` dans `blog/models.py` pour ajouter une relation avec `Auteur` :

```python
class Article(models.Model):
    titre = models.CharField(max_length=200)
    slug = models.SlugField(unique=True)  # Nouveau champ !
    contenu = models.TextField()
    
    # Relation ManyToOne (plusieurs articles par auteur)
    auteur = models.ForeignKey(
        Auteur,
        on_delete=models.CASCADE,  # Supprime les articles si l'auteur est supprimé
        related_name='articles'     # Accès inverse: auteur.articles.all()
    )
    
    date_creation = models.DateTimeField(auto_now_add=True)
    date_modification = models.DateTimeField(auto_now=True)
    publie = models.BooleanField(default=False)
    nombre_vues = models.PositiveIntegerField(default=0)
    
    class Meta:
        ordering = ['-date_creation']
    
    def __str__(self):
        return self.titre
```

⚠️ **Important** : Vous avez ajouté 2 nouveaux champs (`slug` et `auteur`), donc vous devez faire les migrations avant de tester !

**Enregistrez** d'abord les modèles dans `blog/admin.py` :

```python
from django.contrib import admin
from .models import Article, Auteur

admin.site.register(Auteur)
admin.site.register(Article)
```

**Créez les migrations** :

```bash
python manage.py makemigrations
```

⚠️ **Si vous obtenez l'erreur "It is impossible to add a non-nullable field 'auteur' to article"**, c'est parce que vous avez déjà des articles dans la base de données.

**Solution** : Supprimez la base de données ET les migrations, puis recommencez proprement :

```bash
# 1. Supprimer la base de données
rm db.sqlite3

# 2. Supprimer les anciennes migrations de blog
rm blog/migrations/0*.py

# 3. Recréer les tables de base (Django + admin)
python manage.py migrate

# 4. Créer les migrations pour vos modèles (Article avec slug + auteur, Auteur)
python manage.py makemigrations

# 5. Appliquer les migrations
python manage.py migrate

# 6. Recréer le superuser
python manage.py createsuperuser
```

Maintenant votre base de données est propre et contient le modèle `Article` avec tous les champs dès le début !

---

**Options on_delete** (pour information) :

```python
# CASCADE : Supprime les objets liés
auteur = models.ForeignKey(Auteur, on_delete=models.CASCADE)

# PROTECT : Empêche la suppression si des objets liés existent
categorie = models.ForeignKey(Categorie, on_delete=models.PROTECT)

# SET_NULL : Met le champ à NULL
editeur = models.ForeignKey(Editeur, on_delete=models.SET_NULL, null=True)

# SET_DEFAULT : Met une valeur par défaut
statut = models.ForeignKey(Statut, on_delete=models.SET_DEFAULT, default=1)

# SET() : Utilise une fonction personnalisée
def get_deleted_user():
    return Auteur.objects.get_or_create(email='deleted@example.com')[0]

createur = models.ForeignKey(Auteur, on_delete=models.SET(get_deleted_user))

# DO_NOTHING : Ne fait rien (DANGEREUX - peut violer l'intégrité)
responsable = models.ForeignKey(User, on_delete=models.DO_NOTHING)
```

---

**Testez** les relations dans le **shell Django** :

```bash
python manage.py shell
```

```python
from blog.models import Article, Auteur

# Créer un auteur (ou le récupérer s'il existe déjà)
auteur, created = Auteur.objects.get_or_create(
    email="jean@example.com",  # Critère de recherche (unique)
    defaults={
        'nom': "Dupont",
        'prenom': "Jean",
        'pseudo': "jeandupont"
    }
)

if created:
    print(f"Auteur créé : {auteur}")
else:
    print(f"Auteur existant récupéré : {auteur}")

# Créer des articles liés à cet auteur
article1, created1 = Article.objects.get_or_create(
    slug="introduction-django",  # Critère de recherche (unique)
    defaults={
        'titre': "Introduction à Django",
        'contenu': "Django est un framework web...",
        'auteur': auteur,
        'publie': True
    }
)

article2, created2 = Article.objects.get_or_create(
    slug="modeles-django",  # Critère de recherche (unique)
    defaults={
        'titre': "Les modèles Django",
        'contenu': "Les modèles définissent...",
        'auteur': auteur,
        'publie': True
    }
)

print(f"Article 1 : {'créé' if created1 else 'existant'}")
print(f"Article 2 : {'créé' if created2 else 'existant'}")

# Accès inverse (related_name)
print(f"\nArticles de {auteur} :")
for article in auteur.articles.all():
    print(f"  - {article.titre}")

print(f"\nNombre d'articles : {auteur.articles.count()}")
print(f"Articles publiés : {auteur.articles.filter(publie=True).count()}")

# Accès direct
print(f"\nAuteur de l'article 1 : {article1.auteur}")
print(f"Nom : {article1.auteur.nom}")
print(f"Email : {article1.auteur.email}")
```

💡 **Astuce** : `get_or_create()` permet d'éviter l'erreur `UNIQUE constraint failed`. Si l'objet existe déjà, il est récupéré au lieu d'être créé à nouveau.

**Alternative si vous voulez vraiment supprimer et recréer** :

```python
# Supprimer tous les auteurs et articles existants
Article.objects.all().delete()
Auteur.objects.all().delete()

# Puis créer de nouveaux objets
auteur = Auteur.objects.create(
    nom="Dupont", 
    prenom="Jean", 
    email="jean@example.com",
    pseudo="jeandupont"
)
# ... reste du code
```

**Visualisez** dans l'admin :
- Ouvrez `http://127.0.0.1:8000/admin/`
- Vous verrez l'auteur "Jean Dupont" dans la section Auteurs
- Vous verrez ses 2 articles dans la section Articles
- En cliquant sur un article, vous verrez la relation avec l'auteur dans un menu déroulant

**Vous pouvez aussi créer via l'admin** :
1. Créez d'abord un auteur via l'admin
2. Puis créez un article en sélectionnant cet auteur dans le menu déroulant

---

# 🔨 PARTIE 2 : EXERCICES PRATIQUES

**Les exercices 4 à 8 sont des tutoriels guidés** pour vous apprendre :
- Exercices 4-5 : Relations ManyToMany et OneToOne
- Exercices 6-8 : Héritage de modèles (Abstract, Multi-table et Proxy)

---

## Exercice 4 - Relation ManyToMany (TUTORIEL)

**Objectif** : Créer un modèle Tag avec une relation plusieurs-à-plusieurs vers Article.

Une relation **ManyToMany** permet à plusieurs objets A d'avoir plusieurs objets B. Par exemple, un article peut avoir plusieurs tags, et un tag peut être associé à plusieurs articles.

---

### Étape 1 : Créer le modèle Tag

**Ajoutez** dans `blog/models.py` :

```python
class Tag(models.Model):
    nom = models.CharField(max_length=50, unique=True)
    slug = models.SlugField(unique=True)
    description = models.TextField(blank=True)
    couleur = models.CharField(max_length=7, default='#000000')  # Code couleur hex
    
    def __str__(self):
        return self.nom
    
    class Meta:
        ordering = ['nom']  # Ordre alphabétique
```

💡 **Explication** :
- `unique=True` : Pas de doublons pour le nom et le slug
- `blank=True` : La description est optionnelle
- `couleur` : Pour afficher le tag avec une couleur (format hexadécimal comme #3776ab)
- `ordering = ['nom']` : Tri automatique par ordre alphabétique

---

### Étape 2 : Ajouter la relation ManyToMany dans Article

**Modifiez** votre classe `Article` dans `blog/models.py` :

```python
class Article(models.Model):
    # ... vos champs existants (titre, contenu, auteur, etc.) ...
    
    # Relation ManyToMany vers Tag
    tags = models.ManyToManyField(
        Tag,
        blank=True,
        related_name='articles'
    )
```

💡 **Explication** :
- `ManyToManyField(Tag)` : Crée la relation plusieurs-à-plusieurs
- `blank=True` : Un article peut ne pas avoir de tags
- `related_name='articles'` : Permet d'accéder aux articles depuis un tag via `tag.articles.all()`

---

### Étape 3 : Créer et appliquer les migrations

```bash
python manage.py makemigrations
python manage.py migrate
```

Django crée automatiquement une **table intermédiaire** pour stocker les associations article-tag.

---

### Étape 4 : Tester dans le shell Django

```bash
python manage.py shell
```

**Créez des tags :**

```python
from blog.models import Article, Tag

# Créer des tags
tag_python = Tag.objects.create(
    nom="Python",
    slug="python",
    couleur="#3776ab"
)

tag_django = Tag.objects.create(
    nom="Django",
    slug="django",
    couleur="#092e20"
)

tag_web = Tag.objects.create(
    nom="Web",
    slug="web",
    couleur="#e34c26"
)
```

**Associer des tags à un article :**

```python
# Récupérer un article
article = Article.objects.first()

# Ajouter plusieurs tags
article.tags.add(tag_python, tag_django)

# Afficher tous les tags de l'article
print(article.tags.all())
# <QuerySet [<Tag: Django>, <Tag: Python>]>

# Compter les tags
print(article.tags.count())
# 2
```

**Rechercher des articles par tag :**

```python
# Tous les articles avec le tag "Python"
articles_python = Article.objects.filter(tags__nom="Python")
print(articles_python)

# Vérifier si un article a un tag spécifique
has_python = article.tags.filter(nom="Python").exists()
print(has_python)  # True
```

**Accès inverse (depuis le tag) :**

```python
# Tous les articles qui ont le tag "Python"
articles = tag_python.articles.all()
print(articles)
```

**Autres opérations :**

```python
# Retirer un tag
article.tags.remove(tag_django)

# Remplacer tous les tags
article.tags.set([tag_python, tag_web])

# Effacer tous les tags
article.tags.clear()

# Vérifier l'existence
article.tags.filter(nom="Python").exists()

# Accès inverse
tag_python.articles.all()
```

---

## Exercice 5 - Relation OneToOne (TUTORIEL)

**Objectif** : Créer un modèle ProfilAuteur avec une relation un-à-un vers Auteur.

Une relation **OneToOne** permet de séparer les informations d'un modèle en deux tables tout en gardant un lien unique. Par exemple, séparer les informations de base d'un auteur de son profil détaillé.

---

### Étape 1 : Créer le modèle ProfilAuteur

**Ajoutez** dans `blog/models.py` :

```python
class ProfilAuteur(models.Model):
    auteur = models.OneToOneField(
        Auteur,
        on_delete=models.CASCADE,
        related_name='profil',
        primary_key=True
    )
    
    biographie_longue = models.TextField(blank=True)
    twitter = models.CharField(max_length=100, blank=True)
    linkedin = models.URLField(blank=True)
    github = models.CharField(max_length=100, blank=True)
    nombre_followers = models.PositiveIntegerField(default=0)
    notifications_email = models.BooleanField(default=True)
    profil_public = models.BooleanField(default=True)
    
    def __str__(self):
        return f"Profil de {self.auteur}"
```

💡 **Explication** :
- `OneToOneField(Auteur)` : Crée une relation 1-1 unique avec Auteur
- `primary_key=True` : Le profil utilise l'ID de l'auteur (pas de clé séparée)
- `on_delete=models.CASCADE` : Si l'auteur est supprimé, son profil aussi
- `related_name='profil'` : Permet d'accéder au profil via `auteur.profil`
- `blank=True` : Ces champs sont optionnels

---

### Étape 2 : Créer et appliquer les migrations

```bash
python manage.py makemigrations
python manage.py migrate
```

---

### Étape 3 : Tester dans le shell Django

```bash
python manage.py shell
```

**Créer un profil pour un auteur :**

```python
from blog.models import Auteur, ProfilAuteur

# Récupérer un auteur existant
auteur = Auteur.objects.first()

# Créer son profil
profil = ProfilAuteur.objects.create(
    auteur=auteur,
    biographie_longue="Développeur Python passionné...",
    twitter="@johndoe",
    github="johndoe",
    linkedin="https://linkedin.com/in/johndoe",
    nombre_followers=1500,
    profil_public=True
)

print(profil)
# Profil de John Doe
```

**Accéder au profil depuis l'auteur :**

```python
# Accès direct avec la relation OneToOne
print(auteur.profil.twitter)
# @johndoe

print(auteur.profil.nombre_followers)
# 1500
```

**Accéder à l'auteur depuis le profil :**

```python
# Accès inverse
print(profil.auteur.nom)
# John Doe

print(profil.auteur.email)
# john@example.com
```

**Gérer les cas où le profil n'existe pas :**

```python
# Méthode 1 : try/except
try:
    print(auteur.profil.twitter)
except ProfilAuteur.DoesNotExist:
    print("Cet auteur n'a pas de profil")

# Méthode 2 : hasattr
if hasattr(auteur, 'profil'):
    print(f"Twitter: {auteur.profil.twitter}")
else:
    print("Pas de profil")

# Méthode 3 : getattr avec valeur par défaut
twitter = getattr(auteur, 'profil', None)
if twitter:
    print(twitter.twitter)
```

**Mettre à jour un profil :**

```python
# Récupérer et modifier
profil = auteur.profil
profil.nombre_followers = 2000
profil.save()

# Ou en une ligne
ProfilAuteur.objects.filter(auteur=auteur).update(nombre_followers=2000)
```

**Supprimer un profil :**

```python
# Supprimer uniquement le profil
auteur.profil.delete()
# L'auteur existe toujours

# Supprimer l'auteur (supprime aussi le profil grâce à CASCADE)
auteur.delete()
```

**Différences entre relations** (à retenir) :

| Relation | Usage | Exemple |
|----------|-------|---------|
| **ForeignKey** | Un objet A peut avoir plusieurs objets B | Un auteur a plusieurs articles |
| **ManyToMany** | Plusieurs objets A ont plusieurs objets B | Un article a plusieurs tags |
| **OneToOne** | Un objet A a exactement un objet B | Un auteur a un profil |

---

## Exercice 6 - Abstract Base Classes (TUTORIEL)

**Objectif** : Créer des classes abstraites réutilisables pour partager des champs communs.

Les **classes abstraites** permettent de factoriser du code sans créer de table en base de données. Les champs sont **copiés** directement dans les modèles enfants.

---

### Étape 1 : Créer une classe abstraite pour les timestamps

**Ajoutez** dans `blog/models.py` :

```python
from django.db import models
from django.utils import timezone

class TimestampedModel(models.Model):
    """Classe abstraite pour ajouter des timestamps automatiques"""
    date_creation = models.DateTimeField(auto_now_add=True)
    date_modification = models.DateTimeField(auto_now=True)
    
    class Meta:
        abstract = True  # IMPORTANT : Pas de table créée !
```

💡 **Explication** :
- `auto_now_add=True` : Date fixée à la création (ne change jamais)
- `auto_now=True` : Date mise à jour automatiquement à chaque `save()`
- `abstract = True` : Django ne crée **PAS** de table pour ce modèle

---

### Étape 2 : Créer une classe abstraite pour le contenu

**Ajoutez** ensuite :

```python
class BaseContenu(TimestampedModel):
    """Classe abstraite pour tout contenu (hérite de TimestampedModel)"""
    titre = models.CharField(max_length=200)
    slug = models.SlugField(unique=True)
    actif = models.BooleanField(default=True)
    
    class Meta:
        abstract = True
        ordering = ['-date_creation']  # Plus récent en premier
    
    def __str__(self):
        return self.titre
```

💡 **Explication** :
- `BaseContenu` hérite de `TimestampedModel` → récupère `date_creation` et `date_modification`
- Ajoute ses propres champs : `titre`, `slug`, `actif`
- `abstract = True` : Toujours pas de table créée !

---

### Étape 3 : Créer un modèle concret

**Ajoutez** le modèle final :

```python
class Tutoriel(BaseContenu):
    """Tutoriel technique - Modèle concret (crée une table)"""
    description = models.TextField()
    
    NIVEAU_CHOICES = [
        ('debutant', 'Débutant'),
        ('intermediaire', 'Intermédiaire'),
        ('avance', 'Avancé'),
    ]
    niveau = models.CharField(max_length=20, choices=NIVEAU_CHOICES)
    duree_minutes = models.PositiveIntegerField()
    
    # Ce modèle hérite automatiquement de :
    # - titre, slug, actif (de BaseContenu)
    # - date_creation, date_modification (de TimestampedModel)
```

💡 **Explication** :
- **Pas** de `abstract = True` → Django crée une table `blog_tutoriel`
- La table contient **TOUS** les champs hérités + les champs spécifiques
- `choices` : Liste de valeurs autorisées pour le champ

---

### Étape 4 : Créer et appliquer les migrations

```bash
python manage.py makemigrations
python manage.py migrate
```

**Vérifiez les tables créées :**

```bash
python manage.py dbshell
.tables  # (SQLite) ou \dt (PostgreSQL)
```

**Résultat attendu :**
- ✅ Table `blog_tutoriel` existe
- ❌ **PAS** de table pour `TimestampedModel`
- ❌ **PAS** de table pour `BaseContenu`

---

### Étape 5 : Tester dans le shell Django

```bash
python manage.py shell
```

**Créer un tutoriel :**

```python
from blog.models import Tutoriel

# Créer un tutoriel
tuto = Tutoriel.objects.create(
    titre="Introduction à Django",
    slug="intro-django",
    description="Apprenez Django de zéro...",
    niveau="debutant",
    duree_minutes=30
)

print(tuto)
# Introduction à Django

# Vérifier les champs hérités
print(tuto.date_creation)      # 2024-01-15 10:30:00
print(tuto.date_modification)  # 2024-01-15 10:30:00
print(tuto.actif)              # True

# Modifier et sauvegarder
tuto.duree_minutes = 45
tuto.save()

# date_modification est automatiquement mise à jour !
print(tuto.date_modification)  # 2024-01-15 10:31:00
```

**Requêtes sur le modèle :**

```python
# Tous les tutoriels actifs
tutoriels = Tutoriel.objects.filter(actif=True)

# Tutoriels pour débutants
debutants = Tutoriel.objects.filter(niveau='debutant')

# Tutoriels récents (ordre défini dans BaseContenu)
recents = Tutoriel.objects.all()[:5]
```

---

### Structure en base de données

**Table `blog_tutoriel` :**
```sql
id                  INTEGER PRIMARY KEY
titre               VARCHAR(200)
slug                VARCHAR(50) UNIQUE
actif               BOOLEAN
date_creation       DATETIME
date_modification   DATETIME
description         TEXT
niveau              VARCHAR(20)
duree_minutes       INTEGER
```

---

### Avantages de l'héritage abstrait

✅ **DRY (Don't Repeat Yourself)** : Code factorисé, pas de duplication
✅ **Performances** : Pas de JOIN, une seule table
✅ **Flexibilité** : Facile d'ajouter de nouveaux modèles concrets
✅ **Réutilisable** : Les classes abstraites peuvent être utilisées partout

### Inconvénients

❌ **Pas de requêtes polymorphes** : Impossible de faire `BaseContenu.objects.all()`
❌ **Migrations** : Modifier une classe abstraite nécessite de migrer tous les enfants

---

### Autres exemples pratiques

```python
# Créer d'autres modèles concrets
class Article(BaseContenu):
    contenu = models.TextField()
    auteur = models.ForeignKey(Auteur, on_delete=models.CASCADE)
    # Hérite de : titre, slug, actif, date_creation, date_modification

class Video(BaseContenu):
    url_youtube = models.URLField()
    duree_secondes = models.PositiveIntegerField()
    # Hérite de : titre, slug, actif, date_creation, date_modification

# Tous ces modèles ont les champs communs !
```

## Exercice 7 - Multi-table Inheritance (TUTORIEL)

**Objectif** : Créer une hiérarchie de modèles avec tables séparées permettant des requêtes polymorphes.

L'**héritage multi-table** crée une table pour chaque modèle (parent et enfants). Django crée automatiquement une relation OneToOne entre eux. Cela permet des **requêtes polymorphes** sur la classe parente.

---

### Étape 1 : Créer la classe de base CONCRÈTE

**Important** : La classe parente **N'EST PAS** abstraite, elle crée une vraie table !

**Ajoutez** dans `blog/models.py` :

```python
class Publication(models.Model):
    """Classe de base CONCRÈTE (crée une table)"""
    titre = models.CharField(max_length=200)
    date_publication = models.DateField()
    editeur = models.CharField(max_length=100)
    
    def __str__(self):
        return self.titre
    
    class Meta:
        ordering = ['-date_publication']  # Plus récent en premier
```

💡 **Explication** :
- **Pas** de `abstract = True` → Django crée la table `blog_publication`
- Cette table peut contenir des publications "génériques"
- Les enfants hériteront de ces champs

---

### Étape 2 : Créer une classe enfant

**Ajoutez** le modèle `Livre` :

```python
class Livre(Publication):
    """Hérite de Publication - Table séparée avec OneToOne automatique"""
    isbn = models.CharField(max_length=13, unique=True)
    nombre_pages = models.PositiveIntegerField()
    
    FORMAT_CHOICES = [
        ('broche', 'Broché'),
        ('ebook', 'E-book'),
        ('poche', 'Poche'),
    ]
    format = models.CharField(max_length=20, choices=FORMAT_CHOICES)
    
    # Django crée automatiquement cette relation :
    # publication_ptr = models.OneToOneField(Publication, parent_link=True)
```

💡 **Explication** :
- `Livre` hérite de `Publication` (syntaxe Python classique)
- Django crée automatiquement `publication_ptr` (relation OneToOne cachée)
- Table `blog_livre` contient uniquement les champs spécifiques au livre
- Les champs de `Publication` restent dans `blog_publication`

---

### Étape 3 : Créer et appliquer les migrations

```bash
python manage.py makemigrations
python manage.py migrate
```

**Vérifiez les tables créées :**

```bash
python manage.py dbshell
.tables
```

**Résultat attendu :**
- ✅ Table `blog_publication`
- ✅ Table `blog_livre` (avec FK vers publication)

---

### Étape 4 : Tester dans le shell Django

```bash
python manage.py shell
```

**Créer un livre (crée 2 lignes en base) :**

```python
from blog.models import Publication, Livre
from datetime import date

# Créer un livre
livre = Livre.objects.create(
    titre="Django avancé",
    date_publication=date(2024, 1, 15),
    editeur="TechBooks",
    isbn="978-1234567890",
    nombre_pages=450,
    format='broche'
)

print(livre)
# Django avancé

# Accéder aux champs de Publication (transparent, pas de requête supplémentaire)
print(livre.titre)          # "Django avancé"
print(livre.editeur)        # "TechBooks"
print(livre.date_publication)  # 2024-01-15

# Accéder aux champs spécifiques de Livre
print(livre.isbn)           # "978-1234567890"
print(livre.nombre_pages)   # 450
```

**Requêtes polymorphes (le grand avantage) :**

```python
# Créer d'autres types de publications
pub_generale = Publication.objects.create(
    titre="Rapport annuel",
    date_publication=date(2024, 2, 1),
    editeur="Entreprise Corp"
)

# Récupérer TOUTES les publications (livres + publications génériques)
toutes_publications = Publication.objects.all()
print(f"Total : {toutes_publications.count()} publications")

for pub in toutes_publications:
    print(f"\n{pub.titre} ({pub.editeur})")
    
    # Détecter le type réel
    if hasattr(pub, 'livre'):
        print(f"  Type : Livre")
        print(f"  ISBN : {pub.livre.isbn}")
        print(f"  Pages : {pub.livre.nombre_pages}")
    else:
        print(f"  Type : Publication générique")
```

**Filtrer par type :**

```python
# Seulement les livres
livres = Livre.objects.all()

# Publications qui sont des livres
publications_livres = Publication.objects.filter(livre__isnull=False)

# Publications qui NE sont PAS des livres
publications_autres = Publication.objects.filter(livre__isnull=True)
```

**Accès inverse (depuis Publication vers Livre) :**

```python
# Récupérer une publication
pub = Publication.objects.first()

# Vérifier si c'est un livre
if hasattr(pub, 'livre'):
    print(f"C'est un livre : {pub.livre.isbn}")
else:
    print("C'est une publication générique")
```

---

### Structure en base de données

**Table `blog_publication` :**
```sql
id                  INTEGER PRIMARY KEY
titre               VARCHAR(200)
date_publication    DATE
editeur             VARCHAR(100)
```

**Table `blog_livre` :**
```sql
publication_ptr_id  INTEGER PRIMARY KEY → FK vers blog_publication
isbn                VARCHAR(13) UNIQUE
nombre_pages        INTEGER
format              VARCHAR(20)
```

💡 **Important** : `publication_ptr_id` est à la fois la clé primaire ET la clé étrangère !

---

### Créer d'autres types d'enfants

```python
class Magazine(Publication):
    """Magazine périodique"""
    numero = models.PositiveIntegerField()
    periodicite = models.CharField(max_length=50)  # Mensuel, Hebdomadaire...
    
class JournalScientifique(Publication):
    """Journal scientifique"""
    issn = models.CharField(max_length=9, unique=True)
    facteur_impact = models.DecimalField(max_digits=5, decimal_places=2)
    domaine = models.CharField(max_length=100)
```

**Requêtes polymorphes sur tous les types :**

```python
# Toutes les publications (tous types confondus)
toutes = Publication.objects.all()

# Statistiques par type
from django.db.models import Count

stats = Publication.objects.aggregate(
    total=Count('id'),
    livres=Count('livre'),
    magazines=Count('magazine'),
    journaux=Count('journalscientifique')
)

print(stats)
# {'total': 150, 'livres': 80, 'magazines': 50, 'journaux': 20}
```

---

### Avantages de l'héritage multi-table

✅ **Requêtes polymorphes** : Possibilité de requêter sur la classe parente
✅ **Organisation logique** : Chaque table contient ses champs spécifiques
✅ **Relations** : Autres modèles peuvent pointer vers `Publication` (générique)
✅ **POO naturel** : Héritage Python classique

### Inconvénients

❌ **Performance** : Requiert des JOINs (plus lent que l'héritage abstrait)
❌ **Complexité** : 2 lignes par objet enfant (1 dans parent + 1 dans enfant)
❌ **Migrations** : Plus complexes à gérer
❌ **Suppression** : Cascade automatique (supprimer parent = supprimer enfant)

---

### Comparaison : Abstract vs Multi-table

| Critère | Abstract (Exercice 6) | Multi-table (Exercice 7) |
|---------|----------------------|-------------------------|
| **Tables** | 1 table par modèle concret | 1 table parent + 1 table par enfant |
| **Performance** | ⚡ Rapide (pas de JOIN) | 🐌 Lent (JOIN requis) |
| **Requêtes polymorphes** | ❌ Impossible | ✅ Possible |
| **Relations** | Chaque modèle séparé | Peuvent pointer vers parent |
| **Usage** | Factorisation de code | Hiérarchie avec polymorphisme |

### Quand utiliser quoi ?

**Utilisez Abstract** (Exercice 6) quand :
- Vous voulez factoriser du code
- Vous n'avez pas besoin de requêtes polymorphes
- Performance critique

**Utilisez Multi-table** (Exercice 7) quand :
- Vous avez besoin de requêtes sur la classe parente
- Vous voulez des relations vers la classe de base
- Vous avez une vraie hiérarchie de types

## Exercice 8 - Proxy Models (TUTORIEL)

**Objectif** : Créer un modèle proxy pour modifier le comportement sans créer de nouvelle table.

Les **Proxy Models** permettent de créer différentes "vues" du même modèle avec des comportements, méthodes ou ordres différents, **sans créer de nouvelle table**. Tous les proxies partagent la même table en base de données.

---

### Étape 1 : Vérifier le modèle Article de base

**Assurez-vous** que votre modèle `Article` existe dans `blog/models.py` :

```python
class Article(models.Model):
    titre = models.CharField(max_length=200)
    contenu = models.TextField()
    auteur = models.ForeignKey(Auteur, on_delete=models.CASCADE)
    date_publication = models.DateField(null=True, blank=True)
    publie = models.BooleanField(default=False)
    nombre_vues = models.PositiveIntegerField(default=0)
    
    class Meta:
        ordering = ['titre']  # Ordre alphabétique par défaut
    
    def __str__(self):
        return self.titre
```

---

### Étape 2 : Créer un modèle proxy pour les articles publiés

**Ajoutez** dans `blog/models.py` :

```python
class ArticlePublie(Article):
    """Proxy : même table qu'Article, comportement différent"""
    
    class Meta:
        proxy = True  # IMPORTANT : Pas de nouvelle table !
        ordering = ['-date_publication']  # Ordre différent : plus récent en premier
        verbose_name = "Article publié"
        verbose_name_plural = "Articles publiés"
    
    @classmethod
    def get_recents(cls, nombre=5):
        """Retourne les articles publiés les plus récents"""
        return cls.objects.filter(publie=True).order_by('-date_publication')[:nombre]
    
    def incrementer_vues(self):
        """Méthode personnalisée pour incrémenter les vues"""
        self.nombre_vues += 1
        self.save(update_fields=['nombre_vues'])
```

💡 **Explication** :
- `proxy = True` : Utilise la **même table** que `Article`
- `ordering` différent : Les `ArticlePublie` sont triés par date (pas par titre)
- Méthodes personnalisées : `get_recents()` et `incrementer_vues()`
- `verbose_name` : Nom différent dans l'admin Django

---

### Étape 3 : Vérifier qu'aucune migration n'est nécessaire

```bash
python manage.py makemigrations
```

**Résultat attendu :**
```
No changes detected
```

💡 Les Proxy Models ne créent **AUCUNE** migration car ils n'ajoutent pas de table !

---

### Étape 4 : Tester dans le shell Django

```bash
python manage.py shell
```

**Créer des articles :**

```python
from blog.models import Article, ArticlePublie, Auteur
from datetime import date

auteur = Auteur.objects.first()

# Créer via le modèle de base
article1 = Article.objects.create(
    titre="Introduction Django",
    contenu="Contenu...",
    auteur=auteur,
    publie=True,
    date_publication=date(2024, 1, 15)
)

article2 = Article.objects.create(
    titre="Django Avancé",
    contenu="Contenu...",
    auteur=auteur,
    publie=False,  # Brouillon
    date_publication=None
)
```

**Accéder au même article via le proxy :**

```python
# Récupérer via le proxy
article_proxy = ArticlePublie.objects.get(id=article1.id)

print(article_proxy.titre)
# "Introduction Django"

# C'est exactement le MÊME objet en base
print(article1.pk == article_proxy.pk)  # True
print(type(article1))        # <class 'blog.models.Article'>
print(type(article_proxy))   # <class 'blog.models.ArticlePublie'>
```

**Utiliser les méthodes personnalisées :**

```python
# Méthode de classe personnalisée
recents = ArticlePublie.get_recents(3)
print(f"Articles récents : {recents.count()}")

for article in recents:
    print(f"- {article.titre} ({article.date_publication})")

# Méthode d'instance personnalisée
article_proxy.incrementer_vues()
print(f"Vues : {article_proxy.nombre_vues}")  # 1
```

**Vérifier qu'ils partagent la même table :**

```python
# Compter tous les articles
print(f"Article.objects.count() : {Article.objects.count()}")
# 2

# Le proxy voit les mêmes données
print(f"ArticlePublie.objects.count() : {ArticlePublie.objects.count()}")
# 2

# Mais le proxy peut avoir un manager par défaut différent
# Si on filtre seulement les publiés :
print(f"Articles publiés : {ArticlePublie.objects.filter(publie=True).count()}")
# 1
```

**Ordre différent :**

```python
# Via Article : ordre alphabétique (titre)
for a in Article.objects.all():
    print(a.titre)
# Django Avancé
# Introduction Django

# Via ArticlePublie : ordre par date (plus récent)
for a in ArticlePublie.objects.filter(publie=True):
    print(a.titre)
# Introduction Django (date plus récente)
```

---

### Créer un autre proxy : ArticleBrouillon

```python
class ArticleBrouillon(Article):
    """Proxy pour les articles non publiés"""
    
    class Meta:
        proxy = True
        ordering = ['-date_creation']
        verbose_name = "Article brouillon"
        verbose_name_plural = "Articles brouillons"
    
    @classmethod
    def get_anciens(cls, jours=30):
        """Brouillons plus anciens que X jours"""
        from datetime import datetime, timedelta
        date_limite = datetime.now() - timedelta(days=jours)
        return cls.objects.filter(
            publie=False,
            date_creation__lt=date_limite
        )
```

**Utilisation :**

```python
# Tous les brouillons
brouillons = ArticleBrouillon.objects.filter(publie=False)

# Brouillons anciens (à supprimer ?)
anciens = ArticleBrouillon.get_anciens(jours=60)
print(f"{anciens.count()} brouillons de plus de 60 jours")
```

---

### Cas d'usage : Admin Django

Les Proxy Models sont **très utiles** dans l'admin Django pour afficher le même modèle différemment :

```python
from django.contrib import admin

@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):
    list_display = ['titre', 'auteur', 'publie', 'date_publication']
    list_filter = ['publie', 'auteur']

@admin.register(ArticlePublie)
class ArticlePublieAdmin(admin.ModelAdmin):
    list_display = ['titre', 'nombre_vues', 'date_publication']
    list_filter = ['auteur']
    
    def get_queryset(self, request):
        # Afficher seulement les articles publiés
        return super().get_queryset(request).filter(publie=True)

@admin.register(ArticleBrouillon)
class ArticleBrouillonAdmin(admin.ModelAdmin):
    list_display = ['titre', 'auteur', 'date_creation']
    actions = ['publier']
    
    def get_queryset(self, request):
        # Afficher seulement les brouillons
        return super().get_queryset(request).filter(publie=False)
    
    def publier(self, request, queryset):
        queryset.update(publie=True, date_publication=date.today())
    publier.short_description = "Publier les articles sélectionnés"
```

💡 **Résultat** : 3 sections dans l'admin Django pour gérer le même modèle différemment !

---

### Structure en base de données

**UNE SEULE table `blog_article` :**
```sql
id                  INTEGER PRIMARY KEY
titre               VARCHAR(200)
contenu             TEXT
auteur_id           INTEGER → FK vers auteur
date_publication    DATE
publie              BOOLEAN
nombre_vues         INTEGER
```

Tous les proxies (`Article`, `ArticlePublie`, `ArticleBrouillon`) utilisent **cette unique table**.

---

### Avantages des Proxy Models

✅ **Aucun coût en performance** : Même table, pas de JOIN
✅ **Pas de duplication** : Une seule source de vérité
✅ **Pas de migration** : Aucun changement en base de données
✅ **Organisation du code** : Comportements spécialisés
✅ **Admin Django** : Affichages multiples du même modèle
✅ **Méthodes personnalisées** : Chaque proxy peut avoir ses propres méthodes

### Inconvénients

❌ **Pas de nouveaux champs** : Impossible d'ajouter des colonnes
❌ **Même PK** : Tous les proxies partagent les mêmes IDs
❌ **Confusion possible** : Peut être déroutant pour les débutants
❌ **Pas de polymorphisme** : C'est toujours le même modèle

---

### Comparaison des 3 stratégies d'héritage

| Critère | Abstract (Ex 6) | Multi-table (Ex 7) | Proxy (Ex 8) |
|---------|-----------------|-------------------|--------------|
| **Tables créées** | Une par enfant | Une par classe | Une seule |
| **Champs de base hérités** | ✅ Oui (copiés) | ✅ Oui (JOIN) | ✅ Oui (même table) |
| **Nouveaux champs** | ✅ Oui | ✅ Oui | ❌ Non |
| **Requêtes polymorphes** | ❌ Non | ✅ Oui | ❌ Non |
| **Performances** | ⭐⭐⭐ Excellent | ⭐⭐ Moyen (JOINs) | ⭐⭐⭐ Excellent |
| **Cas d'usage** | Factoriser code | Hiérarchie types | Comportement différent |
| **Migrations** | Oui | Oui | Non |

---

### Quand utiliser les Proxy Models ?

**Utilisez Proxy** quand :
- Vous voulez des méthodes/comportements différents sans changer la structure
- Vous voulez plusieurs vues dans l'admin Django
- Vous voulez changer l'ordre par défaut
- Vous ne voulez PAS de nouvelle table
- Performance critique

**N'utilisez PAS Proxy** si :
- Vous avez besoin de nouveaux champs → Utilisez Abstract ou Multi-table
- Vous avez besoin de requêtes polymorphes → Utilisez Multi-table

---

🎉 **Félicitations !** Vous maîtrisez maintenant les 3 types d'héritage Django : Abstract, Multi-table et Proxy !

