# Écrivez votre code ici !
# Consultez le fichier instructions.md pour les consignes

"""
Ce fichier contient des exemples pour créer un package Python.

Pour créer un vrai package, suivez cette structure :

mon_package/
├── mon_package/
│   ├── __init__.py
│   ├── module1.py
│   └── module2.py
├── tests/
│   ├── __init__.py
│   └── test_module1.py
├── README.md
├── LICENSE
├── setup.py (ou pyproject.toml)
└── requirements.txt
"""

# ============= EXEMPLE DE STRUCTURE DE PACKAGE =============

# Contenu de mon_package/__init__.py :
"""
# __init__.py
__version__ = '0.1.0'
__author__ = 'Votre Nom'

from .module1 import fonction1
from .module2 import fonction2

__all__ = ['fonction1', 'fonction2']
"""

# Contenu de mon_package/module1.py :
"""
# module1.py
def fonction1(x):
    '''Retourne le carré de x'''
    return x ** 2
"""

# Contenu de mon_package/module2.py :
"""
# module2.py
def fonction2(x, y):
    '''Additionne deux nombres'''
    return x + y
"""

# ============= SETUP.PY (MÉTHODE CLASSIQUE) =============

setup_py_content = """
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
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.8',
    install_requires=[
        'requests>=2.25.0',
    ],
    extras_require={
        'dev': [
            'pytest>=6.0',
            'black>=21.0',
        ],
    },
)
"""

# ============= PYPROJECT.TOML (MÉTHODE MODERNE) =============

pyproject_toml_content = """
[build-system]
requires = ["setuptools>=45", "wheel"]
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
dependencies = [
    "requests>=2.25.0",
]

[project.optional-dependencies]
dev = [
    "pytest>=6.0",
    "black>=21.0",
]
"""

# ============= TESTS =============

test_content = """
# tests/test_module1.py
import pytest
from mon_package.module1 import fonction1

def test_fonction1():
    assert fonction1(2) == 4
    assert fonction1(3) == 9
    assert fonction1(0) == 0
"""

# ============= CLI AVEC ENTRY POINTS =============

cli_content = """
# mon_package/cli.py
import argparse

def main():
    parser = argparse.ArgumentParser(description='Mon CLI')
    parser.add_argument('name', help='Votre nom')
    parser.add_argument('--greeting', default='Hello', help='Message de salutation')
    
    args = parser.parse_args()
    print(f"{args.greeting}, {args.name}!")

if __name__ == '__main__':
    main()
"""

# Dans setup.py, ajoutez :
"""
setup(
    # ... autres paramètres ...
    entry_points={
        'console_scripts': [
            'mon-commande=mon_package.cli:main',
        ],
    },
)
"""

# ============= COMMANDES UTILES =============

def print_commandes():
    """Affiche les commandes utiles pour le packaging"""
    
    print("=== Commandes pour le packaging Python ===\n")
    
    print("1. Créer un environnement virtuel :")
    print("   python -m venv venv")
    print("   source venv/bin/activate  # Mac/Linux")
    print("   venv\\Scripts\\activate    # Windows\n")
    
    print("2. Installer en mode développement :")
    print("   pip install -e .")
    print("   pip install -e \".[dev]\"  # Avec dépendances dev\n")
    
    print("3. Exécuter les tests :")
    print("   pytest")
    print("   pytest --cov=mon_package\n")
    
    print("4. Construire le package :")
    print("   pip install build")
    print("   python -m build\n")
    
    print("5. Vérifier les distributions :")
    print("   pip install twine")
    print("   twine check dist/*\n")
    
    print("6. Uploader sur TestPyPI :")
    print("   twine upload --repository testpypi dist/*\n")
    
    print("7. Uploader sur PyPI :")
    print("   twine upload dist/*\n")
    
    print("8. Avec Poetry (moderne) :")
    print("   poetry new mon-projet")
    print("   poetry add requests")
    print("   poetry add --group dev pytest")
    print("   poetry install")
    print("   poetry build")
    print("   poetry publish\n")


# ============= EXEMPLE COMPLET DE PACKAGE =============

class ExemplePackage:
    """
    Exemple d'un package complet avec toutes les bonnes pratiques
    """
    
    def __init__(self, name="mon-package"):
        self.name = name
        self.version = "0.1.0"
    
    def afficher_structure(self):
        """Affiche la structure recommandée"""
        structure = """
        mon-package/
        ├── mon_package/              # Code source
        │   ├── __init__.py          # Initialisation du package
        │   ├── module1.py           # Modules
        │   ├── module2.py
        │   └── cli.py               # CLI (optionnel)
        ├── tests/                    # Tests
        │   ├── __init__.py
        │   ├── test_module1.py
        │   └── test_module2.py
        ├── docs/                     # Documentation (optionnel)
        │   └── index.md
        ├── .gitignore               # Fichiers à ignorer
        ├── README.md                # Documentation principale
        ├── LICENSE                  # Licence (MIT, GPL, etc.)
        ├── setup.py                 # Configuration (classique)
        ├── pyproject.toml           # Configuration (moderne)
        ├── requirements.txt         # Dépendances
        └── MANIFEST.in              # Fichiers à inclure
        """
        print(structure)
    
    def afficher_gitignore(self):
        """Affiche un .gitignore recommandé"""
        gitignore = """
        # Python
        __pycache__/
        *.py[cod]
        *$py.class
        *.so
        .Python
        
        # Distribution / packaging
        dist/
        build/
        *.egg-info/
        
        # Virtual environment
        venv/
        env/
        ENV/
        
        # IDE
        .vscode/
        .idea/
        *.swp
        
        # Tests
        .pytest_cache/
        .coverage
        htmlcov/
        """
        print(gitignore)


# ============= TESTS =============

if __name__ == "__main__":
    print("=== Guide de Packaging Python ===\n")
    
    # Afficher les commandes
    print_commandes()
    
    # Afficher la structure
    print("\n=== Structure recommandée ===")
    exemple = ExemplePackage()
    exemple.afficher_structure()
    
    print("\n=== .gitignore recommandé ===")
    exemple.afficher_gitignore()
    
    print("\n=== Contenu des fichiers ===")
    print("\n--- setup.py ---")
    print(setup_py_content)
    
    print("\n--- pyproject.toml ---")
    print(pyproject_toml_content)
    
    print("\n--- tests/test_module1.py ---")
    print(test_content)
    
    print("\n--- mon_package/cli.py ---")
    print(cli_content)
    
    print("\n" + "="*50)
    print("Consultez instructions.md pour les exercices détaillés !")
