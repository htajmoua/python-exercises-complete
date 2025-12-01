# Écrivez votre code ici !
# Consultez le fichier instructions.md pour les consignes

import timeit
import time
from functools import lru_cache

# ============= PARTIE 1 : TIMEIT =============

# Exercice 1 - Mesurer avec timeit
def exemple_timeit():
    """Exemples d'utilisation de timeit"""
    
    # Mesurer une expression simple
    temps = timeit.timeit("'-'.join(str(n) for n in range(100))", number=10000)
    print(f"Generator expression : {temps:.4f}s")
    
    temps = timeit.timeit("'-'.join([str(n) for n in range(100)])", number=10000)
    print(f"List comprehension : {temps:.4f}s")
    
    temps = timeit.timeit("'-'.join(map(str, range(100)))", number=10000)
    print(f"Map : {temps:.4f}s")


# Fonction de timing réutilisable
def mesurer_temps(func, *args, number=1000):
    """Mesure le temps moyen d'exécution"""
    timer = timeit.Timer(lambda: func(*args))
    temps = timer.timeit(number=number)
    return temps / number


# Exercice 2 - Comparer plusieurs approches
def methode1_concat_string():
    """Méthode 1 : Concaténation (LENT)"""
    s = ""
    for i in range(1000):
        s += str(i)
    return s


def methode2_join():
    """Méthode 2 : Join avec generator"""
    return ''.join(str(i) for i in range(1000))


def methode3_list_join():
    """Méthode 3 : Join avec list"""
    return ''.join([str(i) for i in range(1000)])


# ============= PARTIE 2 : OPTIMISATION =============

# Exercice 9 - List comprehensions vs loops
def avec_boucle():
    """Méthode avec boucle for"""
    result = []
    for i in range(1000):
        result.append(i ** 2)
    return result


def avec_comprehension():
    """Méthode avec list comprehension"""
    return [i ** 2 for i in range(1000)]


def avec_map():
    """Méthode avec map"""
    return list(map(lambda x: x ** 2, range(1000)))


# Exercice 10 - Structures de données optimales
def test_list_membership():
    """Test membership avec list - O(n)"""
    lst = list(range(1000))
    return 999 in lst


def test_set_membership():
    """Test membership avec set - O(1)"""
    s = set(range(1000))
    return 999 in s


# Exercice 12 - Générateurs vs listes
def avec_liste(n):
    """Liste : Tout en mémoire"""
    return [i ** 2 for i in range(n)]


def avec_generateur(n):
    """Générateur : Lazy evaluation"""
    return (i ** 2 for i in range(n))


# ============= TP FINAL : NOMBRES PREMIERS =============

# Version 1 : Inefficace
def trouver_nombres_premiers_v1(n):
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


# Version 2 : Optimisation simple
def trouver_nombres_premiers_v2(n):
    """Optimisation : jusqu'à racine carrée"""
    premiers = []
    for num in range(2, n + 1):
        est_premier = True
        for diviseur in range(2, int(num ** 0.5) + 1):
            if num % diviseur == 0:
                est_premier = False
                break
        if est_premier:
            premiers.append(num)
    return premiers


# Version 3 : Crible d'Ératosthène
def crible_eratosthene(n):
    """Crible d'Ératosthène - Très efficace"""
    est_premier = [True] * (n + 1)
    est_premier[0] = est_premier[1] = False
    
    for i in range(2, int(n ** 0.5) + 1):
        if est_premier[i]:
            for j in range(i * i, n + 1, i):
                est_premier[j] = False
    
    return [i for i, prime in enumerate(est_premier) if prime]


# Version 4 : NumPy (optionnel)
def crible_numpy(n):
    """Crible avec NumPy (si disponible)"""
    try:
        import numpy as np
        est_premier = np.ones(n + 1, dtype=bool)
        est_premier[0:2] = False
        
        for i in range(2, int(n ** 0.5) + 1):
            if est_premier[i]:
                est_premier[i*i::i] = False
        
        return np.where(est_premier)[0]
    except ImportError:
        print("NumPy non disponible, utilisez crible_eratosthene")
        return crible_eratosthene(n)


# ============= PROFILING AVEC cProfile =============

def fibonacci_lent(n):
    """Fibonacci récursif (TRÈS LENT)"""
    if n <= 1:
        return n
    return fibonacci_lent(n-1) + fibonacci_lent(n-2)


@lru_cache(maxsize=None)
def fibonacci_rapide(n):
    """Fibonacci avec cache (RAPIDE)"""
    if n <= 1:
        return n
    return fibonacci_rapide(n-1) + fibonacci_rapide(n-2)


def calcul_lourd():
    """Fonction pour profiling"""
    total = 0
    for i in range(1000):
        total += fibonacci_rapide(20)
    return total


# ============= EXERCICES DE COMPLEXITÉ =============

# O(1) - Constant
def get_first(lst):
    """O(1) - Accès constant"""
    return lst[0] if lst else None


# O(n) - Linéaire
def find_max(lst):
    """O(n) - Parcours linéaire"""
    max_val = lst[0]
    for item in lst:
        if item > max_val:
            max_val = item
    return max_val


# O(n²) - Quadratique
def bubble_sort(lst):
    """O(n²) - Tri à bulles"""
    n = len(lst)
    lst = lst.copy()
    for i in range(n):
        for j in range(0, n-i-1):
            if lst[j] > lst[j+1]:
                lst[j], lst[j+1] = lst[j+1], lst[j]
    return lst


# O(log n) - Logarithmique
def binary_search(lst, target):
    """O(log n) - Recherche binaire"""
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
    """O(n log n) - Tri fusion"""
    if len(lst) <= 1:
        return lst
    
    mid = len(lst) // 2
    left = merge_sort(lst[:mid])
    right = merge_sort(lst[mid:])
    
    return merge(left, right)


def merge(left, right):
    """Fusion de deux listes triées"""
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


# ============= TESTS ET BENCHMARKS =============

def comparer_performances():
    """Compare les performances des différentes méthodes"""
    
    print("=== Comparaison String Join ===")
    for func in [methode1_concat_string, methode2_join, methode3_list_join]:
        temps = timeit.timeit(func, number=100)
        print(f"{func.__name__}: {temps:.4f}s")
    
    print("\n=== Comparaison List Comprehension ===")
    for func in [avec_boucle, avec_comprehension, avec_map]:
        temps = timeit.timeit(func, number=1000)
        print(f"{func.__name__}: {temps:.4f}s")
    
    print("\n=== Comparaison Membership ===")
    temps_list = timeit.timeit(test_list_membership, number=10000)
    temps_set = timeit.timeit(test_set_membership, number=10000)
    print(f"List: {temps_list:.4f}s")
    print(f"Set: {temps_set:.4f}s")
    print(f"Set est {temps_list/temps_set:.1f}x plus rapide")


def benchmark_nombres_premiers():
    """Benchmark des algorithmes de nombres premiers"""
    
    print("\n=== Benchmark Nombres Premiers (n=1000) ===")
    n = 1000
    
    for func in [trouver_nombres_premiers_v1, trouver_nombres_premiers_v2, 
                 crible_eratosthene]:
        temps = timeit.timeit(lambda: func(n), number=10)
        print(f"{func.__name__}: {temps:.4f}s")


def demo_profiling():
    """Démonstration du profiling avec cProfile"""
    import cProfile
    import pstats
    
    print("\n=== Profiling avec cProfile ===")
    profiler = cProfile.Profile()
    profiler.enable()
    
    result = calcul_lourd()
    
    profiler.disable()
    
    stats = pstats.Stats(profiler)
    stats.sort_stats('cumulative')
    stats.print_stats(10)


def demo_memoization():
    """Démonstration de la memoization"""
    
    print("\n=== Memoization ===")
    
    # Sans cache
    start = time.time()
    result = fibonacci_lent(30)
    temps_lent = time.time() - start
    print(f"Sans cache (n=30): {temps_lent:.4f}s")
    
    # Avec cache
    start = time.time()
    result = fibonacci_rapide(30)
    temps_rapide = time.time() - start
    print(f"Avec cache (n=30): {temps_rapide:.4f}s")
    print(f"Amélioration: {temps_lent/temps_rapide:.0f}x plus rapide")


# ============= MAIN =============

if __name__ == "__main__":
    print("=== Tests Performance et Profiling ===\n")
    
    # Timeit
    print("1. Exemples timeit")
    exemple_timeit()
    
    # Comparaisons
    print("\n2. Comparaison des performances")
    comparer_performances()
    
    # Nombres premiers
    print("\n3. Benchmark nombres premiers")
    benchmark_nombres_premiers()
    
    # Profiling
    print("\n4. Profiling")
    demo_profiling()
    
    # Memoization
    print("\n5. Memoization")
    demo_memoization()
    
    # Complexité
    print("\n6. Complexité algorithmique")
    print("O(1) - Constant: get_first()")
    print("O(n) - Linéaire: find_max()")
    print("O(n²) - Quadratique: bubble_sort()")
    print("O(log n) - Logarithmique: binary_search()")
    print("O(n log n) - Linéarithmique: merge_sort()")
    
    print("\n" + "="*50)
    print("Consultez instructions.md pour les exercices détaillés !")
