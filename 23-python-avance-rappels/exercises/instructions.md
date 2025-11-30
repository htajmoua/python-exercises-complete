# Instructions - Python Avancé : Rappels et Fondamentaux

Ce module couvre les concepts fondamentaux avancés de Python souvent mal compris, avec un focus sur l'optimisation et la complexité algorithmique.

## Exercice 1 - Affectation par référence vs copie

**Comprenez** la différence entre référence et copie :

```python
# Affectation par référence (pour objets mutables)
list1 = [1, 2, 3]
list2 = list1  # Référence, pas copie
list2.append(4)
print(list1)  # [1, 2, 3, 4] - modifié aussi !

# Copie superficielle (shallow copy)
list3 = list1.copy()  # ou list1[:]
list3.append(5)
print(list1)  # [1, 2, 3, 4] - non modifié

# Copie profonde (deep copy) pour structures imbriquées
import copy
nested = [[1, 2], [3, 4]]
shallow = nested.copy()
deep = copy.deepcopy(nested)

shallow[0].append(3)
print(nested)  # [[1, 2, 3], [3, 4]] - modifié !
print(deep)    # [[1, 2], [3, 4]] - non modifié
```

**Questions** :
- Pourquoi les entiers et chaînes ne sont-ils pas affectés par ce problème ?
- Quelle est la différence entre `is` et `==` ?

## Exercice 2 - Types mutables vs immutables

**Identifiez** les types mutables et immutables :

```python
# Immutables (non modifiables)
a = 5
b = a
a = 10
print(b)  # 5 - inchangé

# Tuple immutable
t = (1, 2, 3)
# t[0] = 10  # TypeError

# String immutable
s = "hello"
# s[0] = "H"  # TypeError
s = s.upper()  # Création d'une nouvelle chaîne

# Mutables
lst = [1, 2, 3]
lst[0] = 10  # OK
dct = {"a": 1}
dct["a"] = 2  # OK

# Piège : tuple avec éléments mutables
t = ([1, 2], [3, 4])
# t[0] = [5, 6]  # TypeError
t[0].append(3)  # OK ! Le tuple est immutable, pas son contenu
print(t)  # ([1, 2, 3], [3, 4])
```

**TP** : Créez une fonction qui retourne True si un objet est mutable.

## Exercice 3 - Passage d'arguments avancé

**Maîtrisez** les arguments de fonction :

```python
# Arguments positionnels et nommés
def fonction(a, b, c=10, d=20):
    return a + b + c + d

print(fonction(1, 2))           # 33
print(fonction(1, 2, c=5))      # 28
print(fonction(1, 2, d=5, c=3)) # 11

# *args et **kwargs
def somme(*args):
    return sum(args)

print(somme(1, 2, 3, 4, 5))  # 15

def afficher_infos(**kwargs):
    for key, value in kwargs.items():
        print(f"{key}: {value}")

afficher_infos(nom="Alice", age=30, ville="Paris")

# Combinaison
def fonction_complete(a, b, *args, c=10, **kwargs):
    print(f"a={a}, b={b}")
    print(f"args={args}")
    print(f"c={c}")
    print(f"kwargs={kwargs}")

fonction_complete(1, 2, 3, 4, c=5, x=10, y=20)

# Forcer les arguments nommés (Python 3+)
def fonction_stricte(a, b, *, c, d):  # c et d DOIVENT être nommés
    return a + b + c + d

# fonction_stricte(1, 2, 3, 4)  # TypeError
print(fonction_stricte(1, 2, c=3, d=4))  # OK
```

**Attention** : Valeur par défaut mutable (PIÈGE CLASSIQUE) :

```python
# MAUVAIS
def ajouter_element(element, liste=[]):
    liste.append(element)
    return liste

print(ajouter_element(1))  # [1]
print(ajouter_element(2))  # [1, 2] - Oups !

# BON
def ajouter_element(element, liste=None):
    if liste is None:
        liste = []
    liste.append(element)
    return liste

print(ajouter_element(1))  # [1]
print(ajouter_element(2))  # [2] - Correct !
```

## Exercice 4 - Variables de classe vs d'instance

**Comprenez** la différence :

```python
class Compteur:
    # Variable de classe (partagée par toutes les instances)
    total = 0
    
    def __init__(self, nom):
        # Variable d'instance (unique à chaque instance)
        self.nom = nom
        Compteur.total += 1
    
    @classmethod
    def afficher_total(cls):
        return cls.total

c1 = Compteur("Premier")
c2 = Compteur("Deuxième")
print(Compteur.total)  # 2

# Piège : modification via l'instance
class Piege:
    valeur = []  # Variable de classe
    
    def ajouter(self, x):
        self.valeur.append(x)  # Modifie la variable de classe !

p1 = Piege()
p2 = Piege()
p1.ajouter(1)
p2.ajouter(2)
print(p1.valeur)  # [1, 2] - Partagé !

# Correct
class Correct:
    def __init__(self):
        self.valeur = []  # Variable d'instance
    
    def ajouter(self, x):
        self.valeur.append(x)
```

## Exercice 5 - Slices avancés

**Maîtrisez** les slices :

```python
lst = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

# Basique
print(lst[2:5])      # [2, 3, 4]
print(lst[:5])       # [0, 1, 2, 3, 4]
print(lst[5:])       # [5, 6, 7, 8, 9]
print(lst[-3:])      # [7, 8, 9]

# Avec step
print(lst[::2])      # [0, 2, 4, 6, 8]
print(lst[1::2])     # [1, 3, 5, 7, 9]
print(lst[::-1])     # [9, 8, 7, 6, 5, 4, 3, 2, 1, 0] - Inversion

# Slices avancés
print(lst[2:8:2])    # [2, 4, 6]
print(lst[-1::-2])   # [9, 7, 5, 3, 1]

# Modification par slice
lst[2:5] = [20, 30, 40]
print(lst)  # [0, 1, 20, 30, 40, 5, 6, 7, 8, 9]

# Suppression par slice
lst[2:5] = []
print(lst)  # [0, 1, 5, 6, 7, 8, 9]

# Insertion par slice
lst[2:2] = [100, 200]
print(lst)  # [0, 1, 100, 200, 5, 6, 7, 8, 9]

# Slices avec objets slice
s = slice(2, 8, 2)
print(lst[s])
```

## Exercice 6 - Introspection

**Explorez** les objets Python :

```python
import inspect

class MaClasse:
    attribut_classe = "classe"
    
    def __init__(self):
        self.attribut_instance = "instance"
    
    def methode(self):
        pass

obj = MaClasse()

# dir() - Liste tous les attributs et méthodes
print(dir(obj))

# type() - Type de l'objet
print(type(obj))  # <class '__main__.MaClasse'>

# hasattr, getattr, setattr
print(hasattr(obj, 'methode'))  # True
print(getattr(obj, 'attribut_instance'))  # "instance"
setattr(obj, 'nouveau', 'valeur')

# vars() - Dictionnaire des attributs
print(vars(obj))  # {'attribut_instance': 'instance', 'nouveau': 'valeur'}

# callable() - Vérifier si c'est appelable
print(callable(obj.methode))  # True
print(callable(obj.attribut_instance))  # False

# inspect module
print(inspect.getmembers(obj))
print(inspect.signature(MaClasse.methode))
print(inspect.getsource(MaClasse))

# __dict__ - Attributs de l'objet
print(obj.__dict__)
print(MaClasse.__dict__)

# isinstance et issubclass
print(isinstance(obj, MaClasse))  # True
print(issubclass(MaClasse, object))  # True
```

## Exercice 7 - Clause else dans les structures de contrôle

**Utilisez** la clause `else` méconnue :

```python
# else dans for (exécuté si pas de break)
def chercher(liste, valeur):
    for item in liste:
        if item == valeur:
            print(f"Trouvé : {item}")
            break
    else:
        print("Non trouvé")

chercher([1, 2, 3], 2)  # Trouvé : 2
chercher([1, 2, 3], 5)  # Non trouvé

# else dans while
compteur = 0
while compteur < 5:
    if compteur == 10:
        break
    compteur += 1
else:
    print("Boucle terminée normalement")

# else dans try/except
try:
    resultat = 10 / 2
except ZeroDivisionError:
    print("Division par zéro")
else:
    print("Pas d'erreur")  # Exécuté si pas d'exception
finally:
    print("Toujours exécuté")
```

## TP Final - Optimisation : Intersection de listes

**Implémentez** différentes méthodes et comparez leur complexité :

```python
# Méthode 1 : Boucles imbriquées - O(n*m)
def intersection_v1(list1, list2):
    result = []
    for item in list1:
        if item in list2 and item not in result:
            result.append(item)
    return result

# Méthode 2 : Set - O(n+m)
def intersection_v2(list1, list2):
    return list(set(list1) & set(list2))

# Méthode 3 : List comprehension avec set - O(n+m)
def intersection_v3(list1, list2):
    set2 = set(list2)
    return [item for item in list1 if item in set2]

# Méthode 4 : Built-in (le plus rapide)
def intersection_v4(list1, list2):
    return list(set(list1).intersection(set(list2)))

# Tests de performance
import timeit

list1 = list(range(1000))
list2 = list(range(500, 1500))

for i, func in enumerate([intersection_v1, intersection_v2, intersection_v3, intersection_v4], 1):
    time = timeit.timeit(lambda: func(list1, list2), number=1000)
    print(f"Méthode {i}: {time:.4f}s")
```

**Questions** :
1. Calculez la complexité en temps de chaque méthode
2. Quelle méthode est la plus rapide ? Pourquoi ?
3. Y a-t-il des différences dans l'ordre des résultats ?
4. Comment gérer les doublons ?

## Exercice 8 - Complexité algorithmique

**Analysez** la complexité :

```python
# O(1) - Constant
def get_first(lst):
    return lst[0] if lst else None

# O(n) - Linéaire
def find_max(lst):
    max_val = lst[0]
    for item in lst:
        if item > max_val:
            max_val = item
    return max_val

# O(n²) - Quadratique
def bubble_sort(lst):
    n = len(lst)
    for i in range(n):
        for j in range(0, n-i-1):
            if lst[j] > lst[j+1]:
                lst[j], lst[j+1] = lst[j+1], lst[j]
    return lst

# O(log n) - Logarithmique
def binary_search(lst, target):
    left, right = 0, len(lst) - 1
    while left <= right:
        mid = (left + right) // 2
        if lst[mid] == target:
            return mid
        elif lst[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    return -1

# O(n log n) - Linéarithmique
def merge_sort(lst):
    if len(lst) <= 1:
        return lst
    mid = len(lst) // 2
    left = merge_sort(lst[:mid])
    right = merge_sort(lst[mid:])
    return merge(left, right)

def merge(left, right):
    result = []
    i = j = 0
    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1
    result.extend(left[i:])
    result.extend(right[j:])
    return result
```

## Checklist de validation

- ✅ Différence référence/copie maîtrisée
- ✅ Types mutables vs immutables compris
- ✅ Arguments avancés (*args, **kwargs) utilisés
- ✅ Variables classe vs instance distinguées
- ✅ Slices avancés maîtrisés
- ✅ Introspection comprise
- ✅ Clause else utilisée correctement
- ✅ TP intersection optimisé et analysé
- ✅ Complexité algorithmique calculée
