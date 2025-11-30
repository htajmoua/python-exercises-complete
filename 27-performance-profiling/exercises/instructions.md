# Instructions - Performance et Profiling

Ce module couvre l'analyse et l'optimisation des performances de vos programmes Python avec des outils de profiling et des techniques d'optimisation.

## Partie 1 - Timeit

### Exercice 1 - Mesurer avec timeit

**En ligne de commande** :

```bash
python -m timeit "'-'.join(str(n) for n in range(100))"
python -m timeit "'-'.join([str(n) for n in range(100)])"
python -m timeit "'-'.join(map(str, range(100)))"
```

**En code Python** :

```python
import timeit

# Mesurer une expression
temps = timeit.timeit("'-'.join(str(n) for n in range(100))", number=10000)
print(f"Temps : {temps:.4f}s")

# Avec setup
setup = "lst = list(range(1000))"
stmt = "sum(lst)"
temps = timeit.timeit(stmt, setup=setup, number=10000)

# Fonction de timing réutilisable
def mesurer_temps(func, *args, number=1000):
    import timeit
    timer = timeit.Timer(lambda: func(*args))
    temps = timer.timeit(number=number)
    return temps / number

def ma_fonction():
    return sum(range(1000))

temps_moyen = mesurer_temps(ma_fonction)
print(f"Temps moyen : {temps_moyen*1000:.4f}ms")
```

### Exercice 2 - Comparer plusieurs approches

**Comparez** différentes méthodes :

```python
import timeit

def methode1_concat_string():
    s = ""
    for i in range(1000):
        s += str(i)
    return s

def methode2_join():
    return ''.join(str(i) for i in range(1000))

def methode3_list_join():
    return ''.join([str(i) for i in range(1000)])

# Comparer
for func in [methode1_concat_string, methode2_join, methode3_list_join]:
    temps = timeit.timeit(func, number=1000)
    print(f"{func.__name__}: {temps:.4f}s")
```

## Partie 2 - cProfile

### Exercice 3 - Profiler un programme

**Créez** un programme à profiler :

```python
# programme.py
def fibonacci(n):
    if n <= 1:
        return n
    return fibonacci(n-1) + fibonacci(n-2)

def calcul_lourd():
    total = 0
    for i in range(1000):
        total += fibonacci(20)
    return total

def main():
    result = calcul_lourd()
    print(f"Résultat : {result}")

if __name__ == '__main__':
    main()
```

**Profilez** :

```bash
python -m cProfile programme.py
python -m cProfile -s cumtime programme.py  # Trié par temps cumulé
python -m cProfile -o output.prof programme.py  # Sauvegarder
```

**En code** :

```python
import cProfile
import pstats

profiler = cProfile.Profile()
profiler.enable()

# Code à profiler
result = calcul_lourd()

profiler.disable()

# Afficher les stats
stats = pstats.Stats(profiler)
stats.sort_stats('cumulative')
stats.print_stats(10)  # Top 10
```

### Exercice 4 - Analyser les résultats

**Visualisez** avec snakeviz :

```bash
pip install snakeviz
python -m cProfile -o program.prof programme.py
snakeviz program.prof
```

## Partie 3 - line_profiler

### Exercice 5 - Profiler ligne par ligne

**Installez** :

```bash
pip install line_profiler
```

**Utilisez** :

```python
# programme.py
@profile  # Décorateur magique pour line_profiler
def fonction_lente():
    total = 0
    for i in range(10000):
        total += i ** 2
    return total

def main():
    result = fonction_lente()
    print(result)

if __name__ == '__main__':
    main()
```

**Exécutez** :

```bash
kernprof -l -v programme.py
```

### Exercice 6 - Optimiser avec line_profiler

**Identifiez** les lignes lentes :

```python
@profile
def traiter_donnees(data):
    # Ligne 1 : Lente ?
    resultats = []
    
    # Ligne 2 : Lente ?
    for item in data:
        # Ligne 3 : Lente ?
        if item % 2 == 0:
            # Ligne 4 : Lente ?
            resultats.append(item ** 2)
    
    return resultats

data = range(100000)
traiter_donnees(data)
```

## Partie 4 - memory_profiler

### Exercice 7 - Profiler la mémoire

**Installez** :

```bash
pip install memory_profiler
```

**Utilisez** :

```python
from memory_profiler import profile

@profile
def fonction_memoire():
    # Créer une grande liste
    lst = [i for i in range(1000000)]
    
    # Créer une copie
    lst2 = lst.copy()
    
    # Traitement
    result = sum(lst2)
    
    return result

fonction_memoire()
```

**Exécutez** :

```bash
python -m memory_profiler programme.py
```

### Exercice 8 - Surveiller la mémoire dans le temps

**Tracez** l'utilisation mémoire :

```python
from memory_profiler import memory_usage
import matplotlib.pyplot as plt

def fonction_test():
    lst = []
    for i in range(1000000):
        lst.append(i)
    return lst

# Mesurer
mem_usage = memory_usage((fonction_test,))

# Tracer
plt.plot(mem_usage)
plt.ylabel('Mémoire (MB)')
plt.xlabel('Temps')
plt.show()
```

## Partie 5 - Optimisation

### Exercice 9 - List comprehensions vs loops

**Comparez** :

```python
import timeit

# Méthode 1 : Boucle for
def avec_boucle():
    result = []
    for i in range(1000):
        result.append(i ** 2)
    return result

# Méthode 2 : List comprehension
def avec_comprehension():
    return [i ** 2 for i in range(1000)]

# Méthode 3 : map
def avec_map():
    return list(map(lambda x: x ** 2, range(1000)))

for func in [avec_boucle, avec_comprehension, avec_map]:
    temps = timeit.timeit(func, number=10000)
    print(f"{func.__name__}: {temps:.4f}s")
```

### Exercice 10 - Structures de données optimales

**Choisissez** la bonne structure :

```python
import timeit

# Test membership avec list vs set
def test_list():
    lst = list(range(1000))
    return 999 in lst

def test_set():
    s = set(range(1000))
    return 999 in s

# List: O(n), Set: O(1)
print("List:", timeit.timeit(test_list, number=10000))
print("Set:", timeit.timeit(test_set, number=10000))

# Test access avec list vs dict
def test_list_access():
    lst = [{'id': i, 'value': i*2} for i in range(1000)]
    return next(item for item in lst if item['id'] == 999)

def test_dict_access():
    dct = {i: i*2 for i in range(1000)}
    return dct[999]

print("List access:", timeit.timeit(test_list_access, number=10000))
print("Dict access:", timeit.timeit(test_dict_access, number=10000))
```

### Exercice 11 - Éviter les copies inutiles

**Optimisez** :

```python
# Mauvais : Copie à chaque itération
def mauvais(data):
    result = []
    for item in data:
        temp = data.copy()  # Copie inutile !
        temp.append(item)
        result.append(temp)
    return result

# Bon
def bon(data):
    result = []
    for item in data:
        result.append(item)
    return result
```

### Exercice 12 - Générateurs vs listes

**Utilisez** des générateurs pour la mémoire :

```python
import sys

# Liste : Tout en mémoire
def avec_liste(n):
    return [i ** 2 for i in range(n)]

# Générateur : Lazy evaluation
def avec_generateur(n):
    return (i ** 2 for i in range(n))

lst = avec_liste(1000000)
gen = avec_generateur(1000000)

print(f"Taille liste : {sys.getsizeof(lst)} bytes")
print(f"Taille générateur : {sys.getsizeof(gen)} bytes")
```

## TP Final - Profiler et optimiser un algorithme

**Programme initial (inefficace)** :

```python
def trouver_nombres_premiers(n):
    """Trouve tous les nombres premiers jusqu'à n (version inefficace)"""
    premiers = []
    for num in range(2, n + 1):
        est_premier = True
        for diviseur in range(2, num):
            if num % diviseur == 0:
                est_premier = False
                break
        if est_premier:
            premiers.append(num)
    return premiers

# Profiler
import cProfile
cProfile.run('trouver_nombres_premiers(10000)')
```

**Étapes d'optimisation** :

```python
# Version 2 : Optimisation simple
def trouver_nombres_premiers_v2(n):
    premiers = []
    for num in range(2, n + 1):
        est_premier = True
        for diviseur in range(2, int(num ** 0.5) + 1):  # Jusqu'à racine carrée
            if num % diviseur == 0:
                est_premier = False
                break
        if est_premier:
            premiers.append(num)
    return premiers

# Version 3 : Crible d'Ératosthène
def crible_eratosthene(n):
    est_premier = [True] * (n + 1)
    est_premier[0] = est_premier[1] = False
    
    for i in range(2, int(n ** 0.5) + 1):
        if est_premier[i]:
            for j in range(i * i, n + 1, i):
                est_premier[j] = False
    
    return [i for i, prime in enumerate(est_premier) if prime]

# Version 4 : NumPy (si disponible)
import numpy as np

def crible_numpy(n):
    est_premier = np.ones(n + 1, dtype=bool)
    est_premier[0:2] = False
    
    for i in range(2, int(n ** 0.5) + 1):
        if est_premier[i]:
            est_premier[i*i::i] = False
    
    return np.where(est_premier)[0]
```

**Comparez** :

```python
import timeit

n = 10000

for func in [trouver_nombres_premiers, trouver_nombres_premiers_v2, 
             crible_eratosthene, crible_numpy]:
    temps = timeit.timeit(lambda: func(n), number=10)
    print(f"{func.__name__}: {temps:.4f}s")
```

## Exercices bonus

### Exercice 13 - Complexité algorithmique

**Calculez** la complexité de ces algorithmes :

```python
# O(1) - Constant
def constant(n):
    return n[0]

# O(log n) - Logarithmique  
def logarithmique(n, target):
    # Binary search
    left, right = 0, len(n) - 1
    while left <= right:
        mid = (left + right) // 2
        if n[mid] == target:
            return mid
        elif n[mid] < target:
            left = mid + 1
        else:
            right = mid - 1

# O(n) - Linéaire
def lineaire(n):
    return sum(n)

# O(n log n) - Linéarithmique
def linearithmique(n):
    return sorted(n)

# O(n²) - Quadratique
def quadratique(n):
    for i in n:
        for j in n:
            pass

# O(2^n) - Exponentiel
def exponentiel(n):
    if n <= 1:
        return 1
    return exponentiel(n-1) + exponentiel(n-1)
```

### Exercice 14 - Memoization

**Optimisez** avec cache :

```python
from functools import lru_cache

# Sans cache - Très lent
def fibonacci_lent(n):
    if n <= 1:
        return n
    return fibonacci_lent(n-1) + fibonacci_lent(n-2)

# Avec cache - Très rapide
@lru_cache(maxsize=None)
def fibonacci_rapide(n):
    if n <= 1:
        return n
    return fibonacci_rapide(n-1) + fibonacci_rapide(n-2)

import timeit
print("Sans cache:", timeit.timeit(lambda: fibonacci_lent(30), number=1))
print("Avec cache:", timeit.timeit(lambda: fibonacci_rapide(30), number=1))
```

## Checklist de validation

- ✅ timeit maîtrisé pour micro-benchmarks
- ✅ cProfile utilisé pour profiling complet
- ✅ line_profiler utilisé pour analyse ligne par ligne
- ✅ memory_profiler utilisé pour analyse mémoire
- ✅ Optimisations appliquées (comprehensions, structures)
- ✅ Générateurs vs listes compris
- ✅ **TP : Algorithme profileé et optimisé**
- ✅ Complexité algorithmique calculée
- ✅ Memoization implémentée
