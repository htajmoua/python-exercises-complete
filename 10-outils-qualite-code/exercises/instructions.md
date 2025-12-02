# Module 10 - Outils de Qualité de Code Python

## 🎯 Objectifs

Apprendre à utiliser les outils essentiels pour maintenir un code Python de qualité :
- **Black** : Formatage automatique du code
- **Ruff** : Linter ultra-rapide (remplace Flake8, isort, etc.)
- **Mypy** : Vérification de types statique
- **Pytest** : Framework de tests
- **ipdb** : Débogueur interactif

**Temps estimé :** 40-50 minutes

---

## 📦 Installation des outils

```bash
# Installer tous les outils en une fois
pip install black ruff mypy pytest ipdb
```

**Vérification de l'installation :**
```bash
black --version
ruff --version
mypy --version
pytest --version
```

---

## Partie 1 : Black - Formatage automatique

### Exercice 1 : Formater du code avec Black

Black reformate automatiquement votre code selon le style PEP 8.

**1. Examinez le fichier `code_mal_formate.py`**

Ce fichier contient du code fonctionnel mais mal formaté.

**2. Vérifiez ce que Black va changer (mode dry-run) :**
```bash
black --check code_mal_formate.py
```

**3. Formatez le fichier :**
```bash
black code_mal_formate.py
```

**4. Observez les changements**

Black a :
- Ajusté les espaces
- Normalisé les quotes (simple → double)
- Formaté les listes et dictionnaires
- Limité les lignes à 88 caractères

💡 **Conseil :** Intégrez Black dans votre éditeur pour un formatage automatique à la sauvegarde.

---

## Partie 2 : Ruff - Linting ultra-rapide

### Exercice 2 : Détecter les problèmes avec Ruff

Ruff détecte les erreurs, mauvaises pratiques et code non utilisé.

**1. Analysez le fichier `code_avec_problemes.py` :**
```bash
ruff check code_avec_problemes.py
```

**2. Corrigez automatiquement ce qui peut l'être :**
```bash
ruff check --fix code_avec_problemes.py
```

**3. Analysez les erreurs restantes**

Ruff détecte :
- Variables non utilisées
- Imports inutiles
- Code mort (unreachable)
- Violations de style
- Problèmes de sécurité potentiels

**4. Corrigez manuellement les erreurs restantes**

Consultez la documentation des codes d'erreur : https://docs.astral.sh/ruff/rules/

---

## Partie 3 : Mypy - Vérification de types

### Exercice 3 : Ajouter et vérifier les types

Mypy vérifie que vous utilisez correctement les types en Python.

**1. Examinez `calculatrice.py` (sans types)**

**2. Ajoutez des annotations de types :**
```python
def addition(a: int, b: int) -> int:
    return a + b

def division(a: float, b: float) -> float:
    if b == 0:
        raise ValueError("Division par zéro")
    return a / b
```

**3. Vérifiez avec Mypy :**
```bash
mypy calculatrice.py
```

**4. Testez avec du code incorrect :**
```python
# Dans test_types.py
from calculatrice import addition

result = addition("5", "10")  # Erreur : str au lieu de int
```

```bash
mypy test_types.py
# Erreur: Argument 1 to "addition" has incompatible type "str"; expected "int"
```

**5. Corrigez les erreurs de types**

---

## Partie 4 : Pytest - Tests automatisés

### Exercice 4 : Écrire et exécuter des tests

**1. Examinez `test_calculatrice.py`**

Structure d'un test pytest :
```python
def test_addition():
    assert addition(2, 3) == 5
    assert addition(-1, 1) == 0
```

**2. Exécutez les tests :**
```bash
pytest
```

**3. Exécutez avec plus de détails :**
```bash
pytest -v  # Verbose
pytest -vv # Très verbose
```

**4. Testez la couverture de code :**
```bash
pip install pytest-cov
pytest --cov=calculatrice
```

**5. Ajoutez des tests pour les cas limites :**
- Division par zéro
- Nombres négatifs
- Nombres à virgule
- Très grands nombres

---

## Partie 5 : ipdb - Débogage interactif

### Exercice 5 : Déboguer avec ipdb

**1. Installation :**
```bash
pip install ipdb
```

**2. Points d'arrêt dans le code**

Utilisez `breakpoint()` pour définir un point d'arrêt :
```python
def test_operations():
    a = 10
    b = 5
    breakpoint()  # Le débogueur s'arrête ici
    resultat = addition(a, b)
    return resultat
```

**Exécutez le fichier de test avec ipdb :**
```bash
# Configurer ipdb comme débogueur par défaut
export PYTHONBREAKPOINT=ipdb.set_trace

# Lancer le test
python test_debug.py
```

Le débogueur s'arrête au `breakpoint()`. Vous pouvez alors :
- Inspecter les variables : `p a`, `p b`
- Avancer ligne par ligne : `n`
- Continuer l'exécution : `c`

**Commandes de base :**
- `n` (next) : Ligne suivante
- `s` (step) : Entrer dans une fonction
- `c` (continue) : Continuer jusqu'au prochain point d'arrêt
- `l` (list) : Voir le code autour
- `p variable` : Afficher la valeur d'une variable
- `q` (quit) : Quitter

**3. Analyse post-mortem**

L'analyse post-mortem permet d'inspecter l'état du programme au moment d'une erreur.

Dans `test_debug.py`, décommentez la fonction `test_erreur()` :
```python
def test_erreur():
    try:
        resultat = division(10, 0)  # Division par zéro
    except Exception as e:
        print(f"Erreur capturée: {e}")
        import ipdb; ipdb.post_mortem()  # Analyse post-mortem
        raise
```

Puis exécutez :
```bash
python test_debug.py
```

Quand l'erreur survient, ipdb vous place dans le contexte exact où elle s'est produite. Vous pouvez :
- Examiner les variables locales
- Remonter la pile d'appels avec `u` (up) et `d` (down)
- Comprendre la cause de l'erreur

💡 **Conseil :** Utilisez ipdb pour comprendre le flux d'exécution et identifier rapidement les bugs.

---

## Comparaison des outils

| Outil | Fonction | Temps | Corrige auto |
|-------|----------|-------|--------------|
| **Black** | Formatage | Très rapide | Oui |
| **Ruff** | Linting | Ultra-rapide | Partiel |
| **Mypy** | Types | Rapide | Non |
| **Pytest** | Tests | Variable | Non |
| **ipdb** | Débogage | Interactif | Non |

---

## 🚀 Workflow recommandé

```bash
# 1. Formatter le code
black .

# 2. Vérifier le linting
ruff check --fix .

# 3. Vérifier les types
mypy .

# 4. Exécuter les tests
pytest

# 5. Vérifier la couverture
pytest --cov=calculatrice
```

---

## ✅ Checklist finale

- [ ] Black installé et utilisé
- [ ] Code formaté automatiquement
- [ ] Ruff détecte les problèmes
- [ ] Corrections automatiques appliquées
- [ ] Mypy configuré
- [ ] Types ajoutés aux fonctions principales
- [ ] Pytest installé
- [ ] Tests écrits et qui passent
- [ ] Couverture de code mesurée
- [ ] ipdb maîtrisé pour le débogage

---

## Ressources

### Documentation officielle
- [Black](https://black.readthedocs.io/)
- [Ruff](https://docs.astral.sh/ruff/)
- [Mypy](https://mypy.readthedocs.io/)
- [Pytest](https://docs.pytest.org/)
- [ipdb](https://github.com/gotcha/ipdb)

### Guides et tutoriels
- [PEP 8 - Style Guide](https://peps.python.org/pep-0008/)
- [PEP 484 - Type Hints](https://peps.python.org/pep-0484/)
- [Real Python - Testing](https://realpython.com/pytest-python-testing/)

---

## Compétences acquises

Après ce module, vous savez :

- Formater automatiquement votre code avec Black  
- Détecter les erreurs et mauvaises pratiques avec Ruff  
- Ajouter et vérifier des types avec Mypy  
- Écrire et exécuter des tests avec Pytest  
- Mesurer la couverture de code  
- Déboguer interactivement avec ipdb  
- Utiliser un workflow de développement professionnel  

**Ces outils sont indispensables pour tout projet Python professionnel ! 🚀**
