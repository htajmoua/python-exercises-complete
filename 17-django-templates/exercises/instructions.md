# Instructions - Django Templates

Les templates Django permettent de générer du HTML dynamique en séparant la logique de présentation du code Python.

## Exercice 1 - Premier template

**Créez** la structure de templates :

```
blog/
  templates/
    blog/
      base.html
      home.html
```

**Créez** `blog/templates/blog/base.html` :

```html
<!DOCTYPE html>
<html lang="fr">
<head>
    <meta charset="UTF-8">
    <title>{% block title %}Mon Blog{% endblock %}</title>
</head>
<body>
    <header>
        <h1>Mon Blog Django</h1>
        <nav>
            <a href="{% url 'blog:home' %}">Accueil</a>
            <a href="{% url 'blog:article_list' %}">Articles</a>
        </nav>
    </header>
    
    <main>
        {% block content %}
        {% endblock %}
    </main>
    
    <footer>
        <p>&copy; 2024 Mon Blog</p>
    </footer>
</body>
</html>
```

**Créez** `blog/templates/blog/home.html` :

```html
{% extends 'blog/base.html' %}

{% block title %}Accueil - {{ block.super }}{% endblock %}

{% block content %}
    <h2>Bienvenue sur mon blog !</h2>
    <p>Découvrez mes derniers articles.</p>
{% endblock %}
```

**Modifiez** la vue `home` :

```python
def home(request):
    return render(request, 'blog/home.html')
```

## Exercice 2 - Variables et filtres

**Créez** `article_list.html` :

```html
{% extends 'blog/base.html' %}

{% block content %}
    <h2>Liste des articles</h2>
    
    {% for article in articles %}
        <article>
            <h3>{{ article.titre|title }}</h3>
            <p>Par {{ article.auteur }} - {{ article.date_creation|date:"d F Y" }}</p>
            <p>{{ article.contenu|truncatewords:30 }}</p>
            <a href="{% url 'blog:article_detail' article.id %}">Lire la suite</a>
        </article>
    {% empty %}
        <p>Aucun article disponible.</p>
    {% endfor %}
{% endblock %}
```

## Exercice 3 - Template tags conditionnels

**Utilisez** les tags `if`, `elif`, `else` :

```html
{% extends 'blog/base.html' %}

{% block content %}
    {% if user.is_authenticated %}
        <p>Bonjour {{ user.username }} !</p>
        {% if user.is_staff %}
            <a href="{% url 'admin:index' %}">Administration</a>
        {% endif %}
    {% else %}
        <p>Veuillez vous connecter.</p>
    {% endif %}
    
    {% for article in articles %}
        {% if article.publie %}
            <h3>{{ article.titre }}</h3>
        {% else %}
            <h3>{{ article.titre }} (Brouillon)</h3>
        {% endif %}
    {% endfor %}
{% endblock %}
```

## Exercice 4 - Filtres personnalisés

**Créez** `blog/templatetags/blog_tags.py` :

```python
from django import template

register = template.Library()

@register.filter
def nombre_mots(value):
    """Compte le nombre de mots"""
    return len(value.split())

@register.filter
def premier_paragraphe(value):
    """Retourne le premier paragraphe"""
    paragraphes = value.split('\n\n')
    return paragraphes[0] if paragraphes else value
```

**Utilisez-le** dans le template :

```html
{% load blog_tags %}

<p>{{ article.contenu|nombre_mots }} mots</p>
<p>{{ article.contenu|premier_paragraphe }}</p>
```

## Exercice 5 - Template tags personnalisés

**Ajoutez** dans `blog_tags.py` :

```python
@register.simple_tag
def articles_count():
    """Retourne le nombre total d'articles"""
    from blog.models import Article
    return Article.publies.count()

@register.inclusion_tag('blog/partials/latest_articles.html')
def show_latest_articles(count=5):
    """Affiche les derniers articles"""
    from blog.models import Article
    articles = Article.publies.all()[:count]
    return {'articles': articles}
```

**Créez** `blog/templates/blog/partials/latest_articles.html` :

```html
<aside class="latest-articles">
    <h3>Derniers articles</h3>
    <ul>
        {% for article in articles %}
            <li><a href="{% url 'blog:article_detail' article.id %}">{{ article.titre }}</a></li>
        {% endfor %}
    </ul>
</aside>
```

**Utilisez-le** :

```html
{% load blog_tags %}

<p>Total: {% articles_count %} articles</p>
{% show_latest_articles 3 %}
```

## Exercice 6 - Static files (CSS, JS, Images)

**Configurez** `settings.py` :

```python
STATIC_URL = '/static/'
STATICFILES_DIRS = [BASE_DIR / 'static']
```

**Créez** la structure :

```
blog/
  static/
    blog/
      css/
        style.css
      js/
        script.js
      images/
        logo.png
```

**Créez** `blog/static/blog/css/style.css` :

```css
body {
    font-family: Arial, sans-serif;
    margin: 0;
    padding: 0;
    background-color: #f4f4f4;
}

header {
    background-color: #333;
    color: white;
    padding: 1rem;
}

nav a {
    color: white;
    margin-right: 1rem;
    text-decoration: none;
}

main {
    padding: 2rem;
    max-width: 1200px;
    margin: 0 auto;
}

article {
    background: white;
    padding: 1.5rem;
    margin-bottom: 1rem;
    border-radius: 5px;
}
```

**Utilisez** dans `base.html` :

```html
{% load static %}
<!DOCTYPE html>
<html>
<head>
    <link rel="stylesheet" href="{% static 'blog/css/style.css' %}">
    <script src="{% static 'blog/js/script.js' %}" defer></script>
</head>
<body>
    <img src="{% static 'blog/images/logo.png' %}" alt="Logo">
    <!-- ... -->
</body>
</html>
```

## Exercice 7 - Pagination dans les templates

**Template avec pagination** :

```html
{% extends 'blog/base.html' %}

{% block content %}
    <h2>Articles (Page {{ page_obj.number }})</h2>
    
    {% for article in page_obj %}
        <article>
            <h3>{{ article.titre }}</h3>
            <p>{{ article.get_preview }}</p>
        </article>
    {% endfor %}
    
    <div class="pagination">
        {% if page_obj.has_previous %}
            <a href="?page=1">« première</a>
            <a href="?page={{ page_obj.previous_page_number }}">précédente</a>
        {% endif %}
        
        <span>Page {{ page_obj.number }} sur {{ page_obj.paginator.num_pages }}</span>
        
        {% if page_obj.has_next %}
            <a href="?page={{ page_obj.next_page_number }}">suivante</a>
            <a href="?page={{ page_obj.paginator.num_pages }}">dernière »</a>
        {% endif %}
    </div>
{% endblock %}
```

## Exercice 8 - Inclusion de templates

**Créez** des templates réutilisables :

`blog/templates/blog/partials/article_card.html` :

```html
<article class="article-card">
    <h3>{{ article.titre }}</h3>
    <div class="meta">
        <span>Par {{ article.auteur }}</span>
        <span>{{ article.date_creation|date:"SHORT_DATE_FORMAT" }}</span>
    </div>
    <p>{{ article.get_preview }}</p>
    {% if show_link %}
        <a href="{% url 'blog:article_detail' article.id %}">Lire plus</a>
    {% endif %}
</article>
```

**Utilisez-le** :

```html
{% for article in articles %}
    {% include 'blog/partials/article_card.html' with show_link=True %}
{% endfor %}
```

## Exercice 9 - Context processors

**Créez** `blog/context_processors.py` :

```python
from .models import Tag

def blog_context(request):
    return {
        'all_tags': Tag.objects.all(),
        'site_name': 'Mon Super Blog',
    }
```

**Ajoutez** dans `settings.py` :

```python
TEMPLATES = [
    {
        # ...
        'OPTIONS': {
            'context_processors': [
                # ... processeurs existants ...
                'blog.context_processors.blog_context',
            ],
        },
    },
]
```

**Utilisez** dans n'importe quel template :

```html
<h1>{{ site_name }}</h1>
<div class="tags">
    {% for tag in all_tags %}
        <span>{{ tag.nom }}</span>
    {% endfor %}
</div>
```

## Exercice 10 - Messages framework

**Dans une vue** :

```python
from django.contrib import messages

def article_create(request):
    if request.method == 'POST':
        # ... traitement ...
        messages.success(request, 'Article créé avec succès!')
        return redirect('blog:article_list')
```

**Dans le template** `base.html` :

```html
{% if messages %}
    <div class="messages">
        {% for message in messages %}
            <div class="alert alert-{{ message.tags }}">
                {{ message }}
            </div>
        {% endfor %}
    </div>
{% endif %}
```

## Exercices bonus

### Exercice 11 - Breadcrumbs
**Créez** un système de fil d'Ariane réutilisable.

### Exercice 12 - Template avec AJAX
**Créez** un système de "load more" pour les articles.

### Exercice 13 - Syntaxe alternative
**Utilisez** la syntaxe `{% with %}` et `{% spaceless %}`.

## Checklist de validation

-  Template inheritance fonctionnel
-  Variables et filtres utilisés
-  Tags conditionnels et boucles maîtrisés
-  Filtres personnalisés créés
-  Template tags personnalisés implémentés
-  Static files configurés et utilisés
-  Pagination dans les templates
-  Inclusion de templates
-  Context processors configurés
-  Messages framework utilisé
