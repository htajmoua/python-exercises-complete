# Instructions - Packaging et Déploiement

Ce module couvre la création, le packaging et la distribution de bibliothèques Python, ainsi que la gestion des environnements.

## Partie 1 - Structure d'un package Python

### Exercice 1 - Créer la structure de base

**Créez** la structure suivante :

```
mon_package/
├── mon_package/
│   ├── __init__.py
│   ├── module1.py
│   └── module2.py
├── tests/
│   ├── __init__.py
│   ├── test_module1.py
│   └── test_module2.py
├── README.md
├── LICENSE
├── setup.py
└── requirements.txt
```

**Créez** `mon_package/__init__.py` :

```python
"""
Mon Package - Une bibliothèque exemple
"""

__version__ = '0.1.0'
__author__ = 'Votre Nom'

from .module1 import fonction1
from .module2 import fonction2

__all__ = ['fonction1', 'fonction2']
```

### Exercice 2 - Créer des modules

**Créez** `mon_package/module1.py` :

```python
"""Module 1 de mon package"""

def fonction1(x):
    """Retourne le carré de x"""
    return x ** 2

def helper_function():
    """Fonction helper privée"""
    pass
```

**Créez** `mon_package/module2.py` :

```python
"""Module 2 de mon package"""

def fonction2(x, y):
    """Additionne deux nombres"""
    return x + y
```

## Partie 2 - Setup.py (méthode classique)

### Exercice 3 - Créer setup.py

**Créez** `setup.py` :

```python
from setuptools import setup, find_packages

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setup(
    name="mon-package",
    version="0.1.0",
    author="Votre Nom",
    author_email="votre.email@example.com",
    description="Un package Python exemple",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/votrenom/mon-package",
    packages=find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.8',
    install_requires=[
        'requests>=2.25.0',
        'numpy>=1.19.0',
    ],
    extras_require={
        'dev': [
            'pytest>=6.0',
            'black>=21.0',
            'flake8>=3.9',
        ],
    },
)
```

### Exercice 4 - Installer en mode développement

**Installez** votre package :

```bash
# En mode développement (editable)
pip install -e .

# Avec dépendances de développement
pip install -e ".[dev]"
```

**Testez** l'import :

```python
import mon_package
print(mon_package.__version__)
from mon_package import fonction1, fonction2
```

## Partie 3 - Pyproject.toml (méthode moderne)

### Exercice 5 - Créer pyproject.toml

**Créez** `pyproject.toml` :

```toml
[build-system]
requires = ["setuptools>=45", "wheel", "setuptools_scm[toml]>=6.2"]
build-backend = "setuptools.build_meta"

[project]
name = "mon-package"
version = "0.1.0"
description = "Un package Python exemple"
readme = "README.md"
requires-python = ">=3.8"
license = {text = "MIT"}
authors = [
    {name = "Votre Nom", email = "votre.email@example.com"}
]
classifiers = [
    "Programming Language :: Python :: 3",
    "License :: OSI Approved :: MIT License",
    "Operating System :: OS Independent",
]
dependencies = [
    "requests>=2.25.0",
    "numpy>=1.19.0",
]

[project.optional-dependencies]
dev = [
    "pytest>=6.0",
    "black>=21.0",
    "flake8>=3.9",
]

[project.urls]
Homepage = "https://github.com/votrenom/mon-package"
Documentation = "https://mon-package.readthedocs.io"
Repository = "https://github.com/votrenom/mon-package"
```

## Partie 4 - Tests

### Exercice 6 - Créer des tests

**Créez** `tests/test_module1.py` :

```python
import pytest
from mon_package.module1 import fonction1

def test_fonction1():
    assert fonction1(2) == 4
    assert fonction1(3) == 9
    assert fonction1(0) == 0

def test_fonction1_negatif():
    assert fonction1(-2) == 4
```

**Exécutez** les tests :

```bash
pytest
pytest --cov=mon_package  # Avec coverage
```

## Partie 5 - Virtualenv et environnements

### Exercice 7 - Créer un virtualenv

**Avec venv** (Python 3.3+) :

```bash
# Créer
python -m venv venv

# Activer
# Mac/Linux :
source venv/bin/activate
# Windows :
venv\Scripts\activate

# Installer des packages
pip install requests numpy

# Sauvegarder les dépendances
pip freeze > requirements.txt

# Désactiver
deactivate
```

### Exercice 8 - Poetry (outil moderne)

**Installez** Poetry :

```bash
curl -sSL https://install.python-poetry.org | python3 -
```

**Créez** un projet avec Poetry :

```bash
poetry new mon-projet
cd mon-projet
```

Structure créée :

```
mon-projet/
├── mon_projet/
│   └── __init__.py
├── tests/
│   └── __init__.py
├── pyproject.toml
└── README.md
```

**Gérez** les dépendances :

```bash
# Ajouter une dépendance
poetry add requests

# Ajouter une dépendance de développement
poetry add --group dev pytest

# Installer toutes les dépendances
poetry install

# Activer l'environnement virtuel
poetry shell

# Exécuter une commande
poetry run python mon_script.py

# Construire le package
poetry build

# Publier sur PyPI
poetry publish
```

### Exercice 9 - Pipenv

**Installez** Pipenv :

```bash
pip install pipenv
```

**Utilisez** Pipenv :

```bash
# Créer un environnement et installer un package
pipenv install requests

# Installer en mode dev
pipenv install --dev pytest

# Activer l'environnement
pipenv shell

# Exécuter une commande
pipenv run python script.py

# Générer requirements.txt
pipenv requirements > requirements.txt
```

## Partie 6 - Distribution sur PyPI

### Exercice 10 - Préparer la distribution

**Créez** les fichiers nécessaires :

**README.md** :

```markdown
# Mon Package

Description de votre package.

## Installation

```bash
pip install mon-package
```

## Utilisation

```python
from mon_package import fonction1
resultat = fonction1(5)
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

**Installez** les outils :

```bash
pip install build twine
```

**Construisez** :

```bash
# Nettoyer les anciens builds
rm -rf dist/ build/ *.egg-info

# Construire
python -m build

# Vérifier les distributions
twine check dist/*
```

### Exercice 12 - Test sur TestPyPI

**Créez** un compte sur https://test.pypi.org/

**Uploadez** :

```bash
# Uploader sur TestPyPI
twine upload --repository testpypi dist/*

# Tester l'installation
pip install --index-url https://test.pypi.org/simple/ mon-package
```

## TP Final - Publier sur PyPI

### Prérequis

1. Créez un compte sur https://pypi.org/
2. Configurez l'authentification

**Créez** `~/.pypirc` :

```ini
[pypi]
username = __token__
password = pypi-AgE...votre-token...
```

### Publier

```bash
# Uploader sur PyPI réel
twine upload dist/*
```

### Vérifier

```bash
# Installer depuis PyPI
pip install mon-package

# Tester
python -c "import mon_package; print(mon_package.__version__)"
```

## Partie 7 - Configuration avancée

### Exercice 13 - Entry points

**Ajoutez** des scripts CLI dans `setup.py` :

```python
setup(
    # ... autres paramètres ...
    entry_points={
        'console_scripts': [
            'mon-commande=mon_package.cli:main',
        ],
    },
)
```

**Créez** `mon_package/cli.py` :

```python
def main():
    print("Hello depuis mon CLI!")

if __name__ == '__main__':
    main()
```

Après installation, vous pouvez exécuter :

```bash
mon-commande
```

### Exercice 14 - Données de package

**Incluez** des fichiers de données :

**setup.py** :

```python
setup(
    # ...
    package_data={
        'mon_package': ['data/*.json', 'templates/*.html'],
    },
    include_package_data=True,
)
```

**MANIFEST.in** :

```
include README.md
include LICENSE
recursive-include mon_package/data *
recursive-include mon_package/templates *
```

### Exercice 15 - Versioning automatique

**Avec setuptools_scm** :

```bash
pip install setuptools_scm
```

**setup.py** :

```python
from setuptools import setup

setup(
    use_scm_version=True,
    setup_requires=['setuptools_scm'],
    # ...
)
```

La version sera automatiquement déterminée depuis Git tags.

## Partie 8 - Buildout (optionnel)

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
pip install zc.buildout
buildout
./bin/python  # Python avec packages installés
```

## Checklist de validation

- ✅ Structure de package créée
- ✅ setup.py configuré
- ✅ pyproject.toml créé (moderne)
- ✅ Tests écrits et exécutés
- ✅ Virtualenv maîtrisé
- ✅ Poetry ou Pipenv utilisé
- ✅ Package construit (wheel + sdist)
- ✅ Uploadé sur TestPyPI
- ✅ **TP : Publié sur PyPI réel**
- ✅ Entry points configurés
- ✅ Documentation README complète
