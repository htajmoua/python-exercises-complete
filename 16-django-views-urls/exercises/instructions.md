# Instructions - Django Views et URLs

Les vues traitent les requêtes HTTP et retournent des réponses. Les URLs définissent le routage des requêtes vers les vues appropriées.

## Exercice 1 - Function-Based Views (FBV) simples

**Créez** plusieurs vues dans `blog/views.py` :

```python
from django.http import HttpResponse, JsonResponse
from django.shortcuts import render
from .models import Article

def home(request):
    return HttpResponse("<h1>Page d'accueil du blog</h1>")

def about(request):
    return HttpResponse("<h1>À propos de nous</h1>")

def contact(request):
    return JsonResponse({'message': 'Page de contact', 'email': 'contact@example.com'})
```

**Configurez** les URLs dans `blog/urls.py` :

```python
from django.urls import path
from . import views

app_name = 'blog'

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('contact/', views.contact, name='contact'),
]
```

## Exercice 2 - URLs avec paramètres

**Ajoutez** des vues avec paramètres :

```python
def article_detail(request, article_id):
    try:
        article = Article.objects.get(id=article_id)
        return HttpResponse(f"<h1>{article.titre}</h1><p>{article.contenu}</p>")
    except Article.DoesNotExist:
        return HttpResponse("Article non trouvé", status=404)

def article_par_annee(request, annee):
    return HttpResponse(f"<h1>Articles de {annee}</h1>")

def article_par_annee_mois(request, annee, mois):
    return HttpResponse(f"<h1>Articles de {mois}/{annee}</h1>")
```

**URLs correspondantes** :

```python
urlpatterns = [
    # ... URLs existantes ...
    path('article/<int:article_id>/', views.article_detail, name='article_detail'),
    path('annee/<int:annee>/', views.article_par_annee, name='par_annee'),
    path('annee/<int:annee>/<int:mois>/', views.article_par_annee_mois, name='par_annee_mois'),
]
```

## Exercice 3 - URLs avec slug

**Ajoutez** un champ `slug` au modèle `Article` :

```python
from django.utils.text import slugify

class Article(models.Model):
    # ... champs existants ...
    slug = models.SlugField(unique=True, blank=True)
    
    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.titre)
        super().save(*args, **kwargs)
```

**Vue avec slug** :

```python
def article_by_slug(request, slug):
    article = Article.objects.get(slug=slug)
    return HttpResponse(f"<h1>{article.titre}</h1>")
```

**URL** :

```python
path('article/<slug:slug>/', views.article_by_slug, name='article_by_slug'),
```

## Exercice 4 - Shortcuts : get_object_or_404

**Utilisez** les shortcuts Django :

```python
from django.shortcuts import get_object_or_404, get_list_or_404

def article_detail_safe(request, article_id):
    article = get_object_or_404(Article, id=article_id, publie=True)
    return HttpResponse(f"<h1>{article.titre}</h1><p>{article.contenu}</p>")

def articles_par_auteur(request, auteur_id):
    articles = get_list_or_404(Article, auteur_id=auteur_id, publie=True)
    html = "<h1>Articles</h1><ul>"
    for article in articles:
        html += f"<li>{article.titre}</li>"
    html += "</ul>"
    return HttpResponse(html)
```

## Exercice 5 - Redirections

**Créez** des vues avec redirections :

```python
from django.shortcuts import redirect
from django.urls import reverse

def ancien_article(request, article_id):
    # Redirection vers la nouvelle URL
    return redirect('blog:article_detail', article_id=article_id)

def redirect_to_home(request):
    return redirect('blog:home')

def redirect_externe(request):
    return redirect('https://www.djangoproject.com/')
```

## Exercice 6 - Requêtes HTTP (GET/POST)

**Gérez** les paramètres GET et POST :

```python
def search(request):
    query = request.GET.get('q', '')
    if query:
        articles = Article.objects.filter(titre__icontains=query)
        html = f"<h1>Résultats pour '{query}'</h1><ul>"
        for article in articles:
            html += f"<li>{article.titre}</li>"
        html += "</ul>"
    else:
        html = "<h1>Aucune recherche</h1>"
    return HttpResponse(html)

def contact_form(request):
    if request.method == 'POST':
        nom = request.POST.get('nom')
        message = request.POST.get('message')
        return HttpResponse(f"Message de {nom} reçu : {message}")
    return HttpResponse("Envoyez un message via POST")
```

## Exercice 7 - Class-Based Views (ListView)

**Créez** des vues basées sur des classes :

```python
from django.views.generic import ListView

class ArticleListView(ListView):
    model = Article
    template_name = 'blog/article_list.html'
    context_object_name = 'articles'
    queryset = Article.publies.all()
    paginate_by = 10
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['titre_page'] = "Tous les articles"
        return context
```

**URL** :

```python
from .views import ArticleListView

path('articles/', ArticleListView.as_view(), name='article_list'),
```

## Exercice 8 - Class-Based Views (DetailView)

**Détail d'un article** :

```python
from django.views.generic import DetailView

class ArticleDetailView(DetailView):
    model = Article
    template_name = 'blog/article_detail.html'
    context_object_name = 'article'
    
    def get_queryset(self):
        return Article.publies.all()
```

**URL** :

```python
path('article/<int:pk>/', ArticleDetailView.as_view(), name='article_detail_cbv'),
```

## Exercice 9 - Class-Based Views (CreateView)

**Création d'un article** :

```python
from django.views.generic import CreateView
from django.urls import reverse_lazy

class ArticleCreateView(CreateView):
    model = Article
    fields = ['titre', 'contenu', 'auteur', 'tags']
    template_name = 'blog/article_form.html'
    success_url = reverse_lazy('blog:article_list')
    
    def form_valid(self, form):
        form.instance.publie = False  # Par défaut non publié
        return super().form_valid(form)
```

## Exercice 10 - Class-Based Views (UpdateView)

**Modification d'un article** :

```python
from django.views.generic import UpdateView

class ArticleUpdateView(UpdateView):
    model = Article
    fields = ['titre', 'contenu', 'tags', 'publie']
    template_name = 'blog/article_form.html'
    
    def get_success_url(self):
        return reverse_lazy('blog:article_detail', kwargs={'pk': self.object.pk})
```

## Exercice 11 - Class-Based Views (DeleteView)

**Suppression d'un article** :

```python
from django.views.generic import DeleteView

class ArticleDeleteView(DeleteView):
    model = Article
    template_name = 'blog/article_confirm_delete.html'
    success_url = reverse_lazy('blog:article_list')
```

## Exercice 12 - Mixins personnalisés

**Créez** des mixins réutilisables :

```python
from django.contrib.auth.mixins import LoginRequiredMixin

class ArticleMixin:
    model = Article
    success_url = reverse_lazy('blog:article_list')

class PublishedArticlesMixin:
    def get_queryset(self):
        return Article.publies.all()

class ArticleListView(PublishedArticlesMixin, ListView):
    model = Article
    template_name = 'blog/article_list.html'
    context_object_name = 'articles'
```

## Exercice 13 - URLs nommées et namespaces

**Organisez** les URLs avec namespaces :

Dans `blog/urls.py` :

```python
app_name = 'blog'

urlpatterns = [
    path('', views.home, name='home'),
    path('articles/', ArticleListView.as_view(), name='article_list'),
    path('article/<int:pk>/', ArticleDetailView.as_view(), name='article_detail'),
    path('article/nouveau/', ArticleCreateView.as_view(), name='article_create'),
    path('article/<int:pk>/modifier/', ArticleUpdateView.as_view(), name='article_update'),
    path('article/<int:pk>/supprimer/', ArticleDeleteView.as_view(), name='article_delete'),
]
```

**Utilisation dans les vues** :

```python
# Avec reverse
from django.urls import reverse
url = reverse('blog:article_detail', kwargs={'pk': 1})

# Avec redirect
return redirect('blog:article_list')
```

## Exercice 14 - Include d'URLs

**Organisez** les URLs par fonctionnalité :

Créez `blog/urls/articles.py` :

```python
from django.urls import path
from .. import views

urlpatterns = [
    path('', views.ArticleListView.as_view(), name='list'),
    path('<int:pk>/', views.ArticleDetailView.as_view(), name='detail'),
    path('nouveau/', views.ArticleCreateView.as_view(), name='create'),
]
```

Dans `blog/urls.py` :

```python
from django.urls import path, include

app_name = 'blog'

urlpatterns = [
    path('articles/', include('blog.urls.articles')),
]
```

## Exercice 15 - Pagination manuelle

**Ajoutez** la pagination dans une FBV :

```python
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

def article_list_paginated(request):
    article_list = Article.publies.all()
    paginator = Paginator(article_list, 5)  # 5 articles par page
    
    page = request.GET.get('page')
    try:
        articles = paginator.page(page)
    except PageNotAnInteger:
        articles = paginator.page(1)
    except EmptyPage:
        articles = paginator.page(paginator.num_pages)
    
    return render(request, 'blog/article_list.html', {'articles': articles})
```

## Exercices bonus

### Exercice 16 - TemplateView
**Créez** une page statique avec `TemplateView`.

### Exercice 17 - FormView
**Créez** une vue de formulaire de contact avec `FormView`.

### Exercice 18 - API JSON simple
**Créez** une vue qui retourne tous les articles au format JSON.

## Checklist de validation

- ✅ FBV créées et fonctionnelles
- ✅ URLs avec paramètres configurées
- ✅ Redirections implémentées
- ✅ Class-Based Views maîtrisées (ListView, DetailView, CreateView, UpdateView, DeleteView)
- ✅ Mixins utilisés pour réutilisation
- ✅ Namespaces et URLs nommées configurées
- ✅ Pagination implémentée
- ✅ Requêtes GET/POST gérées
