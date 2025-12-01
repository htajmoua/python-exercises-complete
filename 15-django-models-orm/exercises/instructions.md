# Instructions - Django Models : Fondamentaux

**🎯 Objectif du module** : Maîtriser les bases des modèles Django - champs, relations et héritage.

Les modèles Django définissent la structure de votre base de données. L'ORM (Object-Relational Mapping) permet d'interagir avec la base de données en Python sans écrire de SQL.

**📚 Format du module** :
- **Partie 1 (Exercices 1-3)** : Exemples guidés - Création de modèles et relations de base
- **Partie 2 (Exercices 4-8)** : Exercices pratiques - À compléter par vos soins

**Prérequis** : Avoir complété le module 14 (Django installé et configuré)

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

**Modifiez** le modèle `Article` pour ajouter une relation avec `Auteur` :

```python
class Article(models.Model):
    titre = models.CharField(max_length=200)
    slug = models.SlugField(unique=True)
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

**Options on_delete** :

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

**Testez** les relations :

```python
# Créer un auteur et ses articles
auteur = Auteur.objects.create(nom="Dupont", prenom="Jean", email="jean@example.com")
article1 = Article.objects.create(titre="Article 1", contenu="...", auteur=auteur)
article2 = Article.objects.create(titre="Article 2", contenu="...", auteur=auteur)

# Accès inverse (related_name)
auteur.articles.all()  # QuerySet[<Article 1>, <Article 2>]
auteur.articles.count()  # 2
auteur.articles.filter(publie=True)

# Accès direct
article1.auteur  # <Auteur: Jean Dupont>
article1.auteur.nom  # "Dupont"
```

---

# 🔨 PARTIE 2 : EXERCICES PRATIQUES

**À partir d'ici, c'est à vous de coder !** Les exercices suivants contiennent des squelettes avec des `TODO` à compléter.

---

## Exercice 4 - Relation ManyToMany (PRATIQUE)

**Objectif** : Créer un modèle Tag avec une relation plusieurs-à-plusieurs vers Article.

**Consignes** :
1. Créez un modèle `Tag` avec les champs : nom, slug, description, couleur
2. Ajoutez une relation ManyToMany dans le modèle Article vers Tag
3. Testez la relation dans le shell Django

**Squelette - `blog/models.py`** (à compléter) :

```python
class Tag(models.Model):
    # TODO : Ajoutez le champ 'nom' (CharField, max_length=50, unique=True)
    nom = # VOTRE CODE ICI
    
    # TODO : Ajoutez le champ 'slug' (SlugField, unique=True)
    slug = # VOTRE CODE ICI
    
    # TODO : Ajoutez le champ 'description' (TextField, blank=True)
    description = # VOTRE CODE ICI
    
    # TODO : Ajoutez le champ 'couleur' (CharField, max_length=7, default='#000000')
    couleur = # VOTRE CODE ICI
    
    def __str__(self):
        # TODO : Retournez le nom du tag
        return # VOTRE CODE ICI
    
    class Meta:
        # TODO : Définissez l'ordre alphabétique par nom
        ordering = # VOTRE CODE ICI

class Article(models.Model):
    # ... champs existants (titre, contenu, auteur, etc.) ...
    
    # TODO : Ajoutez la relation ManyToMany vers Tag
    # Le champ doit s'appeler 'tags'
    # Il doit être optionnel (blank=True)
    # Le related_name doit être 'articles'
    tags = # VOTRE CODE ICI
```

**Indice** :
- Pour ManyToMany : `models.ManyToManyField(ModeleCible, blank=True, related_name='...')`
- Regardez l'exemple de ForeignKey dans l'exercice 3

**Validation** :

```bash
# TODO : Créez les migrations
python manage.py makemigrations
python manage.py migrate

# TODO : Testez dans le shell
python manage.py shell
```

```python
from blog.models import Article, Tag

# TODO : Créez des tags
tag_python = Tag.objects.create(nom="Python", slug="python", couleur="#3776ab")
tag_django = Tag.objects.create(nom="Django", slug="django", couleur="#092e20")

# TODO : Récupérez un article et ajoutez-lui des tags
article = Article.objects.first()
# Utilisez : article.tags.add(tag_python, tag_django)
# VOTRE CODE ICI

# TODO : Affichez tous les tags de l'article
# Utilisez : article.tags.all()
# VOTRE CODE ICI

# TODO : Trouvez tous les articles avec le tag "Python"
# Utilisez : Article.objects.filter(tags__nom="Python")
# VOTRE CODE ICI
```

---

**ManyToMany avec table intermédiaire personnalisée** (BONUS - optionnel) :

```python
class Categorie(models.Model):
    nom = models.CharField(max_length=100)
    slug = models.SlugField(unique=True)
    
    def __str__(self):
        return self.nom

class ArticleCategorie(models.Model):
    """Table intermédiaire personnalisée pour la relation Article-Categorie"""
    article = models.ForeignKey(Article, on_delete=models.CASCADE)
    categorie = models.ForeignKey(Categorie, on_delete=models.CASCADE)
    
    # Champs supplémentaires
    ordre = models.PositiveIntegerField(default=0)
    principale = models.BooleanField(default=False)
    date_ajout = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        unique_together = ['article', 'categorie']
        ordering = ['ordre']
    
    def __str__(self):
        return f"{self.article.titre} → {self.categorie.nom}"

class Article(models.Model):
    # ... champs existants ...
    
    categories = models.ManyToManyField(
        Categorie,
        through='ArticleCategorie',
        related_name='articles'
    )
```

**Utilisation des relations ManyToMany** :

```python
# Créer des tags
tag_python = Tag.objects.create(nom="Python", slug="python")
tag_django = Tag.objects.create(nom="Django", slug="django")

# Ajouter des tags à un article
article = Article.objects.first()
article.tags.add(tag_python, tag_django)

# Retirer un tag
article.tags.remove(tag_python)

# Remplacer tous les tags
article.tags.set([tag_python, tag_django])

# Effacer tous les tags
article.tags.clear()

# Vérifier l'existence
article.tags.filter(nom="Python").exists()

# Accès inverse
tag_python.articles.all()
```

**Avec table intermédiaire personnalisée** :

```python
# Créer la relation avec des données supplémentaires
ArticleCategorie.objects.create(
    article=article,
    categorie=categorie,
    ordre=1,
    principale=True
)

# Accéder aux données intermédiaires
for ac in article.articlecategorie_set.all():
    print(f"{ac.categorie.nom} - Ordre: {ac.ordre} - Principale: {ac.principale}")
```

## Exercice 5 - Relation OneToOne (PRATIQUE)

**Objectif** : Créer un modèle ProfilAuteur avec une relation un-à-un vers Auteur.

**Consignes** :
1. Créez un modèle `ProfilAuteur` avec une relation OneToOne vers `Auteur`
2. Ajoutez les champs : biographie_longue, twitter, linkedin, github, notifications_email, profil_public
3. Testez la relation dans le shell Django

**Squelette - `blog/models.py`** (à compléter) :

```python
class ProfilAuteur(models.Model):
    # TODO : Ajoutez la relation OneToOne vers Auteur
    # Utilisez : models.OneToOneField()
    # Arguments : on_delete=models.CASCADE, related_name='profil', primary_key=True
    auteur = # VOTRE CODE ICI
    
    # TODO : Ajoutez le champ 'biographie_longue' (TextField, blank=True)
    biographie_longue = # VOTRE CODE ICI
    
    # TODO : Ajoutez le champ 'twitter' (CharField, max_length=100, blank=True)
    twitter = # VOTRE CODE ICI
    
    # TODO : Ajoutez le champ 'linkedin' (URLField, blank=True)
    linkedin = # VOTRE CODE ICI
    
    # TODO : Ajoutez le champ 'github' (CharField, max_length=100, blank=True)
    github = # VOTRE CODE ICI
    
    # TODO : Ajoutez le champ 'nombre_followers' (PositiveIntegerField, default=0)
    nombre_followers = # VOTRE CODE ICI
    
    # TODO : Ajoutez le champ 'notifications_email' (BooleanField, default=True)
    notifications_email = # VOTRE CODE ICI
    
    # TODO : Ajoutez le champ 'profil_public' (BooleanField, default=True)
    profil_public = # VOTRE CODE ICI
    
    def __str__(self):
        # TODO : Retournez f"Profil de {self.auteur}"
        return # VOTRE CODE ICI
```

**Indice** :
- OneToOneField est similaire à ForeignKey mais garantit l'unicité
- `primary_key=True` signifie que le profil utilise l'ID de l'auteur

**Validation** :

```bash
# TODO : Créez les migrations
python manage.py makemigrations
python manage.py migrate

# TODO : Testez dans le shell
python manage.py shell
```

```python
from blog.models import Auteur, ProfilAuteur

# TODO : Récupérez un auteur
auteur = Auteur.objects.first()

# TODO : Créez un profil pour cet auteur
# profil = ProfilAuteur.objects.create(auteur=..., twitter="@...", ...)
# VOTRE CODE ICI

# TODO : Accédez au profil depuis l'auteur
# Utilisez : auteur.profil
print(auteur.profil.twitter)

# TODO : Accédez à l'auteur depuis le profil
# Utilisez : profil.auteur
# VOTRE CODE ICI

# TODO : Gérez le cas où un auteur n'a pas de profil
if hasattr(auteur, 'profil'):
    print("A un profil")
else:
    print("Pas de profil")
```

**Différences entre relations** (à retenir) :

| Relation | Usage | Exemple |
|----------|-------|---------|
| **ForeignKey** | Un objet A peut avoir plusieurs objets B | Un auteur a plusieurs articles |
| **ManyToMany** | Plusieurs objets A ont plusieurs objets B | Un article a plusieurs tags |
| **OneToOne** | Un objet A a exactement un objet B | Un auteur a un profil |

---

## Exercice 6 - Abstract Base Classes (PRATIQUE)

**Objectif** : Créer des classes abstraites réutilisables pour partager des champs communs.

**Cas d'usage** : Partager des champs communs sans créer de table pour la classe de base.

**Consignes** :
1. Créez une classe abstraite `TimestampedModel` avec date_creation et date_modification
2. Créez une classe abstraite `BaseContenu` qui hérite de `TimestampedModel`
3. Créez un modèle concret `Tutoriel` qui hérite de `BaseContenu`

**Squelette - `blog/models.py`** (à compléter) :

```python
from django.utils import timezone

class TimestampedModel(models.Model):
    """Classe abstraite pour ajouter des timestamps automatiques"""
    # TODO : Ajoutez le champ 'date_creation' (DateTimeField, auto_now_add=True)
    date_creation = # VOTRE CODE ICI
    
    # TODO : Ajoutez le champ 'date_modification' (DateTimeField, auto_now=True)
    date_modification = # VOTRE CODE ICI
    
    class Meta:
        # TODO : Définissez abstract = True (IMPORTANT !)
        abstract = # VOTRE CODE ICI

class BaseContenu(TimestampedModel):
    """Classe abstraite pour tout contenu"""
    # TODO : Ajoutez le champ 'titre' (CharField, max_length=200)
    titre = # VOTRE CODE ICI
    
    # TODO : Ajoutez le champ 'slug' (SlugField, unique=True)
    slug = # VOTRE CODE ICI
    
    # TODO : Ajoutez le champ 'actif' (BooleanField, default=True)
    actif = # VOTRE CODE ICI
    
    class Meta:
        # TODO : Définissez abstract = True
        abstract = # VOTRE CODE ICI
        # TODO : Définissez l'ordre par date_creation décroissante
        ordering = # VOTRE CODE ICI
    
    def __str__(self):
        # TODO : Retournez le titre
        return # VOTRE CODE ICI

# TODO : Créez un modèle concret 'Tutoriel' qui hérite de BaseContenu
class Tutoriel(BaseContenu):
    """Tutoriel technique"""
    # TODO : Ajoutez le champ 'description' (TextField)
    description = # VOTRE CODE ICI
    
    # TODO : Ajoutez le champ 'niveau' (CharField, max_length=20) avec choix
    # Choix : ('debutant', 'Débutant'), ('intermediaire', 'Intermédiaire'), ('avance', 'Avancé')
    NIVEAU_CHOICES = [
        # VOTRE CODE ICI
    ]
    niveau = # VOTRE CODE ICI
    
    # TODO : Ajoutez le champ 'duree_minutes' (PositiveIntegerField)
    duree_minutes = # VOTRE CODE ICI
    
    # Le modèle hérite automatiquement de : titre, slug, actif, date_creation, date_modification
```

**Indice** :
- `abstract = True` dans `class Meta` empêche la création d'une table
- Les champs de la classe abstraite sont copiés dans les modèles concrets
- L'héritage multiple est possible (hériter de plusieurs classes abstraites)

**Validation** :

```bash
# TODO : Créez les migrations
python manage.py makemigrations
python manage.py migrate

# TODO : Vérifiez qu'il n'y a PAS de table pour TimestampedModel ni BaseContenu
# Il doit y avoir une table blog_tutoriel avec TOUS les champs
python manage.py dbshell
.tables  # (SQLite) ou \dt (PostgreSQL)
```

```python
# TODO : Testez dans le shell
from blog.models import Tutoriel

# TODO : Créez un tutoriel
tuto = Tutoriel.objects.create(
    titre="Introduction Django",
    slug="intro-django",
    description="Apprenez Django...",
    niveau="debutant",
    duree_minutes=30
)

# TODO : Vérifiez que les champs hérités fonctionnent
print(tuto.date_creation)  # Doit afficher la date
print(tuto.titre)          # "Introduction Django"
```

**Résultat en base de données** :
- Table `blog_tutoriel` : id, titre, slug, actif, date_creation, date_modification, description, niveau, duree_minutes
- **PAS** de table pour `TimestampedModel` ni `BaseContenu` (classes abstraites)

**Avantages** :
- DRY (Don't Repeat Yourself)
- Performances optimales (pas de JOIN)
- Code réutilisable

**Inconvénients** :
- Impossible de faire des requêtes polymorphes sur la classe de base
- Changements dans la classe abstraite nécessitent des migrations pour tous les enfants

## Exercice 7 - Multi-table Inheritance (PRATIQUE)

**Objectif** : Créer une hiérarchie de modèles avec tables séparées permettant des requêtes polymorphes.

**Cas d'usage** : Quand vous avez besoin de requêtes sur la classe parente ET les classes enfants.

**Consignes** :
1. Créez une classe de base **CONCRÈTE** `Publication` (pas abstraite !)
2. Créez une classe enfant `Livre` qui hérite de `Publication`
3. Testez les requêtes polymorphes

**Squelette - `blog/models.py`** (à compléter) :

```python
class Publication(models.Model):
    """Classe de base CONCRÈTE (crée une table)"""
    # TODO : Ajoutez le champ 'titre' (CharField, max_length=200)
    titre = # VOTRE CODE ICI
    
    # TODO : Ajoutez le champ 'date_publication' (DateField)
    date_publication = # VOTRE CODE ICI
    
    # TODO : Ajoutez le champ 'editeur' (CharField, max_length=100)
    editeur = # VOTRE CODE ICI
    
    def __str__(self):
        return self.titre
    
    class Meta:
        # TODO : Définissez l'ordre par date_publication décroissante
        ordering = # VOTRE CODE ICI

# TODO : Créez une classe 'Livre' qui hérite de Publication
class Livre(Publication):
    """Hérite de Publication - Table séparée avec OneToOne automatique"""
    # TODO : Ajoutez le champ 'isbn' (CharField, max_length=13, unique=True)
    isbn = # VOTRE CODE ICI
    
    # TODO : Ajoutez le champ 'nombre_pages' (PositiveIntegerField)
    nombre_pages = # VOTRE CODE ICI
    
    # TODO : Ajoutez le champ 'format' avec choices
    # Choix : ('broche', 'Broché'), ('ebook', 'E-book')
    FORMAT_CHOICES = [
        # VOTRE CODE ICI
    ]
    format = # VOTRE CODE ICI
    
    # Django crée automatiquement un lien OneToOne vers Publication :
    # publication_ptr = models.OneToOneField(Publication, parent_link=True)
```

**Indice** :
- **N'ajoutez PAS** `abstract = True` dans `class Meta` de Publication
- L'héritage se fait comme en Python : `class Livre(Publication):`
- Django crée automatiquement la relation OneToOne

**Validation** :

```bash
# TODO : Créez les migrations
python manage.py makemigrations
python manage.py migrate

# TODO : Vérifiez qu'il y a DEUX tables : blog_publication ET blog_livre
python manage.py dbshell
.tables
```

```python
# TODO : Testez dans le shell
from blog.models import Publication, Livre

# TODO : Créez un livre (crée 2 lignes : 1 dans Publication + 1 dans Livre)
livre = Livre.objects.create(
    titre="Django avancé",
    date_publication="2024-01-15",
    editeur="TechBooks",
    isbn="978-1234567890",
    nombre_pages=450,
    format='broche'
)

# TODO : Accédez aux champs de Publication (pas de requête supplémentaire)
print(livre.titre)  # "Django avancé"
print(livre.editeur)  # "TechBooks"

# TODO : ⭐ REQUÊTE POLYMORPHE (très puissant)
# Récupérez TOUTES les publications (livres + autres types)
toutes_publications = Publication.objects.all()
for pub in toutes_publications:
    print(pub.titre)
    # Détectez le type réel
    if hasattr(pub, 'livre'):
        print(f"  → Livre ISBN: {pub.livre.isbn}")
```

**Résultat en base de données** :
- Table `blog_publication` : id, titre, date_publication, editeur
- Table `blog_livre` : id, **publication_ptr_id** (FK→Publication), isbn, nombre_pages, format

**Avantages** :
- Requêtes polymorphes possibles sur la classe parente
- Chaque table contient uniquement ses champs spécifiques

**Inconvénients** :
- Nécessite des JOIN (moins performant que l'héritage abstrait)
- Crée 2 lignes par objet enfant

# Compter par type
from django.db.models import Count, Q
stats = Publication.objects.aggregate(
    total=Count('id'),
    livres=Count('livre'),
    magazines=Count('magazine'),
    journaux=Count('journalscientifique')
)
```

**Avantages** :
- Requêtes polymorphes possibles
- Relations peuvent pointer vers la classe de base
- Héritage "naturel" en POO

**Inconvénients** :
- Requiert des JOINs (moins performant)
- Suppression en cascade complexe
- Migrations plus complexes

## Exercice 8 - Proxy Models (PRATIQUE)

**Objectif** : Créer un modèle proxy pour modifier le comportement sans créer de nouvelle table.

**Cas d'usage** : Ajouter des méthodes ou changer l'ordre par défaut sans dupliquer les données.

**Consignes** :
1. Utilisez le modèle `Article` existant (vérifiez qu'il a les champs: titre, contenu, publie, date_publication)
2. Créez un modèle proxy `ArticlePublie` pour filtrer les articles publiés
3. Ajoutez une méthode personnalisée

**Squelette - `blog/models.py`** (à compléter) :

```python
# Modèle Article existant (vérifiez qu'il contient ces champs)
class Article(models.Model):
    titre = models.CharField(max_length=200)
    contenu = models.TextField()
    auteur = models.ForeignKey(Auteur, on_delete=models.CASCADE)
    date_publication = models.DateField(null=True, blank=True)
    publie = models.BooleanField(default=False)
    nombre_vues = models.PositiveIntegerField(default=0)
    
    class Meta:
        ordering = ['titre']
    
    def __str__(self):
        return self.titre

# TODO : Créez un modèle proxy ArticlePublie qui hérite d'Article
class ArticlePublie(Article):
    """Proxy : même table, comportement différent"""
    
    class Meta:
        # TODO : Définissez proxy = True (IMPORTANT !)
        proxy = # VOTRE CODE ICI
        
        # TODO : Définissez l'ordre par date_publication décroissante
        ordering = # VOTRE CODE ICI
        
        # TODO : Définissez verbose_name = "Article publié"
        verbose_name = # VOTRE CODE ICI
    
    # TODO : Ajoutez une méthode de classe get_recents(nombre=5)
    # qui retourne les articles publiés les plus récents
    @classmethod
    def get_recents(cls, nombre=5):
        # Utilisez : cls.objects.filter(publie=True).order_by(...).[:nombre]
        # VOTRE CODE ICI
        pass
```

**Indice** :
- `proxy = True` dans `class Meta` signifie "même table, comportement différent"
- Les Proxy Models ne nécessitent PAS de migration
- Utile pour l'admin Django (afficher le même modèle différemment)

**Validation** :

```bash
# TODO : Vérifiez qu'aucune migration n'est nécessaire
python manage.py makemigrations
# Devrait afficher "No changes detected"
```

```python
# TODO : Testez dans le shell
from blog.models import Article, ArticlePublie
from datetime import date

# TODO : Créez un article via le modèle de base
article = Article.objects.create(
    titre="Test Proxy",
    contenu="...",
    auteur=auteur,
    publie=True,
    date_publication=date.today()
)

# TODO : Récupérez le même article via le proxy
article_proxy = ArticlePublie.objects.get(id=article.id)
print(article_proxy.titre)  # "Test Proxy"

# TODO : Utilisez la méthode personnalisée
recents = ArticlePublie.get_recents(5)
for a in recents:
    print(a.titre)

# TODO : Vérifiez qu'ils pointent vers la même table
print(Article.objects.count() == ArticlePublie.objects.count())  # True
```

**Résultat** :
- **UNE SEULE** table `blog_article`
- `Article` et `ArticlePublie` pointent vers la même table
- Différences : Meta, méthodes, comportement

**Avantages** :
- Pas de duplication de données
- Pas de migration nécessaire
- Comportements spécialisés
- Utile pour l'admin Django

**Inconvénients** :
- Ne peut pas ajouter de nouveaux champs
- Peut prêter à confusion si mal utilisé
anciens_brouillons = ArticleBrouillon.get_anciens(jours=60)

# Même objet, différentes vues
article = Article.objects.get(id=1)
article_publie = ArticlePublie.objects.get(id=1)
# article == article_publie (même ligne en BDD)
# mais comportement/méthodes différents
```

**Avantages** :
- Aucun coût en performance (même table)
- Organisation du code admin différente
- Méthodes et comportements spécialisés
- Pas de migrations nécessaires

**Inconvénients** :
- Pas de nouveaux champs possibles
- Peut être confusant pour les débutants
- Même PK pour tous les proxies

### Comparaison des 3 stratégies

| Critère | Abstract | Multi-table | Proxy |
|---------|----------|-------------|-------|
| **Tables créées** | Une par enfant | Une par classe | Une seule |
| **Champs de base hérités** | ✅ Oui | ✅ Oui | ✅ Oui (même table) |
| **Nouveaux champs** | ✅ Oui | ✅ Oui | ❌ Non |
| **Requêtes polymorphes** | ❌ Non | ✅ Oui | ❌ Non (même modèle) |
| **Performances** | ⭐⭐⭐ Excellent | ⭐⭐ Moyen (JOINs) | ⭐⭐⭐ Excellent |
| **Cas d'usage** | Partager champs | Hiérarchie de types | Comportement différent |

---

