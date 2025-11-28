# Instructions - Django Forms et Validation

Les formulaires Django permettent de gérer la saisie utilisateur, la validation et la sécurité (CSRF).

## Exercice 1 - Form basique

**Créez** `blog/forms.py` :

```python
from django import forms

class ContactForm(forms.Form):
    nom = forms.CharField(max_length=100, label="Votre nom")
    email = forms.EmailField(label="Votre email")
    sujet = forms.CharField(max_length=200)
    message = forms.CharField(widget=forms.Textarea, label="Votre message")
```

**Vue** :

```python
from .forms import ContactForm

def contact(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            # Traitement des données
            nom = form.cleaned_data['nom']
            email = form.cleaned_data['email']
            messages.success(request, 'Message envoyé!')
            return redirect('blog:home')
    else:
        form = ContactForm()
    
    return render(request, 'blog/contact.html', {'form': form})
```

**Template** `contact.html` :

```html
{% extends 'blog/base.html' %}

{% block content %}
    <h2>Contactez-nous</h2>
    <form method="post">
        {% csrf_token %}
        {{ form.as_p }}
        <button type="submit">Envoyer</button>
    </form>
{% endblock %}
```

## Exercice 2 - ModelForm

**Créez** un ModelForm pour Article :

```python
from django import forms
from .models import Article

class ArticleForm(forms.ModelForm):
    class Meta:
        model = Article
        fields = ['titre', 'contenu', 'auteur', 'tags', 'publie']
        widgets = {
            'contenu': forms.Textarea(attrs={'rows': 10}),
            'tags': forms.CheckboxSelectMultiple(),
        }
        labels = {
            'publie': 'Publier immédiatement',
        }
```

## Exercice 3 - Validation personnalisée

**Ajoutez** des validateurs au Form :

```python
from django.core.exceptions import ValidationError

class ArticleForm(forms.ModelForm):
    class Meta:
        model = Article
        fields = ['titre', 'contenu', 'auteur', 'tags', 'publie']
    
    def clean_titre(self):
        titre = self.cleaned_data.get('titre')
        if len(titre) < 10:
            raise ValidationError("Le titre doit contenir au moins 10 caractères")
        if Article.objects.filter(titre=titre).exists():
            raise ValidationError("Ce titre existe déjà")
        return titre
    
    def clean_contenu(self):
        contenu = self.cleaned_data.get('contenu')
        if len(contenu.split()) < 50:
            raise ValidationError("L'article doit contenir au moins 50 mots")
        return contenu
    
    def clean(self):
        cleaned_data = super().clean()
        titre = cleaned_data.get('titre')
        contenu = cleaned_data.get('contenu')
        
        if titre and contenu and titre.lower() in contenu.lower():
            raise ValidationError("Le titre ne doit pas apparaître dans le contenu")
        
        return cleaned_data
```

## Exercice 4 - Widgets personnalisés

**Personnalisez** l'apparence des champs :

```python
class ArticleForm(forms.ModelForm):
    class Meta:
        model = Article
        fields = ['titre', 'contenu', 'auteur', 'tags']
        widgets = {
            'titre': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Entrez le titre',
            }),
            'contenu': forms.Textarea(attrs={
                'class': 'form-control',
                'rows': 15,
                'placeholder': 'Rédigez votre article...',
            }),
            'auteur': forms.Select(attrs={'class': 'form-select'}),
            'tags': forms.CheckboxSelectMultiple(attrs={'class': 'form-check-input'}),
        }
```

## Exercice 5 - Formulaire avec fichiers

**Ajoutez** un champ image au modèle Article :

```python
class Article(models.Model):
    # ... champs existants ...
    image = models.ImageField(upload_to='articles/', blank=True, null=True)
```

**Installez** Pillow :

```bash
pip install Pillow
```

**Form** :

```python
class ArticleForm(forms.ModelForm):
    class Meta:
        model = Article
        fields = ['titre', 'contenu', 'image', 'auteur']
```

**Vue** :

```python
def article_create(request):
    if request.method == 'POST':
        form = ArticleForm(request.POST, request.FILES)  # Ajoutez request.FILES
        if form.is_valid():
            form.save()
            return redirect('blog:article_list')
    else:
        form = ArticleForm()
    return render(request, 'blog/article_form.html', {'form': form})
```

**Template** :

```html
<form method="post" enctype="multipart/form-data">
    {% csrf_token %}
    {{ form.as_p }}
    <button type="submit">Sauvegarder</button>
</form>
```

## Exercice 6 - Formsets

**Créez** un formset pour gérer plusieurs commentaires :

```python
from django.forms import modelformset_factory
from .models import Commentaire

CommentaireFormSet = modelformset_factory(
    Commentaire,
    fields=['auteur_nom', 'email', 'contenu'],
    extra=3,  # 3 formulaires vides supplémentaires
    can_delete=True
)
```

**Vue** :

```python
def manage_commentaires(request, article_id):
    article = get_object_or_404(Article, id=article_id)
    
    if request.method == 'POST':
        formset = CommentaireFormSet(request.POST, queryset=article.commentaires.all())
        if formset.is_valid():
            instances = formset.save(commit=False)
            for instance in instances:
                instance.article = article
                instance.save()
            formset.save_m2m()
            return redirect('blog:article_detail', pk=article_id)
    else:
        formset = CommentaireFormSet(queryset=article.commentaires.all())
    
    return render(request, 'blog/manage_commentaires.html', {
        'formset': formset,
        'article': article
    })
```

## Exercice 7 - Inline Formsets

**Créez** un inline formset :

```python
from django.forms import inlineformset_factory

CommentaireInlineFormSet = inlineformset_factory(
    Article,
    Commentaire,
    fields=['auteur_nom', 'email', 'contenu'],
    extra=2,
    can_delete=True
)
```

## Exercice 8 - Form rendering manuel

**Personnalisez** complètement le rendu :

```html
<form method="post">
    {% csrf_token %}
    
    <div class="form-group">
        <label for="{{ form.titre.id_for_label }}">{{ form.titre.label }}</label>
        {{ form.titre }}
        {% if form.titre.errors %}
            <div class="errors">{{ form.titre.errors }}</div>
        {% endif %}
        <small>{{ form.titre.help_text }}</small>
    </div>
    
    <div class="form-group">
        <label>{{ form.contenu.label }}</label>
        {{ form.contenu }}
        {% if form.contenu.errors %}
            <div class="errors">{{ form.contenu.errors }}</div>
        {% endif %}
    </div>
    
    {% if form.non_field_errors %}
        <div class="alert alert-danger">
            {{ form.non_field_errors }}
        </div>
    {% endif %}
    
    <button type="submit">Soumettre</button>
</form>
```

## Exercice 9 - Form avec ChoiceField dynamique

**Créez** des choix dynamiques :

```python
class RechercheArticleForm(forms.Form):
    auteur = forms.ModelChoiceField(
        queryset=Auteur.objects.filter(est_actif=True),
        required=False,
        empty_label="Tous les auteurs"
    )
    tag = forms.ModelMultipleChoiceField(
        queryset=Tag.objects.all(),
        required=False,
        widget=forms.CheckboxSelectMultiple
    )
    date_debut = forms.DateField(required=False, widget=forms.DateInput(attrs={'type': 'date'}))
    date_fin = forms.DateField(required=False, widget=forms.DateInput(attrs={'type': 'date'}))
```

## Exercice 10 - Validation avec regex

**Utilisez** des validators :

```python
from django.core.validators import RegexValidator

class CommentaireForm(forms.ModelForm):
    telephone = forms.CharField(
        validators=[RegexValidator(
            regex=r'^\+?1?\d{9,15}$',
            message="Le numéro de téléphone doit être valide"
        )],
        required=False
    )
    
    class Meta:
        model = Commentaire
        fields = ['auteur_nom', 'email', 'contenu', 'telephone']
```

## Exercices bonus

### Exercice 11 - Form wizard
**Créez** un formulaire multi-étapes avec `django-formtools`.

### Exercice 12 - Autocomplete
**Implémentez** un champ autocomplete pour les tags.

### Exercice 13 - Captcha
**Ajoutez** un captcha avec `django-recaptcha`.

## Checklist de validation

- ✅ Forms et ModelForms créés
- ✅ Validation personnalisée implémentée
- ✅ Widgets personnalisés utilisés
- ✅ Upload de fichiers fonctionnel
- ✅ Formsets maîtrisés
- ✅ Rendu manuel de formulaires
- ✅ CSRF protection active
- ✅ Messages d'erreur affichés
