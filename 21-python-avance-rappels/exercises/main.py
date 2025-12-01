# Écrivez votre code ici !
# Consultez le fichier instructions.md pour les consignes

# Exercice 1 - Affectation par référence vs copie
import copy

def test_references():
    """Testez la différence entre référence et copie"""
    list1 = [1, 2, 3]
    list2 = list1  # Référence
    list3 = list1.copy()  # Copie superficielle
    list4 = copy.deepcopy([[1, 2], [3, 4]])  # Copie profonde
    
    # À compléter
    pass


# Exercice 2 - Types mutables vs immutables
def test_mutabilite():
    """Testez les types mutables et immutables"""
    # À compléter
    pass


# Exercice 3 - Passage d'arguments avancé
def fonction_complete(a, b, *args, c=10, **kwargs):
    """Fonction avec tous types d'arguments"""
    # À compléter
    pass


def fonction_avec_defaut_mutable(element, liste=None):
    """ATTENTION : Ne jamais utiliser [] comme valeur par défaut"""
    if liste is None:
        liste = []
    # À compléter
    pass


# Exercice 4 - Variables de classe vs d'instance
class Compteur:
    """Classe pour comprendre les variables de classe"""
    total = 0  # Variable de classe
    
    def __init__(self, nom):
        self.nom = nom  # Variable d'instance
        # À compléter
        pass


# Exercice 5 - Slices avancés
def tester_slices():
    """Maîtrisez les slices"""
    lst = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
    
    # Basique
    print(lst[2:5])
    print(lst[::-1])  # Inversion
    
    # À compléter avec d'autres exemples
    pass


# Exercice 6 - Introspection
def explorer_objet(obj):
    """Utilisez dir(), type(), hasattr(), etc."""
    print(f"Type: {type(obj)}")
    print(f"Attributs: {dir(obj)}")
    # À compléter
    pass


# Exercice 7 - Clause else dans les structures
def chercher_avec_else(liste, valeur):
    """Utilisez la clause else avec for"""
    for item in liste:
        if item == valeur:
            print(f"Trouvé : {item}")
            break
    else:
        print("Non trouvé")


# TP FINAL - Intersection de listes
def intersection_v1_boucles(list1, list2):
    """Méthode 1 : Boucles imbriquées - O(n*m)"""
    result = []
    for item in list1:
        if item in list2 and item not in result:
            result.append(item)
    return result


def intersection_v2_set(list1, list2):
    """Méthode 2 : Set - O(n+m)"""
    return list(set(list1) & set(list2))


def intersection_v3_comprehension(list1, list2):
    """Méthode 3 : List comprehension avec set - O(n+m)"""
    set2 = set(list2)
    return [item for item in list1 if item in set2]


def intersection_v4_builtin(list1, list2):
    """Méthode 4 : Built-in (le plus rapide)"""
    return list(set(list1).intersection(set(list2)))


# Exercice 8 - Complexité algorithmique
def analyser_complexite():
    """Analysez différentes complexités"""
    
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
    
    # À compléter avec vos tests
    pass


# Tests et benchmarks
if __name__ == "__main__":
    print("=== Tests Python Avancé ===\n")
    
    # Test 1 : Références
    print("Test 1 : Références et copies")
    test_references()
    
    # Test 2 : Mutabilité
    print("\nTest 2 : Mutabilité")
    test_mutabilite()
    
    # Test 3 : Slices
    print("\nTest 3 : Slices")
    tester_slices()
    
    # TP : Comparer les performances
    print("\n=== TP : Intersection de listes ===")
    import timeit
    
    list1 = list(range(1000))
    list2 = list(range(500, 1500))
    
    for i, func in enumerate([intersection_v1_boucles, intersection_v2_set, 
                               intersection_v3_comprehension, intersection_v4_builtin], 1):
        time = timeit.timeit(lambda: func(list1, list2), number=1000)
        print(f"Méthode {i} ({func.__name__}): {time:.4f}s")
