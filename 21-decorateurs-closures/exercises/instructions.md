# Instructions - Décorateurs et Closures

Les décorateurs et closures sont des concepts puissants de Python permettant de modifier le comportement de fonctions de manière élégante.

## Partie 1 - Closures

### Exercice 1 - Closure factory

**Objectif** : Créer une factory qui génère des validateurs personnalisés.

**Hints** :
- La factory prend des paramètres de configuration (min, max)
- Elle retourne une fonction de validation qui utilise ces paramètres
- Chaque validateur créé a ses propres limites

**À faire** :
1. Créez `creer_validateur(min_val, max_val)`
2. Retournez une fonction qui vérifie `min_val <= valeur <= max_val`
3. Créez des validateurs spécialisés : `valider_age(0, 120)`, `valider_note(0, 20)`

**Cas d'usage** : Validation de formulaires, configuration dynamique.

## Partie 2 - Décorateurs de base

### Exercice 2 - Premier décorateur

**Objectif** : Créer un décorateur simple qui encapsule l'exécution d'une fonction.

**Hints** :
- Un décorateur est une fonction qui prend une fonction en paramètre
- Il retourne une nouvelle fonction (wrapper) qui encapsule l'originale
- `@decorateur` est syntaxe équivalente à `fonction = decorateur(fonction)`
- Utilisez `*args, **kwargs` pour accepter n'importe quels arguments

**Structure** :
```python
def mon_decorateur(func):
    def wrapper(*args, **kwargs):
        # Avant l'appel
        result = func(*args, **kwargs)  # Appel de la fonction originale
        # Après l'appel
        return result
    return wrapper
```

**À faire** :
1. Affichez "Avant l'appel" avant d'exécuter la fonction
2. Affichez "Après l'appel" après l'exécution
3. N'oubliez pas de retourner le résultat !

### Exercice 3 - Décorateur de timing

**Objectif** : Mesurer le temps d'exécution d'une fonction.

**Hints** :
- Utilisez `time.time()` pour obtenir le timestamp actuel
- Calculez la différence entre le temps de fin et de début
- `@wraps(func)` de `functools` préserve les métadonnées de la fonction originale
- Affichez le temps en secondes avec 4 décimales

**À faire** :
1. Importez `time` et `functools.wraps`
2. Enregistrez `start = time.time()` avant l'appel
3. Enregistrez `end = time.time()` après l'appel
4. Affichez `f"{func.__name__} a pris {end - start:.4f}s"`

**Question** : Pourquoi utiliser `@wraps` ?

### Exercice 4 - Décorateur de logging

**Objectif** : Logger les appels de fonction avec leurs arguments et résultats.

**Hints** :
- Affichez les informations avant ET après l'exécution
- Capturez le résultat pour pouvoir l'afficher et le retourner
- Utilisez des f-strings pour formater le message

**Format attendu** :
```
Appel de fonction_nom avec args=(1, 2), kwargs={'key': 'value'}
fonction_nom a retourné resultat
```

## Partie 3 - Décorateurs avec paramètres

### Exercice 5 - Décorateur paramétré

**Objectif** : Créer un décorateur qui accepte des paramètres.

**Hints** :
- Un décorateur paramétré a **3 niveaux de fonctions** :
  1. Fonction qui prend les paramètres → retourne le décorateur
  2. Décorateur qui prend la fonction → retourne le wrapper
  3. Wrapper qui exécute la fonction

**Structure** :
```python
def repeat(times):          # 1. Prend les paramètres
    def decorator(func):     # 2. Prend la fonction
        @wraps(func)
        def wrapper(*args, **kwargs):  # 3. Exécute
            # Votre code ici
        return wrapper
    return decorator
```

**À faire** :
1. Exécutez la fonction `times` fois
2. Stockez les résultats dans une liste
3. Retournez la liste des résultats

### Exercice 6 - Décorateur de retry

**Objectif** : Réessayer automatiquement une fonction en cas d'échec.

**Hints** :
- Utilisez une boucle `for attempt in range(max_attempts)`
- Encapsulez l'appel dans un `try/except`
- Si c'est la dernière tentative, laissez l'exception se propager avec `raise`
- Sinon, affichez un message et attendez avec `time.sleep(delay)`
- Si succès, retournez immédiatement avec `return`

**À faire** :
1. Créez `retry(max_attempts=3, delay=1)` avec 3 niveaux
2. Gérez les exceptions et les retentatives
3. Testez avec une fonction qui échoue aléatoirement

**Cas d'usage** : Appels réseau, opérations I/O.

## Partie 4 - Décorateurs de classe

### Exercice 7 - Décorateur de classe (Singleton)

**Objectif** : Implémenter le pattern Singleton avec un décorateur.

**Hints** :
- Le pattern Singleton garantit qu'une classe n'a qu'une seule instance
- Utilisez un dictionnaire `instances = {}` pour stocker les instances
- La clé est la classe elle-même : `instances[cls]`
- Vérifiez si l'instance existe avant d'en créer une nouvelle

**Structure** :
```python
def singleton(cls):
    instances = {}
    def get_instance(*args, **kwargs):
        if cls not in instances:
            # Créer et stocker l'instance
        return # L'instance
    return get_instance
```

**À tester** : `db1 = Database()` et `db2 = Database()` → `db1 is db2` doit être `True`

### Exercice 8 - Classe comme décorateur

**Objectif** : Utiliser une classe comme décorateur avec `__call__`.

**Hints** :
- Une classe peut être un décorateur en implémentant `__init__` et `__call__`
- `__init__(self, func)` : Reçoit la fonction à décorer
- `__call__(self, *args, **kwargs)` : Appelé quand on utilise la fonction
- Vous pouvez stocker un état dans `self`

**Structure** :
```python
class CountCalls:
    def __init__(self, func):
        # Initialiser func et count
    
    def __call__(self, *args, **kwargs):
        # Incrémenter count, afficher, appeler func
```

**Avantage** : Stockage d'état plus propre qu'avec une closure.

## Partie 5 - Chaînage de décorateurs

### Exercice 9 - Chaîner plusieurs décorateurs

**Objectif** : Comprendre l'ordre d'application des décorateurs empilés.

**Hints** :
- Les décorateurs s'appliquent de bas en haut (closest to function first)
- Mais s'exécutent de haut en bas à l'appel

**Exemple** :
```python
@uppercase       # 2. Appliqué en second
@exclamation     # 1. Appliqué en premier
def greet(name):
    return f"Hello, {name}"
```

**À faire** :
1. Créez `uppercase` : transforme le résultat en majuscules
2. Créez `exclamation` : ajoute "!" à la fin
3. Testez l'ordre : `greet("Alice")` → `"HELLO, ALICE!"`

**Question** : Que se passe-t-il si vous inversez l'ordre ?

## Partie 6 - Design Patterns avec décorateurs

### Exercice 10 - Pattern Observer

**Objectif** : Implémenter un système d'événements avec décorateurs.

**Hints** :
- L'EventManager stocke les subscribers dans un dictionnaire
- Clé = nom de l'événement, Valeur = liste de fonctions
- Le décorateur `subscribe` ajoute la fonction à la liste
- `trigger` appelle toutes les fonctions abonnées

**Structure** :
```python
class EventManager:
    def __init__(self):
        self.subscribers = {}
    
    def subscribe(self, event_name):
        # Décorateur qui ajoute func à self.subscribers[event_name]
    
    def trigger(self, event_name, *args, **kwargs):
        # Appelle toutes les fonctions abonnées
```

**Cas d'usage** : Systèmes d'événements, plugins, notifications.

## TP Final 1 - Pipeline de consommateurs de données

**Objectif** : Créer un pipeline qui applique plusieurs transformations à des données.

**Hints** :
- Créez un décorateur `pipeline(*decorators)` qui combine plusieurs décorateurs
- Appliquez-les dans l'ordre avec `reversed()` (car les décorateurs s'appliquent de bas en haut)
- Chaque consommateur transforme les données et passe le résultat au suivant

**Transformations à implémenter** :
1. `filter_even` : Garde seulement les nombres pairs
2. `multiply_by_two` : Multiplie chaque nombre par 2
3. `sum_all` : Somme tous les nombres

**Utilisation** :
```python
@pipeline(filter_even, multiply_by_two, sum_all)
def process_data(result):
    return result

data = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(process_data(data))  # Résultat attendu : 60
```

**Calcul** : [2,4,6,8,10] → [4,8,12,16,20] → sum = 60

## TP Final 2 - Système d'événements avec priorités

**Objectif** : Créer un système d'événements avancé avec priorités.

**Hints** :
- Stockez les handlers avec leur priorité : `(priority, func)`
- Triez par priorité décroissante : `sort(key=lambda x: x[0], reverse=True)`
- Les handlers avec priorité plus élevée s'exécutent en premier

**Structure** :
```python
class EventSystem:
    def on(self, event_name, priority=0):
        # Décorateur qui ajoute (priority, func) et trie
    
    def emit(self, event_name, *args, **kwargs):
        # Appelle les handlers dans l'ordre de priorité
```

**Exemple** :
- Priority 10 : Créer compte
- Priority 5 : Envoyer email
- Priority 1 : Logger

## TP Final 3 - Pipeline de générateurs

**Objectif** : Combiner décorateurs et générateurs pour un traitement lazy.

**Hints** :
- Un pipeline de générateurs ne charge pas toutes les données en mémoire
- Chaque étape est un générateur qui `yield` les éléments transformés
- Utilisez `for item in data: yield transform(item)`

**Étapes à implémenter** :
1. `filter_positives` : Ne yield que les nombres > 0
2. `square` : Yield le carré de chaque nombre
3. `limit(n)` : Yield seulement les n premiers éléments

**Structure** :
```python
def generator_pipeline(*steps):
    def decorator(generator):
        def wrapper(*args, **kwargs):
            data = generator(*args, **kwargs)
            # Appliquer chaque step au générateur
        return wrapper
    return decorator
```

**Avantage** : Traitement paresseux, économie de mémoire.

## Checklist de validation

-  Closures comprises et utilisées
-  Décorateurs simples créés
-  Décorateurs avec paramètres maîtrisés
-  Décorateurs de classe implémentés
-  Chaînage de décorateurs fonctionnel
-  Pattern Observer implémenté
-  TP pipeline de consommateurs réalisé
-  TP système d'événements avec priorités complet
-  Générateurs dans pipeline utilisés
