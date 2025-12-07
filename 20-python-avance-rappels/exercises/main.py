# Écrivez votre code ici !
# Consultez le fichier instructions.md pour les consignes

# Exercice 1 - Sets : Opérations et propriétés
def tester_sets_operations():
    """Testez les opérations sur les sets"""
    set1 = {1, 2, 3, 4, 5}
    set2 = {4, 5, 6, 7, 8}
    
    # À compléter : union, intersection, différence, symmetric_difference
    # Testez aussi : issubset, issuperset, isdisjoint, add(), remove()
    pass


def comparer_performance_set_vs_liste():
    """Compare la performance de recherche entre set et liste"""
    import timeit
    
    # À compléter : créez une liste et un set de 10000 éléments
    # Comparez le temps de recherche avec timeit
    pass


# Exercice 2 - Sets avancés : frozenset et cas d'usage
def tester_frozenset():
    """Testez les frozensets"""
    # À compléter : créez un frozenset et testez son immutabilité
    # Utilisez-le comme clé de dict ou dans un set de frozensets
    pass


def elements_uniques_plusieurs_listes(*listes):
    """Retourne les éléments présents dans une seule liste"""
    sets = [set(lst) for lst in listes]
    # Hint : pour chaque set, faites set_i - tous_les_autres, puis union
    pass


def valider_entree(valeur, valeurs_autorisees):
    """Valide si une valeur est dans un ensemble de valeurs autorisées"""
    # À compléter : utilisez l'opérateur in (O(1) avec set)
    pass


# Exercice 3 - Protocole d'itération et itérateurs
class CompteurIterateur:
    """Itérateur personnalisé qui compte de debut à fin
    
    Un itérateur doit implémenter :
    - __iter__() : retourne self
    - __next__() : retourne le prochain élément ou lève StopIteration
    """
    def __init__(self, debut, fin):
        self.debut = debut
        self.fin = fin
        self.actuel = debut  # Compteur actuel
        # À compléter si besoin
    
    def __iter__(self):
        """Retourne l'itérateur lui-même"""
        return self
    
    def __next__(self):
        """Retourne le prochain nombre ou lève StopIteration"""
        if self.actuel > self.fin:
            raise StopIteration
        # À compléter : retourner et incrémenter
        pass


def tester_iterateur():
    """Testez votre itérateur personnalisé"""
    print("Test de l'itérateur :")
    compteur = CompteurIterateur(1, 5)
    # À compléter : boucle for sur compteur
    pass


# Exercice 4 - Générateurs avec yield
def fibonacci(n):
    """Générateur qui produit les n premiers nombres de Fibonacci"""
    a, b = 0, 1
    for _ in range(n):
        # À compléter : yield a, puis a, b = b, a + b
        pass


def nombres_pairs(max_valeur):
    """Générateur qui produit tous les nombres pairs de 0 à max_valeur"""
    for i in range(0, max_valeur + 1, 2):
        # À compléter : yield i
        pass


def lire_lignes_fichier(chemin_fichier):
    """Générateur qui lit un fichier ligne par ligne"""
    with open(chemin_fichier, 'r') as f:
        for ligne in f:
            # À compléter : yield ligne
            pass


def tester_generateurs():
    """Testez vos générateurs"""
    print("\nTest des générateurs :")
    
    # Test Fibonacci
    print("Fibonacci (10 premiers) :")
    # À compléter : afficher les 10 premiers nombres de Fibonacci
    
    # Test nombres pairs
    print("\nNombres pairs jusqu'à 20 :")
    # À compléter : afficher tous les nombres pairs jusqu'à 20
    
    pass


# Exercice 5 - Expressions génératrices et optimisation
def comparer_memoire():
    """Compare l'utilisation mémoire entre list comprehension et expression génératrice"""
    import sys
    
    # List comprehension - crée toute la liste
    liste = [x**2 for x in range(10000)]
    taille_liste = sys.getsizeof(liste)
    
    # Expression génératrice - crée un générateur
    gen = (x**2 for x in range(10000))
    taille_gen = sys.getsizeof(gen)
    
    print(f"Taille de la liste : {taille_liste} bytes")
    print(f"Taille du générateur : {taille_gen} bytes")
    print(f"Différence : {taille_liste - taille_gen} bytes")
    print(f"Ratio : {taille_liste / taille_gen:.1f}x")


def somme_carres_pairs(n):
    """Calcule la somme des carrés des nombres pairs de 0 à n"""
    # Hint : return sum(x**2 for x in range(n+1) if ...)
    pass


def pipeline_generateurs():
    """Pipeline : nombres 0-100 divisibles par 3, carrés, somme"""
    # Hint : return sum(x**2 for x in range(101) if x % 3 == 0)
    pass


def tester_expressions_generatrices():
    """Testez les expressions génératrices"""
    print("\nTest des expressions génératrices :")
    
    print("\nComparaison mémoire :")
    comparer_memoire()
    
    # Test somme carrés pairs
    print(f"\nSomme des carrés des pairs jusqu'à 100 : {somme_carres_pairs(100)}")
    
    # Test pipeline
    print(f"Pipeline de générateurs : {pipeline_generateurs()}")


# Exercice 6 - Affectation par référence vs copie
import copy

def test_references():
    """Testez la différence entre référence et copie"""
    list1 = [1, 2, 3]
    list2 = list1  # Référence
    list3 = list1.copy()  # Copie superficielle
    list4 = copy.deepcopy([[1, 2], [3, 4]])  # Copie profonde
    
    # À compléter
    pass


# Exercice 7 - Types mutables vs immutables
def est_mutable(obj):
    """Retourne True si un objet est mutable, False sinon"""
    try:
        hash(obj)
        return False  # Si hashable, alors immutable
    except TypeError:
        # À compléter
        pass


def test_mutabilite():
    """Testez les types mutables et immutables"""
    # À compléter
    pass


# Exercice 8 - Passage d'arguments avancé
def somme_flexible(*args):
    """Fonction avec *args : accepte un nombre variable d'arguments"""
    # À compléter : calculez la somme de tous les arguments
    pass


def afficher_infos(**kwargs):
    """Fonction avec **kwargs : accepte un nombre variable d'arguments nommés"""
    # À compléter : affichez toutes les paires clé-valeur
    pass


def fonction_complete(a, b, *args, c=10, **kwargs):
    """Fonction combinant tous les types d'arguments"""
    # À compléter : affichez a, b, args, c, kwargs
    pass


def ajouter_element_mauvais(element, liste=[]):
    """PIÈGE ! Ne jamais utiliser [] comme valeur par défaut
    
    Cette fonction a un bug classique : la liste par défaut est partagée
    entre tous les appels de la fonction.
    """
    liste.append(element)
    return liste


def ajouter_element_correct(element, liste=None):
    """Version correcte : utilisez None et créez la liste dans la fonction"""
    if liste is None:
        liste = []
    liste.append(element)
    return liste


# Exercice 9 - Variables de classe vs d'instance
class Compteur:
    """Classe pour comprendre les variables de classe"""
    total = 0  # Variable de classe (partagée par toutes les instances)
    
    def __init__(self, nom):
        self.nom = nom  # Variable d'instance (unique à chaque instance)
        # À compléter : incrémentez le compteur total
        pass
    
    @classmethod
    def afficher_total(cls):
        """Méthode de classe pour afficher le nombre total d'instances"""
        # À compléter : retournez cls.total
        pass


# Exercice 10 - Slices avancés
def tester_slices():
    """Maîtrisez les slices"""
    lst = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
    
    # Basique
    print(lst[2:5])
    print(lst[::-1])  # Inversion
    
    # À compléter avec d'autres exemples
    pass


# Exercice 11 - Introspection
def explorer_objet(obj):
    """Utilisez dir(), type(), hasattr(), etc."""
    print(f"Type: {type(obj)}")
    print(f"Attributs: {dir(obj)}")
    # À compléter
    pass


# Exercice 12 - Clause else dans les structures
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
    resultat = []
    for x in list1:
        if x in list2 and x not in resultat:
            # À compléter : ajouter x au résultat
            pass
    # return resultat


def intersection_v2_set(list1, list2):
    """Méthode 2 : Set - O(n+m)"""
    # Hint : list(set(list1) & set(list2))
    pass


def intersection_v3_comprehension(list1, list2):
    """Méthode 3 : List comprehension avec set - O(n+m)"""
    set2 = set(list2)
    # Hint : [x for x in list1 if x in set2]
    pass


def intersection_v4_builtin(list1, list2):
    """Méthode 4 : Built-in (le plus rapide)"""
    # Hint : list(set(list1).intersection(set(list2)))
    pass


# Tests et benchmarks
if __name__ == "__main__":
    print("=== Tests Python Avancé ===\n")
    
    # Test 1 : Sets
    print("Test 1 : Opérations sur les sets")
    tester_sets_operations()
    
    # Test 2 : frozensets
    print("\nTest 2 : frozensets et cas d'usage")
    tester_frozenset()
    
    # Test 3 : Itérateurs
    print("\nTest 3 : Itérateurs")
    tester_iterateur()
    
    # Test 4 : Générateurs
    print("\nTest 4 : Générateurs")
    tester_generateurs()
    
    # Test 5 : Expressions génératrices
    print("\nTest 5 : Expressions génératrices")
    tester_expressions_generatrices()
    
    # Test 6 : Références
    print("\nTest 6 : Références et copies")
    test_references()
    
    # Test 7 : Mutabilité
    print("\nTest 7 : Mutabilité")
    test_mutabilite()
    
    # Test 8 : Piège des arguments par défaut mutables
    print("\nTest 8 : Piège des arguments par défaut mutables")
    print("Version MAUVAISE :")
    print(ajouter_element_mauvais(1))  # [1]
    print(ajouter_element_mauvais(2))  # [1, 2] - Oups ! Liste partagée
    print("\nVersion CORRECTE :")
    print(ajouter_element_correct(1))  # [1]
    print(ajouter_element_correct(2))  # [2] - Correct !
    
    # Test 9 : Slices
    print("\nTest 9 : Slices")
    tester_slices()
    
    # TP : Comparer les performances
    print("\n=== TP : Intersection de listes ===")
    print("ATTENTION : Implémentez d'abord les 4 fonctions d'intersection avant de lancer le benchmark !\n")
    
    import timeit
    
    list1 = list(range(1000))
    list2 = list(range(500, 1500))
    
    # Décommentez ces lignes une fois vos fonctions implémentées
    # for i, func in enumerate([intersection_v1_boucles, intersection_v2_set, 
    #                            intersection_v3_comprehension, intersection_v4_builtin], 1):
    #     time = timeit.timeit(lambda: func(list1, list2), number=1000)
    #     print(f"Méthode {i} ({func.__name__}): {time:.4f}s")
