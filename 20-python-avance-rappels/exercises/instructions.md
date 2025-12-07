# Instructions - Python Avancé : Rappels et Fondamentaux

Ce module couvre les concepts fondamentaux avancés de Python souvent mal compris, avec un focus sur l'optimisation et la complexité algorithmique.

## Exercice 1 - Sets : Opérations et propriétés

**Objectif** : Maîtriser les sets (ensembles) et leurs opérations mathématiques.

**Hints** :

**Qu'est-ce qu'un set ?**
- Collection **non ordonnée** d'éléments **uniques**
- Très efficace pour tester l'appartenance : O(1) au lieu de O(n) pour les listes
- Supporte les opérations mathématiques d'ensembles
- **Important** : Les éléments doivent être hashables (immutables)

**Création** :
```python
# Différentes façons de créer un set
s1 = {1, 2, 3}
s2 = set([1, 2, 3, 3])  # Les doublons sont automatiquement éliminés
s3 = set()  # Set vide (attention : {} crée un dict vide !)
```

**Opérations ensemblistes** :
- `union` ou `|` : tous les éléments des deux sets
- `intersection` ou `&` : éléments communs
- `difference` ou `-` : éléments dans le premier mais pas le second
- `symmetric_difference` ou `^` : éléments dans l'un ou l'autre mais pas les deux
- `issubset`, `issuperset`, `isdisjoint` : tests de relations

**Expérimentez** :
1. Créez deux sets avec des éléments communs et différents
2. Testez toutes les opérations ensemblistes (union, intersection, différence)
3. Comparez la vitesse de recherche entre `element in liste` vs `element in set` avec `timeit`
4. Essayez d'ajouter un élément mutable (liste) à un set - que se passe-t-il ?

**Méthodes importantes** :
- `add(element)` : ajouter un élément
- `remove(element)` : supprimer (erreur si absent)
- `discard(element)` : supprimer (pas d'erreur si absent)
- `clear()` : vider le set

**Questions** :
- Pourquoi les sets ne peuvent-ils pas contenir de listes ?
- Quelle est la complexité temporelle de `element in set` ?
- Comment éliminer les doublons d'une liste rapidement ?

## Exercice 2 - Sets avancés : frozenset et cas d'usage

**Objectif** : Découvrir les frozensets et les applications pratiques des sets.

**Hints** :

**frozenset - Set immutable** :
- Version immutable d'un set
- Peut être utilisé comme clé de dictionnaire ou élément d'un autre set
- Ne peut pas être modifié après création
- Syntaxe : `frozenset([1, 2, 3])`

**Cas d'usage pratiques** :

**1. Éliminer les doublons** :
```python
liste_avec_doublons = [1, 2, 2, 3, 3, 3]
liste_unique = list(set(liste_avec_doublons))
```

**2. Tester l'appartenance rapidement** :
```python
# O(1) au lieu de O(n)
valeurs_valides = {1, 2, 3, 4, 5}
if user_input in valeurs_valides:  # Très rapide !
    # ...
```

**3. Trouver des éléments uniques/communs** :
```python
utilisateurs_actifs = {'alice', 'bob', 'charlie'}
utilisateurs_premium = {'bob', 'charlie', 'david'}
# Qui est actif ET premium ?
actifs_premium = utilisateurs_actifs & utilisateurs_premium
```

**4. Set de sets (avec frozenset)** :
```python
# Impossible : sets = {{1, 2}, {3, 4}}  # Erreur !
# Possible avec frozenset :
sets = {frozenset([1, 2]), frozenset([3, 4])}
```

**Expérimentez** :
1. Créez un frozenset et essayez de le modifier (vous aurez une erreur)
2. Utilisez un frozenset comme clé de dictionnaire
3. Créez une fonction `elements_uniques_plusieurs_listes(*listes)` qui retourne les éléments présents dans une seule liste
4. Implémentez une fonction de validation rapide avec un set de valeurs autorisées

**Questions** :
- Quand utiliser un set vs un frozenset ?
- Pourquoi un set normal ne peut-il pas être clé de dictionnaire ?
- Comment implémenter efficacement un système de tags/catégories ?

## Exercice 3 - Protocole d'itération et itérateurs

**Objectif** : Comprendre le protocole d'itération en Python et créer un itérateur personnalisé.

**Hints** :

**Protocole d'itération** :
- Un objet est **itérable** s'il implémente `__iter__()` qui retourne un itérateur
- Un objet est un **itérateur** s'il implémente `__iter__()` ET `__next__()`
- `__next__()` retourne le prochain élément ou lève `StopIteration` quand c'est fini
- La boucle `for` utilise ce protocole automatiquement

**Fonctions utiles** :
- `iter(objet)` : retourne un itérateur pour l'objet
- `next(iterateur)` : appelle `__next__()` sur l'itérateur

**Expérimentez** :
1. Créez une classe `CompteurIterateur` qui itère de `debut` à `fin`
2. Implémentez `__iter__()` qui retourne `self`
3. Implémentez `__next__()` qui incrémente et lève `StopIteration` quand fini
4. Testez avec une boucle `for`

**Exemple de structure** :
```python
class MonIterateur:
    def __init__(self, ...):
        # Initialiser les attributs
        pass
    
    def __iter__(self):
        # Retourner self
        pass
    
    def __next__(self):
        # Retourner le prochain élément ou lever StopIteration
        pass
```

**Question** : Quelle est la différence entre un itérable et un itérateur ?

## Exercice 4 - Générateurs avec yield

**Objectif** : Créer des générateurs avec `yield` pour une itération efficace en mémoire.

**Hints** :

**Générateurs** :
- Un générateur est une fonction qui contient `yield` au lieu de `return`
- `yield` **suspend** l'exécution et retourne une valeur, puis reprend où elle s'était arrêtée
- Les générateurs sont des itérateurs créés automatiquement (pas besoin de `__iter__` et `__next__`)
- **Lazy evaluation** : les valeurs sont générées à la demande, pas toutes en mémoire

**Avantages** :
- Économie de mémoire (ne stocke pas toute la séquence)
- Peut générer des séquences infinies
- Code plus simple qu'une classe itérateur

**Expérimentez** :
1. Créez un générateur `fibonacci(n)` qui génère les n premiers nombres de Fibonacci
2. Créez un générateur `lire_fichier_par_morceaux(fichier, taille)` qui lit un fichier par blocs
3. Créez un générateur `nombres_pairs(max)` qui génère tous les nombres pairs jusqu'à max

**Exemple de base** :
```python
def mon_generateur(n):
    i = 0
    while i < n:
        yield i
        i += 1
```

**Questions** :
- Pourquoi les générateurs sont-ils plus efficaces en mémoire que les listes ?
- Pouvez-vous itérer plusieurs fois sur un générateur ? Pourquoi ?

## Exercice 5 - Expressions génératrices et optimisation

**Objectif** : Maîtriser les expressions génératrices et comparer avec les list comprehensions.

**Hints** :

**Expression génératrice** :
- Syntaxe : `(expression for item in iterable if condition)`
- Similaire à list comprehension mais avec `()` au lieu de `[]`
- Retourne un générateur (lazy), pas une liste
- Utilise beaucoup moins de mémoire pour de grandes séquences

**Comparaison** :
```python
# List comprehension - crée toute la liste en mémoire
liste = [x**2 for x in range(1000000)]  # Beaucoup de mémoire !

# Expression génératrice - calcule à la demande
gen = (x**2 for x in range(1000000))    # Très peu de mémoire
```

**Fonctions qui acceptent des générateurs** :
- `sum()`, `min()`, `max()`, `any()`, `all()`
- Ces fonctions consomment le générateur élément par élément

**Expérimentez** :
1. Comparez la mémoire utilisée entre `[x**2 for x in range(1000000)]` et `(x**2 for x in range(1000000))`
2. Utilisez `sum()` avec une expression génératrice pour calculer la somme des carrés
3. Créez un pipeline : `sum(x**2 for x in range(100) if x % 2 == 0)`

**Pipeline de générateurs** :
```python
# Chaîner plusieurs générateurs
nombres = (x for x in range(100))
carres = (x**2 for x in nombres)
pairs = (x for x in carres if x % 2 == 0)
resultat = sum(pairs)
```

**Questions** :
1. Quand utiliser une list comprehension vs une expression génératrice ?
2. Mesurez la différence de mémoire avec `sys.getsizeof()`
3. Que se passe-t-il si vous essayez d'itérer deux fois sur une expression génératrice ?

## Exercice 6 - Affectation par référence vs copie

**Objectif** : Comprendre la différence entre référence et copie en Python.

**Hints** :
- Lorsque vous faites `list2 = list1`, vous créez une référence, pas une copie
- Pour copier une liste, utilisez `.copy()` ou le slicing `[:]`
- Pour les structures imbriquées (listes dans des listes), utilisez `copy.deepcopy()`
- Les objets mutables (listes, dictionnaires) se comportent différemment des immutables (int, str, tuple)

**Expérimentez** :
1. Créez une liste et assignez-la à une autre variable. Modifiez la seconde et observez la première
2. Testez la différence entre `copy()` et `deepcopy()` sur des listes imbriquées
3. Utilisez `id()` pour voir si deux variables pointent vers le même objet

**Questions** :
- Pourquoi les entiers et chaînes ne sont-ils pas affectés par ce problème ?
- Quelle est la différence entre `is` et `==` ?

## Exercice 7 - Types mutables vs immutables

**Objectif** : Distinguer les types mutables et immutables en Python.

**Hints** :
- **Types immutables** : int, float, str, tuple, frozenset - ne peuvent pas être modifiés après création
- **Types mutables** : list, dict, set - peuvent être modifiés en place
- Modifier un immutable crée en fait un nouvel objet en mémoire
- **Piège** : Un tuple est immutable, mais peut contenir des objets mutables !

**Expérimentez** :
1. Essayez de modifier directement un tuple ou une string (vous aurez une erreur)
2. Créez un tuple contenant une liste, puis modifiez la liste
3. Utilisez `id()` avant et après modification pour voir si l'objet change en mémoire

**TP** : Créez une fonction `est_mutable(obj)` qui retourne True si un objet est mutable.

**Astuce** : Utilisez `hash()` - les objets immutables sont hashables, les mutables ne le sont pas (sauf exceptions).

## Exercice 8 - Passage d'arguments avancé

**Objectif** : Maîtriser les différents types d'arguments de fonction en Python.

**Hints** :
- **Arguments positionnels** : doivent être dans l'ordre
- **Arguments nommés** : peuvent être dans n'importe quel ordre si vous spécifiez le nom
- **`*args`** : capture un nombre variable d'arguments positionnels dans un tuple
- **`**kwargs`** : capture un nombre variable d'arguments nommés dans un dictionnaire
- **`*` seul** : force tous les arguments suivants à être nommés

**Expérimentez** :
1. Créez une fonction avec `*args` qui calcule la somme de tous les arguments
2. Créez une fonction avec `**kwargs` qui affiche toutes les paires clé-valeur
3. Combinez tout : `def ma_fonction(a, b, *args, c=10, **kwargs)`

**PIÈGE CLASSIQUE** - Valeur par défaut mutable :
- **Problème** : Ne jamais utiliser `[]` ou `{}` comme valeur par défaut
- **Raison** : La valeur par défaut est créée une seule fois et partagée entre tous les appels
- **Solution** : Utilisez `None` comme valeur par défaut et créez l'objet à l'intérieur de la fonction

**Exemple de piège** :
```python
def ajouter(element, liste=[]):  # MAUVAIS !
    liste.append(element)
    return liste
# Chaque appel réutilise la même liste !
```

## Exercice 9 - Variables de classe vs d'instance

**Objectif** : Comprendre la différence entre variables de classe et d'instance.

**Hints** :
- **Variable de classe** : définie directement dans la classe, partagée par toutes les instances
- **Variable d'instance** : définie dans `__init__` avec `self.`, unique à chaque instance
- Accès variable de classe : `NomClasse.variable` ou `self.variable` (mais attention au piège !)
- Utilisez `@classmethod` pour des méthodes qui travaillent sur la classe elle-même

**Expérimentez** :
1. Créez une classe `Compteur` avec une variable de classe `total` qui compte les instances créées
2. Ajoutez une méthode de classe `@classmethod` pour afficher le total
3. Testez ce qui se passe si vous modifiez une variable de classe via une instance

**PIÈGE** : Variables de classe mutables
- Si vous définissez `valeur = []` au niveau de la classe, TOUTES les instances la partagent
- Pour avoir une liste unique par instance, définissez-la dans `__init__` : `self.valeur = []`

**Question** : Quand utiliser une variable de classe plutot qu'une variable d'instance ?

## Exercice 10 - Slices avancés

**Objectif** : Maîtriser la syntaxe de slicing en Python.

**Hints** :
- **Syntaxe** : `liste[start:stop:step]`
- `start` : index de début (inclus), défaut = 0
- `stop` : index de fin (exclus), défaut = longueur
- `step` : pas, défaut = 1
- **Indices négatifs** : `-1` = dernier élément, `-2` = avant-dernier, etc.
- **Inversion** : utilisez `[::-1]`

**Expérimentez** :
1. Extraire les 5 premiers éléments d'une liste
2. Extraire tous les éléments pairs (indices 0, 2, 4, ...)
3. Inverser une liste avec un slice
4. Remplacer une portion de liste : `lst[2:5] = [20, 30]`
5. Supprimer des éléments : `lst[2:5] = []`
6. Insérer des éléments : `lst[2:2] = [100, 200]`

**Avancé** : Objet slice
- Vous pouvez créer un objet slice réutilisable : `s = slice(2, 8, 2)`
- Puis l'utiliser : `liste[s]`

**Exercices** :
- Comment extraire les 3 derniers éléments ?
- Comment obtenir les éléments d'indices impairs en ordre inverse ?

## Exercice 11 - Introspection

**Objectif** : Explorer et inspecter les objets Python dynamiquement.

**Hints** - Fonctions Built-in :
- **`dir(obj)`** : Liste tous les attributs et méthodes d'un objet
- **`type(obj)`** : Retourne le type de l'objet
- **`hasattr(obj, 'nom')`** : Vérifie si un attribut existe
- **`getattr(obj, 'nom', default)`** : Récupère la valeur d'un attribut
- **`setattr(obj, 'nom', valeur)`** : Définit la valeur d'un attribut
- **`vars(obj)`** ou **`obj.__dict__`** : Dictionnaire des attributs d'instance
- **`callable(obj)`** : Vérifie si un objet est appelable (fonction, méthode, etc.)
- **`isinstance(obj, Class)`** : Vérifie le type d'une instance
- **`issubclass(Class1, Class2)`** : Vérifie l'héritage

**Module inspect** (plus avancé) :
- `inspect.getmembers(obj)` : Liste détaillée des membres
- `inspect.signature(fonction)` : Signature d'une fonction
- `inspect.getsource(Class)` : Code source d'une classe/fonction

**Expérimentez** :
1. Créez une classe simple et utilisez `dir()` pour voir tous ses attributs
2. Utilisez `getattr()` et `setattr()` pour manipuler des attributs dynamiquement
3. Comparez `vars(obj)` et `vars(Classe)` - quelle est la différence ?
4. Testez `callable()` sur différents types d'objets

**Cas d'usage** : Utile pour le débogage, la création d'APIs dynamiques, ou la sérialisation d'objets.

## Exercice 12 - Clause else dans les structures de contrôle

**Objectif** : Découvrir l'utilisation méconnue de `else` avec les boucles et try/except.

**Hints** :

**`else` avec `for` et `while`** :
- Le bloc `else` s'exécute **uniquement si la boucle se termine normalement** (pas de `break`)
- Très utile pour les recherches : "si on n'a pas trouvé..."
- Si vous sortez de la boucle avec `break`, le `else` est ignoré

**`else` avec `try/except`** :
- Le bloc `else` s'exécute **si aucune exception n'a été levée**
- `finally` s'exécute **toujours**, qu'il y ait ou non une exception
- Ordre : `try` → `except` (si erreur) → `else` (si pas d'erreur) → `finally` (toujours)

**Expérimentez** :
1. Créez une fonction de recherche qui utilise `for...else` pour signaler si un élément n'est pas trouvé
2. Testez une boucle `while` avec `else` qui compte jusqu'à 5
3. Utilisez `try/except/else/finally` pour gérer une division

**Question** : Quel est l'avantage d'utiliser `else` avec les boucles plutot qu'un flag booléen ?

## TP Final - Optimisation : Intersection de listes

**Objectif** : Implémenter plusieurs méthodes pour trouver l'intersection de deux listes et comparer leurs performances.

**Taches** :
Implémentez 4 versions différentes pour trouver les éléments communs à deux listes :

**Méthode 1 - Boucles imbriquées** (Approche naïve) :
- Parcourez chaque élément de list1
- Pour chaque élément, vérifiez s'il est dans list2
- Attention aux doublons dans le résultat
- Complexité : O(n×m) - Pourquoi ?

**Méthode 2 - Opérateur set** :
- Convertissez les deux listes en sets
- Utilisez l'opérateur `&` pour l'intersection
- Reconvertissez en liste
- Complexité : O(n+m) - Pourquoi ?

**Méthode 3 - List comprehension + set** :
- Convertissez list2 en set (recherche O(1))
- Utilisez une list comprehension pour filtrer list1
- Avantage : préserve l'ordre de list1
- Complexité : O(n+m)

**Méthode 4 - Built-in `.intersection()`** :
- Utilisez la méthode `.intersection()` des sets
- C'est généralement la plus optimisée

**Benchmark** :
Utilisez le module `timeit` pour comparer les performances :
```python
import timeit
list1 = list(range(1000))
list2 = list(range(500, 1500))
time = timeit.timeit(lambda: votre_fonction(list1, list2), number=1000)
```

**Questions d'analyse** :
1. Quelle est la complexité temporelle de chaque méthode ? Justifiez.
2. Quelle méthode est la plus rapide en pratique ? Correspond-elle à la théorie ?
3. Y a-t-il des différences dans l'ordre des résultats ? Pourquoi ?
4. Comment gérer les doublons dans les listes d'entrée ?
5. Quelle méthode choisir selon le contexte (petites listes, grandes listes, ordre important, etc.) ?

## Checklist de validation

-  Sets et opérations ensemblistes maîtrisés
-  frozenset et cas d'usage compris
-  Protocole d'itération et itérateurs personnalisés implémentés
-  Générateurs avec yield créés et utilisés
-  Expressions génératrices vs list comprehensions comprises
-  Différence référence/copie maîtrisée
-  Types mutables vs immutables compris
-  Arguments avancés (*args, **kwargs) utilisés
-  Variables classe vs instance distinguées
-  Slices avancés maîtrisés
-  Introspection comprise
-  Clause else utilisée correctement
-  TP intersection optimisé et analysé
