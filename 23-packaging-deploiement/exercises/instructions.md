# Instructions - Packaging et Déploiement

Ce module couvre la création, le packaging et la distribution de bibliothèques Python, ainsi que la gestion moderne des environnements avec **uv**.

## Partie 1 - Structure d'un package Python

### Exercice 1 - Créer la structure de base

**Créez** la structure suivante :

```
textanalyzer/
├── textanalyzer/
│   ├── __init__.py
│   ├── analyzer.py      # Module d'analyse de texte
│   └── entities.py      # Module d'extraction d'entités
├── tests/
│   ├── __init__.py
│   ├── test_analyzer.py
│   └── test_entities.py
├── README.md
├── LICENSE
└── pyproject.toml
```

**Créez** `textanalyzer/__init__.py` :

```python
"""
TextAnalyzer - Bibliothèque d'analyse de texte avec spaCy
"""

__version__ = '0.1.0'
__author__ = 'Votre Nom'

from .analyzer import analyze_text, get_tokens, get_pos_tags
from .entities import extract_entities, extract_persons, extract_locations

__all__ = [
    'analyze_text',
    'get_tokens', 
    'get_pos_tags',
    'extract_entities',
    'extract_persons',
    'extract_locations',
]
```

### Exercice 2 - Créer des modules

**Créez** `textanalyzer/analyzer.py` :

```python
"""Module d'analyse de texte avec spaCy"""

import spacy
from typing import List, Dict, Any

# Charger le modèle spaCy (français)
try:
    nlp = spacy.load("fr_core_news_sm")
except OSError:
    print("Modèle spaCy non trouvé. Installez-le avec: python -m spacy download fr_core_news_sm")
    nlp = None


def analyze_text(text: str) -> Dict[str, Any]:
    """
    Analyse complète d'un texte.
    
    Args:
        text: Le texte à analyser
        
    Returns:
        Dictionnaire avec tokens, lemmes, POS tags et dépendances
    """
    if nlp is None:
        raise RuntimeError("Modèle spaCy non chargé")
    
    doc = nlp(text)
    
    return {
        "tokens": [token.text for token in doc],
        "lemmas": [token.lemma_ for token in doc],
        "pos_tags": [token.pos_ for token in doc],
        "n_tokens": len(doc),
        "n_sentences": len(list(doc.sents)),
    }


def get_tokens(text: str) -> List[str]:
    """
    Extrait les tokens d'un texte.
    
    Args:
        text: Le texte à tokeniser
        
    Returns:
        Liste des tokens
    """
    if nlp is None:
        raise RuntimeError("Modèle spaCy non chargé")
    
    doc = nlp(text)
    return [token.text for token in doc]


def get_pos_tags(text: str) -> List[tuple[str, str]]:
    """
    Extrait les tokens avec leurs POS tags.
    
    Args:
        text: Le texte à analyser
        
    Returns:
        Liste de tuples (token, pos_tag)
    """
    if nlp is None:
        raise RuntimeError("Modèle spaCy non chargé")
    
    doc = nlp(text)
    return [(token.text, token.pos_) for token in doc]
```

**Créez** `textanalyzer/entities.py` :

```python
"""Module d'extraction d'entités nommées"""

import spacy
from typing import List, Dict

# Charger le modèle spaCy (français)
try:
    nlp = spacy.load("fr_core_news_sm")
except OSError:
    print("Modèle spaCy non trouvé. Installez-le avec: python -m spacy download fr_core_news_sm")
    nlp = None


def extract_entities(text: str) -> List[Dict[str, str]]:
    """
    Extrait toutes les entités nommées d'un texte.
    
    Args:
        text: Le texte à analyser
        
    Returns:
        Liste de dictionnaires avec les entités et leurs types
    """
    if nlp is None:
        raise RuntimeError("Modèle spaCy non chargé")
    
    doc = nlp(text)
    
    return [
        {
            "text": ent.text,
            "label": ent.label_,
            "start": ent.start_char,
            "end": ent.end_char,
        }
        for ent in doc.ents
    ]


def extract_persons(text: str) -> List[str]:
    """
    Extrait les noms de personnes d'un texte.
    
    Args:
        text: Le texte à analyser
        
    Returns:
        Liste des noms de personnes trouvés
    """
    if nlp is None:
        raise RuntimeError("Modèle spaCy non chargé")
    
    doc = nlp(text)
    return [ent.text for ent in doc.ents if ent.label_ == "PER"]


def extract_locations(text: str) -> List[str]:
    """
    Extrait les noms de lieux d'un texte.
    
    Args:
        text: Le texte à analyser
        
    Returns:
        Liste des lieux trouvés
    """
    if nlp is None:
        raise RuntimeError("Modèle spaCy non chargé")
    
    doc = nlp(text)
    return [ent.text for ent in doc.ents if ent.label_ == "LOC"]
```

## Partie 2 - Configuration avec pyproject.toml

### Exercice 3 - Créer pyproject.toml

**Créez** `pyproject.toml` :

```toml
[build-system]
requires = ["setuptools>=68.0", "wheel"]
build-backend = "setuptools.build_meta"

[project]
name = "textanalyzer"
version = "0.1.0"
description = "Bibliothèque d'analyse de texte avec spaCy"
readme = "README.md"
requires-python = ">=3.10"
license = {text = "MIT"}
authors = [
    {name = "Votre Nom", email = "votre.email@example.com"}
]
classifiers = [
    "Programming Language :: Python :: 3",
    "Programming Language :: Python :: 3.10",
    "Programming Language :: Python :: 3.11",
    "Programming Language :: Python :: 3.12",
    "License :: OSI Approved :: MIT License",
    "Operating System :: OS Independent",
    "Topic :: Text Processing :: Linguistic",
]
dependencies = [
    "spacy>=3.7.0",
]

[project.optional-dependencies]
dev = [
    "pytest>=7.4.0",
    "pytest-cov>=4.1.0",
    "black>=23.0.0",
    "ruff>=0.1.0",
    "mypy>=1.5.0",
]

[project.urls]
Homepage = "https://github.com/votrenom/textanalyzer"
Documentation = "https://textanalyzer.readthedocs.io"
Repository = "https://github.com/votrenom/textanalyzer"
Issues = "https://github.com/votrenom/textanalyzer/issues"

[tool.black]
line-length = 88
target-version = ['py310', 'py311', 'py312']

[tool.ruff]
line-length = 88
target-version = "py310"
select = ["E", "F", "I", "N", "W", "UP"]

[tool.mypy]
python_version = "3.10"
warn_return_any = true
warn_unused_configs = true
disallow_untyped_defs = true

[tool.pytest.ini_options]
testpaths = ["tests"]
python_files = ["test_*.py"]
python_classes = ["Test*"]
python_functions = ["test_*"]
addopts = "-v --cov=textanalyzer --cov-report=term-missing"
```

### Exercice 4 - Installer en mode développement

**Créez** un environnement virtuel et installez votre package :

```bash
# Créer un environnement virtuel
uv venv

# Activer l'environnement
source .venv/bin/activate  # Mac/Linux
# .venv\Scripts\activate  # Windows

# En mode développement (editable)
uv pip install -e .
```

**Testez** l'import :

```python
import textanalyzer
print(textanalyzer.__version__)
from textanalyzer import analyze_text, extract_entities
```

**Installez** le modèle spaCy français :

```bash
# Télécharger le modèle français de spaCy
python -m spacy download fr_core_news_sm
```

**Testez** le package :

```python
from textanalyzer import analyze_text, extract_entities

# Analyser un texte
text = "Emmanuel Macron est à Paris pour rencontrer des dirigeants."
result = analyze_text(text)
print(result)

# Extraire les entités
entities = extract_entities(text)
print(entities)
```

**Installez** les dépendances de développement :

```bash
# Installer toutes les dépendances incluant dev
uv pip install -e ".[dev]"

# Ou ajouter des dépendances avec uv
uv add spacy
uv add --dev pytest pytest-cov black ruff mypy
```

**Utilisez** les outils de développement :

```bash
# Formater le code avec black
uv run black textanalyzer/

# Linter avec ruff
uv run ruff check textanalyzer/

# Type checking avec mypy
uv run mypy textanalyzer/

# Lancer les tests
uv run pytest

# Avec coverage
uv run pytest --cov=textanalyzer --cov-report=html
```

## Partie 3 - Outils de qualité et tests

### Les outils de qualité modernes

Le `pyproject.toml` inclut 4 outils essentiels :

1. **pytest** + **pytest-cov** : Framework de tests et mesure de couverture
2. **black** : Formatage automatique du code (opinionated)
3. **ruff** : Linter ultra-rapide (remplace flake8, isort, etc.)
4. **mypy** : Vérification de types statiques

Ces outils sont configurés dans les sections `[tool.*]` du `pyproject.toml`.

### Exercice 5 - Créer des tests

**Créez** `tests/test_analyzer.py` :

```python
import pytest
from textanalyzer.analyzer import get_tokens, analyze_text


def test_get_tokens():
    """Test de la tokenization"""
    text = "Bonjour le monde"
    tokens = get_tokens(text)
    assert len(tokens) == 3
    assert tokens[0] == "Bonjour"


def test_analyze_text():
    """Test de l'analyse complète"""
    text = "Python est génial."
    result = analyze_text(text)
    
    assert "tokens" in result
    assert "lemmas" in result
    assert "pos_tags" in result
    assert result["n_tokens"] > 0
    assert result["n_sentences"] == 1


def test_analyze_empty_text():
    """Test avec texte vide"""
    result = analyze_text("")
    assert result["n_tokens"] == 0
```

**Créez** `tests/test_entities.py` :

```python
import pytest
from textanalyzer.entities import extract_entities, extract_persons, extract_locations


def test_extract_entities():
    """Test de l'extraction d'entités"""
    text = "Emmanuel Macron habite à Paris."
    entities = extract_entities(text)
    
    assert len(entities) > 0
    assert all("text" in ent for ent in entities)
    assert all("label" in ent for ent in entities)


def test_extract_persons():
    """Test de l'extraction de personnes"""
    text = "Marie et Pierre sont à Lyon."
    persons = extract_persons(text)
    
    # Le résultat peut varier selon le modèle
    assert isinstance(persons, list)


def test_extract_locations():
    """Test de l'extraction de lieux"""
    text = "Paris et Lyon sont en France."
    locations = extract_locations(text)
    
    assert isinstance(locations, list)


def test_no_entities():
    """Test sans entités"""
    text = "Le chat mange."
    entities = extract_entities(text)
    assert isinstance(entities, list)
```

**Exécutez** les tests et outils de qualité :

```bash
# Exécuter les tests
uv run pytest

# Avec coverage
uv run pytest --cov=textanalyzer --cov-report=html

# Formater le code
uv run black textanalyzer/ tests/

# Linter avec ruff (plus rapide que flake8)
uv run ruff check textanalyzer/ tests/

# Réparer automatiquement les erreurs ruff
uv run ruff check --fix textanalyzer/

# Type checking avec mypy
uv run mypy textanalyzer/

# Pipeline complet de qualité
uv run black . && uv run ruff check . && uv run mypy textanalyzer/ && uv run pytest --cov
```

## Partie 4 - Gestion d'environnements avec uv

### Exercice 6 - Installer uv

**Installez** uv (gestionnaire de packages ultra-rapide) :

```bash
# Mac/Linux
curl -LsSf https://astral.sh/uv/install.sh | sh

# Ou avec pip
pip install uv
```

**Vérifiez** l'installation :

```bash
uv --version
```

### Exercice 7 - Créer et gérer un environnement virtuel

**Créez** un environnement virtuel :

```bash
# Créer un venv avec uv
uv venv

# Avec une version Python spécifique
uv venv --python 3.11

# Avec un nom personnalisé
uv venv mon-env
```

**Activez** l'environnement :

```bash
# Mac/Linux
source .venv/bin/activate

# Windows
.venv\Scripts\activate
```

**Installez** des packages :

```bash
# Installer un package (ultra-rapide !)
uv pip install requests

# Installer plusieurs packages
uv pip install requests numpy pandas

# Installer en mode éditable (développement)
uv pip install -e .

# Avec extras
uv pip install -e ".[dev]"
```

### Exercice 8 - Gérer les dépendances avec pyproject.toml et uv

**Toutes les dépendances sont dans pyproject.toml** :

```bash
# Ajouter une dépendance (modifie automatiquement pyproject.toml)
uv add requests

# Ajouter avec contrainte de version
uv add "numpy>=1.20,<2.0"

# Ajouter une dépendance de développement
uv add --dev pytest black

# Retirer une dépendance
uv remove requests
```

**Synchroniser l'environnement** :

```bash
# Installer toutes les dépendances depuis pyproject.toml
uv sync

# Installer uniquement les dépendances de production
uv sync --no-dev
```

**Commandes utiles** :

```bash
# Lister les packages installés
uv pip list

# Afficher les infos d'un package
uv pip show requests

# Mettre à jour toutes les dépendances
uv lock --upgrade

# Mettre à jour une dépendance spécifique
uv add --upgrade requests
```

### Exercice 9 - Créer un projet avec uv init

**Initialisez** un nouveau projet :

```bash
# Créer un nouveau projet
uv init mon-projet
cd mon-projet
```

Structure créée :

```
mon-projet/
├── .venv/           # Environnement virtuel (créé automatiquement)
├── .python-version  # Version Python
├── pyproject.toml   # Configuration du projet
├── README.md
└── hello.py         # Script exemple
```

**Le pyproject.toml généré** :

```toml
[project]
name = "mon-projet"
version = "0.1.0"
description = "Add your description here"
readme = "README.md"
requires-python = ">=3.10"
dependencies = []

[build-system]
requires = ["hatchling"]
build-backend = "hatchling.build"
```

**Ajoutez** des dépendances :

```bash
# Ajouter des dépendances de production
uv add requests
uv add "numpy>=1.20,<2.0"

# Ajouter toutes les dépendances de développement
uv add --dev pytest pytest-cov black ruff mypy

# Le pyproject.toml sera automatiquement mis à jour
```

**Après ajout des dépendances dev, votre pyproject.toml contiendra** :

```toml
[project.optional-dependencies]
dev = [
    "pytest>=7.4.0",
    "pytest-cov>=4.1.0",
    "black>=23.0.0",
    "ruff>=0.1.0",
    "mypy>=1.5.0",
]
```

**Exécutez** votre code et les outils de qualité :

```bash
# Exécuter un script avec l'environnement activé
uv run python hello.py

# Formater le code
uv run black .

# Vérifier le code avec ruff
uv run ruff check .

# Type checking
uv run mypy .

# Exécuter les tests
uv run pytest

# Tests avec coverage
uv run pytest --cov

# Chaîner les commandes (format + lint + test)
uv run black . && uv run ruff check . && uv run pytest
```

## Partie 5 - Distribution sur PyPI

### Exercice 10 - Préparer la distribution

**Créez** les fichiers nécessaires :

**README.md** :

```markdown
# TextAnalyzer 📝

Bibliothèque Python d'analyse de texte utilisant spaCy pour le traitement du langage naturel.

## Fonctionnalités

- 🔤 Tokenization et lemmatisation
- 🏷️ POS tagging (Part-of-Speech)
- 👤 Extraction d'entités nommées (personnes, lieux, organisations)
- 📊 Analyse statistique de texte

## Installation

```bash
pip install textanalyzer
```

Installez le modèle spaCy français :

```bash
python -m spacy download fr_core_news_sm
```

## Utilisation

### Analyse de texte

```python
from textanalyzer import analyze_text

text = "Emmanuel Macron est le président de la France."
result = analyze_text(text)

print(result)
# {
#     'tokens': ['Emmanuel', 'Macron', 'est', 'le', 'président', ...],
#     'lemmas': ['Emmanuel', 'Macron', 'être', 'le', 'président', ...],
#     'pos_tags': ['PROPN', 'PROPN', 'AUX', 'DET', 'NOUN', ...],
#     'n_tokens': 9,
#     'n_sentences': 1
# }
```

### Extraction d'entités

```python
from textanalyzer import extract_entities, extract_persons, extract_locations

text = "Marie habite à Paris et travaille à Lyon."

# Toutes les entités
entities = extract_entities(text)

# Seulement les personnes
persons = extract_persons(text)  # ['Marie']

# Seulement les lieux
locations = extract_locations(text)  # ['Paris', 'Lyon']
```

### Tokenization simple

```python
from textanalyzer import get_tokens, get_pos_tags

text = "Python est un langage de programmation."

tokens = get_tokens(text)
# ['Python', 'est', 'un', 'langage', 'de', 'programmation', '.']

pos_tags = get_pos_tags(text)
# [('Python', 'PROPN'), ('est', 'AUX'), ...]
```

## Développement

```bash
# Cloner le repo
git clone https://github.com/votrenom/textanalyzer
cd textanalyzer

# Créer l'environnement
uv venv
source .venv/bin/activate

# Installer en mode dev
uv pip install -e ".[dev]"

# Lancer les tests
uv run pytest

# Formater le code
uv run black .

# Linter
uv run ruff check .
```

## Licence

MIT
```

**LICENSE** (MIT) :

```
MIT License

Copyright (c) 2024 Votre Nom

Permission is hereby granted, free of charge, to any person obtaining a copy...
```

### Exercice 11 - Construire les distributions

**Installez** les outils avec uv :

```bash
uv pip install build twine
```

**Construisez** :

```bash
# Nettoyer les anciens builds
rm -rf dist/ build/ *.egg-info

# Construire avec uv
uv run python -m build

# Vérifier les distributions
uv run twine check dist/*
```

### Exercice 12 - Test sur TestPyPI

**1. Créez** un compte sur https://test.pypi.org/

**2. Générez** un token API sur https://test.pypi.org/manage/account/token/

**3. Ajoutez** le token TestPyPI dans `~/.pypirc` (section `[testpypi]`)

**4. Uploadez** :

```bash
# Uploader sur TestPyPI
uv run twine upload --repository testpypi dist/*

# Tester l'installation dans un nouvel environnement
uv pip install --index-url https://test.pypi.org/simple/ textanalyzer

# Télécharger le modèle spaCy
python -m spacy download fr_core_news_sm
```

## TP Final - Publier sur PyPI

### Prérequis

**1. Créez un compte sur https://pypi.org/**

**2. Générez un token API :**

- Allez sur https://pypi.org/manage/account/token/
- Cliquez sur "Add API token"
- Nom du token : "textanalyzer-upload" (ou autre)
- Scope : "Entire account" (pour le premier upload) ou "Project: textanalyzer" (si le projet existe déjà)
- Copiez le token (il commence par `pypi-AgE...`)
- ⚠️ **Important** : Sauvegardez-le immédiatement, il ne sera plus visible !

**3. Configurez l'authentification**

**Créez** `~/.pypirc` :

```ini
[pypi]
username = __token__
password = pypi-AgExxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx

[testpypi]
username = __token__
password = pypi-AgExxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx
```

> **Note** : Remplacez les `xxx` par votre vrai token PyPI

### Checklist avant publication

Avant de publier, vérifiez :

- [ ] Tous les tests passent (`uv run pytest`)
- [ ] Code formaté (`uv run black .`)
- [ ] Pas d'erreurs de linting (`uv run ruff check .`)
- [ ] Version correcte dans `pyproject.toml`
- [ ] README.md complet et à jour
- [ ] LICENSE présent
- [ ] Build vérifié (`uv run twine check dist/*`)
- [ ] Testé sur TestPyPI (optionnel mais recommandé)

### Publier

```bash
# Uploader sur PyPI réel
uv run twine upload dist/*
```

**Répondez aux questions** :
- Enter your username: (appuyez sur Entrée, le username est déjà dans .pypirc)
- Enter your password: (appuyez sur Entrée, le token est déjà dans .pypirc)

✅ **Votre package est maintenant public sur PyPI !**

### Vérifier

```bash
# Créer un nouvel environnement pour tester
uv venv test-env
source test-env/bin/activate

# Installer depuis PyPI
uv pip install textanalyzer

# Tester
python -c "import textanalyzer; print(textanalyzer.__version__)"
```

### Erreurs courantes et solutions

**Erreur : "The user 'xxx' isn't allowed to upload to project 'textanalyzer'"**
- Le nom est déjà pris sur PyPI
- Solution : Changez le nom dans `pyproject.toml` (ex: `textanalyzer-votreprenom`)

**Erreur : "File already exists"**
- Vous avez déjà uploadé cette version
- Solution : Incrémentez la version dans `pyproject.toml` (ex: 0.1.0 → 0.1.1)

**Erreur : "Invalid or non-existent authentication"**
- Token incorrect ou expiré
- Solution : Vérifiez le token dans `~/.pypirc` ou générez-en un nouveau

**Erreur : "HTTPError: 403 Forbidden"**
- Pas les permissions pour ce projet
- Solution : Utilisez un token avec le bon scope (Entire account pour le premier upload)

## Partie 6 - Configuration avancée

### Exercice 13 - Entry points

**Ajoutez** des scripts CLI dans `pyproject.toml` :

```toml
[project.scripts]
textanalyzer = "textanalyzer.cli:main"
analyze = "textanalyzer.cli:analyze_cli"
```

**Créez** `textanalyzer/cli.py` :

```python
"""Interface en ligne de commande pour TextAnalyzer"""
import sys
from .analyzer import analyze_text
from .entities import extract_entities


def main():
    """Point d'entrée principal"""
    print("TextAnalyzer - Analyse de texte avec spaCy")
    print("Usage: textanalyzer")
    print("       analyze 'votre texte'")


def analyze_cli():
    """Analyser un texte depuis la ligne de commande"""
    if len(sys.argv) < 2:
        print("Usage: analyze 'votre texte'")
        sys.exit(1)
    
    text = " ".join(sys.argv[1:])
    
    # Analyse
    result = analyze_text(text)
    print(f"\n📊 Analyse de texte:")
    print(f"  Tokens: {result['n_tokens']}")
    print(f"  Phrases: {result['n_sentences']}")
    
    # Entités
    entities = extract_entities(text)
    if entities:
        print(f"\n👤 Entités trouvées:")
        for ent in entities:
            print(f"  - {ent['text']} ({ent['label']})")


if __name__ == '__main__':
    analyze_cli()
```

**Installez** et testez :

```bash
# Installer en mode éditable
uv pip install -e .

# Exécuter les commandes
textanalyzer

analyze "Emmanuel Macron est à Paris."
```

### Exercice 14 - Données de package

**Incluez** des fichiers de données dans `pyproject.toml` :

```toml
[tool.setuptools.package-data]
textanalyzer = ["data/*.json", "templates/*.html"]
```

**Ou utilisez MANIFEST.in** pour plus de contrôle :

```
include README.md
include LICENSE
recursive-include textanalyzer/data *
recursive-include textanalyzer/templates *
```

**Structure recommandée** :

```
textanalyzer/
├── textanalyzer/
│   ├── __init__.py
│   ├── data/
│   │   └── config.json
│   └── templates/
│       └── template.html
└── pyproject.toml
```

### Exercice 15 - Versioning automatique

**Avec setuptools_scm dans pyproject.toml** :

```bash
uv add --dev setuptools-scm
```

**Modifiez** `pyproject.toml` :

```toml
[build-system]
requires = ["setuptools>=64", "setuptools_scm>=8"]
build-backend = "setuptools.build_meta"

[tool.setuptools_scm]
# Version automatiquement déterminée depuis Git tags
```

**Créez** un tag Git :

```bash
git tag v0.1.0
git push --tags
```

La version sera automatiquement déterminée depuis les tags Git.

## Partie 7 - Buildout (optionnel)

### Exercice 16 - Configurer Buildout

**Créez** `buildout.cfg` :

```ini
[buildout]
parts = python

[python]
recipe = zc.recipe.egg
eggs = 
    requests
    numpy
interpreter = python
```

**Utilisez** :

```bash
uv pip install zc.buildout
buildout
./bin/python  # Python avec packages installés
```

## Checklist de validation

-  Structure de package créée
-  ✅ **pyproject.toml** comme unique source de configuration
-  ❌ Pas de setup.py (approche moderne)
-  ❌ Pas de requirements.txt (tout dans pyproject.toml)
-  **Outils de qualité configurés** :
   -  ✅ pytest + pytest-cov pour les tests
   -  ✅ black pour le formatage
   -  ✅ ruff pour le linting (remplace flake8)
   -  ✅ mypy pour le type checking
-  Tests écrits et exécutés avec `uv run pytest`
-  Code formaté avec `uv run black`
-  Code linté avec `uv run ruff check`
-  Types vérifiés avec `uv run mypy`
-  uv installé et environnement virtuel créé
-  Gestion des dépendances avec `uv add` et `uv sync`
-  `uv init` et `uv add --dev` maîtrisés
-  Pipeline de qualité complet (black + ruff + mypy + pytest)
-  Package construit avec `uv run python -m build`
-  Uploadé sur TestPyPI
-  **TP : Publié sur PyPI réel**
-  Entry points configurés dans pyproject.toml
-  Documentation README complète
-  Versioning automatique avec setuptools_scm
