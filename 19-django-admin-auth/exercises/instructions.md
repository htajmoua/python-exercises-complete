# Instructions - Django Admin et Authentification

Le Django Admin est une interface d'administration automatique. L'authentification gère les utilisateurs, permissions et sessions.

## Partie 1 - Django Admin

### Exercice 1 - Enregistrer les modèles

**Modifiez** `blog/admin.py` :

```python
from django.contrib import admin
from .models import Article, Auteur, Tag, Commentaire

admin.site.register(Article)
admin.site.register(Auteur)
admin.site.register(Tag)
admin.site.register(Commentaire)
```

**Accédez** à `/admin/` et explorez l'interface.

### Exercice 2 - ModelAdmin basique

**Personnalisez** l'affichage :

```python
@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):
    list_display = ['titre', 'auteur', 'publie', 'date_creation']
    list_filter = ['publie', 'date_creation', 'auteur']
    search_fields = ['titre', 'contenu']
    date_hierarchy = 'date_creation'
```

### Exercice 3 - Admin avancé

**Ajoutez** plus de fonctionnalités :

```python
@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):
    list_display = ['titre', 'auteur', 'publie', 'date_creation', 'nombre_commentaires']
    list_filter = ['publie', 'date_creation', 'auteur', 'tags']
    search_fields = ['titre', 'contenu', 'auteur__nom']
    prepopulated_fields = {'slug': ('titre',)}
    filter_horizontal = ['tags']
    list_editable = ['publie']
    list_per_page = 20
    
    fieldsets = (
        ('Informations principales', {
            'fields': ('titre', 'slug', 'auteur')
        }),
        ('Contenu', {
            'fields': ('contenu', 'tags')
        }),
        ('Métadonnées', {
            'fields': ('publie', 'date_creation'),
            'classes': ('collapse',)
        }),
    )
    
    def nombre_commentaires(self, obj):
        return obj.commentaires.count()
    nombre_commentaires.short_description = 'Commentaires'
```

### Exercice 4 - Inline admin

**Affichez** les commentaires dans l'admin d'Article :

```python
class CommentaireInline(admin.TabularInline):
    model = Commentaire
    extra = 1
    fields = ['auteur_nom', 'contenu', 'approuve']
    readonly_fields = ['date_creation']

@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):
    inlines = [CommentaireInline]
    # ... autres options ...
```

### Exercice 5 - Actions personnalisées

**Créez** des actions en masse :

```python
@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):
    actions = ['publier_articles', 'depublier_articles']
    
    def publier_articles(self, request, queryset):
        count = queryset.update(publie=True)
        self.message_user(request, f'{count} articles ont été publiés.')
    publier_articles.short_description = "Publier les articles sélectionnés"
    
    def depublier_articles(self, request, queryset):
        count = queryset.update(publie=False)
        self.message_user(request, f'{count} articles ont été dépubliés.')
    depublier_articles.short_description = "Dépublier les articles sélectionnés"
```

### Exercice 6 - Personnalisation visuelle

**Modifiez** l'apparence de l'admin :

```python
# Dans urls.py principal
admin.site.site_header = "Administration de Mon Blog"
admin.site.site_title = "Admin Mon Blog"
admin.site.index_title = "Bienvenue dans l'administration"
```

## Partie 2 - Authentification

### Exercice 7 - Vue de login

**Créez** `accounts/urls.py` :

```python
from django.urls import path
from django.contrib.auth import views as auth_views

app_name = 'accounts'

urlpatterns = [
    path('login/', auth_views.LoginView.as_view(template_name='accounts/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
]
```

**Template** `accounts/templates/accounts/login.html` :

```html
{% extends 'blog/base.html' %}

{% block content %}
    <h2>Connexion</h2>
    <form method="post">
        {% csrf_token %}
        {{ form.as_p }}
        <button type="submit">Se connecter</button>
    </form>
    <p>Pas encore de compte ? <a href="{% url 'accounts:register' %}">S'inscrire</a></p>
{% endblock %}
```

**Configurez** `settings.py` :

```python
LOGIN_REDIRECT_URL = 'blog:home'
LOGOUT_REDIRECT_URL = 'blog:home'
LOGIN_URL = 'accounts:login'
```

### Exercice 8 - Vue de register

**Créez** `accounts/forms.py` :

```python
from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

class UserRegisterForm(UserCreationForm):
    email = forms.EmailField(required=True)
    
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']
```

**Vue** dans `accounts/views.py` :

```python
from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import UserRegisterForm

def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'Compte créé pour {username}!')
            return redirect('accounts:login')
    else:
        form = UserRegisterForm()
    return render(request, 'accounts/register.html', {'form': form})
```

### Exercice 9 - Protéger les vues

**Avec décorateur** :

```python
from django.contrib.auth.decorators import login_required

@login_required
def article_create(request):
    # ... code de la vue ...
```

**Avec mixin (CBV)** :

```python
from django.contrib.auth.mixins import LoginRequiredMixin

class ArticleCreateView(LoginRequiredMixin, CreateView):
    model = Article
    # ...
```

### Exercice 10 - Permissions

**Créez** des permissions personnalisées dans `models.py` :

```python
class Article(models.Model):
    # ... champs ...
    
    class Meta:
        permissions = [
            ("can_publish", "Peut publier des articles"),
            ("can_feature", "Peut mettre en avant des articles"),
        ]
```

**Utilisez-les** :

```python
from django.contrib.auth.decorators import permission_required

@permission_required('blog.can_publish')
def publier_article(request, article_id):
    article = get_object_or_404(Article, id=article_id)
    article.publie = True
    article.save()
    return redirect('blog:article_detail', pk=article_id)
```

### Exercice 11 - Groupes d'utilisateurs

**Dans une vue ou le shell** :

```python
from django.contrib.auth.models import Group, Permission
from django.contrib.contenttypes.models import ContentType
from blog.models import Article

# Créer des groupes
editeurs = Group.objects.create(name='Éditeurs')
auteurs = Group.objects.create(name='Auteurs')

# Ajouter des permissions
content_type = ContentType.objects.get_for_model(Article)
permission = Permission.objects.get(
    codename='can_publish',
    content_type=content_type,
)
editeurs.permissions.add(permission)

# Ajouter un utilisateur à un groupe
user.groups.add(editeurs)
```

### Exercice 12 - Profil utilisateur

**Créez** un modèle `Profil` :

```python
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver

class Profil(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    bio = models.TextField(blank=True)
    photo = models.ImageField(upload_to='profiles/', blank=True)
    site_web = models.URLField(blank=True)
    
    def __str__(self):
        return f'Profil de {self.user.username}'

@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        Profil.objects.create(user=instance)

@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
    instance.profil.save()
```

### Exercice 13 - Vues de mot de passe

**Ajoutez** dans `accounts/urls.py` :

```python
urlpatterns = [
    # ... URLs existantes ...
    path('password-reset/', 
         auth_views.PasswordResetView.as_view(template_name='accounts/password_reset.html'),
         name='password_reset'),
    path('password-reset/done/', 
         auth_views.PasswordResetDoneView.as_view(template_name='accounts/password_reset_done.html'),
         name='password_reset_done'),
    path('password-reset-confirm/<uidb64>/<token>/', 
         auth_views.PasswordResetConfirmView.as_view(template_name='accounts/password_reset_confirm.html'),
         name='password_reset_confirm'),
    path('password-reset-complete/', 
         auth_views.PasswordResetCompleteView.as_view(template_name='accounts/password_reset_complete.html'),
         name='password_reset_complete'),
]
```

## Exercices bonus

### Exercice 14 - Custom User Model
**Créez** un modèle User personnalisé.

### Exercice 15 - Social Auth
**Intégrez** l'authentification via Google/Facebook avec `django-allauth`.

## Checklist de validation

-  Admin personnalisé pour tous les modèles
-  Inlines configurés
-  Actions personnalisées créées
-  Login/Logout/Register fonctionnels
-  Vues protégées avec @login_required
-  Permissions et groupes utilisés
-  Profil utilisateur créé
-  Reset de mot de passe implémenté
